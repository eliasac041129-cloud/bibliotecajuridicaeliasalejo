# [Nivel IV · Libro 4] La Documentación de la Operación: Term Sheet, SPA, APA y SHA

> ⟳ **Apóstrofe de vigencia — léela cada vez.** El Derecho cambia sin avisar: un artículo puede mudar de número, de redacción o quedar **derogado** de un día para otro. El símbolo **⟳** que aparece tras cada artículo citado en este libro significa una sola cosa: *«¿sigue vigente —y con este mismo número— hoy? No lo cites de memoria ni desde este libro: **reitéralo en su código vigente**»* (textos oficiales en [`../../fuentes-legales/`](../../fuentes-legales/)). Caso real: el **art. 390 del CPF** que este proyecto cotejó aparece hoy como **«Derogado»**. Recuerda: un **✅** dice que el dato fue verificado *palabra por palabra a la fecha de su fuente*; la **⟳** te avisa que esa fecha ya quedó atrás y que la última palabra la tiene el código, no el libro.


> Investigaste (Libro 2) y estructuraste (Libro 3). Ahora todo debe convertirse en **texto vinculante**.
> Este es el libro donde el M&A se vuelve **palabra escrita y exigible**: el **Term Sheet/LOI** que fija
> las bases, el **SPA** (compraventa de acciones) y el **APA** (compraventa de activos) que consuman la
> operación, y el **SHA** (convenio entre accionistas) que gobierna la convivencia después. Aquí la
> diferencia entre un abogado bueno y uno extraordinario se mide **cláusula por cláusula**: una palabra
> —"material", "a mi leal saber y entender", "salvo lo revelado"— puede mover millones. Este es el libro
> más operativo y, probablemente, el más rentable de toda la biblioteca.

**Etiquetas:** corporate law · M&A · contratos · term sheet · SPA · APA · SHA · reps & warranties · indemnización · MAC
**Prerrequisitos:** [Libro 1 · Fundamentos de M&A](./01-Fundamentos-de-MA.md), [Libro 2 · Due Diligence](./02-Due-Diligence.md) y [Libro 3 · Estructuras](./03-Estructuras-Fusiones-Escisiones-Adquisiciones.md) + [Contratos Parte General](../Nivel-I-Fundamentos/08-Contratos-Parte-General.md), [Obligaciones](../Nivel-II-Derecho-Civil-Profundo/01-Teoria-General-de-las-Obligaciones-Profundizacion.md), [Contratos Mercantiles](../Nivel-III-Derecho-Mercantil/04-Contratos-Mercantiles.md) y [Gobierno Corporativo](../Nivel-III-Derecho-Mercantil/07-Gobierno-Corporativo.md).
**Estándar:** V3 (43 secciones + secciones transversales).
**⏱ Tiempo estimado de dominio:** 6–8 semanas (≈ 70–90 h de estudio activo). Lectura de
reconocimiento: 12–15 h. *Estúdialo en bloques: arquitectura documental y Term Sheet/LOI → anatomía del
SPA (reps, covenants, condiciones, indemnización, MAC) → disclosure schedules y mecanismos de precio →
APA (asset deal) → SHA (convenio de accionistas).*

> **Aviso de método.** Tratado, no repaso. Aquí aprenderás a **leer y redactar** los contratos del M&A
> entendiendo **por qué** existe cada cláusula, **a quién protege**, **cómo se negocia** y **qué pasa si
> falta o falla**. Cada cláusula se conecta con la due diligence (de dónde nace) y con la estructura (qué
> documento corresponde a cada arquitectura). No memorices cláusulas: **entiende su lógica**.

---

### Nivel de importancia profesional (vista rápida)
```
Litigio              ★★★★☆
Corporate            ★★★★★
M&A                  ★★★★★
Mercado de Valores   ★★★★☆
Venture Capital      ★★★★★
Private Equity       ★★★★★
Gobierno Corporativo ★★★★★
Compliance           ★★★☆☆
Derecho Bancario     ★★★★☆
Empresa Familiar     ★★★★☆
```
*Es la competencia más visible y mejor remunerada del abogado de M&A: redactar y negociar el SPA y el
SHA. Quien domina la documentación con criterio —no como formulario— se vuelve indispensable en cualquier
operación.*

## 1. Introducción

Una operación de M&A vive, finalmente, en **documentos**. Todo lo que investigaste en la due diligence y
todo lo que diseñaste en la estructura debe **plasmarse por escrito** en contratos que sean claros,
completos y, sobre todo, **exigibles**. Este libro estudia los **cuatro documentos nucleares** del M&A:

1. El **Term Sheet** (u hoja de términos) y la **LOI/Carta de Intención** —el acuerdo **preliminar** que
   fija las bases de la negociación, mayormente **no vinculante**—.
2. El **SPA** (*Share Purchase Agreement* / contrato de compraventa de acciones) —el contrato
   **definitivo** del *share deal*, el documento rey del M&A—.
3. El **APA** (*Asset Purchase Agreement* / contrato de compraventa de activos) —el contrato definitivo
   del *asset deal*—.
4. El **SHA** (*Shareholders Agreement* / convenio entre accionistas) —el contrato que **gobierna la
   relación** entre los socios después de la operación (capital, decisiones, salidas)—.

La idea rectora del libro: **el contrato de M&A no describe una compraventa; la diseña como un sistema de
asignación de riesgo a lo largo del tiempo.** A diferencia de comprar un coche (pagas, te lo llevas, fin),
en M&A el contrato regula un **proceso**: lo que cada parte declara (reps), lo que promete hacer y no hacer
entre la firma y el cierre (covenants), las condiciones para cerrar, qué pasa si algo sale mal después
(indemnización), cómo se ajusta el precio, y cómo conviven los socios durante años (SHA). Cada cláusula es
una **pieza de ingeniería** que responde a un riesgo concreto —muchos de ellos detectados en la due
diligence—.

Por eso este libro no es un formulario. Vas a aprender la **gramática del riesgo**: por qué existe cada
cláusula, a quién favorece, cómo se negocia la palabra exacta, y qué consecuencia tiene su redacción. Quien
entiende esa gramática puede leer cualquier SPA del mundo y detectar en minutos dónde está el riesgo y
quién lo soporta. Esa es la habilidad que define al abogado de transacciones de élite.

## 2. Objetivos del libro

Al terminar, el lector será capaz de:

- **Distinguir y articular** los cuatro documentos del M&A (Term Sheet/LOI, SPA, APA, SHA) y saber **cuál
  corresponde** a cada estructura (Libro 3) y **en qué fase** se usa cada uno (Libro 1).
- **Manejar** un **Term Sheet/LOI**: distinguir lo **vinculante** (exclusividad, confidencialidad, ley
  aplicable) de lo **no vinculante** (precio, estructura) y entender por qué esa distinción es crítica.
- **Diseccionar la anatomía del SPA** cláusula por cláusula: objeto y precio, **representations &
  warranties**, **covenants**, **condiciones** (CP), **indemnización** (con *caps*, *baskets*, supervivencia),
  **MAC**, *closing* y *signing*.
- **Entender los *disclosure schedules*** y su diálogo con la due diligence y con las reps (qué se revela
  deja de estar garantizado; el debate del *sandbagging*).
- **Dominar los mecanismos de precio**: precio fijo, *locked box*, *completion accounts*, ajuste por
  capital de trabajo y deuda neta, *earn-out*, *escrow*.
- **Comprender el APA**: cómo se describe el perímetro de activos y pasivos, las cesiones y consentimientos,
  y en qué se diferencia su estructura de la del SPA.
- **Dominar el SHA**: cláusulas de gobierno (consejo, vetos, *deadlock*), de capital (preferencias,
  antidilución) y de transferencia y salida (*lock-up*, *ROFR/ROFO*, *tag along*, *drag along*, *put/call*).
- **Traducir** hallazgos de la due diligence en cláusulas concretas (rep específica, indemnización
  especial, condición, ajuste) y **leer** un contrato detectando dónde está el riesgo y quién lo soporta.

## 3. Importancia profesional

La redacción y negociación de la documentación es **la competencia más visible y mejor remunerada** del
abogado de M&A. Es el producto tangible por el que el cliente paga: el contrato que protege su inversión.
Un socio de M&A se distingue, ante todo, por su **maestría en el SPA y el SHA** —saber qué cláusula pedir,
cómo redactarla, hasta dónde ceder en la negociación y qué riesgo esconde cada palabra del borrador de la
contraparte—.

Esta habilidad tiene una característica peculiar: es **acumulativa y muy difícil de improvisar**. Un buen
contrato de M&A es el resultado de décadas de práctica destilada en cláusulas estándar de mercado, cada
una de las cuales existe porque **algún deal salió mal** y la cláusula nació para evitar que se repita.
Quien entiende esa historia —por qué la cláusula MAC se redacta así tras el caso *Akorn*, por qué los
*caps* y *baskets* limitan la indemnización, por qué el *sandbagging* se pacta expresamente— lee los
contratos con una profundidad que un formulario jamás da.

Para **tu perfil específico** —estructuración de operaciones complejas, M&A, gobierno corporativo y
contratos estratégicos—, este libro es **central**: el SPA/APA es donde se documenta la operación; el SHA
es donde se diseña el **gobierno corporativo contractual** (cómo deciden los socios, cómo entran y salen
inversionistas); y el Term Sheet es donde se sientan las bases de cualquier contrato estratégico. Dominar
esta documentación es dominar el **lenguaje en el que se escriben los acuerdos corporativos**.

## 4. Historia y origen

Los contratos del M&A moderno son, en su forma actual, una **creación de la práctica anglosajona** del
siglo XX, especialmente de los grandes despachos de Nueva York y Londres. A diferencia de las figuras
societarias (que vienen de la ley), la **arquitectura del SPA** —con sus *representations & warranties*,
*covenants*, *conditions* e *indemnification*— se desarrolló como un **producto de la autonomía
contractual**: los abogados, ante operaciones cada vez más grandes y riesgosas, fueron inventando
cláusulas para asignar el riesgo de lo desconocido entre comprador y vendedor.

El origen conceptual está en el **derecho de contratos del common law** y en su lógica de *warranties*
(garantías cuyo incumplimiento da derecho a daños) y *conditions* (condiciones cuyo incumplimiento permite
no cumplir o terminar). Sobre esa base, la práctica transaccional construyó un edificio sofisticado: las
reps para distribuir el riesgo informativo, los *disclosure schedules* para que el vendedor revele
excepciones, la indemnización con sus topes y mínimos para acotar la responsabilidad, la cláusula MAC para
el riesgo del período entre firma y cierre.

El **Term Sheet** y la **LOI** nacieron de la necesidad práctica de **fijar las bases** de una negociación
compleja antes de invertir en la due diligence y en la redacción del contrato definitivo —un "apretón de
manos" estructurado que ordena el proceso sin comprometer aún a las partes en lo sustancial—. El **SHA**,
por su parte, evolucionó del derecho societario y de la necesidad de los socios de regular
**contractualmente** lo que los estatutos no alcanzan a cubrir (especialmente la convivencia entre
mayoritarios y minoritarios, y entre fundadores e inversionistas).

En **México y el civil law**, estos documentos se **adoptaron e integraron** a partir de los años 1990,
adaptando las cláusulas anglosajonas al marco del Código Civil y de Comercio. Hoy un SPA mexicano se
parece muchísimo a uno de Nueva York —porque el M&A es global—, pero se interpreta y ejecuta conforme al
derecho mexicano, lo que genera matices finos que el abogado debe dominar.

## 5. Evolución histórica

La documentación del M&A ha evolucionado en tres movimientos:

**1) De la compraventa simple al contrato de asignación de riesgo.** Originalmente, comprar una empresa se
documentaba como una compraventa más. Con el tiempo, y a medida que los deals revelaban riesgos ocultos
(pasivos, contingencias, información falsa), el contrato se transformó en un **sistema sofisticado de
asignación de riesgo**: las reps, la indemnización y la MAC convirtieron el SPA en una **máquina de
distribuir lo desconocido** entre las partes.

**2) La estandarización de mercado.** La repetición de miles de operaciones generó **estándares de
mercado** para cada cláusula: rangos típicos de *caps* (qué porcentaje del precio puede reclamarse), de
plazos de supervivencia de las reps, de *baskets*. Surgieron documentos de referencia (como el *Model
Stock Purchase Agreement* de la ABA) y bases de *precedents*. El abogado moderno negocia sabiendo qué es
"de mercado" y qué es "agresivo".

**3) La era de los seguros y la eficiencia.** En las últimas dos décadas apareció el **seguro de
representations & warranties (W&I insurance)**, que traslada a una aseguradora el riesgo de que las reps
sean falsas, permitiendo a los vendedores salir "limpios" (sin escrow ni responsabilidad prolongada) y
agilizando los deals. Esto ha **reconfigurado** la negociación de la indemnización en muchas operaciones.
En paralelo, la tecnología (gestión de borradores, control de versiones, revisión asistida) ha acelerado
la producción de contratos, aunque el **criterio** sigue siendo humano.

## 6. Contexto económico

La documentación del M&A tiene una función económica precisa: **reducir los costos de transacción y
distribuir el riesgo de forma eficiente** para que el deal se haga y cree valor. Tres ideas económicas la
gobiernan:

- **El contrato como respuesta a la asimetría de información.** Como vimos en la due diligence (Libro 2),
  el vendedor sabe más que el comprador. Las **reps & warranties** son el mecanismo económico que corrige
  esa asimetría *en el contrato*: el vendedor "garantiza" un estado de cosas y, si miente u omite, paga
  (indemnización). Esto permite al comprador pagar un precio justo en vez de descontar por miedo a lo
  desconocido.
- **La asignación eficiente del riesgo.** La teoría dice que cada riesgo debe asignarse a quien mejor puede
  **controlarlo o soportarlo**. El SPA hace exactamente eso: los riesgos del pasado de la empresa (que el
  vendedor conocía o debía conocer) se le asignan vía reps; los riesgos futuros del negocio (que el
  comprador ahora controla) los asume el comprador; los riesgos concretos detectados se asignan
  específicamente (indemnización especial). Una buena redacción **minimiza el riesgo mal asignado**, que
  es puro valor destruido.
- **Los límites a la responsabilidad como precio implícito.** Los *caps*, *baskets* y plazos de
  supervivencia no son "trucos del vendedor": son la forma de **poner precio** al riesgo residual. Un
  vendedor que garantiza sin límite cobraría más (o no vendería); un *cap* es, en el fondo, un reparto
  económico de cuánto riesgo retiene cada parte. La negociación de estos límites es, en realidad, una
  **negociación de precio encubierta**.

## 7. Contexto político y regulatorio

La libertad para diseñar los contratos del M&A es amplia (autonomía de la voluntad), pero opera dentro de
límites regulatorios que el abogado debe respetar:

- **Límites del orden público y la ley imperativa.** Por más que las partes pacten, no pueden contravenir
  normas imperativas: ciertas protecciones de minorías, reglas societarias de la LGSM, derechos laborales
  irrenunciables, normas de competencia. Una cláusula que las viole es **nula**.
- **Derecho de la competencia (COFECE).** Las cláusulas de **no competencia** del vendedor (muy comunes en
  el SPA) deben ser **razonables** en objeto, tiempo y territorio para no constituir una restricción ilícita
  a la competencia. Y el calendario de *closing* debe respetar la prohibición de *gun jumping*.
- **Régimen de las emisoras (LMV).** Si la *target* es pública, la documentación interactúa con el régimen
  de OPAs, revelación de información e información privilegiada.
- **Inversión extranjera y sectores regulados.** Los contratos deben respetar los límites a la
  participación foránea y prever las autorizaciones sectoriales como condiciones.
- **Validez y forma.** El derecho mexicano impone requisitos de forma para ciertos actos (transmisión de
  inmuebles ante notario, inscripciones registrales), que el contrato debe satisfacer para ser plenamente
  eficaz frente a terceros.

## 8. Contexto social

La documentación de M&A, aunque técnica, refleja y administra **relaciones humanas tensas**. El SPA es el
producto de una **negociación adversarial** entre comprador y vendedor, cada uno tratando de quedarse con
la mejor asignación de riesgo; el contrato es la **foto del equilibrio de poder** alcanzado (un comprador
fuerte logra reps amplias, caps altos y *pro-sandbagging*; un vendedor fuerte, lo contrario). Leer un
contrato es, en parte, leer **quién tenía más poder** en la mesa.

El **SHA**, por su parte, regula una **convivencia de años** entre personas que seguirán siendo socios:
fundadores e inversionistas, familia y fondo, mayoritarios y minoritarios. Sus cláusulas (vetos,
resolución de *deadlocks*, salidas) son, en el fondo, mecanismos para **manejar el conflicto humano**
antes de que ocurra —un "acuerdo prenupcial" empresarial—. El abogado que redacta un SHA está diseñando
**cómo se llevarán las personas** cuando las cosas vayan bien y, sobre todo, cuando vayan mal.

Hay también una dimensión de **confianza y reputación**: aunque el contrato lo prevea todo, las partes
prefieren no litigar (es caro y destruye relaciones). Por eso muchos mecanismos (escrow, ajustes,
arbitraje) buscan resolver los conflictos **sin guerra**. El buen abogado redacta para **prevenir el
litigio**, no solo para ganarlo.

## 9. Contexto empresarial

Desde la óptica del negocio, los documentos del M&A cumplen funciones estratégicas que el abogado debe
entender para servir bien a su cliente:

- **El Term Sheet ordena el proceso y "amarra" al vendedor.** Antes de gastar en due diligence y abogados,
  el comprador quiere **exclusividad** (que el vendedor no negocie con otros) y unas bases claras. El Term
  Sheet le da eso. Para el vendedor, fija expectativas y filtra compradores serios.
- **El SPA protege la inversión y reparte el riesgo del pasado.** Es el documento donde el comprador
  **blinda** lo que pagó: reps que cubren lo desconocido, indemnización para cobrar si algo sale mal,
  ajustes para pagar el precio correcto. Para el vendedor, es donde **acota su responsabilidad** (caps,
  plazos) y logra un "corte limpio".
- **El APA permite comprar selectivamente.** Cuando la estrategia es adquirir solo una parte (una línea,
  una planta, una cartera), el APA es el vehículo: describe con precisión qué se lleva y qué se deja.
- **El SHA diseña el futuro del control y de la salida.** Para un fondo de PE/VC, el SHA es **tan
  importante como el precio**: define sus derechos de gobierno (asientos, vetos), su protección económica
  (preferencias, antidilución) y, sobre todo, **cómo y cuándo saldrá** (drag along, tag along, derechos de
  venta). Para los fundadores, define cuánto control conservan. El SHA es el **contrato del poder y del
  dinero futuro**.

En suma: el abogado que domina estos documentos no solo "redacta"; **diseña la asignación de riesgo, el
gobierno y las salidas** de la operación. Conversa con el negocio (¿qué te preocupa?, ¿qué riesgo no
quieres?, ¿cómo y cuándo quieres salir?) y traduce esas respuestas en cláusulas. Esa es la diferencia
entre un mecanógrafo de contratos y un **arquitecto de operaciones**.

## 10. Definiciones doctrinales

La doctrina transaccional define los documentos y conceptos centrales así:

- **Term Sheet / Hoja de términos:** documento que resume las **condiciones económicas y estructurales
  esenciales** de una operación propuesta, generalmente **no vinculante** en cuanto al fondo, que sirve de
  base para negociar el contrato definitivo. La doctrina lo describe como la "**columna vertebral
  comercial**" del deal.
- **Letter of Intent (LOI) / Carta de Intención:** comunicación formal por la que una parte expresa su
  **intención** de realizar la operación bajo ciertos términos. Funcionalmente se solapa con el Term Sheet;
  suele incorporar **algunas cláusulas vinculantes** (exclusividad, confidencialidad, gastos).
- **SPA (*Share Purchase Agreement*) / Contrato de compraventa de acciones:** contrato **definitivo y
  vinculante** por el cual el vendedor transmite al comprador las **acciones o partes sociales** de la
  *target* a cambio de un precio, regulando exhaustivamente la asignación del riesgo (reps, covenants,
  condiciones, indemnización). Es el documento central del *share deal*.
- **APA (*Asset Purchase Agreement*) / Contrato de compraventa de activos:** contrato definitivo por el
  cual el vendedor transmite **activos (y, en su caso, pasivos) determinados** al comprador. Es el
  documento central del *asset deal*; su rasgo distintivo es la **descripción precisa del perímetro**
  (qué activos y pasivos se incluyen y cuáles se excluyen).
- **SHA (*Shareholders Agreement*) / Convenio entre accionistas:** contrato entre los socios de una
  sociedad (y a veces la sociedad misma) que regula sus **relaciones internas**: gobierno (cómo se decide),
  capital (preferencias, dilución) y transmisión/salida (cómo entran y salen socios). Complementa —y a
  veces "blinda"— los estatutos sociales.
- **Representations & warranties (declaraciones y garantías / manifestaciones):** afirmaciones de hecho
  que una parte (típicamente el vendedor) hace sobre sí misma y sobre la *target* a una fecha determinada,
  y de cuya **falsedad** responde. La doctrina las define como el mecanismo de **asignación contractual del
  riesgo informativo**.
- **Covenants (obligaciones de hacer / no hacer):** compromisos de conducta de las partes, especialmente
  **entre la firma (*signing*) y el cierre (*closing*)** —p. ej., operar el negocio en el curso ordinario,
  no repartir dividendos extraordinarios— y, a veces, posteriores al cierre (no competencia, no
  captación).
- **Conditions precedent (CP) / condiciones suspensivas:** hechos que deben **cumplirse** para que nazca la
  obligación de cerrar (autorizaciones, consentimientos, veracidad de las reps a la fecha de cierre).
- **Indemnification / indemnización:** mecanismo por el cual una parte se obliga a **resarcir** a la otra
  por las pérdidas derivadas del incumplimiento de reps/covenants o de contingencias identificadas.
- **MAC / MAE (*Material Adverse Change / Effect*):** cláusula que permite al comprador **no cerrar** (o
  renegociar) si entre la firma y el cierre ocurre un **cambio sustancialmente adverso** en la *target*.

## 11. Definiciones legales y marco normativo

Estos contratos son, en esencia, **creación de la autonomía de la voluntad**, pero se asientan en el marco
legal mexicano:

- **Libertad contractual y obligatoriedad (CCF y Código de Comercio).** El principio *pacta sunt servanda*
  (los contratos legalmente celebrados obligan a las partes) y la **autonomía de la voluntad** son la base
  legal: las partes pueden diseñar libremente las cláusulas (reps, indemnización, MAC) **dentro de los
  límites** de la ley, el orden público y las buenas costumbres.
- **Compraventa (CCF / Código de Comercio).** El SPA y el APA son, en su núcleo, **compraventas** (de
  acciones o de activos), reguladas supletoriamente por las reglas de la compraventa: cosa, precio,
  obligaciones de transmitir y de pagar, **saneamiento** por vicios ocultos y por evicción —que las reps e
  indemnización **complementan y modulan** contractualmente—.
- **Transmisión de acciones (LGSM / LMV).** La transmisión de acciones nominativas opera por **endoso** e
  inscripción en el **libro de registro de accionistas**; el SPA documenta la obligación, pero la
  transmisión societaria se perfecciona conforme a la LGSM (o la LMV para emisoras).
- **Cesión de derechos y de deudas (CCF).** En el APA, la transmisión de contratos y créditos se rige por
  las reglas de la **cesión de derechos** (notificación al deudor) y de la **asunción de deudas**
  (consentimiento del acreedor cuando se requiera).
- **Vicios del consentimiento (CCF).** El **dolo**, el **error** y la **mala fe** pueden viciar el contrato;
  esto sustenta la responsabilidad del vendedor que **mintió** en sus reps más allá de lo pactado.
- **Convenios entre accionistas (LGSM / LMV).** El derecho mexicano **reconoce y da eficacia** a los
  convenios entre accionistas (particularmente en la **S.A.P.I.** conforme a la LMV, que valida cláusulas
  como restricciones a la transmisión, derechos de veto, *drag/tag along*, opciones), lo que dio base legal
  sólida al **SHA** en México.
- **Condición y término (CCF).** Las **condiciones suspensivas** (CP del *closing*) y los **plazos** se
  rigen por la teoría general de las obligaciones (que estudiaste en Nivel I-II).

> **Nota de método:** la eficacia de ciertas cláusulas "importadas" del common law (p. ej., *sandbagging*,
> ciertos límites de indemnización) depende de su **compatibilidad** con el derecho mexicano; el abogado
> debe redactarlas con anclaje en figuras locales (renuncias, penas convencionales, condiciones) para que
> sean exigibles. Verifica siempre la ley vigente (Manifiesto XI.5).

## 12. Definición sencilla

Piensa en comprar una empresa como en **un matrimonio con acuerdo prenupcial muy detallado**.

- El **Term Sheet / LOI** es el **noviazgo formal**: "queremos casarnos bajo estas condiciones generales,
  y mientras tanto prometemos no salir con nadie más (exclusividad) y no contar nuestros secretos
  (confidencialidad)". Casi nada es obligatorio todavía, salvo esas dos promesas.
- El **SPA** es el **contrato de matrimonio**: lo dice todo. Qué aportas, qué me aseguras que es verdad de
  ti ("no tengo deudas ocultas" = reps), qué prometes hacer hasta la boda ("no gastarás el dinero común" =
  covenants), qué tiene que pasar para casarnos ("que tus papás autoricen" = condiciones), y **qué pasa si
  me mentiste** ("me compensas" = indemnización). Incluso prevé qué ocurre si justo antes de la boda
  descubrimos un desastre (MAC = me puedo echar para atrás).
- El **APA** es como decir: "no me caso contigo entero; me quedo **solo con tu casa y tu coche**, no con
  tus deudas ni con tu suegra". Compras piezas, no a la persona completa.
- El **SHA** es el **reglamento de convivencia** para cuando ya vivimos juntos (varios socios): quién
  decide qué, quién pone cuánto, y —clave— **cómo nos divorciamos** sin destruirnos (cómo y cuándo puede
  irse cada quien, y a qué precio).

La pregunta de fondo en todos: *¿qué me aseguras?, ¿qué pasa si sale mal?, ¿cómo entro y cómo salgo?* Todo
el libro responde, cláusula por cláusula, esas tres preguntas.

## 13. Conceptos fundamentales

Fija este vocabulario; es el idioma del M&A y lo usarás en cada operación de tu carrera:

**Documentos y fases:**
- **Term Sheet / LOI / MOU:** acuerdos **preliminares** (bases de la negociación), mayormente no
  vinculantes salvo cláusulas específicas.
- **SPA / APA:** contratos **definitivos** de compraventa (acciones / activos).
- **SHA:** convenio que **gobierna** la relación entre socios.
- **Signing vs. Closing:** la **firma** del contrato vs. el **cierre** (pago y transmisión); entre ambos se
  cumplen las condiciones (Libro 1).

**El núcleo del SPA:**
- **Representations & warranties (reps):** declaraciones de hecho garantizadas (sobre el título de las
  acciones, estados financieros, contratos, litigios, impuestos, cumplimiento, etc.).
- **Fundamental reps:** las reps "esenciales" (título de las acciones, capacidad, autoridad) que reciben
  protección reforzada (sin tope, plazo largo).
- **Covenants:** obligaciones de hacer/no hacer, pre-cierre (operación ordinaria) y post-cierre (no
  competencia, no captación).
- **Conditions precedent (CP):** condiciones para cerrar (autorizaciones, consentimientos, veracidad de
  reps —*bring-down*—, ausencia de MAC).
- **Indemnification:** la obligación de resarcir; viene modulada por:
  - **Cap (tope):** monto máximo de responsabilidad (a menudo un % del precio).
  - **Basket / deducible:** umbral mínimo de pérdidas acumuladas antes de poder reclamar (tipo *tipping* o
    *true deductible*).
  - **De minimis:** monto mínimo por reclamación individual para que cuente.
  - **Survival (supervivencia):** plazo durante el cual las reps siguen vivas y reclamables.
  - **Special / specific indemnity:** indemnización específica por un riesgo **concreto y conocido** (de la
    due diligence), normalmente **fuera** de caps y baskets.
- **MAC / MAE:** cláusula de cambio adverso relevante (derecho a no cerrar).
- **Disclosure schedules:** anexos donde el vendedor **revela excepciones** a sus reps (lo revelado deja de
  estar garantizado).
- **Sandbagging:** si el comprador que **sabía** que una rep era falsa puede igual reclamar
  (*pro-sandbagging*) o no (*anti-sandbagging*); se pacta expresamente.

**Mecanismos de precio:**
- **Locked box:** precio fijo basado en un balance de referencia pasado, sin ajuste posterior (el riesgo/
  beneficio pasa al comprador desde la fecha del *box*).
- **Completion accounts:** ajuste del precio según el balance al cierre (capital de trabajo, deuda neta,
  caja).
- **Earn-out:** parte del precio **diferida y condicionada** a resultados futuros de la *target*.
- **Escrow / holdback:** retención de parte del precio en garantía de indemnizaciones.

**El núcleo del SHA:**
- **Drag along (derecho de arrastre):** la mayoría que vende puede **obligar** a la minoría a vender en las
  mismas condiciones.
- **Tag along (derecho de acompañamiento):** la minoría puede **sumarse** a la venta de la mayoría en las
  mismas condiciones (protección).
- **ROFR / ROFO (derecho del tanto / de primera oferta):** derechos preferentes de los socios para adquirir
  antes que un tercero.
- **Lock-up:** prohibición temporal de transmitir acciones.
- **Preferencia de liquidación:** derecho del inversionista a cobrar primero (un múltiplo de su inversión)
  en una venta o liquidación.
- **Antidilución:** protección del inversionista frente a emisiones futuras a menor precio (*down round*).
- **Vetos / reserved matters:** decisiones que requieren el consentimiento del inversionista/minoría.
- **Deadlock:** mecanismo para resolver **empates/bloqueos** en la toma de decisiones (p. ej., *buy-sell* o
  "ruleta rusa").
- **Put / Call options:** opciones de **venta** (put, el socio obliga a que le compren) y de **compra**
  (call, obliga a que le vendan) bajo ciertas condiciones.

Con este vocabulario, entramos al **desarrollo absoluto**, donde diseccionamos cada documento por dentro.

## 14. Desarrollo absoluto

Esta es la sección central del libro. La desarrollamos en cinco bloques: **(A)** el **Term Sheet / LOI**
—las bases de la negociación y la trampa de lo "no vinculante"—; **(B)** la **anatomía del SPA, parte I**
—estructura, *representations & warranties*, *covenants* y *conditions*—; **(C)** la **anatomía del SPA,
parte II** —*indemnification*, MAC, *disclosure schedules* y *sandbagging*—; **(D)** los **mecanismos de
precio y el APA** —cómo se fija y ajusta el precio, y las particularidades del *asset deal*—; y **(E)** el
**SHA** —gobierno, capital y salidas—. Estúdialos en ese orden: primero las bases, luego el contrato rey
por dentro, después el precio y el asset deal, y al final el contrato del poder y la salida.

### 14.A · El Term Sheet / LOI (las bases y la trampa de lo "no vinculante")

El **Term Sheet** (u hoja de términos) y la **LOI** (carta de intención) son el **primer documento** de
una operación: resumen las condiciones esenciales sobre las que las partes acuerdan **negociar** el
contrato definitivo. Funcionalmente son casi lo mismo (el Term Sheet suele ser esquemático, por puntos; la
LOI tiene forma de carta); a menudo se usan combinados.

**Qué contiene un Term Sheet típico:**
- **Las partes y la estructura:** quién compra, quién vende, y **qué estructura** (share deal, asset deal,
  fusión —Libro 3—).
- **El precio y su forma:** monto o rango, forma de pago (caja, acciones, diferido), mecanismo de precio
  (locked box vs. completion accounts —sección 14.D—), *earn-out*, *escrow*.
- **Las condiciones esenciales:** due diligence satisfactoria, autorizaciones (COFECE), consentimientos,
  financiamiento.
- **El calendario:** plazos para la due diligence, la negociación y el cierre.
- **Las cláusulas de proceso (las que SÍ suelen ser vinculantes):** **exclusividad** (*no-shop*: el
  vendedor no negocia con otros por un periodo), **confidencialidad** (NDA), **gastos** (quién paga qué),
  **ley aplicable y jurisdicción/arbitraje**.

**La distinción crítica: vinculante vs. no vinculante.** Esta es la lección capital del Term Sheet, y un
error aquí cuesta carísimo. Por regla general:
- Es **NO vinculante** lo **sustantivo**: el precio, la estructura, los términos comerciales. ¿Por qué? Para
  que las partes puedan **retirarse** si la due diligence revela problemas o si la negociación del SPA
  fracasa, sin quedar obligadas a comprar/vender.
- Es **VINCULANTE** lo **procesal**: la exclusividad, la confidencialidad, los gastos, la ley aplicable. El
  comprador **exige** exclusividad vinculante porque va a **invertir** mucho dinero en la due diligence y
  no quiere que el vendedor lo use para subir el precio con otros postores.

**La trampa.** Un Term Sheet **mal redactado** puede volverse **vinculante sin querer**. Si el lenguaje
sugiere un acuerdo cerrado sobre lo sustantivo (o si no se dice claramente que no obliga), un tribunal
podría considerar que existe un **contrato** o, al menos, una **responsabilidad precontractual** (*culpa in
contrahendo*: responsabilidad por romper de mala fe una negociación avanzada). Por eso **toda** hoja de
términos seria incluye una cláusula expresa y destacada que dice, en esencia: *"salvo las cláusulas X, Y y
Z (exclusividad, confidencialidad, gastos, ley aplicable), este documento NO es vinculante y no obliga a
las partes a celebrar la operación"*. Redactar bien esa cláusula es de las primeras cosas que aprende —a
golpes— un abogado junior.

**Para qué sirve, entonces, si casi nada obliga.** Sirve muchísimo: **ordena** la negociación, **alinea**
expectativas, **filtra** a las partes no serias, **amarra** al vendedor con la exclusividad mientras el
comprador invierte en la due diligence, y crea un **compromiso moral y reputacional** (retractarse de lo
acordado en un Term Sheet, aunque no obligue legalmente, tiene costo de reputación). Es el **mapa** que
guía la redacción del SPA.

### 14.B · Anatomía del SPA, parte I (estructura, reps, covenants, condiciones)

El **SPA** es el documento rey. Un SPA típico de M&A tiene una **estructura estándar** que debes conocer
como la palma de tu mano, porque se repite (con variaciones) en todo el mundo:

1. **Definiciones.** El glosario del contrato (términos en mayúscula). Aburrido pero **crítico**: la
   definición de "Pérdidas", "Conocimiento", "Cambio Adverso Relevante" o "Deuda" puede decidir un litigio.
2. **Objeto y precio.** Qué se vende (las acciones), por cuánto, forma de pago y mecanismo de precio.
3. **Representations & warranties** del vendedor (y algunas del comprador).
4. **Covenants** (obligaciones pre-cierre y post-cierre).
5. **Conditions precedent** (condiciones para cerrar).
6. **Indemnification** (con caps, baskets, supervivencia).
7. **Terminación** (cuándo y cómo se puede abandonar la operación; cláusula MAC).
8. **Misceláneos / boilerplate** (ley aplicable, arbitraje, notificaciones, cesión, integridad del
   acuerdo).
9. **Anexos**, incluidos los **disclosure schedules**.

Veamos las tres primeras piezas sustantivas (las demás, en 14.C):

**Representations & warranties (el corazón de la asignación de riesgo).** Son las **afirmaciones de hecho**
que el vendedor garantiza sobre la *target*, referidas a una fecha. Si resultan **falsas**, el comprador
tiene derecho a **indemnización** (o, si se descubre antes del cierre, a no cerrar). Su función económica
—ya lo vimos— es **corregir la asimetría de información**: el vendedor "pone por escrito" que la empresa es
como dice, y responde si no. Las reps típicas cubren:
- **Fundamentales:** título y propiedad de las acciones, capacidad y autoridad para vender, validez del
  contrato. (Reciben protección reforzada: sin tope, plazo largo.)
- **Del negocio:** estados financieros veraces, ausencia de pasivos no revelados, contratos materiales
  vigentes, **cumplimiento legal**, situación **fiscal**, **laboral**, **litigios**, propiedad
  **intelectual**, **permisos**, inmuebles, seguros, ausencia de cambios desde cierta fecha.

La **negociación de las reps** es un arte fino. Tres "perillas" clave:
- ***Knowledge qualifier* ("a leal saber y entender"):** el vendedor solo garantiza lo que **sabe** (no lo
  desconocido). El comprador prefiere reps **sin** este calificador (responsabilidad objetiva); el
  vendedor, **con** él. ¿Y "conocimiento" de quién, y con qué deber de investigar? Se define con cuidado.
- ***Materiality qualifier* ("en todos los aspectos **materiales**"):** acota la rep a lo relevante,
  evitando reclamaciones por nimiedades. El comprador teme que vacíe la rep; se negocia el umbral.
- **Alcance temporal y de excepciones:** "salvo lo revelado en el *disclosure schedule*" (sección 14.C).

**Covenants (las obligaciones de conducta).** Regulan **qué deben (y no deben) hacer** las partes,
sobre todo **entre el *signing* y el *closing*** (el periodo *interim*), cuando el vendedor todavía
controla la empresa pero ya la "vendió". Los más importantes:
- ***Conduct of business* (operación en el curso ordinario):** el vendedor se obliga a **seguir operando
  normalmente** y a **no** hacer cosas que cambien la empresa (no repartir dividendos extraordinarios, no
  endeudarse, no vender activos clave, no subir sueldos, no contratar/despedir masivamente). Protege al
  comprador de recibir una empresa "vaciada" o alterada entre la firma y el cierre.
- ***Access* (acceso):** el comprador puede seguir revisando información (due diligence confirmatoria).
- ***Reasonable/best efforts* (esfuerzos para cerrar):** ambas partes se obligan a gestionar las
  autorizaciones (COFECE) y consentimientos necesarios.
- **Post-cierre:** **no competencia** y **no captación** (*non-compete*, *non-solicit*) del vendedor
  —razonables en tiempo, territorio y objeto para ser válidas (orden público de competencia)—,
  cooperación fiscal, confidencialidad.

**Conditions precedent (las condiciones para cerrar).** Son los **requisitos que deben cumplirse** para que
nazca la obligación de cerrar. Si no se cumplen, la parte beneficiada **no está obligada** a cerrar (y
puede terminar). Las típicas:
- **Autorizaciones regulatorias** (COFECE, sectoriales) y **consentimientos** de terceros (los *change of
  control* detectados en la due diligence —Libro 2—).
- ***Bring-down* de las reps:** que las reps **sigan siendo ciertas** a la fecha de cierre (no solo a la
  firma).
- **Cumplimiento de covenants** hasta el cierre.
- **Ausencia de MAC** (que no haya ocurrido un cambio adverso relevante —sección 14.C—).
- **Entregables del cierre:** los documentos, renuncias de consejeros, libros, etc.

**Idea integradora:** observa cómo el SPA es un **sistema temporal**. Las **reps** miran al **pasado y
presente** (cómo es la empresa). Los **covenants** miran al **periodo intermedio** (qué se hace entre firma
y cierre). Las **condiciones** son la **puerta del cierre**. Y la **indemnización** (14.C) mira al
**futuro** (qué pasa si algo de lo garantizado resulta falso). Cuatro piezas, cuatro momentos: pasado,
intermedio, cierre, futuro. Entender esa **línea de tiempo** es entender el SPA.

### 14.C · Anatomía del SPA, parte II (indemnización, MAC, disclosure schedules, sandbagging)

Aquí están las cláusulas donde se libra la **batalla más dura** de la negociación, porque definen **cuánto
y cómo paga el vendedor** si algo sale mal. Domínalas: son las que más distinguen al abogado experto.

**La indemnización (*indemnification*): el mecanismo de cobro.** Si una rep resulta falsa o se materializa
un riesgo cubierto, el vendedor debe **resarcir** al comprador por las **pérdidas** ("Losses", término
cuya definición se negocia: ¿incluye daño indirecto, lucro cesante, multiplicadores?). Pero esa obligación
viene **modulada** por una serie de límites que son, en el fondo, un **reparto económico del riesgo
residual**:
- **Cap (tope):** el monto **máximo** que el vendedor pagará. Suele expresarse como un **% del precio**
  (las reps del negocio a menudo se topan en un porcentaje; las **fundamentales**, hasta el 100% del
  precio o sin tope). Cuanto más alto el cap, más riesgo retiene el vendedor → es **negociación de precio
  encubierta**.
- **Basket (cesta) / deducible:** un **umbral mínimo** de pérdidas **acumuladas** que deben superarse antes
  de poder reclamar. Dos modalidades: ***tipping basket*** (superado el umbral, se cobra **todo** desde el
  primer peso) y ***true deductible*** (solo se cobra **el exceso** sobre el umbral, como el deducible de
  un seguro). Evita litigios por minucias.
- **De minimis:** un monto **mínimo por reclamación individual** para que cuente hacia el basket (filtra
  reclamaciones triviales).
- **Survival (supervivencia):** el **plazo** durante el cual cada rep sigue "viva" y reclamable tras el
  cierre (típicamente 12-24 meses para las del negocio; **más largo o indefinido** para las fundamentales,
  fiscales y ambientales, que suelen seguir su propia prescripción legal).
- **Special / specific indemnity (indemnización especial):** para un riesgo **concreto y conocido** de la
  due diligence (Libro 2), se pacta una indemnización **específica**, normalmente **fuera de caps y
  baskets** y **al 100%** —porque no es un riesgo "desconocido" que la rep general deba cubrir, sino uno
  **identificado** que el vendedor debe asumir nominalmente—.
- **Recuperación y *mitigation*:** reglas sobre cómo se calcula la pérdida (descontando seguros, beneficios
  fiscales) y el deber del comprador de **mitigar** el daño.
- **Garantía del cobro:** **escrow/holdback** (retención de parte del precio) o, cada vez más, **seguro de
  W&I** (la aseguradora cubre el incumplimiento de las reps).

> **El "paquete de indemnización" es, en realidad, una negociación de cuánto riesgo retiene cada parte.**
> Comprador quiere: caps altos, baskets bajos, supervivencia larga, reps sin *knowledge qualifier*,
> *pro-sandbagging*, escrow grande. Vendedor quiere lo contrario y un "corte limpio". El punto de
> equilibrio refleja el **poder de negociación** y el **precio**.

**La cláusula MAC / MAE (*Material Adverse Change/Effect*): la válvula de escape.** Permite al comprador
**no cerrar** (o renegociar) si, entre la firma y el cierre, ocurre un **cambio sustancialmente adverso** en
la *target*. Es de las cláusulas **más negociadas y litigadas**, porque define **quién soporta el riesgo de
que el mundo cambie** entre firma y cierre. Claves de su redacción:
- **Definición de "material" y "adverso":** ¿qué tan grave y duradero debe ser el cambio? Los tribunales
  (Delaware, *Akorn v. Fresenius* —Libro 2—) exigen un umbral **muy alto**: un golpe **sustancial y
  duradero** al poder de generar ganancias de la empresa, no un mal trimestre.
- **Las *carve-outs* (exclusiones):** el vendedor pelea por **excluir** de la MAC los riesgos
  **sistémicos** (crisis económicas, pandemias, guerras, cambios de ley, condiciones de la industria)
  —porque no son culpa de la empresa—; el comprador acepta excluirlos **salvo** que afecten a la *target*
  **desproporcionadamente** respecto de su industria. La redacción de estas exclusiones es donde se gana o
  se pierde la cláusula.
- **Función:** rara vez se invoca con éxito (el umbral es altísimo), pero su valor está en la **amenaza**:
  da al comprador poder para **renegociar** si las cosas empeoran de verdad antes del cierre.

**Los *disclosure schedules* (anexos de revelación): la otra cara de las reps.** Son los anexos donde el
vendedor **revela las excepciones** a sus reps. Si la rep dice "no hay litigios", el *disclosure schedule*
lista los litigios que **sí** existen; con eso, la rep se entiende **cierta salvo por lo revelado**.
Función doble:
- **Para el vendedor, son su escudo:** lo que **revela** aquí deja de ser un incumplimiento de la rep
  (ya lo dijo). Por eso el vendedor tiene incentivo a **revelar mucho** (vacunarse). Conecta directamente
  con la due diligence: lo que el comprador descubrió y el vendedor reveló, queda "fuera" de la garantía.
- **Para el comprador, son información y delimitación:** le dicen exactamente **qué excepciones** está
  aceptando. El comprador debe **leerlos con lupa**: una revelación amplia o ambigua puede vaciar una rep.
  Se negocian reglas sobre si una revelación en una sección "cuenta" para las demás (*general disclosure*).

**El *sandbagging* (¿puede reclamar el que ya sabía?).** Pregunta fina y muy práctica: si el comprador,
**por la due diligence, sabía** que una rep era falsa, y **aun así cierra**, ¿puede luego **reclamar** la
indemnización?
- ***Pro-sandbagging* (a favor del comprador):** sí puede reclamar, **aunque supiera**; lo que importa es
  lo que dice el contrato, no lo que el comprador conocía. El comprador prefiere esta cláusula.
- ***Anti-sandbagging* (a favor del vendedor):** no puede reclamar por algo que **conocía** al cerrar
  (sería de mala fe cobrar por un riesgo que aceptaste con conocimiento). El vendedor prefiere esta.
- **Se pacta expresamente** en el SPA; si el contrato calla, la respuesta depende del derecho aplicable
  (en algunos sistemas se presume una, en otros la otra). En México, el silencio lleva a discutir buena fe
  y dolo —por eso conviene **pactarlo claramente**—. Este es el punto exacto donde la **due diligence
  (Libro 2) y el contrato se cruzan**: lo que descubriste investigando puede ayudarte o perjudicarte según
  esta cláusula.

**Cómo encaja todo (del hallazgo de la DD a la cláusula).** Cierra el círculo de los Libros 2 y 3: un
**riesgo desconocido** se cubre con **reps generales + indemnización (con caps/baskets)**; un **riesgo
concreto y conocido**, con **indemnización especial** (sin tope, fuera de cesta); un **riesgo subsanable
antes de cerrar**, con **condición al cierre**; el **riesgo de que el mundo cambie** entre firma y cierre,
con la **MAC**; y lo que el vendedor **revela**, sale de la garantía vía **disclosure schedules**. El SPA
es, literalmente, la **due diligence convertida en cláusulas**.

### 14.D · Mecanismos de precio y el APA (cómo se fija el precio y el contrato del asset deal)

**Los mecanismos de precio (cómo se determina y ajusta lo que se paga).** El "precio" de una empresa rara
vez es un número fijo y simple, porque la empresa **cambia** entre el momento en que se acuerda el precio y
el cierre (gana o pierde caja, sube o baja su deuda, varía su capital de trabajo). El SPA debe definir
**cómo se fija y ajusta** el precio. Las dos grandes filosofías:

- **Completion accounts (cuentas al cierre):** se acuerda un **precio base** (sobre un *enterprise value*)
  y se **ajusta** tras el cierre según el balance **real al día del cierre**, típicamente por tres
  variables: **deuda neta** (más deuda → menos precio), **caja** (más caja → más precio) y **capital de
  trabajo** (respecto de un nivel "normal" objetivo). Ventaja: el precio refleja la empresa **exactamente
  al cierre**. Desventaja: exige un **balance de cierre auditado** y suele generar **disputas** sobre las
  cifras (que se resuelven con un experto independiente).
- **Locked box (caja cerrada):** se fija un **precio fijo** sobre un balance de referencia **pasado** (el
  "*box*") y **no hay ajuste posterior**; desde la fecha del *box*, los riesgos y beneficios económicos
  pasan al **comprador** (con protección contra "fugas de valor" —*leakage*—, como dividendos o pagos a
  los vendedores entre el *box* y el cierre). Ventaja: **certeza** y simplicidad, sin disputas
  post-cierre. Desventaja: exige confianza en un balance pasado y una due diligence financiera sólida.
  Muy popular en Europa y en deals de *private equity*.

A esto se suman dos mecanismos que **difieren o condicionan** parte del precio:
- **Earn-out:** una porción del precio se paga **en el futuro** solo si la *target* **alcanza ciertos
  resultados** (ventas, EBITDA, hitos). Sirve para **cerrar la brecha de valuación** (el vendedor cree que
  vale más; el comprador, menos: "demuéstramelo y te pago más"). Es **fuente frecuente de litigios**
  (cómo se mide el resultado, qué pasa si el comprador gestiona la empresa de forma que reduzca el
  *earn-out*), por lo que su redacción debe ser **quirúrgica**.
- **Escrow / holdback:** retención de parte del precio en garantía de indemnizaciones (visto en 14.C);
  también puede retenerse para garantizar el **ajuste** de *completion accounts*.

**El APA (*Asset Purchase Agreement*): el contrato del asset deal.** Cuando la estructura elegida (Libro 3)
es la compra de **activos** y no de acciones, el documento es el **APA**. Comparte mucho con el SPA (tiene
reps, covenants, condiciones, indemnización, MAC), pero su **diferencia esencial** está en cómo describe lo
que se transmite:

- **El perímetro: activos incluidos y excluidos.** El corazón del APA es la **descripción precisa** de los
  ***purchased assets*** (qué se compra: inmuebles, maquinaria, inventario, contratos, PI, cuentas por
  cobrar, permisos) y de los ***excluded assets*** (qué se queda el vendedor). Cualquier ambigüedad genera
  conflicto: en un APA, **lo que no está claramente incluido, se queda fuera**.
- **Pasivos asumidos y excluidos (*assumed / excluded liabilities*).** El APA define **qué pasivos** asume
  el comprador (a veces ninguno; a veces los del negocio en marcha) y cuáles **no** (los "del pasado", que
  quedan con el vendedor). Aquí está la **gran ventaja** del asset deal (aislar pasivos —Libro 3—) **y** su
  límite: recuerda que ciertos pasivos (**laborales, fiscales, ambientales**) pueden **seguir al negocio**
  por mandato legal, pese a lo pactado.
- **Las cesiones y consentimientos (la complejidad del asset deal).** Como no se transmite una sociedad
  sino activos uno por uno (**sucesión particular** —Libro 3—), el APA debe articular la **cesión** de cada
  contrato (con el **consentimiento** de la contraparte cuando se requiera), la transmisión de inmuebles
  (ante notario, con inscripción), la cesión de créditos (con notificación al deudor) y la transferencia de
  PI (ante el IMPI). Esto vuelve el cierre del asset deal **más complejo y condicionado** que el de un
  share deal: muchos consentimientos se convierten en **condiciones al cierre**.
- **Cuestiones laborales (sustitución patronal).** El APA debe resolver la suerte de los **trabajadores**
  (¿se transfieren por sustitución patronal?, ¿se recontratan?, ¿quién asume los pasivos laborales
  acumulados?), un punto sensible y muchas veces decisivo.

**SPA vs. APA (cuadro mental):**

| | SPA (acciones) | APA (activos) |
|---|---|---|
| Qué se transmite | Acciones (la sociedad entera) | Activos y pasivos **descritos** |
| Pasivos | Todos (de la sociedad) | Solo los **asumidos** (+ excepciones legales) |
| Transmisión | Una operación | Cesión **individual** + consentimientos |
| Reps clave | Título de acciones, todo el negocio | Título de **cada activo**, perímetro |
| Cierre | Más simple | Más complejo (consentimientos como CP) |
| Estructura del Libro 3 | Share deal | Asset deal |

**La conexión que cierra el sistema:** el documento **sigue a la estructura**, y la estructura **sigue a la
due diligence**. Si la DD reveló pasivos ocultos graves → estructura *asset deal* (Libro 3) → documento
**APA** con perímetro y pasivos cuidadosamente delimitados. Si la prioridad era continuidad → *share deal*
→ **SPA** con reps fuertes y consentimientos por *change of control* como condiciones. **Investigar →
estructurar → documentar**: la cadena completa del M&A, ahora visible de principio a fin.

### 14.E · El SHA (convenio entre accionistas): gobierno, capital y salidas

El **SPA/APA** consuma la **compra**; el **SHA** (*Shareholders Agreement* / convenio entre accionistas)
gobierna la **convivencia posterior** entre los socios. Es el contrato clave cuando, tras la operación,
**varios socios** quedan juntos: fundadores e inversionistas (VC/PE), familia y fondo, socio estratégico y
control. Para un fondo, el SHA es **tan importante como el precio**, porque define su **poder**, su
**protección económica** y su **salida**. Es también el instrumento del **gobierno corporativo
contractual** —tu área de interés—. Sus cláusulas se agrupan en tres familias:

**1) Gobierno (¿quién decide?).**
- **Composición del consejo:** cuántos asientos tiene cada socio (el inversionista suele negociar uno o
  más, y a veces un **observador**). Define el equilibrio de poder en la administración.
- **Reserved matters / vetos (materias reservadas):** la lista de **decisiones importantes** que requieren
  el **consentimiento** del inversionista/minoría, aunque no controle el consejo: endeudarse por encima de
  X, emitir acciones, vender activos clave, cambiar el giro, aprobar el presupuesto, contratar/remover al
  CEO, hacer otra adquisición, repartir dividendos. Es la **principal protección de poder** del minoritario:
  no gobierna el día a día, pero **bloquea** lo que le importa.
- **Información:** derecho a recibir estados financieros, reportes e información de gestión (*information
  rights*).
- **Resolución de bloqueos (*deadlock*):** qué pasa cuando los socios **no se ponen de acuerdo** en una
  decisión clave y se **paraliza** la empresa. Mecanismos: escalamiento a los directivos/accionistas
  principales, mediación, y —si no hay solución— mecanismos de **compra-venta forzosa**: ***buy-sell* /
  "ruleta rusa"** (un socio pone un precio; el otro elige si **compra** o **vende** a ese precio),
  ***Texas shoot-out*** (ofertas selladas al alza), o la **disolución**. Son cláusulas delicadas: mal
  diseñadas, favorecen a quien tiene más dinero para comprar.

**2) Capital y economía (¿quién pone y quién cobra cuánto?).**
- **Preferencia de liquidación (*liquidation preference*):** derecho del inversionista a **cobrar primero**
  en una venta o liquidación, normalmente un **múltiplo** de su inversión (1x, a veces más), antes de que
  los fundadores reciban nada. Puede ser ***non-participating*** (cobra su preferencia **o** convierte a
  ordinario, lo que más le convenga) o ***participating*** (cobra su preferencia **y además** participa
  como ordinario —más agresiva—). Es la protección económica **central** del VC/PE.
- **Antidilución:** protege al inversionista si la empresa emite acciones nuevas a un **precio menor** que
  el que él pagó (*down round*). Modalidades: ***full ratchet*** (muy agresiva: ajusta su precio al nuevo,
  más bajo) y ***weighted average*** (promedio ponderado, la estándar y más equilibrada).
- **Derechos de preferencia (*preemptive rights / pro rata*):** derecho a **suscribir** acciones en
  emisiones futuras para **mantener su porcentaje** (no diluirse).
- **Compromisos de aportación / *pay-to-play*:** reglas sobre futuras rondas y consecuencias de no
  participar.

**3) Transmisión y salida (¿cómo entro y, sobre todo, cómo salgo?).** Esta es la familia **más
característica** del SHA, porque diseña las **salidas** —lo que más importa a un inversionista—:
- **Lock-up:** prohibición temporal de **vender** acciones (típico para fundadores: que no se vayan
  pronto).
- **ROFR / ROFO (derecho del tanto / de primera oferta):** antes de vender a un tercero, el socio debe
  **ofrecer** primero a los demás (ROFR: igualar la oferta de un tercero; ROFO: ofrecer antes de buscar
  tercero). Evita la entrada de extraños no deseados.
- **Tag along (derecho de acompañamiento):** si el socio mayoritario vende, el **minoritario puede
  sumarse** y vender su parte **en las mismas condiciones**. Es **protección del minoritario**: que no lo
  dejen "atrapado" con un nuevo socio de control que no eligió.
- **Drag along (derecho de arrastre):** si una mayoría (o el inversionista) decide vender el 100%, puede
  **obligar** a los demás socios a **vender también** en las mismas condiciones. Es **clave para el
  inversionista/PE**: garantiza que podrá vender la empresa **entera** (que es lo que un comprador quiere)
  sin que un minoritario lo bloquee. La tensión **drag (mayoría) vs. tag (minoría)** es el corazón de la
  negociación de salidas.
- **Put / Call options:** **put** (el socio puede **obligar** a que le **compren** su parte, p. ej., el
  inversionista si no hay salida en X años) y **call** (puede **obligar** a que le **vendan**, p. ej., la
  empresa recompra al fundador que se va). Definen salidas "forzadas" bajo ciertos disparadores.
- **Cláusulas de salida del inversionista:** compromisos de buscar un **exit** (venta o IPO) en cierto
  horizonte, derechos de **registro** (para vender en bolsa), y *redemption* (rescate).
- **Bad leaver / good leaver:** para fundadores/ejecutivos accionistas: el que se va "mal" (incumpliendo,
  por causa) pierde o vende barato sus acciones no consolidadas; el que se va "bien" conserva más. Alinea
  el incentivo de permanencia.

**Cómo se relaciona el SHA con los estatutos.** El SHA es un **contrato entre los socios** (eficacia
**inter partes**); los **estatutos** son la "constitución" de la sociedad (eficacia **frente a todos**).
Lo ideal es que las cláusulas del SHA que se pueda **se reflejen en los estatutos** (para oponerlas a
terceros y a la sociedad), pero algunas, por su naturaleza, viven solo en el SHA. En México, la
**S.A.P.I.** (regulada por la LMV) fue diseñada precisamente para **dar validez societaria** a muchas de
estas cláusulas (restricciones a la transmisión, vetos, drag/tag, opciones), por lo que es el **vehículo
preferido** para operaciones con inversionistas (VC/PE) —conexión directa con el Libro 7 (PE y VC) y con
Gobierno Corporativo—.

**Idea integradora del SHA.** Mientras el SPA mira al **momento de la compra** (asignar el riesgo del
pasado), el SHA mira a la **vida futura** de la sociedad: cómo se **decide** (gobierno), cómo se **reparte
el dinero** (capital) y cómo se **entra y sale** (transmisión). Diseñar un buen SHA es **anticipar el
conflicto** entre socios y resolverlo por escrito **antes** de que ocurra —el verdadero "acuerdo
prenupcial" empresarial—. Para el abogado que quiere especializarse en **gobierno corporativo y operaciones
complejas**, dominar el SHA es dominar el **instrumento donde se diseña el poder corporativo**.

## 15. Explicación intuitiva

Tres imágenes para fijar la documentación del M&A.

**La metáfora del seguro de auto.** Las **reps & warranties** son como las **declaraciones** que haces al
contratar un seguro ("el coche no ha chocado, lo maneja solo mi hijo de 30, no es de uso comercial"). Si
**mientes** en una declaración y luego chocas, la aseguradora **no paga** (incumpliste una rep → hay
consecuencia). La **indemnización** es el mecanismo de pago, y el **deducible** del seguro es exactamente el
***basket*** (no reclamas por debajo de cierto monto), mientras que la **suma asegurada máxima** es el
***cap***. La **MAC** es como una cláusula que dice "si el coche se destruye totalmente **antes** de que
empiece la póliza, no hay contrato". Toda la lógica del SPA es **lógica de seguro**: declaras, te cubren
dentro de límites, y hay supuestos de escape.

**La metáfora del acuerdo prenupcial (para el SHA).** El SHA es el **acuerdo prenupcial** de los socios:
se firma cuando todos están felices y optimistas, precisamente para decidir **en frío** lo que harán
cuando vengan los problemas. ¿Quién decide las cosas importantes (vetos)? ¿Quién cobra primero si nos
separamos (preferencia de liquidación)? ¿Puedo obligarte a vender conmigo (drag)? ¿Puedo subirme a tu
venta (tag)? ¿Cómo nos divorciamos si no nos ponemos de acuerdo (deadlock)? Nadie firma un prenupcial
pensando en el divorcio, pero **el que no lo firma se arruina cuando llega**.

**La metáfora de la línea de tiempo (para el SPA).** Imagina el SPA como una **película con cuatro actos**:
- **Acto 1 (pasado/presente):** "Te juro que la empresa es así" → **reps**.
- **Acto 2 (entre firma y cierre):** "Y me porto bien hasta que cerremos" → **covenants**.
- **Acto 3 (la puerta del cierre):** "Cerramos solo si se cumplen estas condiciones" → **conditions**.
- **Acto 4 (futuro):** "Y si mentiste, me pagas (dentro de estos límites)" → **indemnización**.
Si entiendes esa secuencia —pasado, intermedio, cierre, futuro—, **nunca te perderás** en un SPA, por
largo que sea.

**La intuición central:** la documentación del M&A **no describe una compraventa; construye un sistema de
asignación de riesgo a lo largo del tiempo**. Cada cláusula responde a una pregunta —¿qué me aseguras?,
¿qué pasa entre firma y cierre?, ¿qué condiciones?, ¿qué pasa si sale mal?, ¿cómo decidimos y salimos?— y
la respuesta **reparte un riesgo** entre las partes. Leer un contrato es, en el fondo, **mapear quién
soporta cada riesgo**. Esa es la habilidad.

## 16. Ejemplos simples

**Ejemplo 1 — La rep que se activa.** El SPA dice: "no existen litigios laborales salvo los del
*disclosure schedule* 3.12". Tras el cierre, aparece un juicio laboral **no listado**, de 2 millones. La
rep era **falsa** → se activa la **indemnización**. Pero si las pérdidas del comprador (2M) no superan el
***basket*** de 3M, **no puede reclamar** todavía; si con otras reclamaciones se supera, cobra (según sea
*tipping* o *deducible*).

**Ejemplo 2 — La condición que salva al comprador.** El SPA pone como **condición al cierre** obtener la
autorización de la COFECE. La COFECE **no autoriza**. El comprador **no está obligado a cerrar** y puede
**terminar** sin penalización: la condición no se cumplió.

**Ejemplo 3 — El tag along en acción.** Un fondo (mayoritario) vende su 60% a un tercero. El fundador
(minoritario, 40%) ejerce su **tag along** y **se suma** a la venta en las mismas condiciones: vende su 40%
al mismo precio por acción, en vez de quedarse atrapado con un nuevo socio de control desconocido.

**Ejemplo 4 — El earn-out que cierra la brecha.** El vendedor pide 100; el comprador ofrece 80 porque duda
de las proyecciones. Acuerdan **80 fijos + 20 de *earn-out*** pagaderos si la empresa alcanza cierto EBITDA
en dos años. Si lo logra, el vendedor cobra los 20; si no, no. Cada quien arriesga su parte de la
discrepancia.

## 17. Ejemplos complejos

**Ejemplo complejo 1 — La guerra de la cláusula MAC.** Se firma un SPA en enero; el cierre es en junio
(pendiente la COFECE). En marzo, una crisis golpea a la *target*: sus ventas caen 40%. El comprador quiere
**salir** invocando la **MAC**. ¿Puede? Depende de la **redacción**: si la crisis es **sistémica** (afecta
a toda la industria) y la MAC **excluye** los eventos sistémicos, el comprador **no** puede salir (asumió
ese riesgo) —**salvo** que la *target* esté afectada **desproporcionadamente** frente a sus competidores—.
Aquí se ve por qué cada palabra de las *carve-outs* de la MAC vale millones: la misma caída puede ser o no
ser una MAC según cómo se redactó la exclusión. (Eco de *Akorn v. Fresenius*, Libro 2.)

**Ejemplo complejo 2 — Sandbagging y disclosure.** Durante la due diligence, el comprador **descubre** un
problema de cumplimiento ambiental, pero el vendedor **no** lo incluye en el *disclosure schedule* y la rep
dice "cumplimos con la normativa ambiental". Tras el cierre, el comprador **reclama** por incumplimiento de
la rep. El vendedor responde: "¡pero tú **lo sabías** por la due diligence!". ¿Quién gana? **Depende de la
cláusula de *sandbagging*:** si es *pro-sandbagging*, el comprador **cobra** (lo que importa es la rep
escrita); si es *anti-sandbagging*, **no** (sabía y aun así cerró). Lección: el comprador que detecta algo
en la DD debe **insistir en que se revele y se cubra con indemnización especial**, o asegurarse de tener
cláusula *pro-sandbagging* —no confiar en reclamar después—.

**Ejemplo complejo 3 — El deadlock que paraliza una JV.** Dos socios al 50/50 en una *joint venture* no se
ponen de acuerdo sobre una inversión clave; el consejo se **empata** y la empresa se **paraliza**. El SHA
preveía una **cláusula de ruleta rusa**: el socio A ofrece comprar la parte de B (o venderle la suya) a un
precio; B elige si **compra o vende** a ese precio. A, que tiene más caja, pone un precio bajo sabiendo que
B no podrá comprar y tendrá que vender barato. *Lección:* las cláusulas de *deadlock* **mal diseñadas
favorecen a quien tiene más dinero**; un buen abogado las calibra (p. ej., con valuación independiente)
para que sean justas. El diseño del SHA **anticipa y resuelve** estos conflictos —o los agrava—.

## 18. Casos reales (operaciones estilizadas y referentes)

> *Nota de método (Manifiesto XI.5): casos estilizados con fines didácticos; verifica los detalles antes
> de citarlos profesionalmente.*

**Las batallas por la cláusula MAC (Tyson Foods, Genesco, Akorn).** Una serie de casos en Delaware definió
el **altísimo umbral** para invocar una MAC y abandonar un deal. Durante años, **ningún** comprador logró
salir por MAC (los tribunales exigían un golpe sustancial y **duradero**), hasta *Akorn v. Fresenius*
(2018), el **primer** caso en que una corte validó la salida —por fraude regulatorio grave de la
*target*—. *Lección:* la MAC es más **amenaza negociadora** que botón de escape fácil; su valor está en el
poder de **renegociar**, no en una salida sencilla.

**La pandemia y las cláusulas MAC (2020).** La crisis sanitaria global disparó disputas sobre si era una
MAC que permitía abandonar deals firmados antes. La respuesta dependió, caso por caso, de las
***carve-outs*** (¿excluía la MAC las "pandemias" o los "eventos sistémicos"?) y del impacto
**desproporcionado** en la *target*. *Lección:* la redacción de las exclusiones de la MAC —que parecía
*boilerplate*— resultó valer cientos de millones. Nada en un SPA es "relleno".

**Los *earn-outs* litigados.** Innumerables disputas post-cierre nacen de *earn-outs*: el vendedor acusa
al comprador de gestionar la empresa para **no** alcanzar la meta (y no pagar); el comprador dice que la
meta simplemente no se cumplió. *Lección:* el *earn-out* cierra la brecha de valuación pero **abre** la
puerta al litigio; debe redactarse con métricas objetivas, *covenants* de gestión y mecanismos de
resolución claros.

## 19. Casos empresariales

**El fondo de PE que negocia el SHA tanto como el precio.** Un fondo invierte en una empresa familiar
tomando el 40%. En el SPA negocia precio y reps; pero invierte **igual energía** en el **SHA**: asegura
**dos asientos** en el consejo, una lista amplia de **vetos** (endeudamiento, adquisiciones, cambio de
CEO), una **preferencia de liquidación 1x**, **antidilución** *weighted average*, y —lo más importante—
un **drag along** que le permitirá **vender la empresa entera** en 5-7 años (su *exit*). *Lección:* para el
inversionista profesional, **cómo gobierna y cómo sale** vale tanto como **cuánto paga**. El abogado que
solo negocia el precio le falla a su cliente.

**La empresa familiar que se blinda con un SHA (protocolo familiar).** Tres hermanos heredan la empresa.
Para evitar que el conflicto la destruya, firman un **SHA/protocolo familiar**: reglas de **gobierno**
(consejo con un independiente, mayorías para decisiones clave), de **transmisión** (ROFR para que las
acciones no salgan de la familia; reglas para herederos), y de **resolución de conflictos** (mediación
antes que litigio; mecanismo de salida para el hermano que quiera irse). *Lección:* el SHA es la
herramienta para que la empresa familiar **sobreviva a la siguiente generación** —conecta con tu interés
en gobierno corporativo y empresa familiar—.

## 20. Casos corporativos (la conexión integral)

Integremos todo el programa y todo el Nivel IV. *Fondo Andes* invierte en *TechMX, S.A.P.I.*, una empresa
tecnológica con tres fundadores, comprando una participación y suscribiendo acciones nuevas.

- **Nivel I-II (Contratos, Obligaciones):** el SPA y el SHA son **contratos** regidos por la teoría general
  (consentimiento, objeto, condiciones, obligaciones de hacer/no hacer).
- **Nivel III (Sociedades, Gobierno Corporativo, LMV):** la **S.A.P.I.** da validez societaria a las
  cláusulas del SHA (vetos, drag/tag, preferencias); el gobierno corporativo del consejo se diseña en el
  SHA.
- **Libro 1 (Fundamentos M&A):** la operación se mapea (signing/closing, asignación de riesgo).
- **Libro 2 (Due Diligence):** la DD de TechMX revela que la **PI clave** está a nombre de un fundador y
  hay un litigio menor → se traduce en cláusulas.
- **Libro 3 (Estructuras):** se decide la estructura (inversión primaria —suscripción— + secundaria —compra
  de acciones de un fundador saliente—).
- **Libro 4 (este):** se documenta todo: **Term Sheet** (con la valuación y los términos clave del SHA),
  **SPA/Subscription Agreement** (con rep específica e **indemnización especial** por la PI del fundador,
  y **condición al cierre** de transferir esa PI a la sociedad), y **SHA** (vetos, preferencia de
  liquidación, antidilución, drag/tag, vesting de los fundadores con *good/bad leaver*).

*Moraleja:* la documentación es el **punto de convergencia final** de toda la operación y de toda tu
formación. El abogado que la domina **traduce** la investigación (DD), la arquitectura (estructura) y la
estrategia del cliente en **texto exigible**. No hay habilidad más definitoria del abogado de M&A.

## 21. Casos internacionales

**El SPA como lengua franca global.** Un SPA negociado en México para una operación transfronteriza se
parece muchísimo a uno de Nueva York o Londres: misma estructura (reps, covenants, conditions,
indemnification, MAC), mismo vocabulario (en inglés). *Lección para tu carrera:* el **inglés jurídico de
transacciones** no es opcional en el M&A de élite; el contrato "habla inglés" aunque la ley aplicable sea
mexicana. Dominar la **terminología y la lógica** de estas cláusulas en inglés es parte del oficio.

**Las diferencias civil law / common law en la interpretación.** Aunque la **forma** del SPA es global, su
**interpretación y ejecución** dependen de la **ley aplicable**. En el common law prima el **texto literal**
del contrato (lo escrito es lo que vale; de ahí contratos larguísimos que lo definen todo). En el civil
law (México) pesan más la **buena fe**, la **intención de las partes** y las normas **imperativas** y
supletorias del Código —lo que puede **modular** cláusulas importadas (p. ej., la eficacia del
*sandbagging* o de ciertas renuncias)—. *Lección:* el abogado mexicano de élite redacta cláusulas
anglosajonas **ancladas** en figuras locales (penas convencionales, condiciones, renuncias válidas) para
que sean **exigibles** aquí.

**El seguro de Reps & Warranties (W&I insurance).** Práctica internacional ya común en México: una
**aseguradora** cubre el riesgo de que las reps sean falsas, permitiendo al vendedor un "corte limpio"
(sin escrow ni responsabilidad prolongada) y agilizando el deal. Reconfigura la negociación de la
indemnización (el comprador reclama a la **aseguradora**, no al vendedor). *Lección:* las aseguradoras
**exigen** una due diligence sólida para emitir la póliza —otra vez, la DD (Libro 2) es la base de todo—.

## 22. Derecho comparado

Los contratos del M&A son globales en su **forma**, pero su **interpretación y exigibilidad** varían según
la tradición jurídica. Tabla comparada esencial para el abogado de M&A:

| Jurisdicción / sistema | Tratamiento de la documentación del M&A |
|---|---|
| **México (Civil Law)** | SPA/APA/SHA por **autonomía de la voluntad** sobre la base de la compraventa y el saneamiento (CCF/CCom). La **S.A.P.I.** (LMV) da validez societaria al SHA (vetos, drag/tag, opciones). Interpretación por **buena fe** e intención; normas imperativas modulan cláusulas importadas (sandbagging, ciertas renuncias). |
| **EE.UU. (Common Law)** | Cuna del SPA moderno. Predomina la **literalidad** del texto y la **autonomía contractual**: el contrato lo define todo (de ahí su extensión). Régimen estatal; *case law* abundante sobre reps, indemnización y MAC. |
| **Delaware** | El estándar de referencia mundial. *Case law* decisivo sobre **MAC** (Akorn, Tyson), interpretación de reps e *indemnification*, y *sandbagging* (Delaware tiende a ser **pro-sandbagging** salvo pacto). La "lengua franca" del M&A. |
| **Reino Unido (Common Law)** | *Caveat emptor* fuerte; el comprador se protege con **warranties** y el vendedor con la **disclosure** (*disclosure letter*). Tiende a ser **anti-sandbagging** (no se reclama por lo conocido). Cláusulas algo más "ligeras" que las de EE.UU. |
| **España (Civil Law)** | *Manifestaciones y garantías* (las reps) sobre la base de la compraventa y el saneamiento por vicios ocultos del Código Civil; fuerte influencia anglosajona vía despachos internacionales. |
| **Unión Europea** | Sin contrato único, pero con impacto del derecho de **competencia** (cláusulas de no competencia razonables; gun jumping) y de **protección de datos** en la documentación. |
| **UNIDROIT (Principios)** | Marco supletorio para contratos internacionales: **buena fe**, deberes de información, **responsabilidad precontractual** (relevante para el Term Sheet/LOI) e interpretación. |
| **CISG** | Aunque regula mercaderías (no acciones), su lógica de **conformidad** y de **deberes de examen/notificación** ilumina la racionalidad de reps y saneamiento. |
| **Civil Law vs. Common Law (síntesis)** | **Common law:** literalidad, autonomía, contratos exhaustivos, tendencia pro-sandbagging (EE.UU.). **Civil law:** buena fe, intención, normas imperativas, saneamiento legal como red de seguridad. En M&A transfronterizo **conviven**: forma anglosajona, ejecución local. |

**Lección comparada clave:** el abogado mexicano de élite redacta cláusulas **anglosajonas** (porque son
el estándar global) pero las **ancla en el derecho mexicano** (penas convencionales, condiciones,
renuncias válidas, definición de pérdidas compatible con el CCF) para que sean **exigibles aquí**. Importar
una cláusula sin adaptarla es un error de novato que puede volverla **inejecutable**.

## 23. Derecho mexicano

La documentación del M&A se asienta en estos pilares del derecho mexicano:

- **Autonomía de la voluntad y *pacta sunt servanda* (CCF, CCom).** La base que permite diseñar libremente
  reps, indemnización, MAC, vetos, drag/tag —dentro de los límites de la ley, el orden público y las buenas
  costumbres—.
- **Compraventa y saneamiento (CCF / CCom).** El SPA y el APA son compraventas; el **saneamiento por vicios
  ocultos y por evicción** es la red de seguridad legal que las reps e indemnización **complementan y
  modulan**. Un comprador puede tener acción por saneamiento **además** de la contractual.
- **Vicios del consentimiento (CCF).** **Dolo** y **mala fe** del vendedor (mentir u ocultar) pueden generar
  **nulidad** y responsabilidad **más allá** de los límites contractuales (caps, baskets) —un argumento
  poderoso del comprador engañado—.
- **Transmisión de acciones (LGSM / LMV).** Endoso e inscripción en el libro de registro; régimen especial
  de la S.A.B.; la **S.A.P.I.** como vehículo que valida las cláusulas del SHA.
- **Cesión de derechos y asunción de deudas (CCF).** Base del APA (cesión de contratos y créditos;
  consentimiento del acreedor para asumir deudas).
- **Penas convencionales y condiciones (CCF).** Figuras locales en las que se **anclan** cláusulas como el
  *break-up fee*, ciertos *earn-outs* y mecanismos de indemnización para que sean exigibles.
- **Cláusulas de no competencia:** válidas si son **razonables** en tiempo, territorio y objeto (límite del
  derecho de competencia y de la libertad de trabajo/comercio).
- **Arbitraje (CCom / convenciones internacionales).** El M&A mexicano usa intensamente el **arbitraje**
  (confidencial, especializado, ejecutable internacionalmente) como foro de resolución de disputas; la
  cláusula arbitral es *boilerplate* crítico.

> **Nota de método:** verifica la compatibilidad y la redacción exigible de cada cláusula importada con el
> derecho mexicano vigente antes de usarla (Manifiesto XI.5). La forma anglosajona **no** garantiza
> eficacia local.

## 24. Jurisprudencia relevante

> *Nota de método: verifica vigencia y datos de identificación antes de citar.*

En México, los criterios relevantes giran en torno a las **figuras que sostienen** la documentación:
- **Saneamiento por vicios ocultos y por evicción:** alcance de la responsabilidad del vendedor por
  defectos no aparentes; relación con las garantías contractuales (reps).
- **Dolo, mala fe y vicios del consentimiento:** cuándo la ocultación de información vicia el contrato y
  permite reclamar más allá de lo pactado.
- **Interpretación de los contratos (intención de las partes, buena fe — CCF):** clave para interpretar
  reps, indemnización, MAC y disclosure schedules.
- **Penas convencionales:** su validez y la facultad de los jueces de moderarlas (relevante para break-up
  fees y mecanismos indemnizatorios).
- **Validez de convenios entre accionistas (S.A.P.I. / LMV):** reconocimiento de la eficacia de vetos,
  restricciones a la transmisión y drag/tag.
- **Arbitraje:** criterios sobre validez de la cláusula arbitral, arbitrabilidad y reconocimiento/
  ejecución de laudos.

En el ámbito **anglosajón** (de gran influencia práctica), el *case law* de **Delaware** sobre **MAC**
(Akorn, Tyson, Genesco), **sandbagging** e interpretación de reps/indemnización es **estudio obligado**,
porque modela cómo se redactan e interpretan estas cláusulas en todo el mundo.

## 25. Criterios de la Suprema Corte / reguladores

- **SCJN / tribunales:** criterios sobre **interpretación contractual**, **buena fe**, **dolo**,
  **saneamiento** y **penas convencionales**, que delimitan la eficacia y los límites de las cláusulas del
  SPA/APA/SHA en México.
- **COFECE:** criterios sobre **cláusulas de no competencia** (razonabilidad) y sobre el respeto al
  calendario regulatorio (gun jumping) que condicionan covenants y condiciones del SPA.
- **CNBV (emisoras):** régimen de revelación y de OPAs que afecta la documentación cuando la *target* es
  pública.
- **Tribunales arbitrales (CANACO, ICC):** aunque sus laudos son confidenciales, la práctica arbitral
  mexicana e internacional ha desarrollado criterios sobre interpretación de SPAs (reps, earn-outs, MAC)
  que nutren la redacción contractual.

## 26. Doctrina nacional

La doctrina mexicana sobre la documentación del M&A proviene de **dos vertientes**: la **civil/mercantil**
clásica (compraventa, saneamiento, vicios del consentimiento, interpretación de contratos, obligaciones),
que da el marco de fondo; y el **know-how transaccional** de los grandes despachos corporativos, que ha
adaptado las cláusulas anglosajonas (reps, indemnización, MAC, drag/tag) al derecho mexicano y vive más en
los *precedents*, los seminarios especializados y la formación interna que en tratados académicos. La
**S.A.P.I.** y la doctrina de la LMV aportaron el sustento societario del SHA.

## 27. Doctrina internacional

- **American Bar Association — *Model Stock Purchase Agreement with Commentary* y *Model Asset Purchase
  Agreement*.** **Lectura imprescindible**: el SPA y el APA cláusula por cláusula, con comentario sobre por
  qué existe y cómo se negocia cada una. El mejor material del mundo para dominar la documentación.
- **Doctrina de Delaware y tratados de M&A (EE.UU.).** Interpretación de reps, indemnización, MAC y
  sandbagging; el *case law* que modela la práctica.
- **Practical Law / PLC y *precedents* de los grandes despachos.** Los **estándares de mercado** de cada
  cláusula (qué cap, qué basket, qué supervivencia son "de mercado").
- **Doctrina de *deal-making* y negociación (Harvard — Subramanian, *Dealmaking*).** El contrato como
  resultado de una negociación estratégica.
- **Materiales sobre W&I insurance.** La práctica del seguro de reps & warranties y su efecto en la
  negociación de la indemnización.
- **UNIDROIT — Principios de los Contratos Comerciales Internacionales.** Buena fe, responsabilidad
  precontractual e interpretación en operaciones transfronterizas.

## 28. Opiniones críticas (postura del Consejo Editorial)

**Primero: entender la lógica, no memorizar el formulario.** Sostenemos que el peor error en la formación
del abogado de M&A es aprender los contratos como **plantillas**. Una cláusula copiada sin entender **por
qué existe, a quién protege y qué pasa si falla** es una bomba de tiempo. Este libro enseña la **gramática
del riesgo**, no un formulario.

**Segundo: la negociación de la indemnización ES negociación de precio.** Criticamos que se traten los
*caps*, *baskets* y la MAC como "cláusulas técnicas" separadas del precio. Son **reparto económico del
riesgo**: cada concesión en indemnización tiene un valor monetario. El abogado que las negocia sin hablar
con el cliente sobre el **precio** y el **riesgo** que está dispuesto a asumir, negocia a ciegas.

**Tercero: nada en un SPA es *boilerplate*.** La pandemia y los casos de MAC demostraron que las cláusulas
"de relleno" (exclusiones de la MAC, ley aplicable, definiciones) pueden valer cientos de millones.
Despreciamos la actitud de "esto es estándar, no lo leas". **Todo** se lee y se entiende.

**Cuarto: el SHA es subestimado y decisivo.** Advertimos que muchos abogados ponen toda la energía en el
SPA (la compra) y descuidan el SHA (la convivencia). Pero para el inversionista, el SHA —gobierno y
salida— vale tanto como el precio. Y para la empresa familiar, es lo que la **salva o la destruye** en la
siguiente generación.

**Quinto: adaptar, no copiar, las cláusulas anglosajonas.** Importar un SPA de Nueva York sin anclarlo en
el derecho mexicano produce cláusulas **inejecutables**. El abogado de élite domina **ambos** mundos.

## 29. Debate doctrinal

- **¿*Pro-sandbagging* o *anti-sandbagging*?** ¿Debe poder reclamar el comprador que **sabía** que la rep
  era falsa? *Postura del Consejo:* en el plano de la **autonomía**, lo que las partes pacten; pero
  recomendamos **pactarlo expresamente** (no dejarlo al silencio) y, en México, ser consciente de que la
  **buena fe** y el **dolo** del CCF pueden modular el resultado. El comprador debe preferir
  *pro-sandbagging* explícito; el vendedor, *anti*.
- **¿Locked box o completion accounts?** ¿Certeza (precio fijo) o exactitud (ajuste al cierre)? *Postura
  del Consejo:* depende del deal —*locked box* da certeza y evita disputas (ideal con DD financiera sólida
  y vendedor confiable); *completion accounts* da precisión (mejor cuando el capital de trabajo es volátil
  o hay desconfianza)—. No hay respuesta única.
- **¿Hasta dónde llega la MAC?** ¿Quién soporta el riesgo de que "el mundo cambie" entre firma y cierre?
  *Postura del Consejo:* el equilibrio razonable es que el **comprador** asuma los riesgos **sistémicos**
  (no son culpa de nadie) y el **vendedor** responda por lo **específico de la target** y por el impacto
  **desproporcionado**. La pelea está en las *carve-outs*, y ahí se gana o se pierde.
- **¿El seguro de W&I diluye el cuidado en la due diligence?** *Postura del Consejo:* no debería —la
  aseguradora **exige** DD rigurosa para emitir la póliza—; el seguro **complementa**, no sustituye, ni la
  due diligence ni el criterio.
- **Drag along vs. tag along: ¿de quién es la operación?** Tensión entre el poder de la **mayoría/
  inversionista** de vender todo (drag) y la protección de la **minoría** de no quedar atrapada (tag).
  *Postura del Consejo:* ambos son legítimos y deben **coexistir** con salvaguardas (precio mínimo, mismas
  condiciones, umbrales); el abogado de la minoría debe **pelear el tag** y acotar el drag (precio justo,
  no por debajo de la inversión).

## 30. Errores comunes

- **Tratar el Term Sheet como inofensivo.** Redactarlo sin la cláusula clara de "no vinculante" y quedar
  atrapado en un compromiso o en responsabilidad precontractual. *Corrección:* distingue expresamente lo
  vinculante (exclusividad, confidencialidad) de lo no vinculante (precio, estructura).
- **Copiar cláusulas sin entenderlas.** Usar un SPA "plantilla" sin saber por qué existe cada cláusula ni
  a quién protege. *Corrección:* domina la **lógica** de cada cláusula antes de redactarla.
- **Descuidar las definiciones.** Subestimar el glosario ("Pérdidas", "Conocimiento", "Deuda"): una
  definición floja vacía o dispara una cláusula. *Corrección:* negocia las definiciones con la misma
  seriedad que el clausulado.
- **Negociar la indemnización sin pensar en el precio.** Tratar caps/baskets/MAC como tecnicismos
  separados del valor. *Corrección:* recuerda que son **reparto económico del riesgo** = precio encubierto.
- **Redactar mal las *carve-outs* de la MAC.** Dejar ambiguo quién soporta los riesgos sistémicos.
  *Corrección:* redacta con precisión las exclusiones y la regla del impacto desproporcionado.
- **Confiar en reclamar después en vez de revelar/cubrir.** Detectar algo en la DD y no exigir
  indemnización especial ni cláusula pro-sandbagging. *Corrección:* traduce el hallazgo en cláusula
  **antes** de cerrar.
- **Descuidar el SHA.** Poner toda la energía en el SPA y dejar el SHA (gobierno, salida) como un anexo.
  *Corrección:* para el inversionista y la empresa familiar, el SHA es **decisivo**.
- **Importar cláusulas anglosajonas sin anclarlas en derecho mexicano.** Volverlas inejecutables.
  *Corrección:* ancla en penas convencionales, condiciones y renuncias válidas del CCF.
- ***Earn-out* mal redactado.** Métricas ambiguas y sin covenants de gestión → litigio asegurado.
  *Corrección:* métricas objetivas, reglas de gestión y mecanismo de resolución.

## 31. Mitos frecuentes

- **"El Term Sheet no obliga a nada."** **Falso.** Sus cláusulas de exclusividad, confidencialidad y
  gastos **sí** obligan, y un mal redactado puede generar responsabilidad precontractual.
- **"Las reps son relleno; lo que importa es el precio."** **Falso.** Las reps **son** parte del precio:
  asignan el riesgo del pasado y determinan cuánto puede reclamar el comprador.
- **"La cláusula MAC me deja salir si el negocio empeora."** **Falso (casi siempre).** El umbral es
  altísimo (sustancial y duradero) y las exclusiones suelen cubrir los riesgos sistémicos. Es más amenaza
  para renegociar que botón de escape.
- **"El asset deal me aísla de todos los pasivos, y el APA lo garantiza."** **Falso.** Los pasivos
  laborales, fiscales y ambientales pueden seguir al negocio pese al APA.
- **"Si lo descubrí en la due diligence, igual puedo reclamar después."** **Depende.** Solo con cláusula
  *pro-sandbagging*; con *anti-sandbagging*, no. Mejor revelar y cubrir con indemnización especial.
- **"El SHA es un trámite posterior."** **Falso.** Para el inversionista vale tanto como el precio
  (gobierno + salida); para la familia, decide la supervivencia del negocio.
- **"Un SPA de Nueva York funciona igual en México."** **Falso.** La forma es global; la **exigibilidad**
  es local. Hay que adaptarlo.

## 32. Preguntas difíciles

1. **¿Por qué lo que el vendedor revela en el *disclosure schedule* lo protege a él?** Porque la rep se
   entiende cierta "**salvo lo revelado**": al revelar una excepción, el vendedor **ya no incumple** la rep
   respecto de eso (el comprador lo aceptó con conocimiento). Por eso el vendedor tiene incentivo a revelar
   mucho (vacunarse) y el comprador a leer los schedules con lupa.
2. **¿Cómo se conecta la due diligence (Libro 2) con el SPA?** Directamente: riesgo **desconocido** → reps
   + indemnización (con caps/baskets); riesgo **concreto conocido** → indemnización **especial** (sin tope);
   riesgo **subsanable** → condición al cierre; riesgo de **cambio** entre firma y cierre → MAC; lo
   **revelado** → sale por disclosure schedules. El SPA es la DD hecha cláusulas.
3. **¿Por qué un fondo pelea el *drag along*?** Porque su negocio es **comprar y vender** (exit); el drag
   le garantiza poder vender la **empresa entera** (lo que un comprador quiere) sin que un minoritario lo
   bloquee. Sin drag, su salida queda a merced de terceros.
4. **¿Locked box o completion accounts para una empresa con capital de trabajo muy volátil?** Tiende a
   convenir **completion accounts** (ajuste al cierre), porque captura las variaciones reales; el *locked
   box* (precio fijo) dejaría el riesgo de esa volatilidad al comprador desde la fecha del box.
5. **¿Qué diferencia a una rep "fundamental" de una "del negocio", y por qué importa?** Las fundamentales
   (título de acciones, capacidad, autoridad) tocan la **esencia** de lo que se compra; por eso reciben
   protección **reforzada** (sin tope, supervivencia larga/indefinida). Las del negocio se topan y caducan
   antes. La distinción define **cuánto y por cuánto tiempo** responde el vendedor.

## 33. Casos de examen (con respuesta modelo)

**Caso A.** *En la due diligence detectaste un litigio fiscal concreto de 5 millones, probable pero no
seguro. El vendedor se niega a bajar el precio. ¿Cómo lo proteges en el SPA?*
**Respuesta modelo:** Como es un riesgo **concreto y conocido**, no basta la rep general: se pacta una
**indemnización especial** por ese litigio específico, **al 100% y fuera de caps y baskets**, respaldada
por un **escrow** suficiente por el plazo de resolución, con **control de la defensa** del litigio
definido. Alternativamente, un **ajuste/retención** de precio por el monto en riesgo. Razonar: riesgo
conocido → indemnización específica, no rep general.

**Caso B.** *Firmas un SPA en enero con cierre en mayo (pendiente COFECE). En marzo, una recesión golpea a
toda la industria y la target pierde 30% de ventas. Tu cliente comprador quiere salir. ¿Puede invocar la
MAC?*
**Respuesta modelo:** Depende de las ***carve-outs*** de la MAC. Si excluye los **eventos sistémicos**
(recesiones, condiciones de la industria) —lo habitual—, el comprador **no** puede salir, **salvo** que la
target esté afectada **desproporcionadamente** frente a sus competidores. Además, el umbral exige un
impacto **sustancial y duradero**, no un mal trimestre. Probablemente **no** procede la salida; sí puede
servir como palanca de **renegociación**. Citar la lógica de Akorn/Tyson.

**Caso C.** *Un fondo invierte 40% en una empresa familiar y quiere asegurar su salida en 6 años. ¿Qué
cláusulas del SHA son imprescindibles?*
**Respuesta modelo:** **Drag along** (para vender el 100% sin bloqueo de la familia), **derechos de
registro/compromiso de exit** (venta o IPO en el horizonte), **preferencia de liquidación** (cobrar
primero), **vetos** sobre decisiones que afecten su salida, y **tag along** (por si la familia vende
antes). Sin drag y sin compromiso de exit, su salida queda atrapada. Conectar: para el inversionista, la
**salida** es lo central del SHA.

## 34. Simulador (ejercicio tipo despacho)

> **Instrucciones:** eres asociado de M&A. Representas al **comprador** (un fondo) en la adquisición del
> 100% de *Distribuidora Sol, S.A.* La DD reveló: (i) un contrato clave con *change of control*; (ii) una
> contingencia fiscal concreta de 8M; (iii) capital de trabajo estacional muy volátil; (iv) la PI de la
> marca a nombre de un accionista. Diseña la **protección documental** antes de leer la guía.

1. ¿Qué mecanismo de **precio** propones, dada la volatilidad del capital de trabajo?
2. ¿Cómo proteges la **contingencia fiscal concreta**?
3. ¿Cómo aseguras la **continuidad del contrato clave** con *change of control*?
4. ¿Cómo resuelves la **PI a nombre del accionista**?
5. ¿Qué pides en **indemnización** (cap, basket, supervivencia, sandbagging) como comprador?

> **Guía de solución (resumen).** **(1)** **Completion accounts** (ajuste por capital de trabajo, deuda
> neta y caja al cierre), por la volatilidad estacional; alternativamente locked box con un *target* de
> capital de trabajo bien calibrado. **(2)** **Indemnización especial** por la contingencia fiscal (100%,
> fuera de cap/basket) + **escrow** por el plazo de prescripción + control de la defensa. **(3)**
> **Consentimiento** de la contraparte como **condición al cierre** (CP); si no se obtiene, derecho a no
> cerrar o ajustar precio. **(4)** **Condición al cierre** de **transferir la PI** a la sociedad + rep
> específica + indemnización por titularidad. **(5)** Como comprador: **cap alto** (o 100% para
> fundamentales/fiscales), **basket bajo** (idealmente *tipping*), **supervivencia larga** (fiscales/
> fundamentales hasta su prescripción), reps **sin** *knowledge qualifier* donde se pueda, y cláusula
> **pro-sandbagging**. Y **escrow** o **W&I insurance** para asegurar el cobro.

## 35. Flashcards

- **¿Qué es vinculante en un Term Sheet?** Lo procesal (exclusividad, confidencialidad, gastos, ley
  aplicable); lo sustantivo (precio, estructura), normalmente NO.
- **¿Las cuatro piezas del SPA en el tiempo?** Reps (pasado) · Covenants (interino) · Conditions (cierre) ·
  Indemnización (futuro).
- **¿Qué son las reps & warranties?** Afirmaciones de hecho garantizadas; si son falsas → indemnización.
- **¿Cap, basket, de minimis, survival?** Tope máximo · umbral mínimo acumulado · mínimo por reclamación ·
  plazo de vigencia de la rep.
- **¿Indemnización especial?** Para riesgo concreto y conocido (de la DD), normalmente sin tope y fuera de
  cesta.
- **¿Qué es la MAC?** Cláusula que permite no cerrar ante un cambio adverso sustancial y duradero; umbral
  altísimo.
- **¿Qué son los disclosure schedules?** Anexos donde el vendedor revela excepciones a sus reps (lo
  revelado deja de estar garantizado).
- **¿Sandbagging?** Si el comprador que sabía puede reclamar (pro) o no (anti); se pacta expresamente.
- **¿Locked box vs. completion accounts?** Precio fijo sobre balance pasado / ajuste según balance al
  cierre.
- **¿Earn-out?** Parte del precio diferida y condicionada a resultados futuros.
- **¿Drag vs. tag along?** La mayoría obliga a vender (drag) / la minoría puede sumarse a la venta (tag).
- **¿Preferencia de liquidación?** Derecho del inversionista a cobrar primero (un múltiplo) en venta/
  liquidación.
- **¿SPA vs. APA?** Compra de acciones (sociedad entera) / compra de activos (perímetro descrito).

## 36. Mapas mentales

```
                     DOCUMENTACIÓN DEL M&A
                              |
   ┌──────────────┬──────────┼───────────────┬──────────────────┐
 TERM SHEET/LOI    SPA           APA            SHA
 (bases;        (share deal;  (asset deal;   (gobierno + capital
  exclusividad   reps,         perímetro,      + salida:
  vinculante;    covenants,    cesiones,       vetos, preferencias,
  resto NO)      conditions,   pasivos         drag/tag, deadlock,
                 indemnización, asumidos)      put/call)
                 MAC, schedules)
```

```
              EL SPA EN EL TIEMPO (4 actos)
  PASADO ───────► REPS & WARRANTIES (cómo es la empresa)
  INTERINO ─────► COVENANTS (qué se hace entre signing y closing)
  CIERRE ───────► CONDITIONS PRECEDENT (puerta del closing)
  FUTURO ───────► INDEMNIFICATION (si algo era falso) + MAC (si todo cambió)
```

## 37. Cuadros comparativos

**Los cuatro documentos**

| | Term Sheet/LOI | SPA | APA | SHA |
|---|---|---|---|---|
| Función | Bases del deal | Comprar acciones | Comprar activos | Gobernar a los socios |
| Vinculante | Parcial | Total | Total | Total |
| Momento | Inicio | Firma/cierre | Firma/cierre | Tras la inversión |
| Núcleo | Exclusividad, precio | Reps, indemnización, MAC | Perímetro, pasivos | Vetos, drag/tag, salida |

**Qué quiere cada parte en la indemnización**

| Variable | Comprador quiere | Vendedor quiere |
|---|---|---|
| Cap (tope) | Alto | Bajo |
| Basket (umbral) | Bajo | Alto |
| Supervivencia | Larga | Corta |
| Knowledge qualifier | Sin él (objetivo) | Con él |
| Sandbagging | Pro | Anti |
| Escrow | Grande | Pequeño / W&I |

**Drag vs. Tag (la tensión de la salida)**

| | Drag along | Tag along |
|---|---|---|
| A favor de | Mayoría / inversionista | Minoría |
| Efecto | Obliga a la minoría a vender | Permite a la minoría sumarse |
| Objetivo | Vender el 100% sin bloqueo | No quedar atrapado con nuevo control |

## 38. Diagramas

**Del hallazgo (DD) a la cláusula (SPA):**
```
Riesgo DESCONOCIDO ─────────► rep general + indemnización (cap/basket)
Riesgo CONCRETO y CONOCIDO ─► indemnización ESPECIAL (sin tope, fuera de cesta)
Riesgo SUBSANABLE ──────────► condición al cierre (CP)
Riesgo de CAMBIO (firma→cierre) ► cláusula MAC
Lo que el vendedor REVELA ──► disclosure schedules (sale de la garantía)
```

**Anatomía del SPA (mapa de secciones):**
```
1. Definiciones  → 2. Objeto y Precio  → 3. Reps & Warranties
→ 4. Covenants  → 5. Conditions Precedent  → 6. Indemnification
→ 7. Terminación / MAC  → 8. Boilerplate (ley, arbitraje)  → 9. Anexos (disclosure schedules)
```

**El SHA (tres familias):**
```
GOBIERNO            CAPITAL                 SALIDA
consejo, vetos,     preferencia liq.,       lock-up, ROFR/ROFO,
información,         antidilución,           tag along, drag along,
deadlock            preemptive rights       put/call, exit/IPO, leaver
```

## 39. Mnemotecnias

- **SPA en el tiempo (RCCI):** **R**eps (pasado) · **C**ovenants (interino) · **C**onditions (cierre) ·
  **I**ndemnización (futuro).
- **Term Sheet:** *"lo sustantivo no obliga; lo procesal sí"* (exclusividad y confidencialidad vinculan).
- **Indemnización:** *"cap arriba, basket abajo, survival el reloj"*.
- **Riesgo conocido vs. desconocido:** *"lo desconocido → rep general; lo conocido → indemnización
  especial"*.
- **MAC:** *"firmar no es cerrar; pero salir por MAC casi nunca"* (umbral altísimo).
- **Disclosure:** *"lo que revelo, ya no lo garantizo"*.
- **Sandbagging:** *"pro = el comprador cobra aunque supiera; anti = no"*.
- **Salidas del SHA:** *"drag arrastra (mayoría), tag acompaña (minoría)"*.
- **Regla de oro:** *"no copies cláusulas; entiende qué riesgo reparte cada una"*.

## 40. Resumen ejecutivo

La documentación es donde el M&A se vuelve **texto vinculante y exigible**. Cuatro documentos nucleares.
El **Term Sheet / LOI** fija las bases de la negociación: lo **sustantivo** (precio, estructura) es **no
vinculante** —para poder retirarse—, pero lo **procesal** (exclusividad, confidencialidad, gastos, ley
aplicable) **sí** obliga; redactar mal la cláusula de "no vinculante" es un error caro. El **SPA**
(compraventa de acciones) es el documento rey: un **sistema de asignación de riesgo en el tiempo** —las
**reps & warranties** garantizan cómo es la empresa (pasado), los **covenants** regulan la conducta entre
firma y cierre (interino), las **conditions precedent** son la puerta del cierre, y la **indemnización**
(con *cap*, *basket*, *de minimis* y *survival*) responde si algo era falso (futuro), mientras la **MAC**
cubre el riesgo de que el mundo cambie entre firma y cierre—. Los **disclosure schedules** revelan
excepciones a las reps (lo revelado deja de estar garantizado), y el **sandbagging** define si el
comprador que ya sabía puede reclamar. El **precio** se fija y ajusta vía *locked box* o *completion
accounts*, con *earn-out* y *escrow*. El **APA** (compraventa de activos) replica la estructura del SPA
pero su corazón es la **descripción del perímetro** (activos/pasivos incluidos y excluidos) y las
**cesiones y consentimientos**. Y el **SHA** gobierna la convivencia de los socios: **gobierno** (consejo,
vetos, deadlock), **capital** (preferencia de liquidación, antidilución) y **salida** (lock-up, ROFR/ROFO,
**tag along**, **drag along**, put/call).

La lección que atraviesa el libro: **no se memorizan cláusulas, se entiende la gramática del riesgo**. Cada
cláusula existe porque responde a una pregunta —¿qué me aseguras?, ¿qué pasa entre firma y cierre?, ¿qué
condiciones?, ¿qué pasa si sale mal?, ¿cómo gobernamos y cómo salimos?— y cada respuesta **reparte un
riesgo** entre las partes. El SPA es, literalmente, **la due diligence convertida en cláusulas**, y el
documento **sigue a la estructura**, que **sigue a la due diligence**: la cadena **investigar → estructurar
→ documentar** queda completa.

Para tu perfil —operaciones complejas, M&A, gobierno corporativo y contratos estratégicos— este libro es
central: el SPA/APA documenta la operación, el SHA **diseña el gobierno corporativo y las salidas por
contrato**, y el Term Sheet sienta las bases de todo acuerdo estratégico. Dominar esta documentación —con
criterio, no como formulario, y anclada en el derecho mexicano— es dominar el **lenguaje en el que se
escriben los acuerdos corporativos**.

## 41. Checklist

**Term Sheet / LOI:**
- [ ] ¿Cláusula **expresa** de "no vinculante" para lo sustantivo, con las excepciones vinculantes
  (exclusividad, confidencialidad, gastos, ley aplicable) claramente identificadas?
- [ ] ¿Exclusividad (*no-shop*) por un plazo razonable que proteja la inversión en la due diligence?

**SPA / APA:**
- [ ] ¿Las **definiciones** clave ("Pérdidas", "Conocimiento", "Deuda", "MAC") están negociadas?
- [ ] ¿Las **reps** cubren todo lo relevante? ¿Distingues fundamentales vs. del negocio? ¿*Knowledge* y
  *materiality qualifiers* calibrados?
- [ ] ¿Los **covenants** protegen el periodo interino (operación ordinaria) y el post-cierre (no
  competencia razonable)?
- [ ] ¿Las **condiciones al cierre** recogen autorizaciones (COFECE), consentimientos por *change of
  control*, *bring-down* de reps y ausencia de MAC?
- [ ] ¿La **indemnización** (cap, basket, de minimis, survival) refleja el reparto de riesgo y el precio
  acordado? ¿Indemnizaciones **especiales** para los riesgos concretos de la DD?
- [ ] ¿La **MAC** y sus *carve-outs* asignan claramente el riesgo sistémico vs. específico?
- [ ] ¿Definiste **sandbagging** (pro/anti) y el **mecanismo de precio** (locked box / completion accounts,
  earn-out, escrow)?
- [ ] **APA:** ¿perímetro de activos/pasivos preciso? ¿Cesiones y consentimientos como CP? ¿Cuestión
  laboral resuelta?
- [ ] ¿Las cláusulas importadas están **ancladas** en derecho mexicano (exigibles)? ¿Cláusula **arbitral**?

**SHA:**
- [ ] **Gobierno:** ¿asientos de consejo, **vetos/materias reservadas**, información, mecanismo de
  *deadlock*?
- [ ] **Capital:** ¿preferencia de liquidación, antidilución, derechos de preferencia?
- [ ] **Salida:** ¿lock-up, ROFR/ROFO, **tag along**, **drag along**, put/call, compromiso de exit/IPO,
  *good/bad leaver*?
- [ ] ¿Lo que se pueda está **reflejado en los estatutos** (S.A.P.I.) para oponerlo a terceros?

## 42. Bibliografía comentada

- **American Bar Association — *Model Stock Purchase Agreement with Commentary* y *Model Asset Purchase
  Agreement*.** **Imprescindible**: el SPA y el APA cláusula por cláusula con comentario. El mejor material
  del mundo para dominar la documentación.
- **Subramanian, *Dealmaking* (Harvard).** El contrato como producto de una **negociación** estratégica
  (setup, MAC, earn-out, drag/tag).
- **Jurisprudencia de Delaware (Akorn, Tyson, Genesco).** Interpretación de la **MAC**, el *sandbagging* y
  las reps; modela la redacción global.
- **Practical Law / PLC y *precedents* de despachos.** Los **estándares de mercado** de cada cláusula (qué
  cap, basket y survival son "de mercado").
- **Ley del Mercado de Valores (S.A.P.I.) y doctrina societaria mexicana.** El sustento legal del **SHA** en
  México (validez de vetos, drag/tag, opciones).
- **Código Civil Federal / Código de Comercio (compraventa, saneamiento, vicios del consentimiento,
  penas convencionales).** La base local en la que se **anclan** las cláusulas para que sean exigibles.
- **Materiales sobre W&I insurance.** Cómo el seguro de reps & warranties reconfigura la indemnización.

## 43. Ruta hacia el siguiente libro

Ya dominas el **lenguaje del M&A**: sabes leer y redactar el Term Sheet, el SPA, el APA y el SHA
entendiendo la lógica de cada cláusula. Con esto cierras la **cadena nuclear** del M&A: **investigar
(Libro 2) → estructurar (Libro 3) → documentar (Libro 4)**. El siguiente paso —según la ampliación que
acordamos para tu perfil— es entender **cómo se financian** las operaciones: la otra mitad de casi todo
deal grande.

- **Siguiente libro:** *[Libro 5 · Derecho Bancario y Financiamiento Corporativo](./05-Derecho-Bancario-y-Financiamiento-Corporativo.md)* —
  la deuda bancaria y **sindicada**, las **garantías** (reales y personales) y los paquetes de garantías,
  los **covenants financieros**, el *project finance*, el **acquisition finance** (cómo se financia
  específicamente una compra/LBO) y los **bonos**. Es la columna que falta para estructurar operaciones
  complejas: casi ningún deal grande se paga solo con caja.
- **Conexión inmediata:** los **covenants** y las **condiciones** que viste en el SPA tienen su gemelo en
  los contratos de financiamiento (los *facilities agreements*); el **escrow** y los mecanismos de precio
  se entienden mejor sabiendo cómo se fondea el comprador; y el **LBO** que anticipamos en el Libro 3
  (NewCo + deuda + fusión apalancada) se documenta con los contratos que estudiarás a continuación.

---

## ✦ ¿Por qué esto importa para un abogado corporativo?

Porque la documentación es **el producto tangible y mejor remunerado** del abogado de M&A: el contrato que
protege la inversión del cliente. Un socio se distingue, ante todo, por su **maestría en el SPA y el SHA**
—saber qué cláusula pedir, cómo redactarla, hasta dónde ceder y qué riesgo esconde cada palabra del
borrador de la contraparte—. Esta habilidad es **acumulativa y difícil de improvisar**: cada cláusula
estándar existe porque algún deal salió mal y nació para evitar que se repita; quien entiende esa historia
lee los contratos con una profundidad que ningún formulario da. Y para quien quiere especializarse en
**operaciones complejas, gobierno corporativo y contratos estratégicos**, este libro es la columna
vertebral: el SPA/APA documenta la operación, el **SHA diseña el gobierno y las salidas por contrato**, y
el Term Sheet sienta las bases de todo acuerdo. Dominar esta documentación es **hablar el idioma en que se
toman y se blindan las grandes decisiones corporativas**.

## ✦ Cómo piensa un socio de un despacho internacional

> *"Cuando recibo el borrador de un SPA, no lo leo de corrido: lo leo como un **mapa de riesgos**. Voy
> directo a tres lugares. Primero, las **reps & warranties** y sus calificadores: ¿qué garantiza el
> vendedor, y cuánto lo diluyen los 'a mi leal saber y entender' y los 'en aspectos materiales'? Cada
> calificador que acepto es un riesgo que le quito al vendedor y se lo paso a mi cliente. Segundo, el
> **paquete de indemnización**: cap, basket, supervivencia, escrow. Esto **no** es técnica jurídica
> aislada: es **precio**. Si acepto un cap del 10% en vez del 30%, le acabo de regalar al vendedor una
> rebaja de riesgo que vale millones; lo negocio hablando con mi cliente de cuánto riesgo quiere retener.
> Tercero, la **MAC** y sus exclusiones: ahí se decide quién carga con que el mundo cambie entre la firma y
> el cierre. Y en el **SHA**, mi obsesión es la **salida**: el precio de entrada se negocia un día, pero la
> salida define el retorno de toda la inversión —drag, tag, preferencia, compromiso de exit—. Mi regla con
> los asociados: **ninguna cláusula es relleno y ninguna se copia sin entender qué riesgo reparte**. El que
> redacta sin entender, tarde o temprano firma una bomba."*

## ✦ Errores que cuestan millones

1. **Term Sheet que obliga sin querer.** Redactarlo de forma que parezca un acuerdo cerrado y quedar
   atrapado en un compromiso o en responsabilidad precontractual. *Prevención:* cláusula expresa de "no
   vinculante" con las excepciones procesales bien delimitadas.
2. **MAC con *carve-outs* mal redactadas.** Que una crisis te deje sin salida (o que se la dé a la
   contraparte) por una exclusión ambigua. *Prevención:* redactar con precisión riesgo sistémico vs.
   específico y la regla del impacto desproporcionado.
3. **No traducir el hallazgo de la DD a una cláusula.** Detectar un riesgo concreto y conformarse con la
   rep general (topada y con basket) en vez de exigir **indemnización especial** sin tope. *Prevención:*
   riesgo conocido → indemnización específica.
4. **Descuidar el SHA (gobierno y salida).** Para el inversionista, una salida mal diseñada (sin drag, sin
   compromiso de exit) atrapa su capital; para la familia, la falta de reglas destruye la empresa.
   *Prevención:* negociar el SHA con la misma energía que el precio.
5. **Importar cláusulas anglosajonas sin anclarlas en derecho mexicano.** Volverlas **inejecutables**
   (sandbagging, ciertas renuncias, penas). *Prevención:* anclar en figuras del CCF/CCom y pactar
   arbitraje.

---

> *Cierre del Libro 4.* Has aprendido a **convertir la operación en texto vinculante**: el Term Sheet que
> ordena, el SPA y el APA que consuman y asignan el riesgo, y el SHA que gobierna la convivencia y diseña
> las salidas. Más importante que las cláusulas, te llevas la **gramática del riesgo**: la capacidad de
> leer cualquier contrato de M&A y ver, en minutos, **dónde está el riesgo y quién lo soporta**. Con esto
> cierras la cadena nuclear del M&A —**investigar → estructurar → documentar**— y tienes ya el oficio
> central del abogado de transacciones. Ahora ampliamos hacia tu perfil: en el **Libro 5 · Derecho
> Bancario y Financiamiento Corporativo** aprenderás **cómo se paga** todo esto —la deuda, las garantías,
> los covenants financieros, el acquisition finance—, la otra mitad de casi cualquier operación compleja.


---

## ⚖️ Suplemento del Consejo Editorial

> *Elevación al estándar de obra de referencia. Doctrina, comparado, caso y criterio; disciplina ⟳.*

### Cómo piensa un socio internacional
La documentación es donde el abogado **materializa la asignación de riesgo**. El socio sabe que el 90% del valor jurídico de un *deal* vive en cuatro lugares del SPA: **declaraciones y garantías**, **obligaciones de hacer/no hacer (*covenants*)**, **condiciones de cierre** e **indemnización** (con sus *caps*, *baskets*, *survival* y *escrow*). El resto es andamiaje. Y el **SHA** define la convivencia futura: consejo, veto, salidas.

### Doctrina y debate
- **Función de las *reps & warranties*:** distribuir el riesgo de información (Akerlof) y crear un derecho de indemnización con base contractual, más fuerte que el saneamiento legal.
- **Debate clásico (planteado por el propio prompt):** *¿deben las reps & warranties sobrevivir cinco años?* Un *survival* largo protege al comprador pero encarece y eterniza el riesgo del vendedor; el mercado tiende a 12-24 meses (salvo fundamentales/fiscales/laborales). No hay respuesta única: **depende del riesgo y del poder de negociación**.
- ***Sandbagging*:** ¿puede el comprador reclamar por una *rep* falsa que **ya conocía**? Cláusula *pro-sandbagging* vs. *anti-sandbagging*.

### Derecho comparado
El SPA moderno es una **importación anglosajona**; el reto en México es adaptarlo sin importar figuras vacías (*consideration*) y engancharlo al derecho local (saneamiento, nulidad, art. 1832/2248 CCF; transmisión art. 129 LGSM ⟳). El **R&W insurance** y las cláusulas *MAC*, *earn-out* y *escrow* ya son estándar en el mercado mexicano de *deals* medianos y grandes.

### Caso real
**Twitter/X–Musk (2022):** Musk quiso invocar información (cuentas *bot*) para desistirse; el SPA tenía cláusulas de *specific performance* y una MAC estrecha. Delaware iba a **forzar el cierre**, y Musk cerró en ~44,000 mdd ⚠️ *verificar*. Lección: la MAC y los *remedies* del SPA no son relleno: deciden si te puedes arrepentir.

### Errores que cuestan millones
- *Survival* y *cap* mal calibrados; **cesta (*basket*)** ambigua (¿deducible o *tipping*?).
- SHA sin **mecanismo de salida** (deadlock, *tag/drag*, *put/call*): socios atrapados.

### Preguntas
- **Criterio:** ¿cinco años de *survival* para las *reps*? Defienda comprador y vendedor.
- **Entrevista:** explique *cap*, *basket* y *escrow* y cómo interactúan.
- **Examen:** enuncie las cuatro secciones de mayor riesgo de un SPA.

### Bibliografía por niveles
- **Básico:** [Banco de Formatos](../../Banco-de-Formatos/) (SPA, term sheet, SHA).
- **Intermedio:** ABA, *Model Stock Purchase Agreement with Commentary*.
- **Avanzado:** Adams, *A Manual of Style for Contract Drafting*.
- **Internacional:** Kling & Nugent, *Negotiated Acquisitions of Companies, Subsidiaries and Divisions*.
