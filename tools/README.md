# Herramientas del proyecto

Scripts de apoyo para mantener la Biblioteca. Requieren Python 3 y `olefile` (`pip install olefile`).

| Script | Qué hace |
|---|---|
| `doc2txt.py` | Convierte un Word **`.doc`** (binario OLE de la Cámara de Diputados) a **texto UTF-8** limpio, parseando el FIB y el *piece table* (CLX) del formato Word. Uso: `python3 tools/doc2txt.py LEY.doc fuentes-legales/NOMBRE.txt` |
| `apostrofe.py` | Añade el marcador **⟳ (apóstrofe de vigencia)** después de cada artículo citado en un `.md`. Idempotente y seguro (no toca bloques de código). Uso: `python3 tools/apostrofe.py archivo.md --apply` (sin `--apply` = simulación) |
| `callout.py` | Inserta el callout **«Apóstrofe de vigencia»** bajo el título `#` de un tratado, con la ruta relativa correcta a `fuentes-legales/`. Idempotente. Uso: `python3 tools/callout.py archivo1.md archivo2.md ...` |

> Los originales en Word `.doc` de las leyes están en [`../fuentes-legales/originales-word/`](../fuentes-legales/originales-word/); los textos ya convertidos y citables, en [`../fuentes-legales/`](../fuentes-legales/).
