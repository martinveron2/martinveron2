"""Modelo potencial 2D de Joukowski para el TP2 NACA 2410.

Ejecución: python joukowski_tp2.py
Salidas PNG/SVG/CSV/JSON en figuras_tp2/joukowski/.
El módulo se puede importar sin ejecutar los gráficos.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

A = 1.0
CENTRO = complex(-0.083608, 0.043340)
RADIO = abs(A - CENTRO)  # borde de fuga: zeta = a
OUT = Path(__file__).resolve().parent / "figuras_tp2" / "joukowski"


def contorno(n: int = 8192):
    """Contorno de fuga a fuga, primero extradós, luego intradós."""
    theta_f = np.angle(A - CENTRO)
    theta = np.linspace(theta_f, theta_f + 2 * np.pi, n, endpoint=False)
    zeta = CENTRO + RADIO * np.exp(1j * theta)
    z = zeta + A**2 / zeta
    x_le = z.real.min()
    cuerda = z.real.max() - x_le
    return zeta, z, (z.real - x_le) / cuerda, z.imag / cuerda, cuerda


def punto_operacion(alpha_grados: float, n: int = 8192):
    """Kutta, velocidad transformada, Cp y fuerzas/momento por presión.

    El potencial usa +i Gamma log(eta)/(2 pi), circulación horaria positiva.
    Cl se proyecta normal al flujo. Cm positivo significa nariz arriba,
    es decir, momento horario para x dirigido del borde de ataque al de fuga.
    """
    alpha = np.deg2rad(alpha_grados)
    zeta, z, x, y, cuerda = contorno(n)
    eta = zeta - CENTRO
    theta_f = np.angle(A - CENTRO)
    gamma = 4 * np.pi * RADIO * np.sin(alpha - theta_f)
    dw = np.exp(-1j * alpha) - np.exp(1j * alpha) * RADIO**2 / eta**2
    dw += 1j * gamma / (2 * np.pi * eta)
    dz = 1 - A**2 / zeta**2
    velocidad = np.divide(dw, dz, out=np.zeros_like(dw), where=abs(dz) > 1e-10)
    # Límite finito en la cúspide: derivadas de segundo orden (l'Hôpital).
    singular = abs(dz) <= 1e-10
    if singular.any():
        d2w = 2 * np.exp(1j * alpha) * RADIO**2 / eta**3
        d2w -= 1j * gamma / (2 * np.pi * eta**2)
        velocidad[singular] = d2w[singular] / (2 * A**2 / zeta[singular]**3)
    cp = 1 - abs(velocidad)**2
    xp, yp = np.roll(x, -1), np.roll(y, -1)
    cp_panel = (cp + np.roll(cp, -1)) / 2
    fx = -np.sum(cp_panel * (yp - y))
    fy = np.sum(cp_panel * (xp - x))
    cl = fy * np.cos(alpha) - fx * np.sin(alpha)
    cd = fx * np.cos(alpha) + fy * np.sin(alpha)
    # Nariz arriba = giro horario para el eje x LE -> TE.
    cm_c4 = -np.sum(cp_panel * (((x + xp) / 2 - .25) * (xp - x)
                                  + ((y + yp) / 2) * (yp - y)))
    return dict(alpha=float(alpha_grados), gamma=float(gamma), cl=float(cl),
                cd=float(cd), cm_c4=float(cm_c4), cp=cp, x=x, y=y,
                zeta=zeta, z=z, cuerda=float(cuerda))


def naca2410(n: int = 1000):
    x = np.linspace(0, 1, n)
    m, p, t = .02, .4, .10
    yc = np.where(x < p, m / p**2 * (2 * p * x - x**2),
                  m / (1 - p)**2 * ((1 - 2*p) + 2*p*x - x**2))
    dyc = np.where(x < p, 2*m/p**2*(p-x), 2*m/(1-p)**2*(p-x))
    yt = 5*t*(.2969*np.sqrt(x)-.1260*x-.3516*x**2+.2843*x**3-.1015*x**4)
    beta = np.arctan(dyc)
    return (x-yt*np.sin(beta), yc+yt*np.cos(beta),
            x+yt*np.sin(beta), yc-yt*np.cos(beta))


def cp_superficies(alpha_grados: float = 3., x_grid=None, n: int = 8192):
    """Cp de ambas caras sobre una malla creciente común de x/c.

    Sirve para superponer la serie Joukowski con PD y XFLR5 sin confundir
    el orden de recorrido del contorno (extradós fuga→ataque e intradós
    ataque→fuga). Conserva ambas caras; no promedia sus presiones.
    """
    p = punto_operacion(alpha_grados, n=n)
    x_grid = np.linspace(0., 1., 201) if x_grid is None else np.asarray(x_grid, dtype=float)
    if x_grid.ndim != 1 or not np.isfinite(x_grid).all() or (x_grid < 0).any() or (x_grid > 1).any():
        raise ValueError("x_grid debe ser un vector finito con 0 <= x/c <= 1")
    le = np.argmin(p["x"])
    x_upper = p["x"][:le+1][::-1]
    cp_upper = p["cp"][:le+1][::-1]
    x_lower = np.r_[p["x"][le:], 1.]
    cp_lower = np.r_[p["cp"][le:], p["cp"][0]]
    return x_grid, np.interp(x_grid, x_upper, cp_upper), np.interp(x_grid, x_lower, cp_lower)


def guardar():
    OUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family":"sans-serif", "font.sans-serif":["Arial","DejaVu Sans"],
                         "font.size":11, "axes.titlesize":12, "figure.dpi":160})
    zeta, z, x, y, cuerda = contorno()
    alphas = np.arange(-8., 12.01, .5)
    polar = [punto_operacion(a) for a in alphas]
    p3 = punto_operacion(3.)
    with (OUT/"polar_joukowski.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["alpha_deg","cl","cm_c4","cd_ideal","gamma"])
        w.writerows((r["alpha"],r["cl"],r["cm_c4"],r["cd"],r["gamma"]) for r in polar)
    with (OUT/"cp_joukowski_3deg.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["superficie","x_c","y_c","cp"])
        le=np.argmin(p3["x"])
        w.writerows(("extrados" if i<=le else "intrados",xx,yy,cc)
                    for i,(xx,yy,cc) in enumerate(zip(p3["x"],p3["y"],p3["cp"])))
    x_common, cp_upper, cp_lower = cp_superficies(3.)
    with (OUT/"cp_joukowski_3deg_malla_comun.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["x_c","cp_extrados","cp_intrados","cp_intrados_menos_extrados"])
        w.writerows(zip(x_common,cp_upper,cp_lower,cp_lower-cp_upper))
    nu=naca2410()
    fig, ax=plt.subplots(figsize=(7.2,4.2))
    ax.plot(x,y,color="#07549A",lw=2,label="Joukowski ajustado")
    ax.plot(nu[0],nu[1],"--",color="#D16C20",lw=1.5,label="NACA 2410")
    ax.plot(nu[2],nu[3],"--",color="#D16C20",lw=1.5)
    ax.set(xlabel="x/c",ylabel="y/c",title="Geometría normalizada: Joukowski y NACA 2410",xlim=(-.03,1.03))
    ax.set_aspect("equal",adjustable="datalim");ax.grid(alpha=.3);ax.legend();fig.tight_layout()
    for ext in ("svg","png"):fig.savefig(OUT/f"Joukowski_geometria.{ext}",dpi=300)
    plt.close(fig)
    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(7.2,7.0),sharex=True)
    ax1.plot(alphas,[r["cl"] for r in polar],color="#07549A",lw=2)
    ax2.plot(alphas,[r["cm_c4"] for r in polar],color="#07549A",lw=2)
    ax1.set(ylabel="cₗ",title="Perfil Joukowski: polar potencial");ax2.set(xlabel="α [°]",ylabel="cₘ,c/4")
    for ax in (ax1,ax2):ax.grid(alpha=.3)
    fig.tight_layout()
    for ext in ("svg","png"):fig.savefig(OUT/f"Joukowski_polares.{ext}",dpi=300)
    plt.close(fig)
    le=np.argmin(p3["x"])
    fig,ax=plt.subplots(figsize=(7.2,4.7))
    ax.plot(p3["x"][:le+1],p3["cp"][:le+1],label="Extradós",color="#07549A",lw=2)
    ax.plot(p3["x"][le+1:],p3["cp"][le+1:],label="Intradós",color="#D16C20",lw=2)
    ax.set(xlabel="x/c",ylabel="Cₚ",title="Joukowski: distribución de presión a α = 3°",xlim=(0,1))
    ax.invert_yaxis();ax.grid(alpha=.3);ax.legend();fig.tight_layout()
    for ext in ("svg","png"):fig.savefig(OUT/f"Joukowski_Cp_3deg.{ext}",dpi=300)
    plt.close(fig)
    resumen={"hipotesis":"2D, estacionario, incompresible, inviscido, irrotacional fuera del perfil; Kutta en fuga",
             "a":A,"centro_real":CENTRO.real,"centro_imag":CENTRO.imag,"radio":RADIO,
             "theta_fuga_grados":float(np.rad2deg(np.angle(A-CENTRO))),
             "cuerda_mapeada":cuerda,"alpha_3":{k:p3[k] for k in ("cl","cm_c4","cd","gamma")}}
    (OUT/"resumen_joukowski.json").write_text(json.dumps(resumen,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(resumen,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    guardar()
