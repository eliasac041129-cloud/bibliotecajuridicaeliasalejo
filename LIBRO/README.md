# 📖 El Libro — Manual para Ejercer el Derecho Corporativo

Este directorio contiene la **versión libro** de toda la Biblioteca: un solo archivo HTML
autocontenido, con estética clásica (tipo Porrúa), listo para leer e **imprimir en PDF**.

## Cómo abrirlo e imprimirlo (PDF)

1. Abre **`Manual-para-Ejercer-el-Derecho-Corporativo.html`** en cualquier navegador (Chrome, Edge, Safari).
   - En GitHub: descárgalo (botón *Download raw file*) y ábrelo con doble clic.
2. Pulsa el botón **«📖 Generar PDF / Imprimir»** (abajo a la derecha), o usa `Ctrl/Cmd + P`.
3. En destino elige **«Guardar como PDF»**. Recomendado:
   - Tamaño: **Carta**; Márgenes: **predeterminados**; **activa** «Gráficos de fondo» para conservar los filetes dorados.
4. Guarda. No importa el número de páginas: el libro pagina solo (cada Parte y capítulo inicia en página nueva).

## Qué contiene
- Portada con el **escudo de la UNAM** (embebido), título, autor (**Elias Alejo**) y fecha.
- Página legal · **Carta de dedicación «Al Elias del futuro»** · Consideraciones para el lector ·
  Finalidad · Estructura · **Índice general**.
- **58 capítulos** (Partes I–VI) + **Anexo A: Banco de Formatos**.
- Colofón final con escudo, autor, fecha y la frase de cierre.

## Cómo se regenera
Si actualizas los tratados, vuelve a compilar el libro con:

```bash
python3 tools/build_libro.py
```

*(Requiere `python3` y `markdown`: `pip install markdown`.)*
