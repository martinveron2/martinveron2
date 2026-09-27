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
# Se incorporarán las series de Perfil Delgado, Joukowski y XFLR5.

# ============================================================
# 5. EJERCICIO 3 — GEOMETRÍA NACA 2410 VS JOUKOWSKI
# ============================================================
# Se incorporará la superposición geométrica de ambos perfiles.

if __name__ == "__main__":
    grafico_cl_experimental()
    grafico_cm_experimental()
    grafico_cl_perfil_delgado()
    grafico_cm_perfil_delgado()
    print(f"Figuras generadas en: {OUT.resolve()}")
