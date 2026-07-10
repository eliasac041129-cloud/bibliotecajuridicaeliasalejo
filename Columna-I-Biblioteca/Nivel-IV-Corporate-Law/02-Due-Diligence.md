# [Nivel IV · Libro 2] Due Diligence (Debida Diligencia)

> ⟳ **Apóstrofe de vigencia — léela cada vez.** El Derecho cambia sin avisar: un artículo puede mudar de número, de redacción o quedar **derogado** de un día para otro. El símbolo **⟳** que aparece tras cada artículo citado en este libro significa una sola cosa: *«¿sigue vigente —y con este mismo número— hoy? No lo cites de memoria ni desde este libro: **reitéralo en su código vigente**»* (textos oficiales en [`../../fuentes-legales/`](../../fuentes-legales/)). Caso real: el **art. 390 del CPF** que este proyecto cotejó aparece hoy como **«Derogado»**. Recuerda: un **✅** dice que el dato fue verificado *palabra por palabra a la fecha de su fuente*; la **⟳** te avisa que esa fecha ya quedó atrás y que la última palabra la tiene el código, no el libro.


> Si el Libro 1 fue el **plano maestro** del M&A, este es el **arte de mirar antes de comprar**. La
> *due diligence* es la investigación sistemática mediante la cual el comprador descubre **qué está
> comprando realmente**: qué vale, qué riesgos esconde, qué contratos pueden caerse, qué pasivos
> ocultos pueden costar más que la empresa. Es la fase de la que depende **todo lo demás** —el precio,
> las *representations & warranties*, las indemnizaciones, las condiciones al *closing* y hasta la
> decisión de seguir o abandonar el deal—. Un abogado de M&A que no sabe hacer una due diligence
> rigurosa es como un cirujano que no sabe leer una radiografía.

**Etiquetas:** corporate law · M&A · due diligence · data room · red flags · gestión de riesgo · DD report
**Prerrequisitos:** [Libro 1 · Fundamentos de M&A](./01-Fundamentos-de-MA.md) + **todo el Nivel III** (especialmente [Sociedades/LGSM](../Nivel-III-Derecho-Mercantil/02-Sociedades-Mercantiles-LGSM.md), [Contratos Mercantiles](../Nivel-III-Derecho-Mercantil/04-Contratos-Mercantiles.md) y [Gobierno Corporativo](../Nivel-III-Derecho-Mercantil/07-Gobierno-Corporativo.md)) + [Obligaciones](../Nivel-II-Derecho-Civil-Profundo/01-Teoria-General-de-las-Obligaciones-Profundizacion.md) y [Responsabilidad Civil](../Nivel-II-Derecho-Civil-Profundo/03-Responsabilidad-Civil.md).
**Estándar:** V3 (43 secciones + secciones transversales).
**⏱ Tiempo estimado de dominio:** 4–5 semanas (≈ 45–55 h de estudio activo). Lectura de
reconocimiento: 8–10 h. *Estúdialo en bloques: qué es y por qué → tipos y áreas de la DD → proceso y
data room → red flags y materialidad → del hallazgo a la cláusula (DD report → SPA).*

> **Aviso de método.** Tratado, no repaso. Aquí aprenderás a **investigar como un abogado de
> transacciones**: no a "leer documentos", sino a **buscar el riesgo**, valorarlo y traducirlo en
> protección contractual. Cada sección conecta la due diligence con el SPA y con la asignación de
> riesgo que viste en el Libro 1.

---

### Nivel de importancia profesional (vista rápida)
```
Litigio              ★★★☆☆
Corporate            ★★★★★
M&A                  ★★★★★
Mercado de Valores   ★★★★☆
Venture Capital      ★★★★★
Private Equity       ★★★★★
Gobierno Corporativo ★★★★☆
Compliance           ★★★★★
Derecho Bancario     ★★★★☆
Empresa Familiar     ★★★★☆
```
*Es la habilidad operativa más demandada al abogado junior y de rango medio en M&A: el deal se gana o
se pierde en la calidad de la due diligence. Dominarla temprano acelera la carrera más que casi
cualquier otra cosa.*

## 1. Introducción

**Due diligence** (literalmente, "diligencia debida") es la **investigación previa y sistemática** que
realiza el comprador —con sus asesores legales, fiscales, financieros y técnicos— sobre la empresa que
pretende adquirir (la *target*), antes de comprometerse de forma definitiva. Su propósito es responder,
con evidencia, tres preguntas que el Libro 1 dejó planteadas: **¿qué estoy comprando realmente?**,
**¿cuánto vale de verdad?** y **¿qué riesgos estoy asumiendo?**

La expresión viene del derecho anglosajón, donde "diligencia debida" es el **estándar de conducta** que
se espera de una persona razonable y prudente antes de tomar una decisión de inversión. En el contexto
del M&A, la due diligence es la **fase de investigación** que se sitúa entre la **LOI/term sheet** (el
acuerdo preliminar) y el **SPA** (el contrato definitivo). Es el momento en que el comprador, que hasta
entonces solo conocía la empresa "por fuera" (el *Information Memorandum*, lo que el vendedor quiso
mostrar), abre la caja negra y examina sus entrañas: sus contratos, sus litigios, sus pasivos fiscales y
laborales, sus permisos, su propiedad intelectual, sus estados financieros.

La idea central de este libro: la due diligence **no es un trámite ni una formalidad**; es el
**corazón analítico** de toda operación de M&A y la principal **herramienta de gestión de riesgo** del
comprador. Todo lo que se descubre (o se deja de descubrir) tiene una consecuencia directa: baja el
precio, exige una *representation* específica, obliga a una indemnización especial, se vuelve una
condición al *closing*, o —en el peor caso— hace que el comprador se retire (*walk away*). Lo que **no
se investiga**, normalmente **no se cubre**; y lo que no se cubre, lo paga el comprador. Por eso decimos
que en M&A "la due diligence investiga y las reps reparten": esa frase, que enunciamos en el Libro 1,
es la columna vertebral de este libro.

## 2. Objetivos del libro

Al terminar, el lector será capaz de:

- **Explicar** qué es la due diligence, por qué existe y qué función cumple dentro del proceso de M&A,
  conectándola con la lógica de asignación de riesgo del Libro 1.
- **Distinguir** los **tipos** de due diligence (legal, fiscal, financiera/contable, laboral,
  regulatoria, ambiental, técnica, de PI, de compliance) y saber **qué busca cada una**.
- **Diseñar** un **plan de due diligence** proporcional al tamaño y al riesgo del deal: alcance,
  equipo, calendario, *checklist* de solicitud de información.
- **Operar** un **data room** (físico o virtual), entender la dinámica de las **Q&A** y proteger la
  confidencialidad y el privilegio.
- **Identificar y jerarquizar *red flags*** (banderas rojas) aplicando el concepto de **materialidad**:
  distinguir lo que mata el deal, lo que baja el precio y lo que solo se documenta.
- **Redactar** un **DD report** útil: ejecutivo, claro, orientado a decisiones, con hallazgos,
  valoración del riesgo y recomendaciones.
- **Traducir** cada hallazgo en una **protección contractual** concreta en el SPA: *representation*
  específica, indemnización especial, ajuste de precio, *escrow*, condición al *closing* o exclusión
  del perímetro.
- **Pensar como un abogado de transacciones**: buscar el riesgo, no solo describir documentos.

## 3. Importancia profesional

Para el abogado corporativo, la due diligence es —junto con la redacción del SPA— la **competencia
operativa central** del M&A, y la que **más temprano** se le exige. El abogado junior de un despacho de
M&A pasa buena parte de sus primeros años **dentro de la due diligence**: revisando contratos en el data
room, levantando *red flags*, redactando secciones del DD report. Hacerlo con rigor, criterio y
velocidad es lo que distingue al asociado que asciende del que se estanca.

¿Por qué es tan importante? Porque la due diligence es el punto donde el abogado **agrega más valor
medible**: cada riesgo que detecta y traduce en una protección contractual es dinero que le ahorra al
cliente; cada riesgo que se le escapa es una pérdida potencial que el cliente sufrirá después del
*closing*, cuando ya no haya remedio fácil. Un solo pasivo fiscal o ambiental no detectado puede valer
más que toda la operación. Por eso los clientes —fondos de *private equity*, corporativos, family
offices— evalúan a sus abogados, en gran medida, por la **calidad de su due diligence**.

Además, la due diligence es **transversal a todas las prácticas**: la misma habilidad se usa en una
adquisición (comprador), en una venta (la *vendor due diligence* que prepara el vendedor), en un
financiamiento (el banco hace su propia DD), en una inversión de *venture capital* o *private equity*,
en una salida a bolsa (*IPO*) y en compliance (la DD de terceros y anticorrupción). Quien domina la due
diligence tiene una herramienta que usará en **toda su carrera**, sea cual sea la operación.

## 4. Historia y origen

La due diligence, como práctica formalizada, nace en el **derecho del mercado de valores de Estados
Unidos**, en particular con la **Securities Act de 1933**, promulgada tras el *crash* de 1929. Esa ley
estableció que quienes participan en la colocación de valores (los *underwriters*, los bancos
colocadores) podían **defenderse** de la responsabilidad por información falsa o incompleta en un
prospecto si demostraban haber realizado una **investigación razonable** —una "diligencia debida"— sobre
la empresa emisora. De ahí el nombre: la *due diligence defense*. La diligencia debida era, en origen,
un **escudo de responsabilidad**: si investigaste con el cuidado de una persona prudente, no respondes
aunque después aparezca un problema que no podías razonablemente conocer.

De ese contexto bursátil, la práctica migró al **mundo de las fusiones y adquisiciones** durante la
segunda mitad del siglo XX, a medida que las operaciones se volvían más grandes, complejas y
apalancadas (especialmente con el auge de los *leveraged buyouts* en los años 1980). Los compradores
—y, sobre todo, los bancos que financiaban las compras— necesitaban un método riguroso para entender qué
estaban comprando o financiando. Los grandes despachos de Wall Street y de la City de Londres
desarrollaron metodologías, *checklists* y equipos especializados, y la due diligence se convirtió en
una **fase estándar e ineludible** de cualquier transacción seria.

En **México**, la práctica se profesionalizó a partir de los años 1990 con la apertura económica, la
llegada de la inversión extranjera, las grandes privatizaciones y la entrada de despachos
internacionales y de los estándares de los fondos globales. Hoy, ninguna operación relevante de M&A en
México se cierra sin una due diligence, y los despachos mexicanos de élite la ejecutan con estándares
plenamente internacionales.

## 5. Evolución histórica

La due diligence ha evolucionado en tres grandes etapas que conviene tener presentes:

**1) De escudo de responsabilidad a herramienta de inversión.** En su origen (años 1930-1960), la due
diligence era sobre todo una **defensa legal** en el contexto bursátil. Con el auge del M&A moderno, se
transformó en una **herramienta de decisión y de negociación**: ya no se investiga solo para "cubrirse",
sino para **valuar, negociar el precio y asignar el riesgo**.

**2) Del cuarto de documentos físico al data room virtual.** Durante décadas, la due diligence se hacía
en un **cuarto físico** (el *data room*), normalmente en las oficinas del vendedor o de sus abogados,
donde se apilaban cajas de documentos y los abogados del comprador acudían a revisarlos bajo vigilancia,
sin poder fotocopiar lo sensible. La revolución digital (años 2000 en adelante) trajo los **Virtual Data
Rooms (VDR)**: plataformas seguras en línea donde se cargan miles de documentos, con control de accesos,
marcas de agua, registro de quién vio qué y módulos de **Q&A**. Esto aceleró y globalizó la práctica:
hoy un equipo en Nueva York, Londres y Ciudad de México revisa el mismo data room simultáneamente.

**3) De la revisión exhaustiva a la due diligence inteligente y asistida por tecnología.** El volumen de
información creció tanto que revisar "todo" se volvió imposible y antieconómico. La práctica moderna se
orienta al **riesgo y a la materialidad**: se define un **umbral** (no se revisan contratos por debajo de
cierto monto), se prioriza lo crítico y se usa **tecnología** —herramientas de revisión de contratos
asistida por *machine learning*, que detectan cláusulas de *change of control*, de no competencia, de
exclusividad, etc.—. El abogado moderno no compite con la máquina en velocidad de lectura; compite en
**criterio**: saber qué buscar, qué significa lo que encuentra y cómo traducirlo en protección.

## 6. Contexto económico

Económicamente, la due diligence es un mecanismo para reducir la **asimetría de información**, el
problema que el premio Nobel George Akerlof describió en su célebre análisis del "mercado de los
limones": el vendedor **siempre sabe más** sobre la empresa que el comprador. Esa asimetría, si no se
corrige, lleva a dos males: o el comprador paga de más (porque no ve los defectos) o se retrae de
comprar (porque desconfía y descuenta en exceso). La due diligence es la inversión que el comprador hace
para **igualar el terreno informativo** y poder valuar con realismo.

Tiene, además, una clara **lógica de costo-beneficio**. La due diligence cuesta dinero (honorarios de
abogados, contadores, asesores; tiempo de los ejecutivos) y, sobre todo, **tiempo** —que en un deal es
un recurso crítico—. Por eso su alcance debe ser **proporcional**: en una compra de cientos de millones
se justifica una DD exhaustiva; en una adquisición pequeña, una DD focalizada en los riesgos clave. La
pregunta económica siempre es: *¿el costo de investigar este riesgo adicional es menor que la pérdida
esperada (probabilidad × impacto) si no lo investigo?* Ese cálculo —no la exhaustividad ciega— es lo que
guía a un buen abogado de M&A.

Finalmente, la due diligence influye directamente en el **precio y en la estructura**. Los hallazgos se
traducen en **descuentos** (el comprador baja su oferta), en **ajustes** (mecanismos de precio como el
*locked box* o el *completion accounts*), en **retenciones** (*escrow*, *holdback*) y en la propia
**elección de estructura** (un riesgo de pasivos ocultos alto empuja hacia un *asset deal* o hacia reps
e indemnizaciones reforzadas, como vimos en el Libro 1).

## 7. Contexto político y regulatorio

La due diligence no ocurre en el vacío: opera dentro de un marco regulatorio que, en ciertas áreas,
**la vuelve obligatoria o de altísimo riesgo omitirla**. Tres ejemplos centrales:

- **Competencia económica (COFECE).** Antes del *closing*, muchas operaciones requieren autorización de
  concentración. La DD debe evaluar si la operación es notificable y qué riesgo de competencia tiene
  (recuerda el *gun jumping* del Libro 1: no integrar antes de la autorización).
- **Anticorrupción y compliance (FCPA, UK Bribery Act, Ley General de Responsabilidades
  Administrativas).** Si la *target* incurrió en corrupción, el comprador puede **heredar la
  responsabilidad** (sucesión de responsabilidad). Las autoridades de EE.UU. han sido explícitas: una
  due diligence anticorrupción rigurosa es esperada, y su ausencia agrava la sanción. Esta es una de las
  áreas donde "no investigar" es jurídicamente peligrosísimo.
- **Sectores regulados.** En banca, seguros, telecomunicaciones, energía, salud, etc., el cambio de
  control puede requerir autorización del regulador sectorial, y la DD debe mapear permisos, concesiones
  y licencias y verificar su **transferibilidad** y su vigencia.

A esto se suman las tendencias regulatorias recientes: el **escrutinio de inversión extranjera** en
sectores estratégicos (presente en muchas jurisdicciones), la regulación de **protección de datos**
(que vuelve la DD de privacidad cada vez más relevante) y los crecientes requerimientos **ESG**, que han
dado lugar a una *due diligence* de sostenibilidad y derechos humanos en las cadenas de suministro.

## 8. Contexto social

Aunque la due diligence parezca un asunto puramente técnico-financiero, tiene una dimensión social y
humana que el buen abogado no ignora. **Primero**, la DD toca a las **personas** de la empresa: la
revisión laboral examina contratos, sindicatos, pasivos por despidos, planes de pensiones; los hallazgos
pueden anticipar reestructuras y despidos post-*closing*, con impacto real en trabajadores y comunidades.
Manejar esa información con sensibilidad y confidencialidad es parte del oficio.

**Segundo**, la due diligence se desarrolla en un clima de **tensión y desconfianza estructural**: el
vendedor quiere mostrar lo mejor y minimizar lo malo; el comprador busca defectos. El abogado opera en
esa tensión y debe equilibrar **rigor** (encontrar todo lo relevante) con **eficiencia diplomática** (no
incendiar la relación con peticiones desmesuradas que descarrilen el deal). La habilidad social —saber
qué preguntar, cómo y a quién— es tan importante como la técnica.

**Tercero**, en operaciones con dimensión social fuerte (empresas familiares, negocios con arraigo
local, ESG), la DD revela información sensible sobre prácticas ambientales, condiciones laborales o
relaciones con comunidades. El abogado moderno entiende que estos hallazgos no son solo "riesgos
legales", sino también **riesgos reputacionales** que pueden afectar el valor y la viabilidad del
negocio adquirido.

## 9. Contexto empresarial

Desde la perspectiva de la empresa y del inversionista, la due diligence cumple funciones que van más
allá de lo jurídico. Para el **comprador estratégico** (una empresa que adquiere a otra de su sector),
la DD no solo busca riesgos: también **verifica las sinergias** que justifican el precio (¿son reales
los ahorros de costos, las ventas cruzadas, el acceso a mercados?) y sirve para **planear la
integración** post-*closing* (conocer los sistemas, los contratos, la plantilla). Para el **comprador
financiero** (un fondo de *private equity*), la DD valida la **tesis de inversión**: la calidad de los
flujos (la *Quality of Earnings*), la capacidad de la empresa para soportar el apalancamiento del LBO y
las palancas de creación de valor para el *exit*.

La due diligence también moldea la **gobernanza del deal**: sus hallazgos suben a los comités de
inversión y a los consejos, que deciden si aprobar, a qué precio y con qué condiciones. Un buen DD report
es, en la práctica, **el documento sobre el que se toma la decisión de invertir millones**. De ahí que
su redacción —ejecutiva, clara, jerarquizada por riesgo— sea una habilidad de primer orden.

Conviene también distinguir la **buy-side due diligence** (la que hace el comprador, el caso típico) de
la **vendor due diligence o VDD** (la que el vendedor encarga sobre su propia empresa antes de venderla,
para anticipar problemas, ordenar la casa y agilizar el proceso, entregando un reporte a los posibles
compradores). La VDD es cada vez más común en procesos competitivos (subastas) porque acelera el deal y
fortalece la posición negociadora del vendedor. Ambas usan la misma técnica; cambian el cliente y el
objetivo.

## 10. Definiciones doctrinales

La doctrina especializada en M&A define la due diligence con matices que vale la pena conocer porque
revelan distintas facetas de la institución:

- **Como proceso de investigación:** la due diligence es *"el proceso de investigación y análisis que
  un comprador potencial realiza sobre una empresa objetivo para evaluar sus activos, pasivos, riesgos y
  oportunidades antes de consumar una adquisición"*. Esta definición subraya su carácter **procesal y
  analítico**.
- **Como gestión de riesgo:** otros autores la definen como *"el ejercicio sistemático de
  identificación, valoración y asignación de los riesgos asociados a una transacción"*. Aquí el énfasis
  está en su función de **risk management**: no basta encontrar el riesgo, hay que valorarlo y decidir
  quién lo soporta.
- **Como estándar de conducta (origen anglosajón):** en su acepción original, *"diligencia debida"* es
  el **grado de cuidado** que una persona razonable y prudente emplearía en sus propios asuntos antes de
  tomar una decisión de inversión. Esta es la raíz del concepto: un **estándar de comportamiento
  diligente** cuya satisfacción genera consecuencias jurídicas (la *due diligence defense*).
- **Como puente entre la información y el contrato:** la doctrina transaccional moderna la describe como
  *"el mecanismo que traduce la realidad de la empresa en cláusulas del contrato de compraventa"*. Esta
  es, quizá, la definición más útil para el abogado: la DD es el **puente** entre lo que la empresa **es**
  y lo que el SPA **dice**.

Ninguna definición es completa por sí sola. La due diligence es, a la vez, **proceso** (cómo se hace),
**función** (para qué sirve: gestionar riesgo) y **estándar** (con qué grado de cuidado). El abogado
maduro las integra: investiga con rigor (proceso), para asignar el riesgo (función), con el cuidado de
un profesional prudente (estándar).

## 11. Definiciones legales y marco normativo

A diferencia de otras instituciones de este programa, la due diligence **no está regulada por una ley
específica que la defina y la imponga en términos generales** en el M&A privado mexicano. Es,
fundamentalmente, una **práctica contractual y profesional** —un *uso* del comercio internacional
adoptado en México—. Sin embargo, el ordenamiento jurídico la rodea y la conecta por varias vías:

- **Securities Act de 1933 (EE.UU.), §11 y §12:** la fuente histórica. Establece la *due diligence
  defense* para los participantes en una colocación de valores: la investigación razonable como eximente
  de responsabilidad por información defectuosa en el prospecto. Es derecho extranjero, pero su lógica
  permea toda la práctica global.
- **Deberes fiduciarios del administrador (deber de diligencia):** en México, la **LGSM** y la **Ley del
  Mercado de Valores** imponen a los administradores el deber de obrar con la **diligencia de un
  administrador prudente** y de manera **informada**. Un consejo que aprueba una adquisición relevante
  **sin** una due diligence adecuada puede estar incumpliendo su deber de diligencia (recuerda *Smith v.
  Van Gorkom* del libro de Gobierno Corporativo: decidir sin informarse rompe la *business judgment
  rule*). Aquí la DD deja de ser opcional: es parte del **proceso informado** que exige el deber
  fiduciario.
- **Régimen de competencia económica (LFCE):** impone la obligación de **notificar** concentraciones que
  superen ciertos umbrales y de no consumarlas antes de la autorización; la DD evalúa esta exposición.
- **Régimen anticorrupción y de prevención de lavado:** la **FCPA**, la **UK Bribery Act** y la **Ley
  General de Responsabilidades Administrativas** generan, en la práctica, una **exigencia de DD de
  compliance**: el comprador puede heredar responsabilidad, y la ausencia de investigación agrava la
  posición.
- **Obligaciones de información y buena fe (Código Civil/Código de Comercio):** los deberes
  precontractuales de información y de buena fe en la negociación (que estudiaste en Obligaciones y
  Contratos) son el telón de fondo civil que da sustento al intercambio de información durante la DD y a
  la responsabilidad por dolo o reticencia del vendedor.

En síntesis: la due diligence no nace de un artículo que ordene "harás due diligence", sino de la
**convergencia** del deber fiduciario de diligencia, del régimen de responsabilidad, de la buena fe
contractual y de la práctica profesional internacional. Es derecho **vivo y consuetudinario** antes que
codificado.

## 12. Definición sencilla

Imagina que vas a comprar una **casa usada**. Antes de firmar y pagar, harías —si eres prudente— varias
cosas: contratarías a un **arquitecto** para que revise si hay grietas, humedad o problemas
estructurales; pedirías al Registro Público que confirme que el vendedor es el **dueño real** y que la
casa no tiene **hipotecas, embargos o deudas**; revisarías que no haya **adeudos** de predial, agua o
mantenimiento; verificarías que los **permisos** de construcción estén en regla; y comprobarías que no
haya un **inquilino** con derecho a quedarse. Toda esa investigación —mirar **antes** de comprar, para
saber qué estás comprando y qué problemas escondidos puede tener— es la **due diligence**.

La due diligence en M&A es exactamente eso, pero sobre una **empresa** en lugar de una casa, y mil veces
más compleja: en vez de revisar grietas y la escritura, revisas **contratos, litigios, impuestos,
permisos, deudas laborales, propiedad intelectual y estados financieros**. La pregunta es la misma:
*¿qué estoy comprando de verdad, cuánto vale y qué problemas trae escondidos?* Y la lógica también: lo
que descubres te sirve para **bajar el precio, pedir garantías al vendedor, o retirarte si la casa está
podrida por dentro**.

## 13. Conceptos fundamentales

Antes de entrar al desarrollo, fija estos **conceptos clave** que se usarán en todo el libro. Aprende
cada término con su definición rigurosa; son el vocabulario del oficio.

- **Target (empresa objetivo):** la empresa que se pretende adquirir, sobre la cual recae la
  investigación.
- **Buy-side / Sell-side:** el lado del comprador / el lado del vendedor. La DD típica es *buy-side*; la
  *vendor due diligence* (VDD) es *sell-side*.
- **Data room (cuarto de datos):** el repositorio —hoy casi siempre virtual (**VDR**)— donde el vendedor
  pone a disposición del comprador la información y los documentos de la *target* para su revisión.
- **Due diligence request list (DDRL) / checklist:** la **lista de solicitud de información**: el
  documento donde el comprador pide, ordenadamente y por áreas, todos los documentos que necesita
  revisar.
- **Q&A (preguntas y respuestas):** el proceso, gestionado dentro del data room, mediante el cual el
  comprador formula preguntas sobre la información y el vendedor responde. Genera un **rastro
  documental** importante.
- **Red flag (bandera roja):** un hallazgo que representa un **riesgo relevante**. Se distinguen por
  gravedad: las que pueden **matar el deal** (*deal breakers*), las que **bajan el precio** o exigen
  protección, y las que solo se **documentan**.
- **Materialidad (*materiality*):** el **umbral de relevancia** a partir del cual un hallazgo importa.
  Es un concepto central: se fija un monto o un criterio (p. ej., "solo revisamos contratos de más de
  X" o "solo reportamos contingencias superiores a Y") para concentrar el esfuerzo en lo que de verdad
  mueve la aguja.
- **DD report (reporte de due diligence):** el documento donde el equipo plasma los **hallazgos**, su
  **valoración** y sus **recomendaciones**. Puede ser *full report* (exhaustivo) o *red flag report*
  (solo los riesgos relevantes, el más usado en la práctica moderna).
- **Disclosure schedules (anexos de revelación):** los anexos del SPA donde el vendedor **revela
  excepciones** a sus *representations*. Son la otra cara de la DD: lo que el vendedor revela aquí,
  normalmente **deja de estar cubierto** por la garantía. La DD y los *disclosure schedules* dialogan
  constantemente.
- **Representations & warranties (declaraciones y garantías):** las afirmaciones que el vendedor hace
  sobre la *target* en el SPA (p. ej., "no hay litigios distintos de los revelados"). Son el principal
  vehículo para **asignar al vendedor** el riesgo de lo que la DD no pudo verificar del todo.
- **Indemnification (indemnización):** el mecanismo por el cual el vendedor se obliga a **compensar** al
  comprador si una *representation* resulta falsa o si se materializa un riesgo identificado. Suele venir
  con **topes** (*caps*), **mínimos** (*baskets/de minimis*) y **plazos de supervivencia**.
- **Escrow / holdback:** la **retención** de una parte del precio (en una cuenta de garantía o por el
  propio comprador) para responder por eventuales indemnizaciones. Es la DD convertida en **garantía de
  cobro**.
- **Condition precedent (condición al closing):** un requisito que debe cumplirse **antes** del cierre
  (p. ej., obtener una autorización o subsanar un hallazgo de la DD).
- **Walk-away right (derecho a retirarse):** la facultad del comprador de **abandonar** la operación si
  la DD revela algo inaceptable o si no se cumplen las condiciones.
- **Quality of Earnings (QoE):** el análisis financiero que evalúa la **calidad y sostenibilidad** de
  las utilidades de la *target* (cuánto del resultado es recurrente y real). Es central en la DD
  financiera, sobre todo para fondos.

Con este vocabulario fijado, ya podemos entrar al **desarrollo absoluto** de la materia.

## 14. Desarrollo absoluto

Esta es la sección central del libro. La desarrollamos en cinco bloques: **(A)** las áreas o tipos de
due diligence —qué se investiga y qué busca cada especialista—; **(B)** el proceso y sus fases —cómo se
ejecuta de principio a fin—; **(C)** el data room y la dinámica de Q&A —dónde y cómo se revisa—; **(D)**
los *red flags* y la materialidad —cómo se jerarquiza el riesgo—; y **(E)** del hallazgo a la cláusula
—cómo cada riesgo se traduce en protección contractual—. Estúdialos en ese orden: primero qué se busca,
luego cómo, después cómo se valora y, por último, qué se hace con lo encontrado.

### 14.A · Las áreas de la due diligence (qué se investiga y qué busca cada una)

La due diligence es **multidisciplinaria**: distintos especialistas revisan distintas dimensiones de la
*target*, coordinados por el abogado de M&A (que suele actuar como director de orquesta del *workstream*
legal y como punto de integración de los hallazgos). Estas son las áreas principales. Aprende, de cada
una, **qué busca** y **cuáles son sus *red flags* típicos**.

**1) Due diligence corporativa/societaria.** Es la base. Verifica que la *target* **existe legalmente y
es lo que dice ser**: acta constitutiva y estatutos vigentes; que las **acciones existen y están
válidamente emitidas y pagadas**; el **libro de registro de accionistas** (¿quién es realmente dueño de
qué?); las actas de asambleas y de consejo; los poderes vigentes; y, crucialmente, la **cadena de
titularidad** (¿el vendedor es de verdad el dueño de las acciones que vende?). *Red flags típicos:*
acciones mal emitidas, capital no pagado, conflictos entre socios, opciones o convertibles olvidados que
diluyen, poderes revocados, falta de quórum en decisiones clave. **Sin propiedad clara de las acciones,
no hay nada que comprar**: esta área es condición de todo lo demás.

**2) Due diligence contractual.** Revisa los **contratos materiales** de la empresa: con clientes,
proveedores, distribuidores, arrendamientos, financiamientos, licencias. Busca tres cosas sobre todo:
**(i)** cláusulas de **change of control** (que permiten a la contraparte terminar o renegociar el
contrato si la *target* cambia de dueño —el riesgo de que el activo se evapore justo al comprar—);
**(ii)** cláusulas de **exclusividad, no competencia o *most favored nation*** que limiten el negocio; y
**(iii)** **obligaciones onerosas, penas, garantías o plazos** problemáticos. *Red flags típicos:*
contratos clave con *change of control*, dependencia de un solo cliente o proveedor, contratos vencidos
o sin firmar, penalizaciones desproporcionadas.

**3) Due diligence fiscal.** Examina la **situación tributaria**: declaraciones, pago de impuestos,
créditos fiscales, devoluciones, regímenes especiales, precios de transferencia (operaciones
intragrupo), y **contingencias fiscales** (impuestos que la autoridad podría reclamar). Es de las áreas
más delicadas porque los pasivos fiscales **pueden ser enormes y ocultos**, y porque la estructura de la
operación (share vs. asset) tiene fuertes consecuencias fiscales. *Red flags típicos:* esquemas
agresivos de elusión, deducciones cuestionables, precios de transferencia sin soporte, créditos fiscales
inexistentes, omisiones que prescriben pronto, contingencias por operaciones simuladas (en México, el
temido riesgo de **EFOS/EDOS** —empresas que facturan operaciones simuladas—).

**4) Due diligence financiera y contable (incluye Quality of Earnings).** Verifica que los **estados
financieros reflejen la realidad** y analiza la **calidad de las utilidades** (QoE): cuánto del
resultado es **recurrente y sostenible** frente a lo que es extraordinario o "maquillado". Revisa deuda
(incluida la **deuda oculta** y los pasivos contingentes), capital de trabajo, la caja real, y la base
sobre la que se calculará el precio. *Red flags típicos:* ingresos inflados o reconocidos antes de
tiempo, gastos capitalizados indebidamente, deuda no revelada, dependencia de ingresos no recurrentes,
capital de trabajo deteriorado.

**5) Due diligence laboral y de seguridad social.** Revisa la **relación con los trabajadores**:
contratos, plantilla, sindicatos y contrato colectivo, prestaciones, planes de pensiones, pasivos por
despidos, juicios laborales, y el cumplimiento de cuotas de seguridad social (IMSS, INFONAVIT) y de la
normativa sobre **subcontratación** (en México, la reforma que prohibió la subcontratación de personal,
con fuertes contingencias para quien la usó mal). *Red flags típicos:* juicios laborales numerosos,
pasivos por pensiones subvaluados, esquemas de *outsourcing* ilegales, sindicato hostil, pasivos por
prima de antigüedad.

**6) Due diligence regulatoria y de permisos.** Verifica que la *target* tiene **todos los permisos,
licencias, concesiones y autorizaciones** que su actividad requiere, que están **vigentes** y que son
**transferibles** (o que sobreviven al cambio de control). En sectores regulados (banca, energía,
telecom, salud), evalúa si la operación requiere **autorización del regulador**. *Red flags típicos:*
operar sin permiso, permisos a punto de vencer o no transferibles, incumplimientos sancionables,
concesiones con cláusulas de reversión.

**7) Due diligence de competencia económica (antitrust).** Evalúa si la operación es **notificable** a
la COFECE (o a autoridades extranjeras si hay efectos transfronterizos), el **riesgo de que se objete**
(por crear poder de mercado) y el calendario que ello impone. Conecta directamente con el *gun jumping*
del Libro 1. *Red flags típicos:* alta concentración resultante, riesgo de condiciones o de bloqueo,
operaciones previas no notificadas.

**8) Due diligence ambiental.** Especialmente relevante en industria, energía, minería, inmobiliario y
manufactura. Revisa permisos ambientales, cumplimiento de la normativa, **pasivos por contaminación**
(que pueden ser enormes y de largo plazo), estudios de impacto, y responsabilidad por sitios
contaminados. *Red flags típicos:* suelos o aguas contaminados, falta de autorización de impacto
ambiental, sanciones de la autoridad ambiental, pasivos de remediación.

**9) Due diligence de propiedad intelectual (PI) y tecnología.** Verifica la **titularidad y vigencia**
de marcas, patentes, derechos de autor y nombres de dominio; que la PI **clave del negocio sea
propiedad de la target** (y no de un fundador a título personal, error frecuente en *startups*); las
licencias (especialmente de software, incluido el riesgo del *open source*); y litigios de
infracción. *Red flags típicos:* PI registrada a nombre equivocado, marcas no renovadas, licencias de
software sin pagar, software propio que infringe *open source*, dependencia de PI de terceros.

**10) Due diligence de tecnología, datos y ciberseguridad.** Cada vez más central. Revisa los sistemas,
la dependencia tecnológica, el cumplimiento de **protección de datos personales** (consentimientos,
avisos de privacidad, transferencias), y el historial de **incidentes de ciberseguridad** (brechas de
datos que generan pasivos y daño reputacional). *Red flags típicos:* brechas de datos no reportadas,
incumplimiento de la normativa de privacidad, sistemas obsoletos, dependencia de un proveedor crítico.

**11) Due diligence de compliance y anticorrupción.** Revisa el **programa de cumplimiento** de la
*target*, su exposición a **corrupción** (especialmente si hace negocios con el gobierno o en
jurisdicciones de riesgo), prevención de lavado de dinero, sanciones internacionales, y conflictos de
interés. Como vimos, aquí "no investigar" es peligrosísimo: el comprador puede **heredar la
responsabilidad** por actos de corrupción de la *target*. *Red flags típicos:* pagos sospechosos a
funcionarios o intermediarios, ausencia de programa de compliance, operaciones en países sancionados,
banderas de lavado.

**12) Due diligence de litigios y contingencias.** Mapea **todos los juicios y procedimientos** en los
que la *target* es parte (civiles, mercantiles, laborales, fiscales, administrativos, penales) y estima
su **probabilidad e impacto**. Es transversal a varias áreas. *Red flags típicos:* litigios de alto
monto, demandas colectivas, investigaciones de autoridades, contingencias mal provisionadas.

**Cómo encaja todo:** el abogado de M&A **coordina** estas áreas, integra los hallazgos en una **visión
de riesgo única** y los traduce en decisiones de precio, estructura y contrato. No necesita ser experto
fiscal o ambiental, pero **sí** debe saber qué busca cada área, **leer** sus reportes con criterio
jurídico y **conectar** los puntos: un *red flag* fiscal puede exigir una indemnización especial; uno de
*change of control*, una condición al *closing*; uno ambiental grave, un descuento, un *escrow* o el
abandono del deal.

### 14.B · El proceso de due diligence (de principio a fin)

La due diligence no es leer documentos al azar: es un **proceso ordenado** con fases bien definidas.
Domínalo como un protocolo; así sabrás siempre en qué punto estás y qué falta.

**Fase 0 — Preparación y *scoping* (definir el alcance).** Antes de pedir un solo documento, el equipo
define el **alcance** (*scope*): ¿qué áreas se revisan?, ¿con qué profundidad?, ¿cuál es el **umbral de
materialidad** (no revisar contratos por debajo de cierto monto)?, ¿cuál es el calendario y el
presupuesto? El alcance se fija según el **tamaño y el riesgo** del deal y según la **tesis** del
comprador (un estratégico mira sinergias e integración; un fondo mira QoE y capacidad de
apalancamiento). *Error clásico del junior:* lanzarse a revisar sin un *scope* claro y ahogarse en
documentos irrelevantes. **El alcance bien definido es la mitad del trabajo.**

**Fase 1 — Solicitud de información (*request list* / DDRL).** El comprador entrega al vendedor una
**lista estructurada** de la información que necesita, organizada por áreas (corporativo, contractual,
fiscal, laboral, etc.). Las *request lists* suelen partir de un *checklist* maestro del despacho que se
**adapta** al deal concreto. La calidad de la lista marca el ritmo: pedir de más satura y enoja; pedir
de menos deja huecos de riesgo. Es habitual hacer **rondas** (una lista inicial y solicitudes
complementarias según lo que se va encontrando).

**Fase 2 — Apertura y población del data room.** El vendedor **carga** la información solicitada en el
**Virtual Data Room (VDR)**, organizada en carpetas que normalmente espejan la *request list*. El
comprador obtiene accesos (con distintos niveles según la sensibilidad). En procesos competitivos
(subastas), el vendedor controla qué se revela y cuándo (a veces hay información ultrasensible —precios,
clientes— que solo se abre en fases avanzadas o en un *clean room* para evitar problemas de competencia).

**Fase 3 — Revisión y análisis.** El equipo del comprador **revisa** sistemáticamente, área por área,
registrando hallazgos. Aquí entran el criterio, la técnica y, hoy, la **tecnología** de revisión asistida
(para detectar cláusulas tipo en grandes volúmenes de contratos). Cada revisor levanta los **red flags**
de su área y los documenta con referencia precisa (qué documento, qué cláusula, qué riesgo, qué impacto
estimado).

**Fase 4 — Q&A (preguntas y respuestas).** Cuando la información del data room es insuficiente, ambigua o
genera dudas, el comprador formula **preguntas** a través del módulo de Q&A del VDR, y el vendedor
responde. Este proceso: **(i)** llena los huecos de información; **(ii)** genera un **rastro documental**
valioso (las respuestas del vendedor pueden ser, en sí mismas, una forma de revelación o de
*representation* informal); y **(iii)** permite calibrar la **transparencia y cooperación** del vendedor
(un vendedor evasivo es, en sí mismo, una bandera).

**Fase 5 — Reporte (DD report).** El equipo consolida los hallazgos en el **DD report** (típicamente un
*red flag report*: solo lo relevante). Aquí la información cruda se convierte en **inteligencia para la
decisión**: hallazgo → riesgo → impacto → recomendación. Lo veremos a fondo en la sección 14.E y en la
sección 21.

**Fase 6 — Traducción al contrato y a la negociación.** Los hallazgos **alimentan** la negociación del
precio y la redacción del SPA: reps específicas, indemnizaciones especiales, ajustes, *escrow*,
condiciones al *closing*, exclusiones del perímetro. Esta es la fase donde la DD **paga**: un hallazgo
que no se traduce en protección contractual es trabajo perdido.

**Fase 7 — DD confirmatoria (entre *signing* y *closing*).** Si hay separación entre firma y cierre
(*gap*), suele hacerse una **due diligence confirmatoria** o de actualización (*bring-down*): verificar
que nada relevante cambió, que las condiciones se cumplieron y que las reps siguen siendo ciertas a la
fecha del *closing*. Conecta con los *covenants* de operación ordinaria y con la cláusula MAC del Libro 1.

**Una idea rectora del proceso:** la due diligence es **iterativa**, no lineal. Lo que se encuentra en
una fase genera nuevas preguntas y nuevas solicitudes en la anterior. El buen abogado **navega** ese
ciclo con orden, sin perder de vista ni el bosque (la tesis del deal y el riesgo agregado) ni los árboles
(el hallazgo concreto en la cláusula concreta).

### 14.C · El data room y la dinámica de la información

El **data room** es el escenario físico (hoy virtual) de la due diligence, y entender su dinámica es
parte del oficio.

**Del cuarto físico al VDR.** Como vimos, antes era un cuarto con cajas de documentos vigilado; hoy es
una **plataforma en línea segura** (Virtual Data Room). El VDR aporta ventajas decisivas: acceso
simultáneo de equipos en varias ciudades, **control de permisos** por usuario y por carpeta, **marcas de
agua** y bloqueo de descarga/impresión para lo sensible, y un **registro de auditoría** (*audit log*)
que muestra quién vio qué y cuándo —dato relevante si después se discute qué fue revelado—.

**Estructura del data room.** Suele organizarse en carpetas que espejan las áreas de la DD: 1.
Corporativo; 2. Contratos materiales; 3. Fiscal; 4. Financiero; 5. Laboral; 6. Permisos y regulatorio;
7. Propiedad intelectual; 8. Litigios; 9. Inmuebles; 10. Seguros; etc. Un data room **bien organizado**
acelera la revisión; uno caótico (documentos sin nombrar, escaneos ilegibles, faltantes) es, en sí
mismo, una **señal** sobre la calidad de la gestión de la *target*.

**La dinámica de poder informativo.** El vendedor **controla** qué pone en el data room y cómo lo
presenta; el comprador busca lo que falta y lo que se esconde. Por eso el abogado del comprador debe leer
no solo lo que **está**, sino detectar lo que **no está** (¿por qué no hay contrato con el principal
cliente?, ¿por qué falta el dictamen fiscal de un año?). Las **ausencias** suelen decir tanto como los
documentos.

**Q&A: el arte de preguntar.** El módulo de Q&A es una herramienta poderosa y delicada. Buenas prácticas:
**(i)** preguntar de forma **precisa y referenciada** (a qué documento se refiere la pregunta); **(ii)**
escalar la presión de forma gradual (primero pedir el documento faltante, luego preguntar por su
ausencia); **(iii)** documentar todo (las respuestas pueden tener valor probatorio o servir de base a una
*representation*); y **(iv)** cuidar el **tono** (un Q&A agresivo o desmesurado puede deteriorar la
relación y el deal). Recuerda: lo que el vendedor **responde** o **revela** en el Q&A puede luego limitar
su responsabilidad (si reveló un problema, difícilmente podrá el comprador reclamar después por algo que
**sabía**: es el principio anglosajón del *sandbagging*, que se negocia expresamente en el SPA).

**Confidencialidad y privilegio.** Todo el ejercicio se ampara en el **NDA** firmado al inicio (Libro 1).
Además, el abogado debe cuidar el **secreto profesional / privilegio legal**: ciertos documentos
(opiniones legales, análisis de litigios) son sensibles, y su manejo en el data room debe proteger el
privilegio para que no se entienda renunciado. En operaciones transfronterizas, las reglas de privilegio
varían por jurisdicción —un punto fino que distingue al abogado sofisticado—.

**Información competitivamente sensible y *clean teams*.** Cuando comprador y *target* son competidores,
revelar precios, clientes o estrategias durante la DD puede violar la **ley de competencia** (intercambio
de información sensible, *gun jumping* informativo). La solución profesional son los **clean teams**:
equipos restringidos (a veces asesores externos) que revisan la información ultrasensible **sin**
trasladarla a quienes toman decisiones comerciales hasta que la operación se autoriza y cierra. Es un
matiz avanzado, pero crítico en deals entre competidores.

### 14.D · Red flags y materialidad (cómo se jerarquiza el riesgo)

Encontrar problemas es fácil; **toda** empresa los tiene. El arte de la due diligence no es hacer una
lista infinita de defectos, sino **jerarquizar**: distinguir lo que importa de lo que no, y dentro de lo
que importa, lo grave de lo manejable. Dos conceptos gobiernan esta jerarquía: la **materialidad** y la
**clasificación de los red flags**.

**La materialidad (*materiality*).** Materialidad es el **umbral de relevancia**: el punto a partir del
cual un hallazgo merece atención, reporte o protección contractual. Sin un umbral, el equipo se ahoga y
el DD report se vuelve inútil (mil hallazgos triviales esconden los cinco que de verdad importan). La
materialidad se fija de dos formas: **cuantitativa** (un monto: "solo revisamos/reportamos contingencias
superiores a X"; "solo contratos por encima de Y") y **cualitativa** (por naturaleza del riesgo: ciertos
temas —corrupción, titularidad de las acciones, permisos esenciales, *change of control* en el contrato
clave— importan **aunque** el monto sea bajo, porque ponen en riesgo el negocio mismo o generan
responsabilidad penal/regulatoria). El abogado experto **calibra** la materialidad al inicio (en el
*scoping*) y la ajusta sobre la marcha. Esta misma noción reaparecerá en el SPA: las reps suelen tener
*materiality qualifiers* ("salvo por lo que no sea material...") que se negocian palabra por palabra.

**La clasificación de los red flags.** Un buen reporte clasifica cada hallazgo según su gravedad. Un
esquema práctico de tres (o cuatro) niveles:

- **🔴 Deal breaker (mata el deal):** riesgo tan grave que, si no se resuelve, justifica **abandonar** la
  operación. Ejemplos: la *target* no es realmente dueña de su activo principal; un pasivo fiscal o
  ambiental que excede el valor de la empresa; corrupción sistémica con exposición penal; ausencia del
  permiso sin el cual el negocio no puede operar. Ante un *deal breaker*, las opciones son: resolverlo
  antes del *closing* (condición), reestructurar radicalmente, o retirarse.
- **🟠 Riesgo mayor (afecta precio/estructura/protección):** riesgo relevante pero **manejable** mediante
  herramientas contractuales. Es el caso más frecuente y el corazón del trabajo. Ejemplos: una
  contingencia fiscal significativa pero acotada (→ indemnización especial + *escrow*); un contrato clave
  con *change of control* (→ consentimiento como condición al *closing*); un litigio relevante (→ rep
  específica + indemnización). Estos hallazgos **no matan el deal**: lo **reprecian** y lo **blindan**.
- **🟡 Riesgo menor / a documentar:** hallazgos de bajo impacto que se **registran** (para tenerlos
  mapeados, exigir su subsanación o cubrirlos con reps generales), pero que no mueven el precio ni la
  estructura. Ejemplos: contratos menores vencidos pero renovables, formalidades societarias pendientes
  de bajo riesgo.
- **🟢 Sin observaciones / conforme:** áreas revisadas donde no se encontró riesgo relevante. Reportarlo
  también es valioso: da **confianza** y delimita el alcance de lo revisado.

**La matriz de riesgo (probabilidad × impacto).** Para jerarquizar con rigor, el abogado piensa cada
hallazgo en dos ejes: **probabilidad** de que el riesgo se materialice y **impacto** (cuánto costaría si
ocurre). Lo de **alta probabilidad y alto impacto** es prioridad uno; lo de **baja probabilidad y bajo
impacto**, se documenta y sigue. Esta matriz —heredada de la gestión de riesgo— es la herramienta mental
que convierte una lista de defectos en una **estrategia de protección**.

**Una advertencia de criterio.** El junior tiende a reportar **todo** con el mismo tono alarmante (para
"cubrirse"), lo que vuelve el reporte inútil y mina su credibilidad. El abogado maduro **jerarquiza y
recomienda**: dice qué es grave, qué es manejable y qué es ruido, y **propone** la solución contractual.
La diferencia entre "encontré 200 problemas" y "encontré 200 hallazgos, de los cuales 3 son críticos y
así los resolvemos" es la diferencia entre un revisor de documentos y un **asesor de transacciones**.

### 14.E · Del hallazgo a la cláusula (la due diligence se convierte en protección)

Aquí está la **lección más importante de todo el libro**, la que separa a quien "hace due diligence" de
quien **agrega valor**: cada hallazgo relevante debe **traducirse** en una protección contractual
concreta. La due diligence que no se traduce en el SPA es trabajo desperdiciado. Estas son las **seis
herramientas** de traducción y cuándo se usa cada una:

**1) Ajuste de precio (descuento).** Cuando el hallazgo revela que la empresa **vale menos** de lo
pensado (deuda mayor, capital de trabajo deteriorado, ingresos no recurrentes, un pasivo cierto), la
respuesta natural es **bajar el precio**. *Ejemplo:* la DD financiera revela que el 30% de los ingresos
provenían de un contrato que ya terminó → el comprador reduce su oferta o cambia el múltiplo de
valuación.

**2) Representation & warranty específica.** Cuando el hallazgo revela un **área de riesgo** sobre la que
el comprador quiere que el vendedor **garantice** un estado de cosas, se redacta una **rep específica**.
*Ejemplo:* la DD detecta un historial de problemas de cumplimiento ambiental → se exige una rep robusta
de que "la *target* cumple en todos los aspectos materiales con la normativa ambiental, salvo lo
revelado en el *disclosure schedule* X". Si la rep resulta falsa, se activa la indemnización.

**3) Indemnización especial (*special / specific indemnity*).** Cuando el hallazgo revela un riesgo
**concreto e identificado** (no una incertidumbre general), no basta una rep: se pacta una
**indemnización específica** que cubre **ese** riesgo nominalmente, a menudo **fuera de los topes y
mínimos** generales y **aunque el riesgo ya fuera conocido**. *Ejemplo:* la DD fiscal identifica una
contingencia concreta por una deducción cuestionable de 2022 → indemnización especial del vendedor por
"cualquier crédito fiscal derivado de la deducción X del ejercicio 2022", al 100% y sin tope. Esta es la
herramienta estrella para los *red flags* mayores **conocidos**.

**4) Retención del precio (*escrow* / *holdback*).** Cuando el riesgo es relevante y se quiere asegurar
el **cobro** de una eventual indemnización, se **retiene** parte del precio en una cuenta de garantía
(*escrow*) por un plazo, liberándose si el riesgo no se materializa. *Ejemplo:* ante una contingencia
fiscal o un litigio en curso, se deja el 10% del precio en *escrow* por 24 meses. Convierte la promesa de
indemnizar en **dinero disponible**.

**5) Condición al *closing* (*condition precedent*).** Cuando el riesgo **puede y debe resolverse antes
del cierre**, se vuelve **condición**: el comprador no está obligado a cerrar hasta que se subsane.
*Ejemplo:* la DD detecta que el contrato con el cliente clave tiene *change of control* → se pacta como
condición al *closing* obtener el **consentimiento** de ese cliente; o que se obtenga la autorización de
la COFECE; o que se regularice un permiso vencido.

**6) Exclusión del perímetro o cambio de estructura.** Cuando el riesgo está **localizado** en un activo,
una subsidiaria o una línea de negocio, a veces la mejor solución es **dejarlo fuera** de la compra
(reestructurar el perímetro) o **cambiar de estructura** (de *share deal* a *asset deal* para no heredar
los pasivos ocultos, como vimos en el Libro 1). *Ejemplo:* la DD ambiental revela un sitio gravemente
contaminado → se excluye ese inmueble de la operación, o se compra vía *asset deal* dejando el pasivo en
el vendedor.

**El cuadro mental que debes memorizar** (lo retomaremos en la sección 37):

| Tipo de hallazgo | Herramienta típica |
|---|---|
| La empresa vale menos | Ajuste/descuento de precio |
| Área de riesgo a garantizar | Representation & warranty específica |
| Riesgo concreto **conocido** | Indemnización especial (sin tope, fuera de cesta) |
| Asegurar el cobro de la indemnización | *Escrow* / *holdback* |
| Riesgo subsanable antes de cerrar | Condición al *closing* |
| Riesgo localizado en un activo/pasivo | Exclusión del perímetro / cambio de estructura |
| Riesgo intolerable e irresoluble | *Walk away* (abandonar el deal) |

Interioriza esta tabla: es el **puente** entre el Libro 2 (due diligence) y el Libro 4 (documentación:
SPA). El abogado que, ante cada hallazgo, ya está pensando en cuál de estas herramientas aplicar, **piensa
como un abogado de M&A**. Ese es exactamente el objetivo de este libro.

## 15. Explicación intuitiva

Piensa en la due diligence con tres metáforas que te ayudarán a retenerla y a explicarla.

**La metáfora médica.** Comprar una empresa sin due diligence es como **operar a un paciente sin
estudios previos**. El *Information Memorandum* del vendedor es lo que el paciente te cuenta de sus
síntomas (subjetivo, incompleto, a veces engañoso). La due diligence son los **análisis de sangre, las
radiografías y la resonancia**: la evidencia objetiva de lo que de verdad ocurre por dentro. Las **áreas**
de la DD son las distintas especialidades (el cardiólogo mira el corazón = la DD financiera; el
traumatólogo, los huesos = la DD de activos; etc.). Los **red flags** son los hallazgos clínicos, y la
**materialidad** es saber distinguir un lunar inofensivo de un tumor. El **DD report** es el diagnóstico
integrado, y las **cláusulas del SPA** son el tratamiento: a veces operas (cierras el deal con
protecciones), a veces medicas (ajustes y condiciones), a veces decides **no operar** (walk away).

**La metáfora del iceberg.** Lo que el vendedor te muestra de inicio es la **punta del iceberg** —lo que
flota a la vista, cuidadosamente presentado—. La due diligence es **bucear** para ver la masa sumergida:
los pasivos ocultos, las contingencias, los contratos con trampa. La mayoría de los deals que destruyen
valor no chocan con lo que se veía, sino con lo que estaba **bajo el agua** y no se buscó.

**La metáfora del detective.** El abogado de DD es un **detective**, no un archivista. No se limita a
catalogar los documentos que le entregan; **interroga** la realidad: ¿por qué falta este contrato?, ¿por
qué los ingresos saltaron justo el año de la venta?, ¿por qué hay un pago a un "consultor" sin contrato?
Busca lo que **no cuadra**, sigue los hilos, y entiende que **las ausencias y las incongruencias** suelen
ser las pistas más reveladoras. El buen detective tiene una teoría del caso (la tesis del riesgo) y busca
evidencia que la confirme o la desmienta.

La intuición central que debes interiorizar: **la due diligence convierte la incertidumbre en riesgo
manejable**. Antes de la DD, el comprador no sabe qué no sabe (incertidumbre pura). Después de una buena
DD, sabe qué riesgos existen, cuánto pueden costar y cómo protegerse. No elimina el riesgo —eso es
imposible—, pero lo vuelve **conocido, medido y asignado**. Y un riesgo conocido y asignado es, en el
mundo de los negocios, un riesgo que se puede **precificar y soportar**.

## 16. Ejemplos simples

**Ejemplo 1 — El cliente que era todo.** Una empresa de servicios parece muy rentable. La DD financiera
revela que **el 70% de sus ingresos** provienen de **un solo cliente**, y la DD contractual encuentra que
ese contrato **vence en seis meses** y tiene cláusula de *change of control*. *Lección:* la empresa vale
mucho menos de lo que aparenta; su valor depende de renovar (y de obtener el consentimiento de) un solo
contrato. Herramientas: descuento de precio + condición al *closing* (obtener consentimiento y renovación)
+ posible *earn-out* atado a la renovación.

**Ejemplo 2 — El dueño que no era dueño.** Un fundador vende su *startup*. La DD de PI descubre que la
**marca y el software** —el activo central— están registrados a nombre del **fundador como persona
física**, no de la sociedad que se vende. *Lección:* se compraría una cáscara sin su activo principal.
Herramienta: condición al *closing* de **transferir la PI a la sociedad** antes de cerrar (y rep + indemnización por titularidad).

**Ejemplo 3 — La deuda escondida.** Los estados financieros muestran poca deuda, pero la DD encuentra
**avales y garantías** que la empresa otorgó a favor de una compañía hermana. *Lección:* hay deuda
**oculta** (contingente) que no aparecía en el balance. Herramienta: ajuste de precio (la deuda neta sube)
+ rep específica + indemnización.

**Ejemplo 4 — El permiso vencido.** Una planta industrial opera con una licencia ambiental **vencida hace
un año**. *Lección:* riesgo de clausura y sanciones. Herramienta: condición al *closing* de regularizar la
licencia + rep de cumplimiento ambiental + indemnización por contingencias previas al cierre.

## 17. Ejemplos complejos

**Ejemplo complejo 1 — La contingencia fiscal con efecto en cascada.** Un grupo industrial mexicano va a
ser adquirido por un fondo. La DD fiscal detecta que, durante tres ejercicios, la *target* dedujo pagos a
una empresa proveedora que la autoridad podría considerar **operaciones simuladas (EFOS)**. La
contingencia es grande pero **incierta** (depende del criterio de la autoridad y de plazos de
prescripción). Complejidad: no se puede solo "bajar el precio" porque el monto es incierto, ni ignorarlo
porque podría ser enorme. *Solución integrada:* **(i)** indemnización especial del vendedor por esa
contingencia concreta, **al 100% y sin tope**, **(ii)** respaldada por un **escrow** de monto suficiente
por el plazo de prescripción, **(iii)** con un mecanismo de **control de la defensa** (¿quién dirige el
litigio fiscal si la autoridad reclama, el comprador o el vendedor que indemniza?) y **(iv)** una rep
fiscal robusta. Aquí ves cómo **varias herramientas se combinan** para un solo riesgo.

**Ejemplo complejo 2 — El deal entre competidores con información sensible.** Una empresa quiere comprar a
un **competidor directo**. La DD requiere revisar **precios, márgenes y lista de clientes** de la *target*
—información competitivamente sensible cuyo intercambio, antes de la autorización de competencia, podría
constituir *gun jumping* informativo y violar la LFCE—. Complejidad: el comprador **necesita** la
información para valuar, pero **no puede** verla libremente sin riesgo regulatorio. *Solución:* montar un
**clean team** —asesores externos y un grupo restringido que **no** participa en decisiones comerciales—
que revisa la información ultrasensible y entrega al comprador solo **conclusiones agregadas**, hasta que
la COFECE autorice y el deal cierre. Ilustra cómo la DD debe respetar el marco de competencia del Libro 1.

**Ejemplo complejo 3 — La PI heredada con *open source* contaminante.** Una empresa de tecnología
desarrolla software propietario que vende con licencia. La DD técnica descubre que el código incorpora
componentes de **software libre (open source)** bajo licencias "copyleft" (tipo GPL) que **obligarían** a
liberar el código propietario que las usa. Complejidad: el activo central (el software) podría estar
**jurídicamente contaminado**, comprometiendo todo el modelo de negocio. *Solución:* análisis técnico-legal
detallado del alcance, rep específica de PI y de cumplimiento de licencias, indemnización especial, y
—según gravedad— condición al *closing* de **remediar** el código o, si es irremediable, reevaluación del
precio o *walk away*.

## 18. Casos reales (operaciones estilizadas y referentes)

> *Nota de método (Manifiesto XI.5): los casos se presentan de forma estilizada, con fines didácticos.
> Verifica los detalles antes de citarlos profesionalmente.*

**HP – Autonomy (2011), el caso emblemático del fracaso de la DD.** Hewlett-Packard compró la empresa de
software Autonomy por más de 11,000 millones de dólares y, poco después, tuvo que reconocer una pérdida
contable masiva (alrededor de 8,800 millones), alegando que las cuentas de Autonomy habían sido
**infladas** antes de la venta. El caso —que derivó en litigios y procesos penales por años— se estudia en
todo el mundo como el ejemplo de una **due diligence financiera insuficiente** (o de hallazgos ignorados
por la prisa de cerrar). *Lección:* la **Quality of Earnings** importa más que cualquier otra cosa cuando
se paga un múltiplo alto por una empresa de software; y ninguna presión por cerrar justifica saltarse la
verificación de los ingresos.

**Bank of America – Countrywide / Merrill Lynch (2008).** En plena crisis financiera, adquisiciones hechas
con DD apresurada dejaron a Bank of America con **pasivos legales y regulatorios** enormes (heredados de
las prácticas hipotecarias y de los activos tóxicos de las empresas adquiridas), que costaron decenas de
miles de millones en años posteriores. *Lección:* en una compra se **heredan los pasivos** —legales,
regulatorios, reputacionales—; la prisa y la euforia son enemigas de la due diligence.

**Las MAC y la DD confirmatoria (caso *Akorn v. Fresenius*, Delaware, 2018).** Fresenius había acordado
comprar a la farmacéutica Akorn, pero durante el período entre firma y cierre descubrió **graves
problemas de cumplimiento regulatorio** en Akorn (datos falseados ante la FDA). Un tribunal de Delaware
permitió a Fresenius **abandonar** el deal invocando un *Material Adverse Effect* —el primer caso en que
una corte de Delaware validó una salida por MAC—. *Lección:* la **due diligence confirmatoria** entre
*signing* y *closing* y una **cláusula MAC** bien redactada (Libro 1) son la última línea de defensa
cuando aparecen problemas graves después de firmar.

## 19. Casos empresariales

**El fondo de Private Equity y la Quality of Earnings.** Un fondo de PE evalúa comprar una cadena de
restaurantes. Su DD financiera (QoE) descubre que buena parte de la "utilidad" provenía de **no haber
invertido en mantenimiento** de los locales (lo que infla el resultado a corto plazo pero deteriora el
negocio) y de **ingresos extraordinarios** por venta de inmuebles. La utilidad **recurrente y real** era
mucho menor. *Decisión empresarial:* el fondo recalculó el múltiplo sobre el EBITDA **normalizado**,
bajando su oferta sustancialmente, y condicionó el deal a un plan de inversión en mantenimiento. La DD
**salvó** al fondo de pagar de más por utilidades ilusorias.

**La empresa familiar y el orden de la casa (vendor due diligence).** Una familia decide vender su empresa
manufacturera. Antes de salir al mercado, encarga una **vendor due diligence** que revela problemas
ocultos: formalidades societarias incompletas, un par de contingencias laborales y PI mal registrada.
*Decisión empresarial:* en lugar de esperar a que los compradores lo descubran (y descuenten el precio o
desconfíen), la familia **regulariza** todo antes de vender, ordena la casa y entrega un VDD report
limpio. Resultado: proceso más rápido, más compradores interesados y mejor precio. Ilustra el valor
estratégico de la DD **del lado del vendedor**.

## 20. Casos corporativos (la conexión integral)

Este caso integra **todo** lo aprendido hasta ahora en el programa. *Corporación Alfa* (estratégico)
quiere adquirir a *Beta, S.A.P.I.*, una empresa tecnológica con inversionistas de venture capital.

- **Del Nivel I (Obligaciones, Contratos):** la DD contractual analiza los contratos materiales de Beta
  como **fuentes de obligaciones**, buscando cargas, condiciones y cláusulas de *change of control*.
- **Del Nivel II (Responsabilidad civil, Garantías):** la DD de litigios estima la **responsabilidad
  civil** contingente de Beta; los hallazgos se traducen en **garantías** contractuales (reps,
  indemnización, escrow).
- **Del Nivel III (Sociedades/LGSM, Gobierno Corporativo, Valores):** la DD corporativa revisa la
  estructura de **S.A.P.I.** de Beta, los **derechos de los inversionistas de VC** (asientos, vetos,
  preferencias de liquidación, *drag/tag along*) que afectan **cómo** se puede comprar; la DD de gobierno
  evalúa los **deberes del consejo** de Beta al vender (Revlon) y si hay conflictos.
- **Del Libro 1 de este nivel (Fundamentos de M&A):** los hallazgos determinan la **estructura** (¿share
  o asset?), las **fases** (¿qué se vuelve condición al *closing*?) y la **asignación de riesgo** (reps,
  MAC, escrow).
- **De este Libro 2:** la DD **integra** todo en un DD report jerarquizado y lo traduce en el SPA.

*Moraleja:* la due diligence es el **punto donde converge toda tu formación jurídica**. No es una
habilidad aislada: es la aplicación simultánea, bajo presión y con sentido práctico, de **todo** el
derecho privado que has estudiado. Por eso es tan formativa y tan valorada.

## 21. Casos internacionales

**Cross-border due diligence (operaciones transfronterizas).** Cuando se compra una empresa con
operaciones en varios países, la DD se vuelve **multijurisdiccional**: equipos locales en cada país revisan
el cumplimiento bajo su propio derecho (laboral, fiscal, regulatorio, de competencia), coordinados por un
despacho líder. Surgen retos finos: **diferencias de privilegio legal** (lo que es confidencial en un país
puede no serlo en otro), **distintos umbrales de notificación de competencia** (una operación puede
requerir autorización en la UE, EE.UU., Brasil y México a la vez), y **regímenes de protección de datos**
divergentes (el GDPR europeo impone reglas estrictas a la transferencia de datos personales durante la DD).

**FCPA y due diligence anticorrupción en adquisiciones.** El Departamento de Justicia de EE.UU. ha sido
explícito en su doctrina sobre **sucesión de responsabilidad**: cuando una empresa sujeta a la FCPA compra
otra que incurrió en corrupción, puede **heredar** esa responsabilidad —pero una **due diligence
anticorrupción rigurosa**, seguida de medidas correctivas, mitiga sustancialmente la exposición—. Esto ha
vuelto la DD de compliance un **estándar global ineludible** en cualquier operación con nexo estadounidense
o con operaciones en mercados de riesgo. *Lección:* en el M&A internacional, "no investigué la corrupción"
no es una defensa; es un **agravante**.

**El estándar de los fondos globales en México.** Cuando un fondo de PE o un corporativo internacional
adquiere en México, importa su **estándar de DD**: QoE exhaustiva, DD de compliance y anticorrupción,
revisión laboral fina (incluido el régimen de subcontratación), y exigencias de ESG. El abogado mexicano
de élite debe operar con **estándares plenamente internacionales**, hablar el lenguaje de los fondos y
entender sus *checklists* y sus prioridades. Esa es, precisamente, la formación que persigue esta
biblioteca.

## 22. Derecho comparado

La due diligence es una práctica **global**, pero el marco jurídico que la rodea —y, sobre todo, la regla
sobre **quién soporta el riesgo de lo que no se reveló**— varía según la tradición jurídica. Esta es la
tabla comparada que todo abogado de M&A debe tener en la cabeza:

| Jurisdicción / sistema | Cómo trata la due diligence y la asignación de riesgo informativo |
|---|---|
| **México (Civil Law)** | DD como práctica contractual; el Código de Comercio y el Civil imponen **buena fe** y deberes de información precontractual; el riesgo se asigna por **reps & warranties** e indemnización en el SPA (importadas del common law). El **dolo/reticencia** del vendedor puede generar nulidad o responsabilidad. |
| **EE.UU. (Common Law)** | Origen de la práctica moderna. Predomina el principio de ***caveat emptor*** (el comprador se cuida) atenuado: lo que importa es lo **pactado** en el SPA (reps, indemnización, *sandbagging*). El sistema confía en la **autonomía contractual** y en una DD exhaustiva. |
| **Delaware** | El estándar de referencia mundial en M&A. Jurisprudencia riquísima sobre **deberes del consejo** (decidir informado: la DD como parte del deber de diligencia), interpretación de **MAC** y de reps. El *case law* de Delaware es la "lengua franca" del M&A. |
| **España (Civil Law)** | DD muy extendida (influencia anglosajona vía despachos internacionales); el Código Civil aporta el **saneamiento por vicios ocultos** y la responsabilidad por dolo; el riesgo se pacta en *manifestaciones y garantías* (las reps en español). |
| **Reino Unido (Common Law)** | *Caveat emptor* fuerte: el vendedor **no** tiene un deber general de revelar; el comprador se protege con **warranties** y con la **disclosure** del vendedor (los *disclosure letters*). La DD es esencial porque "lo que no preguntas/garantizas, lo pierdes". |
| **Unión Europea** | Sin un régimen único de DD privada, pero con **fuerte impacto** del derecho de **competencia** (control de concentraciones), **protección de datos (GDPR)** —que condiciona el manejo de datos en la DD— y, crecientemente, normas de **due diligence en sostenibilidad y derechos humanos** (cadenas de suministro). |
| **UNIDROIT (Principios)** | Aportan los **deberes de buena fe y de información** en la negociación y la doctrina de la **responsabilidad precontractual** (*culpa in contrahendo*), marco supletorio útil en contratos internacionales. |
| **CISG (Compraventa internacional)** | Regula la conformidad de las mercancías y los deberes de examen del comprador; aunque pensada para mercaderías, su **lógica** (examinar y notificar defectos) ilumina la racionalidad de la DD. |
| **Civil Law vs. Common Law (síntesis)** | El **civil law** tiende a proteger al comprador con **deberes legales de información y saneamiento**; el **common law** confía en la **autonomía contractual** (reps, warranties, disclosure). En la práctica del M&A global, **gana el modelo common law**: el SPA con reps e indemnización es el estándar **aunque la ley aplicable sea civil**. |

**La gran lección comparada:** sin importar la jurisdicción, el M&A internacional se documenta con el
**aparato contractual del common law** (reps & warranties, indemnización, disclosure schedules,
sandbagging, MAC). Por eso un abogado mexicano de M&A debe dominar ese aparato **tanto** como su propio
Código Civil: la operación se rige por derecho mexicano, pero **habla inglés contractual**.

## 23. Derecho mexicano

En México, la due diligence se asienta sobre varios pilares del ordenamiento, aunque ninguno la regule
de forma autónoma:

- **Buena fe y deberes precontractuales (Código Civil Federal y locales; Código de Comercio).** La
  negociación debe conducirse de buena fe; el **dolo** (maquinaciones para engañar) y la **mala fe**
  (incluida la **reticencia** —callar lo que se debía decir—) vician el consentimiento y pueden generar
  **nulidad** y **responsabilidad por daños**. Este es el respaldo civil de la DD y de las reps: si el
  vendedor ocultó dolosamente un pasivo, el comprador tiene acción aun más allá del contrato.
- **Saneamiento por vicios ocultos y por evicción (CCF).** El régimen civil de la compraventa obliga al
  vendedor a responder por los **defectos ocultos** de la cosa y por la **evicción** (que un tercero
  prive al comprador de lo adquirido). En M&A, este régimen se **complementa y desplaza** contractualmente
  con reps e indemnización a la medida.
- **Deber de diligencia de los administradores (LGSM; LMV para emisoras).** Los administradores deben
  obrar como un **administrador prudente** y de manera **informada**. Aprobar una adquisición relevante
  sin DD adecuada puede comprometer su responsabilidad: la DD es parte del **proceso informado** que
  exige el deber fiduciario (conecta con Gobierno Corporativo y con *Van Gorkom*).
- **Ley Federal de Competencia Económica (LFCE).** Régimen de **concentraciones**: notificación a la
  **COFECE** según umbrales, prohibición de consumar antes de la autorización (*gun jumping*), y reglas
  sobre el intercambio de información sensible entre competidores durante la DD (*clean teams*).
- **Régimen fiscal (CFF) y el riesgo EFOS/EDOS.** El **artículo 69-B ⟳ del Código Fiscal** y el régimen de
  operaciones simuladas hacen de la DD fiscal un área de altísima sensibilidad: comprar una empresa que
  facturó o dedujo operaciones simuladas puede heredar contingencias graves.
- **Materia laboral (LFT) y subcontratación.** La reforma que **prohibió la subcontratación de personal**
  (permitiendo solo servicios especializados registrados —REPSE) volvió crítica la DD laboral: esquemas
  de *outsourcing* mal estructurados generan pasivos y responsabilidad solidaria.
- **Protección de datos (LFPDPPP).** Condiciona el tratamiento y la transferencia de datos personales
  durante la DD y vuelve relevante la DD de privacidad.

**En suma:** el derecho mexicano **no impone** la due diligence con un mandato expreso, pero la **exige
de hecho** por la convergencia del deber fiduciario, la buena fe, el saneamiento, y los regímenes de
competencia, fiscal y laboral. Omitirla es, a la vez, una imprudencia de negocio y una posible
**infracción de deberes**.

## 24. Jurisprudencia relevante

> *Nota de método: verifica la vigencia y los datos de identificación de los criterios antes de citarlos
> en un escrito profesional.*

En México, no existe una línea jurisprudencial abundante y específica sobre "due diligence" como tal
(por ser práctica contractual), pero sí criterios relevantes en las **instituciones que la sostienen**:

- **Sobre dolo, mala fe y reticencia en los contratos:** criterios que desarrollan cuándo el silencio o
  la ocultación de información relevante vicia el consentimiento y genera nulidad o responsabilidad
  —fundamento para reclamar cuando el vendedor ocultó pasivos que una DD habría detectado—.
- **Sobre el saneamiento por vicios ocultos:** criterios sobre el alcance de la responsabilidad del
  vendedor por defectos no aparentes y la carga de la prueba.
- **Sobre buena fe contractual y responsabilidad precontractual:** criterios que reconocen deberes de
  conducta en la etapa de negociación.
- **Sobre interpretación de los contratos conforme a la intención de las partes (CCF):** clave para
  interpretar reps, indemnizaciones y *disclosure schedules*.

En el ámbito **anglosajón** (de altísima influencia práctica), la "jurisprudencia" relevante es el
*case law* de **Delaware**, que sí es abundante y determinante: la doctrina sobre **MAC** (*Akorn v.
Fresenius*), sobre el **deber de informarse** del consejo (*Smith v. Van Gorkom*) y sobre la
interpretación de reps y de *indemnification*. Para el abogado de M&A, este *case law* es **estudio
obligado**, porque modela cómo se redactan e interpretan las cláusulas en todo el mundo.

## 25. Criterios de la Suprema Corte / reguladores

- **SCJN:** sus criterios sobre **buena fe, dolo y vicios del consentimiento** en materia contractual, y
  sobre **interpretación de los contratos**, son el telón de fondo que da fuerza a las reclamaciones
  derivadas de información ocultada en una operación.
- **COFECE:** sus **guías y resoluciones** sobre concentraciones definen umbrales de notificación,
  plazos, el tratamiento del **gun jumping** y el manejo de información sensible entre competidores
  durante la DD (relevante para diseñar *clean teams*).
- **SAT:** sus criterios y el régimen del **art. 69-B CFF ⟳** (operaciones simuladas) marcan el riesgo
  central de la DD fiscal en México.
- **CNBV (para emisoras):** en operaciones sobre empresas públicas, el régimen de la LMV (revelación,
  OPAs, información privilegiada) condiciona qué y cómo se revela en la DD.

## 26. Doctrina nacional

La doctrina mexicana sobre due diligence se ha desarrollado principalmente desde la **práctica de los
despachos corporativos** y desde la doctrina mercantil y de competencia, más que desde tratados
académicos clásicos. Las fuentes útiles son: la doctrina civil sobre **buena fe, vicios del consentimiento
y saneamiento** (que da el marco de fondo), la doctrina mercantil y societaria (LGSM, gobierno
corporativo) y la doctrina de **competencia económica** (concentraciones, gun jumping). El abogado
mexicano completa esta base con la **literatura transaccional internacional**, que es donde la DD está
más desarrollada técnicamente.

## 27. Doctrina internacional

La doctrina internacional sobre due diligence es vasta y eminentemente **práctica**:

- **Literatura transaccional de los grandes despachos y *Practical Law / PLC*:** guías cláusula por
  cláusula, *checklists* de DD por área e industria, y *precedents* de mercado. Es el material de trabajo
  diario del abogado de M&A.
- **American Bar Association — *Model Stock Purchase Agreement* y materiales de DD:** referencia sobre
  cómo los hallazgos de la DD se reflejan en reps, indemnización y *disclosure schedules*.
- **Doctrina de negociación y *deal-making* (Harvard — Sebenius, Subramanian):** entiende la DD como parte
  del **diseño de la transacción** y de la dinámica de información entre las partes.
- **Doctrina de compliance y anticorrupción (FCPA Resource Guide del DOJ/SEC):** estándar sobre la DD
  anticorrupción en adquisiciones y la sucesión de responsabilidad.
- **Doctrina de valuación y finanzas (para la QoE):** conecta la DD financiera con la valuación
  (anticipa el Nivel V).

## 28. Opiniones críticas (postura del Consejo Editorial)

Nuestra postura, como Consejo, sobre la due diligence:

**Primero: la DD vale por lo que se traduce, no por lo que se revisa.** Criticamos la cultura del
"revisar todo" y del DD report de 400 páginas que nadie lee. Una DD excelente es **selectiva,
jerarquizada y orientada a la decisión**. El mejor due diligence report cabe, en su parte ejecutiva, en
pocas páginas: los *deal breakers*, los riesgos mayores y su traducción contractual. Lo demás es anexo.

**Segundo: el riesgo de la DD defensiva.** Advertimos contra el abogado que reporta todo con tono
alarmante para "cubrirse". Esa práctica **destruye valor**: enturbia la decisión, dispara honorarios y
mina la credibilidad del asesor. El cliente no paga por una lista de defectos; paga por **criterio**.

**Tercero: la tecnología es palanca, no sustituto del juicio.** La revisión asistida por IA acelera la
detección de cláusulas tipo, pero la **valoración del riesgo** y su **traducción contractual** siguen
siendo humanas. El abogado que solo "corre la herramienta" sin entender lo que encuentra no agrega valor;
el que usa la herramienta para liberar tiempo y concentrarse en el criterio, **multiplica** su valor.

**Cuarto: la DD es una habilidad de carrera, no una tarea de novatos.** Aunque el junior la ejecuta,
dominarla con criterio es lo que forma al socio. Quien aprende a **ver el riesgo y a traducirlo** temprano,
acelera su carrera más que quien solo "redacta contratos".

## 29. Debate doctrinal

- **¿*Caveat emptor* o deber de revelar? (common law vs. civil law).** El common law parte de que el
  comprador debe cuidarse (de ahí la DD exhaustiva); el civil law impone deberes de información y
  saneamiento al vendedor. *Postura del Consejo:* en el M&A moderno **gana la lógica contractual** —lo
  que importa es lo pactado (reps, disclosure)— pero el abogado mexicano debe recordar que su derecho
  ofrece **una red de seguridad adicional** (dolo, saneamiento) que el common law puro no tiene.
- **¿*Sandbagging* sí o no?** Debate clásico: si el comprador **sabía** (por la DD) que una rep era falsa
  y aun así cierra, ¿puede luego reclamar la indemnización (*pro-sandbagging*) o no (*anti-sandbagging*)?
  Se resuelve **expresamente** en el SPA. *Postura del Consejo:* el comprador prefiere cláusula
  *pro-sandbagging* (puede reclamar aunque supiera); el vendedor, lo contrario; quien tiene más poder de
  negociación impone su preferencia. Es un punto donde la DD y el contrato se cruzan de forma fascinante.
- **¿Hasta dónde llega la DD razonable?** ¿Cuánto es suficiente? El debate sobre el **alcance óptimo**
  enfrenta la exhaustividad (más seguridad) contra el costo y el tiempo (más fricción). *Postura del
  Consejo:* la respuesta es la **proporcionalidad al riesgo** (la matriz probabilidad × impacto), no un
  estándar fijo.
- **DD vs. seguros de reps & warranties (*W&I insurance*).** Tendencia creciente: trasladar el riesgo de
  las reps a un **seguro** (*Warranty & Indemnity insurance*) en vez de a un *escrow*. *Debate:* ¿el
  seguro reduce el incentivo a hacer una DD rigurosa? *Postura del Consejo:* no debería —las aseguradoras
  **exigen** una DD sólida para emitir la póliza—; el seguro **complementa**, no sustituye, a la due
  diligence.

## 30. Errores comunes

- **Empezar sin un *scope* claro.** Revisar documentos sin haber definido alcance, materialidad y
  prioridades: el equipo se ahoga en lo irrelevante y se le escapa lo crítico. *Corrección:* define el
  *scope* y el umbral de materialidad **antes** de abrir el data room.
- **Confundir cantidad con calidad.** Un DD report enorme no es un buen DD report. *Corrección:*
  jerarquiza (deal breaker / mayor / menor) y orienta a la decisión.
- **No traducir los hallazgos al contrato.** El error más caro: detectar un riesgo y **no** convertirlo
  en rep, indemnización, ajuste o condición. *Corrección:* para cada *red flag* mayor, define ya la
  herramienta de protección (sección 14.E).
- **Olvidar el *change of control*.** No revisar si los contratos clave se caen al cambiar el dueño.
  *Corrección:* búscalo sistemáticamente y vuélvelo condición al *closing*.
- **DD de compliance superficial.** Subestimar el riesgo de corrupción heredada. *Corrección:* DD
  anticorrupción rigurosa, sobre todo con nexo FCPA o mercados de riesgo.
- **Ignorar las ausencias.** Revisar solo lo que está en el data room sin preguntarse qué falta y por
  qué. *Corrección:* lee también los **huecos**; úsalos en el Q&A.
- **Romper el privilegio o la confidencialidad.** Manejar mal documentos privilegiados o información
  sensible entre competidores. *Corrección:* cuida el privilegio y usa *clean teams* cuando haya riesgo
  de competencia.
- **Prisa por cerrar.** Saltarse o apresurar la DD por presión de tiempo (el error de HP-Autonomy).
  *Corrección:* ninguna prisa justifica no verificar lo crítico (titularidad, QoE, compliance).

## 31. Mitos frecuentes

- **"La due diligence garantiza que no habrá sorpresas."** **Falso.** La DD **reduce y administra** el
  riesgo; no lo elimina. Por eso existen las reps, la indemnización y el *escrow*: para lo que la DD no
  pudo ver.
- **"Hay que revisar absolutamente todo."** **Falso.** Revisar todo es imposible y antieconómico. La DD
  moderna es **selectiva y proporcional al riesgo** (materialidad).
- **"La DD es trabajo de juniors, sin importancia estratégica."** **Falso.** La ejecutan juniors, pero
  define **precio, estructura, contrato y la decisión misma** de comprar. Es de lo más estratégico del
  deal.
- **"Si está en el data room, está cubierto."** **Falso.** Lo que el vendedor **revela** (en el data
  room, en el Q&A, en los *disclosure schedules*) suele **dejar de estar garantizado**: el comprador
  "ya lo sabía". De ahí el debate del *sandbagging*.
- **"Con un seguro de reps & warranties no necesito DD."** **Falso.** Las aseguradoras **exigen** una DD
  sólida para emitir la póliza; el seguro complementa, no sustituye.
- **"La DD legal y la financiera son mundos separados."** **Falso.** Se cruzan constantemente: una deuda
  oculta (financiera) nace de un aval (legal); una contingencia fiscal (legal) altera la QoE (financiera).

## 32. Preguntas difíciles

1. **¿Por qué lo que el vendedor revela en la DD puede *reducir* la protección del comprador?** Porque,
   bajo la lógica de las reps, el comprador se protege de lo **desconocido**; si el vendedor **reveló** un
   problema (en el *disclosure schedule*), el comprador lo **conocía** y, salvo cláusula
   *pro-sandbagging*, no podrá reclamar por él después. Revelar es, para el vendedor, una forma de
   **vacunarse** contra reclamaciones.
2. **¿Cuándo conviene un *asset deal* en vez de un *share deal* por razones de DD?** Cuando la DD revela
   un **riesgo alto de pasivos ocultos** (fiscales, ambientales, laborales) difíciles de acotar: el
   *asset deal* permite **dejar los pasivos** en el vendedor y comprar solo los activos limpios (Libro 1).
3. **¿Cómo investigar a un competidor sin violar la ley de competencia?** Con un **clean team**: un grupo
   restringido (a menudo asesores externos) que revisa la información competitivamente sensible y entrega
   solo conclusiones agregadas, hasta que la operación se autoriza y cierra. Evita el *gun jumping*
   informativo.
4. **Si la DD detecta corrupción en la *target*, ¿qué debe hacer el comprador?** Evaluar la gravedad y la
   exposición (FCPA/local), exigir remediación, estructurar protecciones (indemnización especial,
   posible *asset deal* para aislar), y —si es sistémica e irremediable— considerar el *walk away*. "No
   investigué" no es defensa; "investigué y remedié" sí mitiga.
5. **¿Una DD impecable exonera al consejo si el deal sale mal?** En buena medida sí: una DD adecuada es
   parte del **proceso informado** que activa la *business judgment rule* (Gobierno Corporativo). El
   consejo que decidió **informado** está protegido aunque el resultado sea malo; el que decidió **sin
   informarse** (Van Gorkom), no.

## 33. Casos de examen (con respuesta modelo)

**Caso A.** *Tu cliente quiere comprar una empresa de logística. La DD revela que su contrato más
importante (40% de los ingresos) contiene una cláusula que permite al cliente terminarlo si la empresa
cambia de control. ¿Qué recomiendas?*
**Respuesta modelo:** Es un *red flag* **mayor** (alto impacto sobre el valor). Herramientas combinadas:
**(i)** condición al *closing* de obtener el **consentimiento** del cliente a la operación (o una
renovación); **(ii)** si no se obtiene, derecho del comprador a **no cerrar** o a **ajustar el precio**;
**(iii)** posible **earn-out** atado a la conservación del contrato; **(iv)** rep específica del vendedor
sobre el estado del contrato. Razonar el porqué: el valor de la *target* depende de ese contrato, así que
hay que **asegurar su continuidad antes de pagar**.

**Caso B.** *La DD fiscal identifica una contingencia concreta y conocida por una deducción cuestionable
de un ejercicio anterior, de monto significativo pero incierto. ¿Cómo lo proteges en el SPA?*
**Respuesta modelo:** Por ser un riesgo **concreto y conocido**, no basta la rep general: se pacta una
**indemnización especial** por esa contingencia específica, **al 100%, fuera de los topes y mínimos
generales**, **respaldada por un *escrow*** suficiente por el plazo de prescripción, y con una cláusula
de **control de la defensa** del eventual litigio fiscal. Mencionar que un riesgo **conocido** se cubre
con indemnización **específica**, no con la rep general (que cubre lo desconocido).

**Caso C.** *El comprador y la target son competidores directos. ¿Cómo organizas la DD de la información
de precios y clientes?*
**Respuesta modelo:** Mediante un **clean team**: grupo restringido o asesores externos que revisan la
información sensible **sin** trasladarla a los equipos comerciales que toman decisiones, entregando solo
conclusiones agregadas, hasta obtener la autorización de la COFECE y cerrar. Fundar en el riesgo de
**gun jumping** informativo y la violación a la LFCE.

## 34. Simulador (ejercicio tipo despacho)

> **Instrucciones:** eres asociado de M&A. Tu socia te asigna la coordinación de la DD legal en la
> compra de *Manufacturas del Norte, S.A.* (industrial, 600 empleados, una planta, exporta a EE.UU.).
> Trabaja el caso por pasos antes de leer la guía.

1. **Scoping:** define el alcance y las **áreas prioritarias** dado el perfil (industrial, exportadora,
   muchos empleados). ¿Qué materialidad propondrías?
2. **Request list:** redacta las **5 solicitudes más importantes** que pedirías primero y por qué.
3. **Hipótesis de riesgo:** anticipa los **3 *red flags* más probables** dado el perfil de la empresa.
4. **Q&A:** formula 3 preguntas precisas que harías si el data room **no** incluye los permisos
   ambientales.
5. **Traducción:** para cada *red flag* anticipado, indica la **herramienta de protección** (sección
   14.E).

> **Guía de solución (resumen).** **(1)** Prioriza **ambiental** (planta industrial), **laboral** (600
> empleados, posible sindicato y pasivos), **fiscal** (exportadora: IVA, devoluciones, precios de
> transferencia), **regulatoria** (permisos de operación) y **contractual** (clientes de exportación con
> *change of control*). Materialidad: contratos > X y contingencias > Y, salvo temas cualitativos
> (permisos esenciales, ambiental, titularidad). **(2)** Acta constitutiva y libro de accionistas
> (titularidad); contratos materiales (clientes/proveedores); permisos ambientales y de operación;
> situación fiscal (declaraciones, devoluciones, precios de transferencia); pasivos laborales y contrato
> colectivo. **(3)** Pasivo ambiental de la planta; contingencia laboral/sindical o de subcontratación;
> contingencia fiscal por exportación/devoluciones. **(4)** "¿Cuenta la planta con autorización de
> impacto ambiental vigente? Favor de cargarla", "¿Existen procedimientos o sanciones de la autoridad
> ambiental en los últimos 5 años?", "¿Hay estudios de suelo/agua del sitio?". **(5)** Ambiental →
> condición al *closing* (regularizar) + rep + indemnización + posible *escrow*; laboral → rep +
> indemnización por contingencias previas al cierre; fiscal → indemnización especial + *escrow*.

## 35. Flashcards

- **¿Qué es la due diligence?** La investigación previa y sistemática del comprador sobre la *target*
  para saber qué compra, cuánto vale y qué riesgos asume.
- **¿Cuál es la lección central del libro?** "La DD investiga y las reps reparten": cada hallazgo
  relevante se traduce en una protección contractual.
- **¿Qué es la materialidad?** El umbral (cuantitativo y cualitativo) a partir del cual un hallazgo
  importa.
- **¿Tres niveles de red flag?** Deal breaker (mata el deal) / mayor (precio-estructura-protección) /
  menor (a documentar).
- **¿Qué es un data room (VDR)?** El repositorio virtual seguro donde el vendedor pone la información para
  su revisión.
- **¿Qué es la *Quality of Earnings*?** El análisis de cuán recurrentes y reales son las utilidades de la
  *target*.
- **¿Qué es un *clean team*?** Grupo restringido que revisa información sensible entre competidores sin
  trasladarla a las áreas comerciales, para evitar *gun jumping*.
- **¿Riesgo concreto y conocido se cubre con...?** Indemnización **especial** (no con la rep general).
- **¿Riesgo subsanable antes de cerrar se cubre con...?** Condición al *closing*.
- **¿Qué es el *sandbagging*?** Que el comprador reclame por una rep que sabía falsa; se pacta expresamente
  en el SPA.
- **¿Qué es la *vendor due diligence*?** La DD que encarga el **vendedor** sobre su propia empresa antes
  de venderla.
- **¿Origen del concepto?** La *due diligence defense* de la Securities Act de 1933 (EE.UU.).

## 36. Mapas mentales

```
                         DUE DILIGENCE
                              |
   ┌──────────────┬──────────┼───────────────┬──────────────┐
 ¿QUÉ ES?     ¿QUÉ BUSCA?   PROCESO        RED FLAGS      TRADUCCIÓN
investigación  el riesgo    scope→request  materialidad   al SPA
previa y       (no solo     →data room→    (deal breaker/ (precio, rep,
sistemática    describir)   revisión→Q&A   mayor/menor)   indemnización,
del comprador               →report→SPA→   prob × impacto escrow, condición,
                            confirmatoria                 exclusión, walk away)
```

```
                    ÁREAS DE LA DD
   Corporativa · Contractual · Fiscal · Financiera (QoE)
   Laboral · Regulatoria/Permisos · Competencia · Ambiental
   PI · Tecnología/Datos · Compliance/Anticorrupción · Litigios
        (el abogado de M&A las COORDINA e INTEGRA)
```

## 37. Cuadros comparativos

**Hallazgo → herramienta de protección (cuadro maestro)**

| Tipo de hallazgo | Herramienta |
|---|---|
| La empresa vale menos | Ajuste/descuento de precio |
| Área de riesgo a garantizar | Rep & warranty específica |
| Riesgo concreto **conocido** | Indemnización especial (sin tope, fuera de cesta) |
| Asegurar el cobro | *Escrow* / *holdback* |
| Riesgo subsanable antes de cerrar | Condición al *closing* |
| Riesgo localizado en activo/pasivo | Exclusión del perímetro / *asset deal* |
| Riesgo intolerable e irresoluble | *Walk away* |

**Buy-side DD vs. Vendor DD (VDD)**

| | Buy-side DD | Vendor DD |
|---|---|---|
| Quién la encarga | El comprador | El vendedor |
| Objetivo | Detectar riesgos para protegerse | Ordenar la casa y agilizar la venta |
| Cuándo | Tras la LOI | Antes de salir al mercado |
| Uso del reporte | Negociar precio y SPA | Entregar a posibles compradores |

**Full report vs. Red flag report**

| | Full report | Red flag report |
|---|---|---|
| Contenido | Exhaustivo, área por área | Solo riesgos relevantes |
| Extensión | Larga | Ejecutiva |
| Uso típico | Deals grandes/complejos | La mayoría de los deals modernos |

## 38. Diagramas

**Ciclo de la due diligence:**
```
SCOPING (alcance + materialidad)
   → REQUEST LIST (solicitud de información)
   → DATA ROOM (el vendedor carga; el comprador accede)
   → REVISIÓN + Q&A (encontrar y aclarar el riesgo)
   → DD REPORT (hallazgo → riesgo → impacto → recomendación)
   → TRADUCCIÓN AL SPA (precio, reps, indemnización, escrow, condiciones)
   → [signing] → DD CONFIRMATORIA / bring-down → [closing]
```

**Embudo de jerarquización del riesgo:**
```
TODOS los hallazgos
      │  (filtro: materialidad)
      ▼
Hallazgos MATERIALES
      │  (matriz: probabilidad × impacto)
      ▼
🔴 Deal breaker → resolver/condición o WALK AWAY
🟠 Mayor        → precio / rep específica / indemnización / escrow / condición
🟡 Menor        → documentar / rep general
🟢 Conforme     → reportar (da confianza)
```

## 39. Mnemotecnias

- **Las 3 preguntas de la DD:** *"¿QUÉ compro, CUÁNTO vale, qué RIESGOS trae?"*
- **El proceso (SRDRRT):** **S**cope · **R**equest list · **D**ata room · **R**evisión+Q&A · **R**eport ·
  **T**raducción al SPA.
- **La regla de oro:** *"la DD investiga, las reps reparten, el escrow asegura, la condición exige, el
  walk away salva"*.
- **Materialidad:** *"no todo importa; importa lo material"* (cuánto + naturaleza).
- **Riesgo conocido vs. desconocido:** *"lo desconocido → rep general; lo conocido → indemnización
  especial"*.
- **Competidores:** *"entre competidores, clean team o gun jumping"*.
- **El gran error:** *"hallazgo sin cláusula = trabajo perdido"*.

## 40. Resumen ejecutivo

La **due diligence** es la investigación previa y sistemática mediante la cual el comprador descubre
**qué está comprando realmente**: cuánto vale la *target* y qué riesgos esconde. Nació como una **defensa
de responsabilidad** en el derecho bursátil estadounidense (Securities Act de 1933) y se transformó en la
**herramienta central de gestión de riesgo** del M&A moderno. Es multidisciplinaria —corporativa,
contractual, fiscal, financiera (con la *Quality of Earnings*), laboral, regulatoria, de competencia,
ambiental, de PI, de tecnología y datos, de compliance y de litigios— y la coordina el abogado de M&A,
que **integra** los hallazgos en una visión de riesgo única.

Su proceso es ordenado e iterativo: definir el **alcance y la materialidad**, emitir la **request list**,
poblar y revisar el **data room** (hoy virtual, con su dinámica de **Q&A**), levantar y **jerarquizar los
*red flags*** (deal breaker / mayor / menor, según una matriz de probabilidad × impacto), consolidarlos en
un **DD report** ejecutivo y orientado a la decisión, y —la lección capital del libro— **traducir cada
hallazgo en una protección contractual**: ajuste de precio, *representation* específica, indemnización
especial, *escrow*, condición al *closing*, exclusión del perímetro o, en el extremo, el *walk away*. La
due diligence que no se traduce al SPA es trabajo perdido.

Para el lector, este libro es la **competencia operativa** que más temprano se le exigirá y la que más
acelera una carrera en M&A. Conecta hacia atrás con **todo** el programa (sociedades, contratos,
responsabilidad, garantías, gobierno corporativo, competencia, fiscal, laboral) y hacia adelante con la
**documentación** (Libro 4: el SPA y sus reps, indemnización y *disclosure schedules*) y con las
**estructuras** (Libro 3: cómo un hallazgo empuja de *share* a *asset deal*). Dominar la due diligence es
empezar a **pensar como un abogado de transacciones**: no describir documentos, sino **buscar el riesgo,
valorarlo y asignarlo**.

## 41. Checklist

**Antes de abrir el data room (scoping):**
- [ ] ¿Está definido el **alcance** por áreas y la **materialidad** (cuantitativa y cualitativa)?
- [ ] ¿La DD es **proporcional** al tamaño y al riesgo del deal y a la **tesis** del comprador?
- [ ] ¿Hay **equipo, calendario y presupuesto** y una *request list* adaptada al deal?

**Durante la revisión:**
- [ ] **Titularidad:** ¿el vendedor es realmente dueño de las acciones/activos? ¿Las acciones están bien
  emitidas y pagadas?
- [ ] **Change of control:** ¿qué contratos clave se caen o renegocian al cambiar el dueño?
- [ ] **QoE:** ¿las utilidades son **recurrentes y reales**? ¿Hay deuda oculta o pasivos contingentes?
- [ ] **Fiscal/laboral/ambiental:** ¿contingencias materiales (EFOS, subcontratación, contaminación)?
- [ ] **Permisos:** ¿vigentes y **transferibles**? ¿La operación requiere autorización (COFECE/sectorial)?
- [ ] **Compliance:** ¿exposición a corrupción/lavado? (riesgo de responsabilidad heredada)
- [ ] ¿Leíste las **ausencias** y las aclaraste por **Q&A**? ¿Cuidaste **privilegio** y *clean teams*?

**Al cerrar la DD:**
- [ ] ¿El **DD report** está jerarquizado (deal breaker / mayor / menor) y orientado a la decisión?
- [ ] Para cada *red flag* mayor: ¿definiste la **herramienta** (precio, rep, indemnización, escrow,
  condición, exclusión)?
- [ ] ¿Previste la **DD confirmatoria** entre *signing* y *closing* (bring-down + MAC)?

## 42. Bibliografía comentada

- **American Bar Association, *Model Stock Purchase Agreement with Commentary*.** **Imprescindible** para
  ver cómo los hallazgos de la DD se convierten en reps, indemnización y *disclosure schedules*.
- **Securities Act de 1933 (EE.UU.), §11 — la *due diligence defense*.** La fuente histórica del concepto:
  la investigación razonable como eximente de responsabilidad.
- **FCPA Resource Guide (DOJ/SEC).** El estándar global sobre **DD anticorrupción** en adquisiciones y la
  sucesión de responsabilidad. Lectura obligada para compliance.
- **Jurisprudencia de Delaware (*Akorn v. Fresenius* —MAC—; *Smith v. Van Gorkom* —deber de informarse—).**
  Cómo la DD se conecta con el derecho del consejo y con la salida del deal.
- **Ley Federal de Competencia Económica y guías de la COFECE.** Concentraciones, *gun jumping* y manejo
  de información sensible (clean teams) durante la DD.
- **Código Fiscal de la Federación, art. 69-B ⟳ (operaciones simuladas).** El núcleo del riesgo de la DD
  fiscal en México.
- **Doctrina civil sobre buena fe, dolo y saneamiento (CCF).** La red de seguridad que el derecho
  mexicano añade a las protecciones contractuales.
- **Practical Law / PLC y manuales de DD de los grandes despachos.** Los *checklists* y *precedents* de
  mercado, herramienta de trabajo diario.

## 43. Ruta hacia el siguiente libro

Ya sabes **investigar lo que se compra** y **traducir el riesgo en protección**. El siguiente paso es
entender en detalle las **arquitecturas jurídicas** mediante las cuales se ejecuta la transacción: cómo,
exactamente, se compra y se combina una empresa.

- **Siguiente libro:** *[Libro 3 · Estructuras: fusiones, escisiones y adquisiciones](./03-Estructuras-Fusiones-Escisiones-Adquisiciones.md)* —
  el desarrollo a fondo del *share deal*, el *asset deal*, la **fusión** (por absorción y por integración),
  la **escisión**, y las reestructuras; sus requisitos corporativos (LGSM), efectos, derechos de los
  acreedores y de las minorías, y consecuencias fiscales. Es el "cómo" jurídico de lo que en el Libro 1
  viste como mapa.
- **Conexión inmediata:** en este Libro 2 aprendiste que un **hallazgo de la DD empuja la elección de
  estructura** (un riesgo alto de pasivos ocultos favorece el *asset deal*; la necesidad de continuidad
  de contratos y permisos favorece el *share deal* o la fusión). El Libro 3 te dará el dominio técnico de
  cada estructura para tomar —y ejecutar— esa decisión con maestría.

---

## ✦ ¿Por qué esto importa para un abogado corporativo?

Porque la due diligence es la **primera competencia real** que un despacho de M&A le exige a un abogado, y
la que **más valor medible** aporta al cliente. Cada riesgo que el abogado detecta y traduce en protección
contractual es dinero ahorrado; cada riesgo que se le escapa, una pérdida que el cliente sufrirá después
del *closing*, cuando ya no hay remedio fácil. Un solo pasivo fiscal o ambiental no detectado puede valer
más que la empresa entera. Además, la DD es **transversal**: la misma habilidad se usa en una adquisición,
una venta, un financiamiento, una inversión de VC/PE, una salida a bolsa y un programa de compliance.
Quien domina la due diligence tiene una herramienta que usará toda su carrera y desarrolla, de paso, el
músculo mental que define al gran abogado de transacciones: **ver el riesgo donde otros ven papeles**.

## ✦ Cómo piensa un socio de un despacho internacional

> *"Cuando dirijo una due diligence, no busco 'revisar todo' —eso es imposible y nadie lo paga—. Busco
> **el riesgo que mueve la aguja**. Lo primero que pregunto a mi equipo es: '¿qué tres cosas, si están
> mal, hacen que mi cliente NO compre o pague mucho menos?' Eso ordena el trabajo. Vivo obsesionado con
> tres áreas: la **titularidad** (¿de verdad es dueño de lo que vende?), la **calidad de las utilidades**
> (¿estos números son reales y recurrentes, o están maquillados?) y el ***change of control*** (¿el
> activo se evapora justo cuando compramos?). Y exijo a cada asociado la misma disciplina: no quiero un
> reporte de 300 páginas con todo lo que encontraron; quiero **tres niveles** —lo que mata el deal, lo
> que repreciamos o blindamos, y lo que solo documentamos— y, para cada riesgo mayor, **la cláusula**
> que lo resuelve. Un hallazgo sin cláusula es trabajo perdido. La due diligence no termina cuando
> entiendo el riesgo; termina cuando lo **traduje** en una protección que mi cliente pueda cobrar."*

## ✦ Errores que cuestan millones

1. **DD financiera superficial (el síndrome HP-Autonomy).** Pagar un múltiplo alto sin verificar la
   *Quality of Earnings* y descubrir después que los ingresos estaban inflados. *Prevención:* QoE
   rigurosa; ninguna prisa por cerrar justifica no verificar los números.
2. **Ignorar el *change of control*.** No detectar que los contratos o permisos clave se cancelan al
   cambiar el dueño, y comprar una empresa que se vacía de valor el día del *closing*. *Prevención:*
   mapearlos y volverlos **condición al *closing*** (consentimientos).
3. **DD de compliance ausente.** No investigar la corrupción y **heredar** responsabilidad penal y
   regulatoria (FCPA). *Prevención:* DD anticorrupción rigurosa y remediación documentada; "no investigué"
   agrava la sanción.
4. **No traducir los hallazgos al contrato.** Detectar el riesgo y no convertirlo en rep, indemnización
   especial, *escrow* o condición: el comprador termina pagando un riesgo que **sí** se había visto.
   *Prevención:* para cada *red flag* mayor, define la herramienta de la sección 14.E.
5. **Intercambiar información sensible entre competidores sin *clean team*.** Revisar precios y clientes
   del competidor antes de la autorización y caer en *gun jumping* informativo (multas de competencia).
   *Prevención:* *clean teams* y conclusiones agregadas hasta el *closing*.

---

> *Cierre del Libro 2.* Has aprendido a **mirar antes de comprar**: a investigar la empresa por dentro,
> jerarquizar el riesgo y —lo esencial— **traducir cada hallazgo en una protección contractual**. La due
> diligence es la bisagra entre conocer la realidad de la *target* y plasmarla en el contrato; conecta
> todo lo que estudiaste (sociedades, contratos, responsabilidad, gobierno, competencia, fiscal, laboral)
> en una sola habilidad práctica de élite. Con el mapa del M&A (Libro 1) y el arte de la due diligence
> (Libro 2) en tu poder, estás listo para dominar las **arquitecturas de la transacción**. Avanzamos al
> **Libro 3 · Estructuras: fusiones, escisiones y adquisiciones**, donde aprenderás, con precisión
> técnica, **cómo** se compra y se combina una empresa.
