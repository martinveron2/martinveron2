# TP2 Aerodinámica Teórica — NACA 2410
# Archivo maestro de gráficos — Python / Matplotlib
# Martín Verón de Astrada
#
# Fuente experimental:
# NACA Research Memorandum L7I22 — Figure 17 — NACA 2410
# Serie R = 3.0 × 10^6
#
# Este archivo se ampliará con todos los gráficos del TP.
# Cada bloque corresponde a una figura o ejercicio del informe.

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path("figuras_tp2")
OUT.mkdir(exist_ok=True)

# ============================================================
# ESTILO GENERAL
# ============================================================

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "legend.fontsize": 9,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 160,
    "savefig.dpi": 300,
})

# ============================================================
# 1. REFERENCIA EXPERIMENTAL — NACA 2410 — R = 3.0 × 10^6
# ============================================================

alpha_cl = np.array([
    -6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
], dtype=float)

cl_exp = np.array([
    -0.4322,-0.3183,-0.2086,-0.1047,0.0002,0.1118,0.2238,0.3311,
    0.4474,0.5741,0.6710,0.7679,0.8723,0.9766,1.0810,1.1779,
    1.2822,1.3866,1.4760,1.5580,1.6102,1.6102,1.4760,1.2599
], dtype=float)

# Para la comparación del momento se conserva el tramo útil lineal.
alpha_cm = np.arange(-6, 15, dtype=float)
cm_exp = np.full_like(alpha_cm, -0.0465, dtype=float)

def grafico_cl_experimental():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(
        alpha_cl, cl_exp,
        marker="o", linewidth=1.5, markersize=4,
        label="Referencia experimental"
    )
    ax.set_xlim(-8, 20)
    ax.set_xticks([-8,-4,0,4,8,12,16,20])
    ax.set_ylim(-0.8, 2.0)
    ax.set_yticks([-0.8,-0.4,0.0,0.4,0.8,1.2,1.6,2.0])
    ax.set_xlabel("α₀ [deg]")
    ax.set_ylabel("cₗ [-]")
    ax.set_title("NACA 2410 — Referencia experimental — R = 3.0 × 10⁶")
    ax.grid(True, alpha=0.35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "01_Referencia_Experimental_Cl.png", bbox_inches="tight")
    plt.close(fig)

def grafico_cm_experimental():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(
        alpha_cm, cm_exp,
        marker="o", linewidth=1.5, markersize=4,
        label="Referencia experimental"
    )
    ax.set_xlim(-8, 20)
    ax.set_xticks([-8,-4,0,4,8,12,16,20])
    ax.set_ylim(-0.12, 0.0)
    ax.set_yticks([-0.12,-0.10,-0.08,-0.06,-0.04,-0.02,0.0])
    ax.set_xlabel("α₀ [deg]")
    ax.set_ylabel("cₘ,c/4 [-]")
    ax.set_title("NACA 2410 — Referencia experimental — R = 3.0 × 10⁶")
    ax.grid(True, alpha=0.35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "02_Referencia_Experimental_Cm.png", bbox_inches="tight")
    plt.close(fig)

# ============================================================
# 2. EJERCICIO 1 — PERFIL DELGADO (PD)
# ============================================================
# Teoría lineal de perfil delgado aplicada a la línea media NACA 2410.
# Resultados empleados en el informe:
# alpha_L=0 = -2.077 deg
# dCl/dalpha = 2*pi rad^-1 = 0.10966 deg^-1
# Cm,c/4 = -0.05312

alpha_pd = np.array([-6,-4,-2,0,2,3,4,6,8,10,12], dtype=float)

cl_pd = np.array([
    -0.430,-0.211,0.008,0.228,0.447,0.557,0.666,0.886,1.105,1.324,1.544
], dtype=float)

cm_pd = np.full_like(alpha_pd, -0.05312, dtype=float)

def grafico_cl_perfil_delgado():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(
        alpha_pd, cl_pd,
        marker="o", linewidth=1.5, markersize=4,
        label="Perfil Delgado (PD)"
    )
    ax.set_xlim(-8, 14)
    ax.set_xticks([-8,-4,0,4,8,12])
    ax.set_ylim(-0.8, 1.8)
    ax.set_yticks([-0.8,-0.4,0.0,0.4,0.8,1.2,1.6])
    ax.set_xlabel("α [deg]")
    ax.set_ylabel("cₗ [-]")
    ax.set_title("NACA 2410 — Perfil Delgado — cₗ = f(α)")
    ax.grid(True, alpha=0.35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "03_Perfil_Delgado_Cl.png", bbox_inches="tight")
    plt.close(fig)

def grafico_cm_perfil_delgado():
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(
        alpha_pd, cm_pd,
        marker="o", linewidth=1.5, markersize=4,
        label="Perfil Delgado (PD)"
    )
    ax.set_xlim(-8, 14)
    ax.set_xticks([-8,-4,0,4,8,12])
    ax.set_ylim(-0.12, 0.0)
    ax.set_yticks([-0.12,-0.10,-0.08,-0.06,-0.04,-0.02,0.0])
    ax.set_xlabel("α [deg]")
    ax.set_ylabel("cₘ,c/4 [-]")
    ax.set_title("NACA 2410 — Perfil Delgado — cₘ,c/4 = f(α)")
    ax.grid(True, alpha=0.35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "04_Perfil_Delgado_Cm.png", bbox_inches="tight")
    plt.close(fig)

# ============================================================
# 3. EJERCICIO 1 — SUPERPOSICIÓN PD / PJ / XFLR5 / EXPERIMENTAL
# ============================================================
# Se incorporarán aquí las cuatro series definitivas de c_l(α)
# y c_m,c/4(α), manteniendo este mismo estilo gráfico.

# ============================================================
# 4. EJERCICIO 2 — Cp(x) A α = 3°
# ============================================================

alpha_ej2 = np.deg2rad(3.0)

# --- Perfil Delgado
I0_pd = 0.004493
A0_pd = alpha_ej2 - I0_pd
A1_pd = 0.081495
A2_pd = 0.013861

theta_pd = np.linspace(0.010, np.pi - 0.001, 1600)
x_cp_pd = (1.0 - np.cos(theta_pd)) / 2.0

g_pd = (
    A0_pd * (1.0 + np.cos(theta_pd)) / np.sin(theta_pd)
    + A1_pd * np.sin(theta_pd)
    + A2_pd * np.sin(2.0 * theta_pd)
)

cp_pd_extrados = 1.0 - (1.0 + g_pd) ** 2
cp_pd_intrados = 1.0 - (1.0 - g_pd) ** 2

# --- Perfil de Joukowski
# Misma geometría adoptada en el Ejercicio 1.
a_j = 1.0
z0_j = -0.083608 + 0.043340j
R_j = 1.084474
theta_bf_j = np.angle(a_j - z0_j)

# Condición de Kutta.
Gamma_j = 4.0 * np.pi * R_j * np.sin(alpha_ej2 - theta_bf_j)

theta_j = np.linspace(
    theta_bf_j + 1e-3,
    theta_bf_j + 2.0 * np.pi - 1e-3,
    5000
)

z_j = z0_j + R_j * np.exp(1j * theta_j)

dW_dz_j = (
    np.exp(-1j * alpha_ej2)
    - (R_j ** 2) * np.exp(1j * alpha_ej2) / (z_j - z0_j) ** 2
    + 1j * Gamma_j / (2.0 * np.pi * (z_j - z0_j))
)

dzeta_dz_j = 1.0 - a_j ** 2 / z_j ** 2
vel_j = np.abs(dW_dz_j / dzeta_dz_j)
cp_j = 1.0 - vel_j ** 2

zeta_j = z_j + a_j ** 2 / z_j
x_j = (
    (zeta_j.real - zeta_j.real.min())
    / (zeta_j.real.max() - zeta_j.real.min())
)

mask_sup_j = theta_j < theta_bf_j + np.pi
mask_inf_j = ~mask_sup_j

x_j_sup = x_j[mask_sup_j]
cp_j_sup = cp_j[mask_sup_j]
x_j_inf = x_j[mask_inf_j]
cp_j_inf = cp_j[mask_inf_j]

ord_sup = np.argsort(x_j_sup)
ord_inf = np.argsort(x_j_inf)

x_j_sup = x_j_sup[ord_sup]
cp_j_sup = cp_j_sup[ord_sup]
x_j_inf = x_j_inf[ord_inf]
cp_j_inf = cp_j_inf[ord_inf]

# --- XFLR5
# Operating point real documentado: alpha=3 deg, Re=3.0e6,
# Mach=0, Ncrit=9, Cp_min ~= -1.0007.
#
# La serie siguiente reproduce la traza XFLR5 que ya estaba incorporada en
# la versión de referencia del informe y queda centralizada aquí para que
# todo el TP se grafique desde Python. Si se recupera la exportación tabulada
# x/c-Cp del operating point, esta única serie debe reemplazarse sin tocar
# el resto del flujo de generación.

x_xflr5_cp = np.array([
    0.005,0.010,0.020,0.030,0.050,0.080,0.100,0.150,0.200,
    0.300,0.400,0.500,0.600,0.700,0.800,0.900,0.950,0.980,0.995
], dtype=float)

cp_xflr5_extrados = np.array([
    -0.9007,-0.9873,-1.0007,-0.9877,-0.9503,-0.9040,-0.8816,
    -0.8344,-0.7881,-0.6987,-0.5695,-0.4669,-0.3742,-0.2873,
    -0.1887,-0.0604,0.0364,0.1159,0.1541
], dtype=float)

cp_xflr5_intrados = np.array([
    0.9219,0.7062,0.4588,0.3254,0.1958,0.1159,0.0946,0.0629,
    0.0596,0.0629,0.0629,0.0629,0.0728,0.0861,0.0960,0.1159,
    0.1291,0.1402,0.1729
], dtype=float)

def grafico_ejercicio2_cp_alpha3():
    fig, ax = plt.subplots(figsize=(7.7, 4.9))

    ax.plot(
        x_cp_pd, cp_pd_extrados,
        linewidth=1.6,
        label="PD - extradós"
    )
    ax.plot(
        x_cp_pd, cp_pd_intrados,
        "--", linewidth=1.6,
        label="PD - intradós"
    )
    ax.plot(
        x_j_sup, cp_j_sup,
        linewidth=1.6,
        label="PJ - extradós"
    )
    ax.plot(
        x_j_inf, cp_j_inf,
        "--", linewidth=1.6,
        label="PJ - intradós"
    )
    ax.plot(
        x_xflr5_cp, cp_xflr5_extrados,
        linewidth=2.2,
        label="XFLR5 - extradós"
    )
    ax.plot(
        x_xflr5_cp, cp_xflr5_intrados,
        "--", linewidth=2.2,
        label="XFLR5 - intradós"
    )

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(1.2, -5.0)
    ax.set_xlabel("x/c")
    ax.set_ylabel("Cₚ")
    ax.set_title("NACA 2410 — Distribución de presión a α = 3°")
    ax.grid(True, alpha=0.30)
    ax.legend(ncol=2, loc="upper right")

    fig.tight_layout()
    fig.savefig(
        OUT / "05_Ejercicio2_Cp_alpha3_superpuesto.png",
        bbox_inches="tight"
    )
    plt.close(fig)

# ============================================================
# 5. EJERCICIO 3 — GEOMETRÍA NACA 2410 VS JOUKOWSKI
# ============================================================
# Se incorporará la superposición geométrica de ambos perfiles.

if __name__ == "__main__":
    grafico_cl_experimental()
    grafico_cm_experimental()
    grafico_cl_perfil_delgado()
    grafico_cm_perfil_delgado()
    grafico_ejercicio2_cp_alpha3()
    print(f"Figuras generadas en: {OUT.resolve()}")
