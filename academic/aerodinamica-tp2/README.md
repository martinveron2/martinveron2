# TP2 — Aerodinámica Teórica — NACA 2410

Repositorio de apoyo reproducible para los gráficos del **TP2 de Aerodinámica Teórica**.

## Criterio de trabajo

Todos los gráficos del TP se generan con **Python + Matplotlib** desde un único archivo maestro, de modo que las figuras incluidas en el informe puedan reproducirse y actualizarse sin edición manual.

## Alcance actual

Actualmente el archivo maestro contiene:

- referencia experimental NACA 2410 para **R = 3.0 × 10^6**;
- curva **cₗ = f(α)** de Perfil Delgado;
- curva **cₘ,c/4 = f(α)** de Perfil Delgado.

El mismo archivo se irá ampliando con:

- Perfil de Joukowski;
- resultados XFLR5;
- superposición final del Ejercicio 1;
- distribución **Cp(x)** a **α = 3°** del Ejercicio 2;
- superposición geométrica NACA 2410 / Joukowski del Ejercicio 3.

## Fuente experimental

**NACA Research Memorandum L7I22 — Figure 17**  
Perfil NACA 2410, cuerda de 24 in.

Los puntos experimentales se emplean como base de comparación con Perfil Delgado, Perfil de Joukowski y XFLR5.

## Archivo principal

`TP2_NACA2410_GRAFICOS_MASTER.py`

## Ejecución

```bash
python TP2_NACA2410_GRAFICOS_MASTER.py
```

Las figuras se generan automáticamente en la carpeta `figuras_tp2/`.

### Figuras generadas actualmente

- `01_Referencia_Experimental_Cl.png`
- `02_Referencia_Experimental_Cm.png`
- `03_Perfil_Delgado_Cl.png`
- `04_Perfil_Delgado_Cm.png`

Las figuras de Perfil Delgado incluidas en el informe Word se generan directamente desde este archivo maestro.
