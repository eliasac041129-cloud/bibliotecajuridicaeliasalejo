# Sistema de Repaso y Retención

> **Por qué existe.** Leer un tratado una vez no es dominarlo. La [Guía Metodológica](../GUIA-METODOLOGICA.md)
> lo dice: el dominio exige **recuperación activa** (recordar sin mirar) y **repaso espaciado** (repasar en
> intervalos crecientes). Esta carpeta convierte ese principio en herramientas concretas para que el
> conocimiento de la Biblioteca **se quede** en tu memoria de largo plazo —no solo para el examen, sino
> para el ejercicio profesional—.

> **⚠️ Aviso de verificación.** Las tarjetas y preguntas contienen **datos duros** (artículos, tasas,
> plazos) marcados con **⚠️** cuando deben confirmarse contra el texto vigente (Protocolo de Verificación).
> **Nunca** memorices un número como definitivo: memoriza el **concepto** y la **ubicación** del dato, y
> **verifica** el número en la fuente antes de usarlo en un asunto real. Contenido a fecha: **2026-07**.

---

## Qué hay en esta carpeta

| Archivo | Qué es | Cómo se usa |
|---------|--------|-------------|
| [`flashcards-anki.csv`](./flashcards-anki.csv) | Mazo de tarjetas para **repaso espaciado** (importable en Anki) | Impórtalo a Anki y repasa 15-20 min/día |
| [`banco-de-preguntas.md`](./banco-de-preguntas.md) | **Banco de preguntas** por área, con respuestas modelo | Autoexamínate por escrito (no solo mental) |

---

## Cómo importar el mazo a Anki

**Anki** es un programa gratuito de repaso espaciado (escritorio y móvil). Para importar el mazo:

1. Descarga e instala **Anki** (https://apps.ankiweb.net/) — *(enlace informativo; verifica la fuente
   oficial)*.
2. Crea un mazo nuevo, p. ej. **"AJE · Derecho"**.
3. Menú **Archivo → Importar** y selecciona [`flashcards-anki.csv`](./flashcards-anki.csv).
4. El archivo ya incluye las directivas de importación en las primeras líneas:
   - `#separator:Pipe` → el separador de campos es la barra vertical `|`.
   - `#html:false` → texto plano.
   - `#tags column:3` → la tercera columna es la etiqueta (materia), para filtrar por tema.
5. Mapea: **Campo 1 = Anverso (pregunta)**, **Campo 2 = Reverso (respuesta)**, **Columna 3 = Etiquetas**.
6. Importa. Repasa **todos los días** (Anki te muestra solo las tarjetas "vencidas": 15-20 min bastan).

> Si prefieres no usar Anki, el CSV se abre en cualquier hoja de cálculo (Excel, Google Sheets): usa la
> columna 1 como pregunta y tápate la columna 2 (respuesta) para autoevaluarte.

---

## Cómo estudiar con este sistema (rutina recomendada)

Integra esto en el [Sistema Diario](../Columna-II-Hoja-de-Ruta/02_PLAN_OPERATIVO_DIARIO_AJE.md):

1. **Al terminar de leer un tratado**, no pases al siguiente sin antes: (a) hacer sus **flashcards**
   (sección 35 de cada tratado) y (b) resolver su bloque en el **banco de preguntas**.
2. **Cada día**, dedica **15-20 min** al repaso espaciado en Anki (recuperación activa de lo ya visto).
3. **Cada semana**, toma un bloque del banco de preguntas y **respóndelo por escrito** (escribir obliga a
   estructurar; es más exigente que "recordar mental").
4. **Antes de un examen**, filtra el mazo por la **etiqueta** de la materia y repasa intensivo + resuelve
   los "casos de examen" (sección 33) de los tratados correspondientes.

> **La ciencia detrás:** el **efecto de prueba** (recuperar es aprender, no solo repasar) y el **espaciado**
> (repasar justo antes de olvidar) multiplican la retención frente a la relectura pasiva. Estudia **menos
> horas pero mejor**.

---

## Cómo crecer el mazo

Cada tratado de la Biblioteca ya trae su sección **35. Flashcards**. Para ampliar tu mazo:
1. Abre el tratado, copia sus flashcards.
2. Conviértelas al formato `pregunta|respuesta|Materia` (una por línea).
3. Pégalas al final de [`flashcards-anki.csv`](./flashcards-anki.csv) (o impórtalas por separado).
4. Marca ⚠️ los datos duros que debas verificar.

*Sistema vivo: crece con cada tratado que domines. El objetivo no es "tener" las tarjetas, sino
**repasarlas** hasta que el conocimiento sea tuyo.*
