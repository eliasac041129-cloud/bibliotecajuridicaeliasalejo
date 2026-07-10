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

## Cómo agregar nuevas fuentes

1. Descarga el texto oficial (Cámara de Diputados / DOF).
2. Conviértelo a **UTF-8** y guárdalo como `.txt` aquí (no PDF: el texto plano es citable y verificable).
   ```bash
   iconv -f WINDOWS-1252 -t UTF-8 "descarga.txt" > fuentes-legales/NOMBRE-LEY.txt
   ```
3. Registra la verificación en el [Protocolo](../PROTOCOLO_DE_VERIFICACION.md) §V.
