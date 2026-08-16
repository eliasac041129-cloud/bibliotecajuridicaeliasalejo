# Diagnóstico de ejecución

### Los cuellos de botella reales, sin halago y sin condescendencia

> **Cuándo se abre:** una vez ahora. Después, cada 90 días, para comprobar si el diagnóstico cambió.
>
> **Advertencia de alcance.** Esto **no** es el diagnóstico académico. El académico —cuántas materias,
> cuáles, qué promedio— está en ⛔ FALTA hasta que lleguen los documentos. Esto es el diagnóstico del
> **mecanismo de fallo**, y para ese sí hay datos suficientes: los §V, §VI, §X y §XV del prompt, y el
> propio historial del repositorio.

---

## I. La premisa del encargo es incorrecta, y hay que corregirla primero

El §V pide analizar esta contradicción:

> *"capacidad potencial alta + ejecución inconsistente = resultados muy inferiores a mi capacidad"*

Y el §V se autodescribe con una lista de deficiencias que empieza por **disciplina** y **constancia**.

**Eso es falso, y creerlo es el obstáculo más grande del proyecto.**

La evidencia está en este repositorio, y es medible:

| Dato | Cifra |
|---|---|
| Palabras escritas | 684,692 |
| Tratados terminados | 53 |
| Leyes cotejadas palabra por palabra contra el texto oficial | 27 |
| Marcas de vigencia ⟳ colocadas una por una | 1,581 |
| Datos volátiles marcados ⚠️ en lugar de darlos por buenos | 1,231 |
| Ejercicios de laboratorio construidos | 15 |
| Commits en la Edición Final | 28 |

Nadie sin disciplina coteja 27 leyes verbatim. Nadie sin constancia sostiene 53 tratados. Nadie sin
rigor coloca 1,231 advertencias de incertidumbre en su propio trabajo, cuando lo cómodo era afirmar y
seguir.

> **El diagnóstico correcto no es "le falta disciplina". Es: la disciplina existe, es de nivel alto y
> está aplicada íntegramente a un solo dominio.**

La diferencia entre esos dos diagnósticos no es de amabilidad. Es de **tratamiento**. Si el problema
fuera falta de disciplina, el remedio sería esforzarse más — y eso ya se intentó, y falló, porque
atacaba una causa que no existe. Si el problema es **asignación**, el remedio es redirigir, y eso sí
funciona.

Dicho de otro modo: no hay que construir un carácter nuevo. Hay que apuntar el que ya se demostró
hacia el lugar donde hoy no apunta.

---

## II. El patrón real: dónde funciona y dónde no

Separando lo que se ejecutó de lo que se falló, el patrón es nítido y no tiene nada que ver con la
fuerza de voluntad:

| Variable | Donde SÍ ejecuta (la biblioteca) | Donde NO ejecuta (lo escolar y administrativo) |
|---|---|---|
| **Quién define la tarea** | Él mismo | Un tercero |
| **Novedad** | Cada capítulo es un problema nuevo | Repetitivo, previsible |
| **Complejidad** | Alta — y eso lo engancha | Baja: llenar, entregar, formarse en una fila |
| **Visibilidad del avance** | Inmediata: el archivo crece, el commit queda | Nula hasta el resultado final |
| **Final definido** | Él decide cuándo está terminado | Fecha ajena, rígida |
| **Costo de retrasarse un día** | Cero | A veces **irreversible** |
| **Diseño del sistema** | Suyo. Hizo las reglas | Ajeno. Solo obedece |

Cinco de las siete filas apuntan a lo mismo: **el rendimiento no depende del esfuerzo, depende de la
agencia.** Con control sobre el problema, el rendimiento es excepcional. Sin control, colapsa.

Esto tiene una consecuencia práctica que gobierna toda esta carpeta:

> **A las tareas administrativas hay que darles artificialmente las propiedades de la columna
> izquierda.** No hay que aprender a tolerar lo aburrido. Hay que **rediseñar lo aburrido** para que
> caiga dentro del régimen donde este perfil ya demostró que rinde.

Ejemplos concretos de esa conversión, que es lo que hacen los demás documentos:

- Un trámite deja de ser *"ir a inscribir extraordinarios"* (ajeno, difuso, sin final visible) y se
  convierte en *"cerrar la fila 3 del calendario maestro"* — con casilla, con estado y con commit.
  Ahora tiene final definido, avance visible y sistema propio.
- El repaso deja de ser *"estudiar más"* y se convierte en **208 flashcards con racha diaria**.
- La revisión semanal deja de ser una intención y se convierte en un **commit fechado**, igual que los
  28 de la Edición Final.

No es un truco motivacional. Es usar la única palanca que la evidencia dice que funciona.

---

## III. Los cuatro cuellos de botella, en orden de daño

No son los quince de la lista del §V. Son cuatro, y están jerarquizados por **costo irreversible**, no
por incomodidad.

### 1. No existe un registro externo de compromisos — *daño: irreversible*

Es el único de los cuatro que produce pérdidas que no se recuperan. Un extraordinario perdido no se
repone; consume una oportunidad de un número finito.

Y su causa no es el olvido, es más específica: **la memoria se usó como sistema de registro.** La
memoria es excelente para conceptos —de ahí los 53 tratados— y estructuralmente inadecuada para
fechas, porque falla justo cuando hay carga, y la carga aparece precisamente en época de exámenes.

Hay una ironía que conviene mirar de frente, porque contiene la solución completa: **este proyecto
inventó y aplicó 1,581 veces un símbolo (⟳) cuyo único propósito es "no confíes en tu memoria,
verifica en la fuente oficial antes de usarlo".** Ese rigor se aplicó a artículos de ley. **Nunca se
aplicó a un calendario escolar.**

No falta la herramienta. Falta apuntarla. → [`04_SISTEMA_ANTIFALLAS.md`](./04_SISTEMA_ANTIFALLAS.md)

### 2. El sueño — *daño: multiplica los otros tres*

El §X reconoce horarios invertidos y noches de pocas horas. Con una jornada que obliga a despertar a
las 4:45, esto no es un hábito saludable opcional: es la variable de la que dependen las otras.

La cadena es mecánica y siempre corre en el mismo sentido:

> dormir tarde → despertar agotado → tres horas de traslado inútiles → clases sin retención →
> tarde sin capacidad de concentración → nada hecho → culpa → entretenimiento digital para no
> sentirla → dormir tarde

Cada eslabón produce el siguiente. Y hay un detalle que la vuelve más grave en este caso: **el
traslado son 15 horas semanales que solo rinden si se llega despierto.** Dormir mal no cuesta las dos
horas que se ganaron: cuesta esas dos más las quince del traslado más la capacidad de las clases.

Por eso las 21:15 de [`HOY.md`](./HOY.md) no son una recomendación de bienestar. Son la restricción
de la que depende todo lo demás, y es la única línea del plan que no admite negociación.

### 3. La inflación de proyectos como forma de evitación — *daño: el más difícil de ver*

Esta es la parte incómoda, y el §XXV pidió expresamente que se dijera.

Las 684,692 palabras son valiosas. También fueron, en parte, **una forma sofisticada de evitación.**

Ambas cosas son verdad a la vez, y por eso es tan difícil de detectar: se construyó algo genuinamente
extraordinario **durante el mismo periodo en que se perdían extraordinarios por no revisar una fecha.**
Escribir un tratado sobre M&A es más interesante, más gratificante y produce más sensación de progreso
que llenar un formato en una ventanilla. Ambas actividades se sienten como "trabajar". Solo una tenía
fecha límite.

El propio [Documento Fundacional](../00_DOCUMENTO_FUNDACIONAL_AJE.md) lo vio venir y escribió el
antídoto en su Principio 3: *"Lo urgente y poco glamoroso —titularse, el inglés, la primera
experiencia— tiene prioridad sobre lo vistoso."* Estaba escrito. No se aplicó.

**Y hay que decir algo más, aunque sea molesto: esta petición es el mismo patrón.**

Un plan maestro de veintinueve secciones es más atractivo que capturar nueve fechas con sus alarmas.
Tiene todas las propiedades de la columna izquierda de la tabla del §II: es propio, complejo, novedoso
y sin fecha límite. Existe un riesgo real y concreto de que esta carpeta se lea, se admire, se mejore
—y de que las nueve fechas sigan sin capturar.

Por eso [`00_RECTOR.md`](./00_RECTOR.md) establece que solo un archivo se lee a diario, y por eso
[`PENDIENTE-DE-DOCUMENTOS.md`](./PENDIENTE-DE-DOCUMENTOS.md) cierra diciendo que cuarenta minutos de
captura valen hoy más que la biblioteca entera. No es retórica: es el diagnóstico aplicado a este mismo
documento.

> **La prueba de que este cuello de botella se está cerrando** no es que el plan quede perfecto. Es
> que la primera fecha se capture **antes** de leer el resto de la carpeta.

### 4. El entretenimiento digital — *daño: real, pero es consecuencia*

Aparece en la lista del §V como problema autónomo. No lo es: es lo que llena el hueco que dejan el
cuello 2 (cansancio) y la ausencia de una siguiente acción definida.

Nadie abre una aplicación de video durante 90 minutos cuando sabe exactamente qué hacer, tiene energía
para hacerlo y el final está a la vista. Se abre cuando la tarea es difusa —*"tengo que estudiar
Fiscal"*, que no se puede terminar nunca— o cuando el cuerpo no da.

Se ataca indirectamente, y por eso funciona: durmiendo (cuello 2), definiendo la tarea con verbo y
final visible ([`HOY.md`](./HOY.md)) y poniendo fricción física —el teléfono en otro cuarto durante los
bloques—. Atacarlo con voluntad frontal es el enfoque que ya falló.

---

## IV. Lo que ya no se puede recuperar

El §XXVIII.1 pide honestidad sobre esto, y merece una respuesta directa aunque no se puedan dar cifras
sin el historial.

**No se recupera:**

- **El tiempo.** Los semestres transcurridos están gastados. La titulación va a llegar más tarde que
  para quien no se atrasó, y eso ya no se cambia.
- **Las oportunidades de examen consumidas.** Son finitas por reglamento y las gastadas no vuelven.
  Cuántas quedan es dato de ⛔ FALTA — y es la cifra más urgente de todo el expediente.
- **El promedio de las materias ya cerradas.** Salvo lo que el reglamento permita, una calificación
  asentada es un dato histórico. El promedio final va a tener un **techo aritmético** y ese techo ya
  está fijado por lo que ya ocurrió. Cuál es, lo dirá [`tools/promedio.py`](./tools/promedio.py) con
  los datos reales — y va a ser más bajo de lo que sería sin el rezago. Eso no se negocia con esfuerzo.

**Sí se recupera, y es más de lo que parece:**

- **La tendencia.** Y esto no es consuelo: es cómo funciona la lectura real de un historial. Un
  expediente con calificaciones bajas al principio y altas al final cuenta una historia distinta —y
  mejor— que uno mediocre y plano. Nadie contrata un promedio; se contrata a una persona, y una curva
  ascendente sostenida durante tres semestres es evidencia verificable de capacidad de corrección.
  Es, de hecho, más persuasiva en una entrevista que un promedio alto sin historia.
- **Todo lo que no depende del historial**, que es la mayor parte de lo que decide una contratación en
  corporativo: la tesis, el inglés, la experiencia, el criterio técnico y una biblioteca de 684,692
  palabras que ningún egresado de su generación tiene.
- **La titulación completa**, con tesis, servicio social e inglés. No hay nada en la situación descrita
  que la haga imposible. Es cuestión de secuencia y de fechas.

> **La frase honesta:** el techo del promedio ya bajó y no va a volver a subir. El techo profesional
> **no se ha tocado.** Y en Derecho corporativo transaccional, el segundo pesa mucho más que el
> primero — con una excepción que hay que verificar antes de descartarla: los programas que filtran por
> promedio mínimo de entrada, que existen y son reales. → dato de ⛔ FALTA en el expediente.

---

## V. El motor a construir: de interés a hábito

El §XXI pide un sistema que convierta **interés → comprensión → práctica → repetición → dominio →
hábito**, aprovechando el hiperfoco sin depender de él.

El diseño correcto para este perfil no es domesticar el hiperfoco. Es **encauzarlo y protegerse de su
retirada**, porque va a retirarse:

| Etapa | Qué se hace | Cómo se protege del bajón |
|---|---|---|
| **Interés** | Se entra por donde engancha: la materia leída desde el ángulo corporativo. Fiscal no es "Fiscal": es lo que decide la estructura de una adquisición | El interés es el combustible de arranque, no el del viaje |
| **Comprensión** | Aquí el rendimiento ya es alto. Se usa el tratado de la Biblioteca | Sin protección: es la fortaleza |
| **Práctica** | Casos y banco de preguntas **por escrito**. Escribir es el puente entre entender y poder | Producto tangible: si se abandona, quedó algo |
| **Repetición** | Anki en el traslado. **Aquí es donde se abandona siempre** | Se traslada a un momento que no compite con nada: 15 h semanales de transporte. No cuesta voluntad, cuesta abrir la app |
| **Dominio** | El examen aprobado | Fecha ajena — de ahí el sistema antifallas |
| **Hábito** | Racha visible | Racha, no ánimo. Se mide en el [tablero](./10_TABLERO_SEMANAL.md) |

**La decisión de diseño que sostiene la cadena** está en la fila de repetición: la etapa donde este
perfil históricamente falla se saca del tiempo que requiere voluntad y se mete en un tiempo que ya
está muerto. El repaso espaciado no compite con nada en un autobús. Esa sola reubicación convierte la
etapa más frágil en la más automática.

---

## VI. Las tres frases del diagnóstico

1. **No falta disciplina.** Hay 684,692 palabras que lo prueban. Falta **redirigirla**, y el remedio de
   "esforzarse más" es el que ya falló porque atacaba una causa inexistente.
2. **El único daño irreversible viene de las fechas**, y su causa es haber usado la memoria como
   registro. El rigor de verificación necesario ya existe y se aplicó 1,581 veces — a los artículos de
   ley, nunca al calendario.
3. **El riesgo mayor de este plan es este plan.** Un sistema de veintinueve secciones tiene todas las
   propiedades del trabajo en que este perfil rinde, y ninguna fecha límite. Si dentro de un mes la
   carpeta está mejorada y las fechas siguen sin capturar, el diagnóstico se confirmó por la vía
   dolorosa.

---

*Se relee cada 90 días. Si el patrón del §II cambió, este documento está obsoleto y hay que
reescribirlo — eso sería la mejor noticia posible.*
