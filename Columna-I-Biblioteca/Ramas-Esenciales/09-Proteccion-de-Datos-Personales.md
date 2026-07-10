# [Ramas Esenciales · Libro 9] Protección de Datos Personales

> ⟳ **Apóstrofe de vigencia — léela cada vez.** El Derecho cambia sin avisar: un artículo puede mudar de número, de redacción o quedar **derogado** de un día para otro. El símbolo **⟳** que aparece tras cada artículo citado en este libro significa una sola cosa: *«¿sigue vigente —y con este mismo número— hoy? No lo cites de memoria ni desde este libro: **reitéralo en su código vigente**»* (textos oficiales en [`../../fuentes-legales/`](../../fuentes-legales/)). Caso real: el **art. 390 del CPF** que este proyecto cotejó aparece hoy como **«Derogado»**. Recuerda: un **✅** dice que el dato fue verificado *palabra por palabra a la fecha de su fuente*; la **⟳** te avisa que esa fecha ya quedó atrás y que la última palabra la tiene el código, no el libro.


> Los datos son "el nuevo petróleo": las empresas viven de recolectar, procesar y monetizar información de
> personas —clientes, empleados, usuarios—. Pero esa información **pertenece**, en cierto sentido, a quien
> la genera, y el derecho lo protege: la **protección de datos personales** garantiza que las personas
> controlen quién usa su información y para qué. Para el abogado corporativo, esto es riesgo puro y
> creciente: un mal manejo de datos se traduce en **multas enormes**, crisis reputacional y contingencias
> que aparecen en toda **due diligence** de empresas tecnológicas y de consumo. En la economía digital, el
> compliance de datos dejó de ser accesorio: es **licencia para operar**.

**Etiquetas:** datos personales · privacidad · LFPDPPP · aviso de privacidad · derechos ARCO · transferencias · ciberseguridad · conexión con DD tecnológica y compliance
**Prerrequisitos:** [Personas (I-05)](../Nivel-I-Fundamentos/05-Personas.md), [Constitucional (02)](./02-Derecho-Constitucional-y-Amparo.md), [Administrativo (03)](./03-Derecho-Administrativo.md). **Se complementa con** [Propiedad Intelectual (07)](./07-Propiedad-Intelectual.md) y [Compliance (06)](./06-Derecho-Penal-Economico-y-Compliance.md).
**Estándar:** V3 (43 secciones + secciones transversales).
**⏱ Tiempo estimado de dominio:** 4–6 semanas (≈ 40–55 h de estudio activo). Lectura de
reconocimiento: 6–8 h. *Estúdialo así: qué es el dato personal y la autodeterminación informativa → los
principios y deberes → derechos ARCO → aviso de privacidad y transferencias → seguridad y brechas → la
protección de datos en M&A y compliance.*

> **⚠️ AVISO DE VERIFICACIÓN. Contenido a fecha: 2026-07.** En México rige la **Ley Federal de Protección
> de Datos Personales en Posesión de los Particulares (LFPDPPP)** para el **sector privado** (y otra ley
> para el sector público). Los principios, montos de multas y la **autoridad** cambian con reformas.
> Siguiendo el [Protocolo de Verificación](../../PROTOCOLO_DE_VERIFICACION.md), este tratado enseña la
> **lógica y la estructura** y marca **⚠️** todo artículo, monto y dato como *"verificar contra el texto
> vigente"*.

> **🛑 ACTUALIZACIÓN CRÍTICA — Extinción del INAI (reforma 2024-2025).** La misma **reforma constitucional
> de "simplificación orgánica" de 2024** que extinguió a la COFECE y al IFT **también extinguió al INAI**
> (Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales), la
> autoridad garante en la materia. **Verificado ✅ (2026-07):** sus funciones se transfirieron a la
> **Secretaría Anticorrupción y Buen Gobierno** (dependiente del Ejecutivo federal), a partir del
> **21 de marzo de 2025**. **Verificado ✅ verbatim contra la nueva LFPDPPP (texto vigente, DOF
> 14-11-2025), archivada en [`fuentes-legales/`](../../fuentes-legales/):** la **nueva Ley Federal de
> Protección de Datos Personales en Posesión de los Particulares** (que **abrogó la de 2010**) designa
> como autoridad a la **"Secretaría" = Secretaría Anticorrupción y Buen Gobierno** (art. 2, fr. XV ✅) y
> le fija sus atribuciones en los **arts. 38-39 ✅**; conserva los **derechos ARCO** (art. 21 ✅).
> **Esto no cambia los principios ni los deberes de las empresas, pero sí la autoridad ante la que se
> tramitan procedimientos.** Donde este tratado diga "INAI", entiende **la Secretaría Anticorrupción y
> Buen Gobierno** (autoridad garante vigente). ⟳ *Reverifica ante posibles reformas.* Contenido reformulado.

> **Aviso de método.** Tratado, no repaso. Aquí aprendes a proteger uno de los activos y riesgos más
> importantes de la empresa digital: **los datos de las personas**.

---

### Nivel de importancia profesional (vista rápida)
```
Litigio              ★★★☆☆
Corporate            ★★★★☆
M&A                  ★★★★☆
Mercado de Valores   ★★★☆☆
Venture Capital      ★★★★☆
Private Equity       ★★★☆☆
Gobierno Corporativo ★★★★☆
Compliance           ★★★★★
Derecho Bancario     ★★★★☆
Empresa Familiar     ★★☆☆☆
```
*En compliance y en empresas digitales vale ★★★★★: el manejo de datos es riesgo regulatorio, reputacional
y contractual de primer orden, y activo estratégico.*

---

## 1. Introducción

Cada vez que una persona da su nombre, su correo, su teléfono, su huella, su historial de compras o su
ubicación, genera **datos personales**: cualquier información que la **identifica o la hace
identificable**. Las empresas recolectan y procesan cantidades masivas de estos datos, y con ellos crean
valor (marketing, crédito, personalización, IA). El derecho responde con una idea poderosa: la
**autodeterminación informativa** —el derecho de cada persona a **controlar** su información: saber quién
la tiene, para qué, y poder acceder, rectificar, cancelar u oponerse a su uso—. Ese es el objeto de la
**protección de datos personales**.

No es un derecho abstracto: se traduce en **deberes concretos** para quien maneja datos (el
"**responsable**"): informar mediante un **aviso de privacidad**, obtener **consentimiento**, limitar el
uso a lo necesario, **proteger** los datos con medidas de seguridad, respetar los **derechos ARCO**
(Acceso, Rectificación, Cancelación, Oposición) y regular las **transferencias** a terceros. Incumplir
genera **multas cuantiosas**, y —en un mundo de filtraciones masivas y ciberataques— **crisis
reputacionales** que destruyen la confianza.

Para el abogado corporativo, este libro es indispensable en la **economía digital**. Los datos son, a la
vez, un **activo** (bases de clientes, información valiosa) y un **pasivo/riesgo** (contingencias por
incumplimiento, brechas de seguridad). En M&A tecnológico, la **due diligence de datos** revela si la
empresa maneja legalmente su información —y si su activo estrella (una base de datos) es lícito y
transferible—.

## 2. Objetivos del libro

Al terminar, el lector será capaz de:

- **Definir el dato personal** (y el **dato sensible**) y explicar la **autodeterminación informativa** y
  su base constitucional (art. 16 CPEUM ✅ ⟳).
- **Dominar los principios** del tratamiento: **licitud, consentimiento, información, calidad, finalidad,
  lealtad, proporcionalidad y responsabilidad**.
- **Manejar los deberes**: **aviso de privacidad**, seguridad, confidencialidad y la gestión de los
  **derechos ARCO**.
- **Comprender las transferencias** de datos (nacionales e internacionales) y sus requisitos.
- **Entender la seguridad de datos y las brechas** (vulneraciones): prevención, respuesta y notificación.
- **Conocer a la autoridad** garante (tras la extinción del INAI ⚠️) y el procedimiento sancionador.
- **Aplicar la materia a la práctica corporativa**: la **due diligence de datos**, las cláusulas de datos
  en contratos, y el compliance de privacidad.

## 3. Importancia profesional

La protección de datos es una **práctica en explosión**, empujada por la digitalización, la nube, la IA y
los estándares globales (sobre todo el **GDPR** europeo, que fijó el estándar mundial). Los despachos tienen
áreas de **privacidad y protección de datos** que asesoran en: **avisos de privacidad y políticas**,
**compliance** (mapeo de datos, evaluaciones de impacto), **transferencias internacionales**, **respuesta
a brechas** e **investigaciones**, y **M&A** (due diligence de datos). Para el joven que quiere el nicho
corporativo con enfoque **tecnológico y de consumo**, es imprescindible: no se puede estructurar la compra
o financiamiento de una empresa cuyo activo son los **datos** sin entender su régimen. Además, cruza con
ciberseguridad, PI (datos como activo) y compliance penal (delitos informáticos).

## 4. Historia de la institución

La protección de datos nace del miedo, tras la Segunda Guerra Mundial y la era de las computadoras, a que
el Estado y las corporaciones acumularan **poder sobre las personas mediante su información**. Alemania
acuñó el concepto de **autodeterminación informativa** (célebre sentencia del Tribunal Constitucional
alemán sobre el censo, 1983 ⚠️). Europa lideró con el **Convenio 108** (1981) y la **Directiva de 1995**,
que culminaron en el **Reglamento General de Protección de Datos (GDPR)** de la Unión Europea (adoptado el
27-abr-2016, **aplicable desde el 25-may-2018** ✅) —hoy
el **estándar de oro** mundial, con multas de hasta un porcentaje de la facturación global—. México elevó
la protección de datos a rango **constitucional** (reformas a los arts. 6 y 16 ✅ ⟳) y expidió la
**LFPDPPP** para el sector privado. ⚠️ *Verificar fechas.*

## 5. Evolución histórica

En **México** (⚠️ verificar):
1. **Rango constitucional:** los arts. 6 y 16 ⟳ reconocen el acceso a la información y la protección de datos
   personales como derechos.
2. **LFPDPPP (nueva ley, vigente DOF 14-11-2025 ✅; abrogó la de 2010 ⟳)** y su Reglamento: régimen del **sector privado** (principios, ARCO, aviso de
   privacidad, transferencias, sanciones), aplicado por el entonces **IFAI/INAI**.
3. **Ley para el sector público** (sujetos obligados): régimen paralelo para entes públicos.
4. **Extinción del INAI (reforma 2024-2025 ✅):** la autoridad garante autónoma desapareció con la
   simplificación orgánica; sus funciones pasaron a la **Secretaría Anticorrupción y Buen Gobierno** (a
   partir del **21-mar-2025**), con una **nueva Ley General de Protección de Datos Personales** ⚠️.
Tendencias globales que México sigue: influencia del **GDPR**, retos de la **inteligencia artificial** y el
*big data*, la **ciberseguridad** y la protección de datos de **menores** y **biométricos**.

## 6. Contexto económico

Los datos son un **activo económico** de primer orden: alimentan la publicidad dirigida, el crédito, la
personalización y la **inteligencia artificial**. Modelos de negocio enteros (redes sociales, plataformas)
se basan en datos. Pero ese activo tiene un **costo regulatorio**: recolectarlos y usarlos exige cumplir la
ley, y hacerlo mal genera **multas y pérdida de confianza** (el activo más valioso de una empresa digital).
La protección de datos, bien gestionada, es **ventaja competitiva** (confianza del usuario) y, mal
gestionada, **pasivo explosivo**. En M&A, una base de datos **lícita y bien documentada** vale; una
**ilícita o contaminada** es un riesgo que baja el precio o mata el *deal*.

## 7. Contexto político

La protección de datos enfrenta intereses poderosos: el **poder del Estado** (vigilancia, seguridad
nacional), el **poder de las grandes plataformas** (que viven de los datos) y el **derecho de las
personas** a su privacidad. Su regulación es un campo de tensión global: Europa (GDPR) apuesta por derechos
fuertes; EE. UU. tiene un mosaico sectorial; y la geopolítica de los datos (transferencias
internacionales, soberanía de datos, IA) es tema de política comercial. En México, la **extinción del INAI**
—una autoridad autónoma— reabrió el debate sobre quién debe garantizar estos derechos y con qué
independencia. ⚠️

## 8. Contexto social

La privacidad es un **derecho humano** ligado a la dignidad y la libertad: sin control sobre la propia
información, la persona queda expuesta a la manipulación, la discriminación y la vigilancia. En la era
digital, la sociedad vive una tensión entre la **comodidad** (servicios gratuitos a cambio de datos) y la
**privacidad**. Han ganado relevancia la protección de **menores**, de datos **sensibles** (salud,
biométricos, orientación) y frente a la **IA** (perfilamiento, decisiones automatizadas). Para la empresa,
la dimensión social se traduce en **confianza**: los usuarios premian a quien respeta su privacidad y
castigan a quien la traiciona (una brecha de datos puede hundir una marca).

## 9. Contexto empresarial

En la empresa, los datos están en todo: **clientes** (marketing, CRM), **empleados** (RH, nómina,
biométricos), **usuarios** (plataformas, apps), **proveedores** y **vigilancia** (cámaras, accesos). Cada
tratamiento exige **base legal, aviso de privacidad y seguridad**. Momentos críticos: **recolectar** (¿con
qué consentimiento y finalidad?), **usar y compartir** (¿transferencias autorizadas?), **proteger**
(medidas de seguridad, ciberseguridad), **responder a brechas** (¿qué hacer ante un hackeo o filtración?) y
**responder a los titulares** (derechos ARCO). En M&A tecnológico, la **due diligence de datos** determina
si la base de datos —a menudo el activo principal— es **lícita, segura y transferible**, y si hay
contingencias (multas, brechas, demandas).


## 10. Definiciones doctrinales

- **Autodeterminación informativa** (doctrina alemana, sentencia del censo 1983 ⚠️): el derecho de la
  persona a **decidir** sobre la revelación y el uso de sus datos; base conceptual de toda la materia.
- **Privacidad como control** (Alan Westin): la privacidad es la facultad de determinar **qué información
  sobre uno** se comunica a otros y cómo.
- **Privacy by design / by default** (Ann Cavoukian): la protección de datos debe integrarse **desde el
  diseño** de productos y procesos, no añadirse después. ⚠️ *Verificar formulaciones.*

## 11. Definiciones legales

- **Dato personal (LFPDPPP ✅):** cualquier información **concerniente a una persona física identificada o
  identificable**.
- **Dato sensible (LFPDPPP ✅):** el que afecta la esfera más íntima o cuyo uso indebido puede causar
  discriminación o riesgo grave (origen racial, salud, creencias, orientación sexual, datos biométricos,
  etc.); exige protección reforzada y **consentimiento expreso**.
- **Responsable:** quien **decide** sobre el tratamiento de los datos. **Encargado:** quien los trata **por
  cuenta** del responsable.
- **Tratamiento:** cualquier operación con datos (obtención, uso, divulgación, almacenamiento).
- **Aviso de privacidad:** documento por el que el responsable **informa** al titular qué datos recaba,
  para qué y cómo ejercer sus derechos.
- **Derechos ARCO:** **A**cceso, **R**ectificación, **C**ancelación y **O**posición del titular sobre sus
  datos.

## 12. Definición sencilla

Tus datos (nombre, correo, salud, ubicación) son como **tus llaves personales**: la ley dice que las
empresas que las usan deben (1) **avisarte** que las tienen y para qué (aviso de privacidad), (2) pedir tu
**permiso** (consentimiento), (3) usarlas **solo para lo que dijeron** y no de más, (4) **guardarlas
seguras** (para que no las roben), y (5) devolvértelas o borrarlas si lo pides (derechos ARCO). Si una
empresa pierde tus llaves (brecha de seguridad) o las usa mal, hay **multas** y pierde tu confianza. En
corto: **el derecho que te da control sobre tu información y obliga a las empresas a cuidarla.**

## 13. Conceptos fundamentales (glosario riguroso)

- **Titular:** la persona a quien pertenecen los datos.
- **Responsable / encargado:** quien decide vs. quien procesa por cuenta del primero (relación regulada por
  contrato).
- **Consentimiento:** tácito o **expreso** (y expreso **por escrito** para datos sensibles/financieros ⚠️).
- **Principios (LFPDPPP ✅):** licitud, consentimiento, información, calidad, finalidad, lealtad,
  proporcionalidad y responsabilidad.
- **Deberes:** de **seguridad** (medidas administrativas, físicas y técnicas) y de **confidencialidad**.
- **Aviso de privacidad:** integral, simplificado o corto.
- **Derechos ARCO** (+ portabilidad y, en algunos marcos, derecho al olvido ⚠️).
- **Transferencia vs. remisión:** transferencia = a un tercero **distinto** (responsable/encargado externo);
  remisión = al **encargado** que trata por cuenta del responsable.
- **Brecha / vulneración de seguridad:** pérdida, robo o acceso no autorizado a datos; obliga a **notificar**
  ⚠️.
- **Evaluación de impacto (PIA/DPIA):** análisis de riesgos de un tratamiento (estándar GDPR).
- **Privacy by design/by default:** privacidad incorporada desde el diseño.

## 14. Desarrollo absoluto (núcleo doctrinal)

### 14.1 Fundamento y ámbito

La protección de datos tiene base **constitucional** (arts. 6 y 16 CPEUM ✅ ⟳: protección de datos como
derecho, autodeterminación informativa) y legal: la **LFPDPPP** rige el **sector privado** (empresas), y
otra ley rige a los **sujetos obligados** (sector público). El derecho protege a la **persona física**
(titular) frente a quien trata sus datos (**responsable**). *Para la empresa, la primera pregunta es
siempre: ¿qué datos trato, de quién, para qué, y con qué base legal?*

### 14.2 Los principios del tratamiento (el "cómo" legal)

Todo tratamiento debe respetar los **principios** (LFPDPPP ✅): **licitud** (conforme a la ley);
**consentimiento** (permiso del titular, expreso para sensibles); **información** (avisar mediante el aviso
de privacidad); **calidad** (datos exactos y actualizados); **finalidad** (usarlos solo para los fines
informados); **lealtad** (sin engaño); **proporcionalidad** (solo los datos necesarios); y
**responsabilidad** (el responsable debe **poder demostrar** que cumple —*accountability*—). Violar un
principio (p. ej. usar datos para un fin no informado) es incumplimiento sancionable.

### 14.3 El aviso de privacidad y el consentimiento

El **aviso de privacidad** es la pieza operativa central: informa al titular **qué datos** se recaban,
**para qué**, si habrá **transferencias**, y **cómo ejercer** sus derechos ARCO y revocar el
consentimiento. El **consentimiento** puede ser **tácito** (si el aviso está disponible y el titular no se
opone) o **expreso** (requerido para datos **financieros/patrimoniales**, y **por escrito** para datos
**sensibles**) ⚠️. *Un aviso de privacidad mal hecho —o inexistente— es de los incumplimientos más comunes
y sancionados.*

### 14.4 Los derechos ARCO (y más)

El titular puede ejercer, ante el responsable, los **derechos ARCO**: **Acceso** (saber qué datos suyos se
tienen y cómo se usan), **Rectificación** (corregir datos inexactos), **Cancelación** (eliminarlos cuando
proceda) y **Oposición** (a un tratamiento específico). El responsable debe tener un **procedimiento** para
atenderlos en plazos legales ⚠️. Marcos modernos (GDPR) añaden **portabilidad** y el **derecho al olvido**
(supresión), que influyen en México. La **revocación del consentimiento** es también un derecho del titular.

### 14.5 Transferencias de datos (nacionales e internacionales)

Compartir datos con terceros exige reglas. Hay que distinguir la **transferencia** (a un tercero
responsable, que exige informarla en el aviso y, según el caso, consentimiento) de la **remisión** (al
**encargado** que procesa por cuenta del responsable, regulada por un **contrato de encargo** con
obligaciones de seguridad y confidencialidad). Las **transferencias internacionales** son sensibles: el
responsable sigue siendo garante de que el receptor cumpla estándares equivalentes. El **GDPR** condiciona
fuertemente las transferencias fuera de la UE (decisiones de adecuación, cláusulas contractuales tipo) —un
tema crítico para empresas que operan con Europa—. ⚠️

### 14.6 Seguridad de datos y brechas (vulneraciones)

El responsable debe implementar **medidas de seguridad** (administrativas, físicas y técnicas) proporcionales
al riesgo, y mantener la **confidencialidad**. Cuando ocurre una **brecha** (robo, pérdida, hackeo, acceso
no autorizado), surgen deberes de **respuesta**: contener, evaluar, **notificar** a los titulares afectados
(y, según el marco, a la autoridad) sin demora, y remediar ⚠️. La **ciberseguridad** es hoy inseparable de
la protección de datos: la mayoría de las grandes contingencias nacen de **ciberataques**. *La respuesta a
una brecha —rápida, documentada y transparente— puede ser la diferencia entre una crisis manejable y una
catástrofe reputacional y legal.*

### 14.7 La autoridad y el régimen sancionador

Históricamente, la autoridad garante fue el **INAI** (antes IFAI): recibía denuncias, investigaba,
resolvía procedimientos de protección de derechos y **sancionaba** con multas (que podían ser muy elevadas,
en UMA, con agravantes para datos sensibles) ⚠️. **Con la reforma 2024-2025, el INAI se extinguió** y sus
funciones pasaron a la **Secretaría Anticorrupción y Buen Gobierno** (desde el **21-mar-2025**), bajo una
**nueva Ley General de Protección de Datos Personales** ✅ (ver el recuadro del encabezado). **El régimen de
deberes y sanciones subsiste; cambia la autoridad ante la que se litiga.** *Verifica siempre la autoridad y
la ley vigentes.*

### 14.8 La protección de datos en M&A y compliance

En M&A tecnológico/de consumo, la **due diligence de datos** verifica: ¿la empresa tiene **avisos de
privacidad** correctos y consentimientos válidos?, ¿su **base de datos** (a menudo el activo estrella) se
obtuvo lícitamente y es **transferible**?, ¿cumple **seguridad** y ha sufrido **brechas**?, ¿tiene
contingencias o procedimientos con la autoridad?, ¿sus **transferencias internacionales** cumplen? Los
hallazgos se trasladan al SPA (declaraciones y garantías de datos, indemnización, condiciones de
remediación). El **compliance de datos** (mapeo, políticas, PIA, respuesta a brechas, contratos de encargo)
es parte del gobierno corporativo moderno. Conéctalo con
[Due Diligence (IV-02)](../Nivel-IV-Corporate-Law/02-Due-Diligence.md) y con
[Compliance (06)](./06-Derecho-Penal-Economico-y-Compliance.md).


## 15. Explicación intuitiva (el modelo mental)

Piensa en los datos como algo que **prestas, no regalas**. Cuando das tu información a una empresa, es como
prestarle tus llaves para un uso concreto: puede usarlas **solo para eso** (finalidad), debe **cuidarlas**
(seguridad), avisarte si va a **dárselas a alguien más** (transferencia) y **devolvértelas o botarlas** si
lo pides (ARCO). La empresa es la **custodia** de algo que sigue siendo, en control, tuyo.

Segundo modelo, el del **"ciclo de vida del dato"**: cada dato entra (recolección → base legal + aviso),
se usa (finalidad + proporcionalidad), se comparte (transferencia/remisión + contrato), se guarda
(seguridad) y sale (cancelación/olvido). El compliance de datos consiste en **controlar cada etapa de ese
ciclo**. El abogado de privacidad **mapea el ciclo** y pone controles en cada punto.

## 16. Ejemplos simples

1. **Marketing sin consentimiento.** Una empresa usa correos de clientes para publicidad sin avisarlo →
   viola finalidad e información (aviso de privacidad) ⚠️.
2. **Dato sensible sin consentimiento expreso.** Recabar datos de salud sin consentimiento **por escrito**
   → incumplimiento agravado ⚠️.
3. **Brecha de seguridad.** Un hackeo expone datos de clientes → deber de **notificar** y remediar ⚠️.

## 17. Ejemplos complejos (multivariable)

**La app con base de datos "sucia".** Un fondo evalúa comprar una app con 5 millones de usuarios (su activo
estrella). La **DD de datos** revela: (a) el aviso de privacidad no informaba el uso publicitario ni las
transferencias; (b) muchos consentimientos son dudosos; (c) hubo una **brecha** no notificada; (d) transfiere
datos a un proveedor en el extranjero sin contrato de encargo adecuado. Consecuencia: la base de datos —el
activo— tiene **vicios de origen** y contingencias (multas, demandas). Remedio: rehacer avisos y
consentimientos, regularizar transferencias, evaluar la brecha, y trasladar el riesgo al SPA (R&W de datos,
indemnización, condiciones). Un activo "sucio" puede valer mucho menos —o nada—.

**Transferencia internacional a la nube.** Una empresa mexicana usa un proveedor de nube en EE. UU./Europa.
Debe: firmar un **contrato de encargo/remisión** con obligaciones de seguridad y confidencialidad, informar
la transferencia en el **aviso de privacidad**, y —si hay conexión con la UE— cumplir las reglas del
**GDPR** para transferencias internacionales. Ignorarlo genera incumplimiento en varias jurisdicciones.

## 18. Casos reales (estilizados y jurisprudenciales)

- **Multas récord bajo el GDPR (2018+ ⚠️):** sanciones de cientos de millones a grandes tecnológicas por
  bases legales inválidas y transferencias ilícitas —establecieron el estándar global de riesgo—.
- **Brechas masivas de datos:** filtraciones de millones de registros que costaron multas, demandas
  colectivas y colapso reputacional a grandes empresas.
- **Criterios del extinto INAI / autoridad garante:** resoluciones sobre avisos de privacidad,
  consentimiento y derechos ARCO. ⚠️ *Verificar autoridad y criterios vigentes.*

## 19. Casos empresariales

Una empresa de retail lanza un programa de lealtad y recaba datos masivos sin un aviso de privacidad claro,
los usa para fines no informados y los comparte con socios comerciales sin base. Un titular denuncia. La
empresa enfrenta un procedimiento sancionador y una crisis de confianza. El remedio (implementar avisos
correctos, mapear datos, contratos con terceros, política de seguridad) llega bajo presión. Lección: el
**compliance de datos temprano** —barato— evita la **sanción y la crisis** —caras—.

## 20. Casos corporativos (en transacciones)

En M&A tecnológico y de consumo, los datos son a menudo **el activo**. La **DD de datos** verifica licitud
de la base, avisos, consentimientos, seguridad, brechas, transferencias y contingencias con la autoridad.
Sus hallazgos determinan el **precio** (una base lícita y bien documentada vale; una contaminada, no) y las
**cláusulas** del SPA (declaraciones y garantías de datos, indemnización, condiciones de remediar). En
integraciones post-cierre, combinar bases de datos de dos empresas exige cuidar las **finalidades** y bases
legales originales (no se pueden "mezclar" datos libremente). Conéctalo con
[Documentación (IV-04)](../Nivel-IV-Corporate-Law/04-Documentacion-Term-Sheet-SPA-APA-SHA.md).

## 21. Casos internacionales (*cross-border*)

El **GDPR** europeo es **el estándar global** y tiene **alcance extraterritorial**: se aplica a empresas de
cualquier país que ofrezcan bienes/servicios o monitoreen a personas en la **UE**, con multas de hasta un
porcentaje de la **facturación mundial** ⚠️. Además, las **transferencias internacionales** de datos están
muy reguladas (decisiones de adecuación, cláusulas contractuales tipo). Para el corporativo cross-border,
esto significa que una empresa mexicana con clientes o proveedores europeos puede quedar sujeta al GDPR, y
que estructurar los **flujos internacionales de datos** (dónde se alojan, quién los procesa) es un tema
central de compliance y de M&A global. ⚠️ *Verificar marcos aplicables.*


## 22. Derecho comparado

- **Unión Europea (GDPR):** el estándar mundial; derechos fuertes (acceso, olvido, portabilidad), *privacy
  by design*, evaluaciones de impacto, notificación de brechas, y **multas de hasta % de facturación
  global**; alcance **extraterritorial**.
- **Estados Unidos:** mosaico **sectorial** (salud —HIPAA—, financiero, menores) y estatal (California
  **CCPA/CPRA**); no hay una ley federal general única. ⚠️
- **América Latina:** varios países siguieron el modelo GDPR (Brasil **LGPD**, etc.).
- **México:** modelo de **ley general** para el sector privado (LFPDPPP) influido por Europa; con la
  extinción del INAI, la **arquitectura institucional** está en transición. ⚠️

## 23. Derecho mexicano (régimen positivo)

- **Constitucional:** arts. 6 y 16 ⟳ (acceso a la información y protección de datos/autodeterminación
  informativa) ⚠️.
- **Sector privado:** **LFPDPPP (nueva ley vigente DOF 14-11-2025 ✅; sustituyó a la de 2010 ⟳)** y su **Reglamento**; lineamientos del aviso de privacidad y de
  seguridad.
- **Sector público:** ley de protección de datos de **sujetos obligados**.
- **Autoridad:** históricamente el **INAI** (extinto en la reforma 2024-2025 ⚠️); funciones reasignadas a
  la nueva estructura —**verificar**—.
- **Conexos:** delitos informáticos (CPF), ciberseguridad, y regulación sectorial (financiera, salud,
  telecom). ⚠️ *Verificar vigencia y autoridad.*

## 24. Jurisprudencia relevante

Líneas para estudiar y **verificar en el SJF** y en criterios de la autoridad garante:
- **Alcance del dato personal** e **identificabilidad**.
- **Validez del consentimiento** y suficiencia del **aviso de privacidad**.
- **Datos sensibles** y consentimiento expreso por escrito.
- **Derechos ARCO** y plazos de atención.
- **Ponderación** entre protección de datos, acceso a la información y libertad de expresión.

> ⚠️ **Advertencia de integridad (Protocolo):** verifica montos de multas, plazos y criterios en el texto
> vigente (LFPDPPP/Reglamento) y ante la autoridad garante vigente (tras la extinción del INAI).

## 25. Criterios de la Suprema Corte y de la autoridad garante

La SCJN ha desarrollado la **autodeterminación informativa** como derecho autónomo y su **ponderación** con
el acceso a la información y la libertad de expresión. La autoridad garante (INAI y ahora su sucesora ⚠️)
genera criterios prácticos sobre avisos, consentimiento, ARCO y sanciones. La **transición institucional**
tras 2024 generará nuevos criterios —a **verificar**—. ⚠️

## 26. Doctrina nacional

- **Autores mexicanos de derecho a la información y protección de datos** (obra generada en torno al
  IFAI/INAI y a la academia).
- **Comentarios a la LFPDPPP y su Reglamento** de despachos especializados en privacidad.
⚠️ *Verificar ediciones y su actualización tras la reforma 2024-2025.*

## 27. Doctrina internacional

- **Alan Westin, *Privacy and Freedom*.** Fundamento del concepto moderno de privacidad como control.
- **Ann Cavoukian**, *Privacy by Design*.
- **Comentarios y guías del Comité Europeo de Protección de Datos (EDPB)** sobre el **GDPR**. Referencia
  global.
- **Literatura sobre datos, IA y vigilancia** (el debate contemporáneo sobre poder e información).

## 28. Opiniones críticas (postura del Consejo)

Nuestra postura: la protección de datos es un derecho **cada vez más central** en la economía digital, y su
cumplimiento pasó de "buena práctica" a **riesgo material** (multas, brechas, reputación). Para el
corporativo, el mensaje es doble: (1) tratar los datos como **activo y pasivo a la vez** —cuidarlos crea
valor y confianza; descuidarlos crea contingencias explosivas—; y (2) construir **compliance de privacidad
genuino** (mapeo, avisos, seguridad, respuesta a brechas), no de papel. Vemos con preocupación la
**extinción del INAI**: la protección de datos requiere una autoridad **técnica e independiente**, y su
debilitamiento eleva la incertidumbre. La recomendación práctica: aun con la transición institucional, los
**deberes subsisten** —cumplir el estándar (idealmente alineado al GDPR) protege a la empresa sin importar
qué autoridad lo vigile—.

## 29. Debate doctrinal (controversias vivas)

- **Extinción del INAI:** ¿quién garantiza la protección de datos con independencia técnica? ⚠️
- **IA y datos:** perfilamiento, decisiones automatizadas y entrenamiento de modelos con datos personales.
- **Derecho al olvido vs. libertad de información:** hasta dónde borrar información pública.
- **Transferencias internacionales:** soberanía de datos vs. economía global de la nube.
- **Datos biométricos y de menores:** nivel de protección reforzada necesario.


## 30. Errores comunes

1. **No tener (o tener mal) el aviso de privacidad.** El incumplimiento más frecuente y sancionado.
2. **Usar datos para fines no informados** (violar la **finalidad**), p. ej. reutilizar datos de un
   servicio para marketing sin base.
3. **Recabar datos sensibles sin consentimiento expreso por escrito** ⚠️.
4. **No firmar contrato de encargo** con proveedores que procesan datos (nube, marketing, cobranza).
5. **No tener plan de respuesta a brechas** (ni notificación) → la crisis se agrava.
6. **Transferir datos al extranjero** sin base ni cláusulas adecuadas (riesgo GDPR).
7. **Comprar una empresa cuya base de datos es "sucia"** sin DD ni protección contractual.

## 31. Mitos frecuentes

- *"Los datos que recabo son míos."* **Falso:** eres **custodio/responsable**; el control es del titular.
- *"Si el usuario aceptó los términos, puedo usar sus datos para lo que sea."* **Falso:** rige la
  **finalidad** informada.
- *"Una brecha se maneja en silencio."* **Riesgoso:** hay **deber de notificar** y el silencio agrava el
  daño ⚠️.
- *"El GDPR no me aplica porque estoy en México."* **Falso:** aplica si ofreces bienes/servicios o
  monitoreas a personas en la UE.
- *"Con la desaparición del INAI ya no hay obligaciones."* **Falso:** los deberes **subsisten**; cambia la
  autoridad ⚠️.

## 32. Preguntas difíciles

1. ¿Quién es el "dueño" de los datos: la persona o la empresa que los recaba? ¿Qué significa "control"?
2. ¿Cómo concilias el **derecho al olvido** con la **libertad de información**?
3. ¿Puede entrenarse una **IA** con datos personales? ¿Bajo qué condiciones? ⚠️
4. Con el **INAI extinto**, ¿cómo cambia tu estrategia de compliance y de defensa? ⚠️
5. ¿Cuándo una empresa mexicana queda sujeta al **GDPR** europeo?

## 33. Casos de examen (con respuesta modelo)

**Caso.** Un fondo evaluará comprar una fintech con 2 millones de usuarios (datos financieros y de
identidad). Como su abogado, ¿qué revisas de datos y qué exiges?

**Respuesta modelo.** **DD de datos**: (1) **avisos de privacidad** y **consentimientos** (expresos, por ser
datos **financieros**) ⚠️; (2) **licitud** de la base y su **transferibilidad**; (3) **medidas de
seguridad** y **ciberseguridad**; (4) historial de **brechas** y su notificación; (5) **transferencias**
(nube, terceros) y contratos de encargo; (6) contingencias/procedimientos con la autoridad garante; (7)
si aplica el **GDPR** (usuarios en la UE). Exigencias como **condición de cierre**: regularizar avisos y
consentimientos, contratos de encargo, plan de brechas; y **declaraciones y garantías de datos**,
indemnización y **escrow** por contingencias. Verifica autoridad y montos vigentes ⚠️.

## 34. Simulador (ejercicio tipo despacho)

> **Rol:** asociado de privacidad/corporativo. **Cliente:** una startup que lanzará una app con datos de
> salud (sensibles) y usuarios en México y España. **Tarea:** entrega en una cuartilla (a) el **mapa de
> datos** y sus bases legales; (b) el **aviso de privacidad** y el tipo de **consentimiento** requerido
> (sensibles → expreso por escrito); (c) las medidas de **seguridad** y el **plan de respuesta a brechas**;
> (d) el análisis de **GDPR** por los usuarios en España y las **transferencias internacionales**. Marca ⚠️
> lo que debas verificar (autoridad, montos, plazos).

## 35. Flashcards

- **P:** ¿Dato personal? · **R:** Información concerniente a una **persona física identificada o
  identificable**.
- **P:** ¿Dato sensible? · **R:** El de la esfera íntima o de riesgo de discriminación (salud, biométricos,
  orientación); consentimiento **expreso por escrito** ⚠️.
- **P:** ¿Derechos ARCO? · **R:** **A**cceso, **R**ectificación, **C**ancelación, **O**posición.
- **P:** ¿Responsable vs. encargado? · **R:** Quien **decide** el tratamiento vs. quien lo procesa **por
  cuenta** del responsable.
- **P:** ¿Documento clave de información al titular? · **R:** El **aviso de privacidad**.
- **P:** ¿Estándar global de referencia? · **R:** El **GDPR** europeo (extraterritorial; multas por % de
  facturación) ⚠️.
- **P:** ¿Qué pasó con el INAI? · **R:** Se **extinguió** (reforma 2024-2025); funciones reasignadas ⚠️.
- **P:** ¿Ley del sector privado en México? · **R:** La **LFPDPPP** ⚠️.

## 36. Mapa mental

```
PROTECCIÓN DE DATOS PERSONALES (arts. 6 y 16 CPEUM ✅ · LFPDPPP)
├── QUÉ: dato personal / dato SENSIBLE (protección reforzada)
├── QUIÉN: titular · RESPONSABLE · encargado
├── PRINCIPIOS: licitud · consentimiento · información · calidad · finalidad · lealtad · proporcionalidad · responsabilidad
├── DEBERES: aviso de privacidad · seguridad · confidencialidad
├── DERECHOS: ARCO (+ portabilidad/olvido ⚠️) · revocación
├── TRANSFERENCIAS: nacional/internacional · remisión (encargado, contrato)
├── SEGURIDAD y BRECHAS: medidas · notificación · ciberseguridad
├── AUTORIDAD: INAI (extinto 2024-25 ⚠️) → sucesora · sanciones
└── EN M&A: DD de datos (¿base lícita, segura, transferible?) → R&W + indemnización
```

## 37. Cuadros comparativos

| Criterio | **Dato personal** | **Dato sensible** |
|----------|-------------------|-------------------|
| Ejemplos | Nombre, correo, teléfono | Salud, biométricos, orientación, creencias |
| Consentimiento | Tácito/expreso | **Expreso y por escrito** ⚠️ |
| Protección | Estándar | Reforzada |

| Criterio | **Responsable** | **Encargado** |
|----------|-----------------|---------------|
| Rol | **Decide** el tratamiento | Procesa **por cuenta** del responsable |
| Instrumento | Aviso de privacidad | **Contrato de encargo** |

| Criterio | **México (LFPDPPP)** | **UE (GDPR)** |
|----------|----------------------|---------------|
| Alcance | Nacional | Extraterritorial |
| Multas | En UMA ⚠️ | % de facturación global ⚠️ |
| Derechos | ARCO | ARCO + portabilidad + olvido |

## 38. Diagramas (ciclo de vida del dato)

```
RECOLECCIÓN (base legal + aviso de privacidad + consentimiento)
      │
USO (solo la FINALIDAD informada + proporcionalidad)
      │
COMPARTIR (transferencia/remisión + contrato de encargo)
      │
GUARDAR (seguridad + confidencialidad) ──(brecha)──► CONTENER + NOTIFICAR + REMEDIAR ⚠️
      │
SALIDA (cancelación / oposición / olvido — derechos ARCO)
```

## 39. Mnemotecnias

- **Derechos — "ARCO"**: **A**cceso · **R**ectificación · **C**ancelación · **O**posición.
- **"Los datos se prestan, no se regalan"** (el control sigue en el titular).
- **Sensibles = expreso + por escrito.**
- **Responsable decide, encargado ejecuta** (por contrato).
- **"Aviso + consentimiento + finalidad + seguridad"** = las 4 columnas del cumplimiento.


## 40. Resumen ejecutivo

La protección de datos personales garantiza la **autodeterminación informativa**: el control de la persona
sobre su información (base constitucional en los arts. 6 y 16 ✅ ⟳; ley del sector privado: **LFPDPPP**).
Impone al **responsable** deberes: respetar los **principios** (licitud, consentimiento, información,
calidad, finalidad, lealtad, proporcionalidad, responsabilidad), informar mediante **aviso de privacidad**,
obtener **consentimiento** (expreso y por escrito para datos **sensibles**), atender los **derechos ARCO**,
regular las **transferencias** y garantizar la **seguridad** (con deber de responder y notificar **brechas**).
El estándar global es el **GDPR** europeo (extraterritorial, multas por % de facturación). En México, la
**reforma 2024-2025 extinguió al INAI** y reasignó sus funciones ⚠️: los deberes subsisten, cambia la
autoridad. Para el corporativo, los datos son **activo y pasivo**: la **due diligence de datos** y las
declaraciones y garantías de datos son centrales en M&A tecnológico y de consumo.

## 41. Checklist del profesional

- [ ] ¿Hay **aviso de privacidad** correcto (integral/simplificado) y **consentimiento** válido?
- [ ] ¿El tratamiento respeta la **finalidad** informada y la **proporcionalidad**?
- [ ] ¿Los **datos sensibles/financieros** tienen consentimiento **expreso/por escrito**? ⚠️
- [ ] ¿Hay **contratos de encargo** con proveedores que procesan datos (nube, etc.)?
- [ ] ¿Están reguladas las **transferencias** (nacionales e internacionales; GDPR si aplica)?
- [ ] ¿Hay **medidas de seguridad** y **plan de respuesta a brechas** (con notificación)?
- [ ] ¿Existe un procedimiento para atender **derechos ARCO** en plazo?
- [ ] En M&A: ¿hice **DD de datos** (licitud/transferibilidad de la base) y trasladé el riesgo al SPA?
- [ ] ¿Verifiqué **autoridad, montos y plazos** vigentes (tras la extinción del INAI)? ⚠️

## 42. Bibliografía comentada

- **Westin, *Privacy and Freedom*.** El fundamento del concepto de privacidad como control.
- **Cavoukian, *Privacy by Design*.** El principio de privacidad desde el diseño.
- **Guías del EDPB sobre el GDPR.** Referencia global imprescindible (bases legales, transferencias,
  brechas).
- **Comentarios a la LFPDPPP y su Reglamento** de despachos especializados (cotejar con la reforma
  2024-2025 ⚠️).
- **Textos vigentes (obligatorio):** **CPEUM arts. 6 y 16 ⟳**, **LFPDPPP** y su **Reglamento**, lineamientos
  vigentes, en el **DOF**; y el **GDPR** para lo internacional. ⚠️ *Verifica la autoridad garante vigente.*

## 43. Ruta hacia el siguiente libro

Con la protección de datos dominada, cierras el círculo del **riesgo digital**. Continúa con el
[**Derecho Ambiental (Ramas Esenciales · 10)**](./10-Derecho-Ambiental.md), otro pasivo oculto que estalla
en la due diligence industrial. Este libro se conecta con la
[**Propiedad Intelectual (07)**](./07-Propiedad-Intelectual.md) (los datos como activo), con el
[**Compliance penal (06)**](./06-Derecho-Penal-Economico-y-Compliance.md), con el
[**Administrativo (03)**](./03-Derecho-Administrativo.md) (la autoridad garante) y con la
[**Due Diligence (IV-02)**](../Nivel-IV-Corporate-Law/02-Due-Diligence.md) en M&A tecnológico.

---

## ✦ ¿Por qué esto importa para un abogado corporativo?

Porque en la economía digital **los datos son, a la vez, el activo más valioso y el pasivo más explosivo**
de muchas empresas. El corporativo que domina la protección de datos (1) **verifica** en la due diligence
si la base de datos —a menudo el activo estrella de una fintech, una app o un retailer— es **lícita, segura
y transferible**; (2) construye el **compliance de privacidad** (avisos, consentimientos, seguridad,
contratos de encargo, plan de brechas) que protege a la empresa de multas y crisis; (3) estructura las
**transferencias internacionales** (crítico si hay nexo con la UE y el GDPR); y (4) traslada el riesgo de
datos al **contrato** (declaraciones y garantías, indemnización). Ignorar los datos en un *deal* tecnológico
es comprar un activo que puede estar **contaminado de origen** —y una contingencia regulatoria que crece
cada año—.

## ✦ Cómo piensa un socio de un despacho internacional

Un socio de privacidad/tecnología de las áreas de datos de firmas globales (**Baker McKenzie**, **Hogan
Lovells**) o de despachos mexicanos especializados piensa la protección de datos como **gestión de riesgo
del ciclo de vida del dato**: mapea qué datos entran, cómo se usan, con quién se comparten y cómo se
protegen, y pone controles en cada punto. Trabaja con el estándar **más alto** (el GDPR) como referencia,
porque protege a la empresa sin importar la jurisdicción y porque muchos clientes tienen exposición europea.
En M&A, su reflejo es la **DD de datos**: nunca deja que su cliente compre una base "sucia" sin
declaraciones, indemnización y remediación. Y ante una **brecha**, activa un protocolo de crisis (contener,
evaluar, notificar, comunicar) sabiendo que la **rapidez y la transparencia** definen si el incidente es
manejable o catastrófico.

## ✦ Errores que cuestan millones

- **Base de datos "sucia" no detectada en DD:** comprar como activo estrella una base con avisos/
  consentimientos inválidos o una brecha no notificada —contingencia de multas y demandas—.
- **Brecha mal gestionada:** no contener ni notificar a tiempo → sanción agravada y colapso reputacional.
- **Ignorar el GDPR** teniendo usuarios en la UE: exposición a multas por porcentaje de la **facturación
  global**.
- **Transferencias internacionales sin base** (nube, proveedores extranjeros) sin contratos ni cláusulas
  adecuadas.
- **Reutilizar datos para fines no informados** (violar la finalidad), p. ej. tras una fusión mezclar bases
  sin base legal.

## ✦ Nivel de importancia profesional

```
Litigio              ★★★☆☆
Corporate            ★★★★☆
M&A                  ★★★★☆
Mercado de Valores   ★★★☆☆
Venture Capital      ★★★★☆
Private Equity       ★★★☆☆
Gobierno Corporativo ★★★★☆
Compliance           ★★★★★
Derecho Bancario     ★★★★☆
Empresa Familiar     ★★☆☆☆
```

---

> **Cierre.** La protección de datos es el derecho que da a las personas **control sobre su información** y
> a las empresas el deber de cuidarla. Domínala y sabrás proteger —y valuar— uno de los activos centrales de
> la economía digital. Recuerda el Principio Supremo: con la **extinción del INAI** y la evolución
> constante (IA, GDPR), **verifica la ley, la autoridad y los montos vigentes** antes de aconsejar.

*Tratado del Proyecto AJE · Ramas Esenciales · Libro 9 · Estándar V3. Contenido conceptual a 2026-07;
verifica todo artículo, monto, plazo y la autoridad garante vigente contra su texto vigente (LFPDPPP y
Reglamento) tras la reforma de simplificación orgánica 2024-2025.*


---

## ⚖️ Suplemento del Consejo Editorial

> *Elevación al estándar de obra de referencia. Doctrina, comparado, caso y criterio; disciplina ⟳.*

### Cómo piensa un socio internacional
Los datos son **activo y pasivo** a la vez: valen (la empresa vive de ellos) y arriesgan (una brecha o una sanción hunden la valuación). En M&A, el socio hace ***privacy due diligence***: ¿la empresa trata datos con base legal?, ¿hubo brechas?, ¿puede transferir la base de datos al comprador? Comprar una empresa de datos sin revisar su cumplimiento es heredar una bomba regulatoria.

### Doctrina y debate
- **Privacidad como derecho:** Warren & Brandeis (*The Right to Privacy*, 1890, "el derecho a ser dejado en paz") y la **autodeterminación informativa** (Tribunal Constitucional alemán, sentencia del censo, 1983).
- **Debate:** ¿consentimiento (modelo clásico) o **responsabilidad proactiva** (*accountability*, *privacy by design*) del GDPR? El consentimiento "de casilla" está en crisis.

### Derecho comparado
El **GDPR** europeo (2018) es el estándar global (extraterritorial, multas de hasta 4% de la facturación mundial). EE. UU. carece de ley federal única (modelo sectorial + CCPA en California). México: **nueva LFPDPPP (2025)** ⟳ con autoridad en la **Secretaría Anticorrupción y Buen Gobierno**.

### Caso real
**Cambridge Analytica / Facebook (2018):** uso indebido de datos de ~87 millones de usuarios ⚠️ *verificar*; costó a Meta una multa de **5,000 mdd** de la FTC y daño reputacional histórico. **Multas GDPR a Meta/Amazon** (cientos de millones de euros). Lección: los datos mal gobernados son el nuevo pasivo ambiental de la economía digital.

### Errores que cuestan millones
- Transferir una base de datos en un *deal* **sin base legal** para el nuevo tratamiento.
- No tener **plan de respuesta a brechas** ni *privacy by design*.

### Preguntas
- **Criterio:** ¿el consentimiento sigue siendo un modelo viable o debe regir la *accountability*?
- **Entrevista:** ¿qué revisa en un *privacy due diligence*?
- **Examen:** explique la autodeterminación informativa.

### Bibliografía por niveles
- **Básico:** LFPDPPP (2025) y su Reglamento.
- **Intermedio:** GDPR (texto y guías del CEPD).
- **Avanzado:** Solove, *Understanding Privacy*.
- **Internacional:** Warren & Brandeis, *The Right to Privacy* (Harvard Law Review, 1890).
