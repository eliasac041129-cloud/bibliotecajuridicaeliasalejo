# Tablero semanal

### Las trece variables, medidas cada domingo

> **Cuándo se abre:** domingo por la noche, después de la revisión de fechas del
> [sistema antifallas](./04_SISTEMA_ANTIFALLAS.md) §V. Doce minutos.
>
> El §XXVIII.12 pide poder medir cada semana trece cosas. Aquí están las trece, con la regla que las
> hace útiles: **se registra lo que pasó, no lo que se pretendía.** Un tablero maquillado es peor que
> no tener tablero, porque produce la sensación de control sin el control.

---

## I. La plantilla

Se copia cada semana. Se llena a mano o en el repositorio; si es en el repositorio, termina en
`git commit` — así queda constancia fechada, como los 28 commits de la Edición Final.

```
════════════════════════════════════════════════════════════════════
  SEMANA DEL ______________ AL ______________          Nº ____
════════════════════════════════════════════════════════════════════

 1. FECHAS
    Próxima irrecuperable: ____________________  faltan ____ días
    ¿Está hecha o en curso?                            [ ] sí  [ ] no
    ¿Alguna fecha cambió esta semana?                  [ ] sí  [ ] no
    ¿Decidí algo sobre una línea ⛔ FALTA?             [ ] sí  [ ] NO ←debe ser NO

 2. MATERIAS
    Materia foco de la semana: ____________________
    Bloques de 90 min cumplidos:        ___ / 5
    Bloques de 75 min cumplidos:        ___ / 5
    Horas de estudio profundo:          ___ h    (meta 16)

 3. CALIFICACIONES
    Exámenes / entregas esta semana: ____________________
    Resultado: ____________________

 4. ASISTENCIA
    Clases perdidas: ___    Motivo: ____________________

 5. SUEÑO ← la variable que sostiene el resto
    Noches dormido antes de 21:30:      ___ / 7
    Hora más tardía: ______   Hora media de despertar: ______

 6. EJERCICIO
    Sesiones:  ___ / 3        ¿Rutina escrita antes de entrar?  [ ] sí

 7. INGLÉS  (traslado de ida)
    Días con 40 min de audio:           ___ / 5
    Actividad de la semana (rotación de la Columna II): ____________

 8. REPASO
    Días de Anki en el traslado:        ___ / 5
    Tarjetas nuevas añadidas: ___

 9. TESIS
    Sesiones (martes/jueves):           ___ / 2
    Producto verificable: ____________________
    ¿Quedó texto redactado, no solo fichas?            [ ] sí  [ ] no

10. INGLÉS/SERVICIO/TRÁMITES — avance administrativo
    Trámite movido esta semana: ____________________
    Siguiente paso concreto:    ____________________

11. DINERO
    Ingresos: ______   Gastos: ______   ¿Todo registrado?  [ ] sí

12. RELACIONES
    Días con los 45 min protegidos:     ___ / 5
    ¿Miros conoce las 3 fechas del mes?               [ ] sí
    Tiempo con familia: ____________________

13. VIDA ESPIRITUAL
    Iglesia domingo:                                   [ ] sí
    Días de oración (anclada a 4:45 / 21:00):  ___ / 7

────────────────────────────────────────────────────────────────────
 CONDUCTA DEL MES (de 08_FORMACION_DEL_HOMBRE): ________________
 Días cumplida: ___ / 7

 DÍAS SIN CERO:  ___ / 7        ← la única cifra que no puede bajar de 6
 ¿Dos días seguidos en cero?    [ ] sí ← si es sí, ver protocolo de recaída

────────────────────────────────────────────────────────────────────
 LO QUE ME FRENÓ ESTA SEMANA (una línea, sin adjetivos):
 ____________________________________________________________

 EL AJUSTE PARA LA PRÓXIMA (uno, concreto):
 ____________________________________________________________
════════════════════════════════════════════════════════════════════
```

---

## II. Las tres cifras que importan

Trece variables son demasiadas para vigilar de continuo. Si una semana solo hay tiempo para mirar tres:

| Cifra | Meta | Por qué esta |
|---|---|---|
| **Días sin cero** | ≥ 6 de 7 | Es el indicador adelantado de todo. Cae antes de que caigan las calificaciones |
| **Noches dormido antes de 21:30** | ≥ 6 de 7 | Es la causa, no el efecto. Cuando esta baja, las otras doce bajan la semana siguiente |
| **Casilla 1.4 en NO** | Siempre NO | Es la única que protege de un daño irreversible |

Las otras diez describen. **Estas tres predicen.**

---

## III. Cómo se lee el tablero

**Una semana mala no es información.** Todo el mundo tiene semanas malas y reaccionar a una es la forma
más rápida de abandonar el sistema. No se hace nada.

**Dos semanas iguales sí lo son.** Ahí hay un patrón, y se corrige **una sola cosa** — la que está más
arriba en la cadena causal, que casi siempre es el sueño.

**Tres semanas iguales significan que el sistema está mal diseñado, no que falte esfuerzo.** Esta es la
regla más importante del documento y contradice el instinto: si algo falla tres semanas seguidas, no hay
que esforzarse más. Hay que **cambiar el diseño**, porque un sistema que exige heroísmo semanal ya
falló. Se relee [`03_DIAGNOSTICO_DE_EJECUCION.md`](./03_DIAGNOSTICO_DE_EJECUCION.md) §II y se rediseña
el bloque que no aguanta.

### El diagnóstico rápido por patrón

| Lo que muestra el tablero | Causa probable | Dónde se arregla |
|---|---|---|
| Bloques cumplidos pero calificaciones malas | Método, no cantidad | [`GUIA-METODOLOGICA.md`](../GUIA-METODOLOGICA.md) |
| Bloque 1 sí, Bloque 2 no | Gimnasio comiendo la noche, o cansancio acumulado | [`05`](./05_SISTEMA_SEMANAL_Y_DIARIO.md) §IV |
| Inglés y Anki en cero | No se está usando el traslado. **15 h semanales perdidas** | [`05`](./05_SISTEMA_SEMANAL_Y_DIARIO.md) §II |
| Tesis en cero tres semanas | Falta la fecha externa: el tema no está registrado | [`07`](./07_PLAN_DE_TESIS.md) §V |
| Sueño bajo y todo lo demás bajo | Es la causa raíz. No tocar nada más | [`05`](./05_SISTEMA_SEMANAL_Y_DIARIO.md) §III |
| Todo cumplido salvo trámites | El patrón conocido: lo administrativo se evita | [`03`](./03_DIAGNOSTICO_DE_EJECUCION.md) §II |
| Se leyó biblioteca sin atarla a examen/tesis | La biblioteca volvió a ser procrastinación | [`06`](./06_RUTA_DE_LA_BIBLIOTECA.md) §VII |

---

## IV. La revisión de los 90 días

Cada doce semanas se miran los doce tableros juntos. No las cifras de una semana: **la tendencia.**

- ¿Los días sin cero subieron, bajaron o se mantuvieron?
- ¿Cuántas fechas irrecuperables se cumplieron **sin** depender de la memoria?
- ¿La conducta del mes se sostuvo cuando llegó la siguiente?
- ¿Qué se abandonó primero cuando apretó la semana? **Eso es el punto débil real del sistema**, y es
  más informativo que cualquier meta.

Y la pregunta que decide si el proyecto está funcionando de verdad:

> **¿El expediente académico de estas doce semanas es mejor que el de las doce anteriores?**

No "me siento mejor organizado". Materias, calificaciones, trámites movidos. El
[diagnóstico](./03_DIAGNOSTICO_DE_EJECUCION.md) §IV dice que lo único recuperable es la **tendencia**;
esta es la medición de la tendencia, y es lo que un despacho va a leer en el historial.

---

*La revisión de hábitos de estudio, inglés y Laboratorio ya existe en la
[Columna II](../Columna-II-Hoja-de-Ruta/02_PLAN_OPERATIVO_DIARIO_AJE.md) §VIII–IX y no se duplica: este
tablero la absorbe y le añade las variables que allí no existían — sueño, ejercicio, dinero,
relaciones, vida espiritual y trámites.*
