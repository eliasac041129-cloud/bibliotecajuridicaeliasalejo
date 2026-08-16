# tools/ — Proyecto Remontada

## `promedio.py`

Calculadora de promedio y techo alcanzable. Contesta el §XIV.4 del encargo, que exige números y
prohíbe expresamente prometer un promedio matemáticamente imposible.

```bash
python3 tools/promedio.py --autotest              # verifica la aritmética (10 pruebas)
python3 tools/promedio.py --plantilla > historial.csv
python3 tools/promedio.py historial.csv --meta 8.5
```

### Qué calcula

- **Promedio actual** sobre lo ya acreditado.
- **Escenarios** con calificación supuesta 6, 7, 8, 9 y 10 en todo lo pendiente.
- **Techo matemático**: el promedio final si se sacara 10 en absolutamente todo lo que falta. Si la
  meta declarada lo supera, el programa lo dice y **se niega a validarla**.
- **Calificación media requerida** para alcanzar una meta, por búsqueda binaria.
- **Ranking de impacto**: cuánto sube el promedio final subir cada pendiente de 8 a 10, ponderado por
  créditos.
- **Alerta de oportunidades agotadas** para las materias con 2 o más intentos.

### Las dos decisiones que no puede inventar

El resultado cambia según dos reglas que están en `REGLAMENTO EXTRAORDINARIOS.pdf` y en el Reglamento
General de Exámenes, y que el programa **no supone**:

1. **¿La calificación reprobada sigue contando en el promedio después de aprobar la materia?**
   → `--reprobadas {ignora,cuenta}`
2. **¿El promedio se pondera por créditos o es media simple?**
   → `--ponderacion {creditos,simple}`

Por defecto calcula **las cuatro combinaciones** y advierte que ninguna cifra es definitiva hasta
confirmarlas. Es la aplicación del
[Principio 1](../../00_DOCUMENTO_FUNDACIONAL_AJE.md): antes que dar un número cómodo, dar el rango
honesto.

### Formato del CSV

```csv
clave,materia,creditos,calificacion,estado,intentos
1101,Derecho Romano,8,9,acreditada,1
1203,Obligaciones,10,5,reprobada,2
1204,Sociedades Mercantiles,10,,pendiente,0
```

`estado`: `acreditada` · `reprobada` · `pendiente`. Las líneas que empiezan con `#` se ignoran.

Si alguna fila tiene un error, el programa **no calcula nada** y lo enumera. Un promedio calculado
sobre datos dudosos es peor que ningún promedio.

### Nota sobre datos personales

Este repositorio es público. Conviene llenar el CSV **sin** número de cuenta ni nombre: la calculadora
solo necesita clave, créditos, calificación, estado e intentos. Ver
[`documentos/README.md`](../documentos/README.md).
