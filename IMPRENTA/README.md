# Ficha técnica para imprenta

PDF paginados de la obra, generados con `tools/build_impreso.py`. **No son el HTML
de pantalla reescalado**: llevan caja tipográfica de libro, márgenes espejeados,
cabeceras corridas, folios y capítulos que abren en página impar.

Todas las cifras de abajo están **medidas sobre el PDF real**, no estimadas.

---

## Las dos opciones

| | `lectura/` | `academico/` |
|---|---|---|
| Medida cerrado | 155 × 230 mm | 155 × 230 mm |
| Cuerpo / interlínea | 10.5 pt / 1.36 | 10 pt / 1.30 |
| Columnas | 1 | 1 |
| Margen interior (lomo) | 18 mm | 17 mm |
| **Margen exterior (para anotar)** | **26 mm** | 19 mm |
| Margen superior / inferior | 17 / 20 mm | 16 / 18 mm |
| Tomo I | 665 pp. | 561 pp. |
| Tomo II | 641 pp. | 531 pp. |
| Tomo III | 661 pp. | 555 pp. |
| **Total** | **1,967 pp.** | **1,647 pp.** |
| Lomo por tomo (70 g + tapa dura) | ≈ 3.6 cm | ≈ 3.1 cm |

`lectura` es la recomendada: cuerpo mayor, más aire entre líneas y margen exterior
de 26 mm, que es donde caben las notas. `academico` ahorra 320 páginas —un centímetro
menos de lomo por tomo— a costa de medio punto de cuerpo y 7 mm de margen.

## Papel: es el papel, no el texto, lo que define el grosor

Lomo medido para un tomo de `lectura` (333 hojas), tapa dura incluida:

| Papel | Calibre | Lomo | ¿Se puede subrayar? |
|---|---|---|---|
| Papel biblia 40 g | 0.050 mm | 2.3 cm | **No.** El marcador traspasa y se ve por el reverso |
| Offset ahuesado 60 g | 0.078 mm | 3.2 cm | Sí, con lápiz y bolígrafo fino |
| **Offset ahuesado 70 g** | **0.092 mm** | **3.7 cm** | **Sí — el equilibrio recomendado** |
| Offset ahuesado 80 g | 0.105 mm | 4.1 cm | Sí, incluso con marcador |
| Bond blanco 90 g (print on demand) | 0.114 mm | 4.4 cm | Sí, pero abulta sin necesidad |

**Especificación recomendada:** offset **ahuesado** (crema, no blanco: cansa menos la
vista en jornadas largas) de **70 g** con opacidad ≥ 90 %, **cosido Smyth** (a 660
páginas el lomo encolado se rompe con el uso), tapa dura y **guardas**. Tinta negra
a una sola pasada; no hay color en el interior.

## Lo que esto descarta

**Print on demand no sirve para un tomo de este tamaño.** Amazon KDP tiene un tope de
828 páginas en blanco y negro y usa el papel más grueso de la tabla. Los tres tomos
entrarían por separado, pero saldrían más gordos y en papel blanco. Esto pide
**imprenta offset con encuadernador**.

## Cómo regenerar

```
pip install weasyprint markdown
python3 tools/build_impreso.py --listar-formatos
python3 tools/build_impreso.py --formato lectura --tomos 3
python3 tools/build_impreso.py --calibrar        # mide los 4 formatos y extrapola
```

Fuentes necesarias en el sistema: **Noto Serif** (texto), **DejaVu Serif** (aporta el
glifo de ⟳, que Noto Serif no trae y que aparece 1,581 veces), **DejaVu Sans Mono**
(los 201 diagramas) y **Noto Sans Symbols 2** (semáforo ✅ ⚠️).

## Reparto en tomos

No es arbitrario: `repartir()` hace una partición lineal por programación dinámica
que minimiza el tomo más gordo conservando el orden de la obra. El desvío entre
tomos queda en 2.4 %.

| Tomo | Contenido | Capítulos |
|---|---|---|
| I | Fundamentos · Civil Profundo · Mercantil (parte) | 21 |
| II | Mercantil (resto) · Derecho Corporativo | 13 |
| III | Maestría · Ramas Esenciales · Anexos A y B | 19 |
