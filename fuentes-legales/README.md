# Fuentes legales (textos oficiales)

Esta carpeta guarda los **textos oficiales vigentes** de las leyes que la Biblioteca usa como
**fuente primaria** para el sello *"Referencia Verificada"* del [Protocolo de Verificación](../PROTOCOLO_DE_VERIFICACION.md).

Cuando un tratado marca un artículo con **✅ (verificado verbatim)**, significa que su número y
contenido fueron cotejados **palabra por palabra** contra el texto de esta carpeta.

## Contenido actual

| Archivo | Ley | Versión | Codificación |
|---|---|---|---|
| `CFF-Codigo-Fiscal-de-la-Federacion.txt` | Código Fiscal de la Federación | TEXTO VIGENTE — última reforma **DOF 09-04-2026** | UTF-8 |
| `LISR-Ley-del-Impuesto-sobre-la-Renta.txt` | Ley del Impuesto sobre la Renta | TEXTO VIGENTE — última reforma **DOF 01-04-2024** | UTF-8 |
| `LGSM-Ley-General-de-Sociedades-Mercantiles.txt` | Ley General de Sociedades Mercantiles | TEXTO VIGENTE — última reforma **DOF 20-10-2023** (cantidades actualizadas DOF 26-12-2025) | UTF-8 |
| `LGTOC-Ley-General-de-Titulos-y-Operaciones-de-Credito.txt` | Ley General de Títulos y Operaciones de Crédito | TEXTO VIGENTE — última reforma **DOF 26-03-2024** | UTF-8 |
| `LMV-Ley-del-Mercado-de-Valores.txt` | Ley del Mercado de Valores | TEXTO VIGENTE — última reforma **DOF 14-11-2025** | UTF-8 |
| `CCF-Codigo-Civil-Federal.txt` | Código Civil Federal | TEXTO VIGENTE — última reforma **DOF 14-11-2025** | UTF-8 |
| `LFT-Ley-Federal-del-Trabajo.txt` | Ley Federal del Trabajo | TEXTO VIGENTE — última reforma **DOF 14-05-2026** | UTF-8 |
| `CPF-Codigo-Penal-Federal.txt` | Código Penal Federal | TEXTO VIGENTE — última reforma **DOF 13-03-2026** | UTF-8 |
| `LAmp-Ley-de-Amparo.txt` | Ley de Amparo | TEXTO VIGENTE — última reforma **DOF 16-10-2025** | UTF-8 |

## Cómo consultar un artículo

Los artículos se rotulan `Artículo N.-` o `Artículo No.-`. Para localizar uno:

```bash
grep -nE "^ *Artículo 67" fuentes-legales/CFF-Codigo-Fiscal-de-la-Federacion.txt
```

## Aviso permanente ⚠️

El derecho fiscal es **volátil**: tasas, tarifas, montos (UMA), estímulos e incluso números de
artículo cambian **cada año** con la Miscelánea Fiscal y las Leyes de Ingresos. Estos textos reflejan
la fecha indicada arriba. **Antes de citar en un asunto real, reemplaza estos archivos por la versión
del ejercicio fiscal correspondiente** (descárgala de [diputados.gob.mx](https://www.diputados.gob.mx/LeyesBiblio/index.htm)
o del DOF) y vuelve a cotejar.

## El símbolo ⟳ (apóstrofe de vigencia)

En los tratados verás **⟳** después de cada artículo citado. Significa: *«¿sigue vigente y con este
número hoy? — reitéralo en el código de esta carpeta antes de citarlo».* Nace de un caso real de este
proyecto: el **art. 390 del CPF**, al cotejarlo, resultó **«Derogado»**. Por eso ninguna cita —ni
siquiera las marcadas ✅— se toma como eterna: **✅** = verificado *a la fecha de su fuente*; **⟳** =
esa fecha ya envejece, la última palabra la tiene el código.

## Cómo agregar nuevas fuentes

1. Descarga el texto oficial (Cámara de Diputados / DOF), en **texto** o **Word**.
2. Conviértelo a **UTF-8** y guárdalo como `.txt` aquí (no PDF: el texto plano es citable y verificable).
   - Si viene como **texto** en Latin-1/Windows-1252:
     ```bash
     iconv -f WINDOWS-1252 -t UTF-8 "descarga.txt" > fuentes-legales/NOMBRE-LEY.txt
     ```
   - Si viene como **Word `.doc`** (binario OLE, como los de la Cámara de Diputados), usa el
     extractor incluido en `tools/doc2txt.py` (parsea el *piece table* del formato Word):
     ```bash
     python3 tools/doc2txt.py "LEY.doc" fuentes-legales/NOMBRE-LEY.txt
     ```
3. **Verifica verbatim** algunos artículos emblemáticos (número ↔ contenido) contra el `.txt`.
4. Registra la verificación en el [Protocolo](../PROTOCOLO_DE_VERIFICACION.md) §V.
