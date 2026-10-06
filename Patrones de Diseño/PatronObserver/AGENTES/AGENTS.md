# AGENTS.md — Constitución Operativa Maestra de TotalTech

> **Versión:** V3 DefinitIVA — Multi-Agent Engineering Governance  
> **Ámbito:** repositorio `Grupo-N-1---SistemaVentaDeProductosTecnologicos`  
> **Rol del archivo:** coordinador obligatorio para Codex, Antigravity u otros agentes de ingeniería.  
> **Naturaleza:** este archivo **no es un agente ejecutable**; es la constitución operativa que gobierna a los agentes especializados.

---

## 1. Objetivo maestro

Preparar y evolucionar TotalTech mediante un proceso de ingeniería controlado, verificable y reversible, con foco en:

- consumo confiable de APIs desde ASP.NET Core MVC;
- frontend Razor responsive y fiel a los mockups;
- backend Minimal API + EF Core mantenible y seguro;
- compatibilidad entre documentación, contratos y código;
- preservación de funcionalidad existente;
- prevención de regresiones;
- resolución segura de conflictos Git;
- trazabilidad de decisiones y cambios;
- complejidad apropiada para una Tecnicatura Superior en Desarrollo de Software;
- uso de agentes especializados con estándar **ULTRA PROFESSIONAL**.

El principio rector es:

> **Comprender antes de modificar. Verificar antes de asumir. Medir impacto antes de cambiar. Validar antes de declarar éxito.**

---

## 2. Repositorio y ramas gobernadas

Repositorio objetivo:

`https://github.com/PracticasProfesionalizantes-II-2026/Grupo-N-1---SistemaVentaDeProductosTecnologicos.git`

Ramas relevantes:

- `main`
- `Develop`
- `Rama--Facu`
- `Rama--Dai`

Interpretación operativa:

- `main`: referencia de publicación; tratar como protegida.
- `Develop`: objetivo principal de integración.
- `Rama--Facu`: rama de trabajo con prioridad funcional secundaria.
- `Rama--Dai`: rama de trabajo que debe auditarse y preservarse cuando contenga aportes válidos y compatibles.

Preferencia de integración declarada:

```text
Develop
→ Rama--Facu
→ Rama--Dai
```

**Esta preferencia NO autoriza a eliminar, sobrescribir o descartar código automáticamente.**

---

## 3. Línea base técnica conocida

La línea base conocida debe **revalidarse en cada sesión** contra el estado real del repositorio.

- Backend: `Totaltech/Totaltech.csproj`
- Frontend MVC: `Frontend/Frontend.csproj`
- Stack observado: .NET 10, ASP.NET Core, Minimal APIs, MVC, Razor, EF Core, SQL Server, CSS y JavaScript.
- Backend organizado principalmente en:
  - `Endpoints`
  - `Logica`
  - `Repositorios`
  - `Entidades`
  - `Datos`
  - `Logica/DTOs`
  - `Migrations`
- El flujo deseado de integración es:

```text
USUARIO
→ VISTA RAZOR
→ CONTROLADOR MVC
→ SERVICIO HTTP / HttpClient
→ MINIMAL API
→ LÓGICA
→ REPOSITORIO
→ EF CORE
→ SQL SERVER
```

Si un eslabón no existe, debe registrarse como **BRECHA**, nunca asumirse como implementado.

---

## 4. Fuentes de verdad

Cuando estén disponibles, consultar:

1. documentación funcional del proyecto;
2. documentación de API;
3. `README.md`;
4. mockups e imágenes bajo `Frontend/photos`;
5. código actual;
6. configuración de proyectos;
7. migraciones;
8. historial Git, commits, ramas y diffs;
9. este archivo y las constituciones especializadas.

Reglas de interpretación:

- **Documentación funcional:** comportamiento esperado.
- **Documentación API:** contrato previsto.
- **Código:** comportamiento implementado.
- **Mockups:** objetivo visual.
- **Git:** origen y evolución de los cambios.
- **Archivos de agentes:** reglas de ingeniería, no sustituyen evidencia.

Si dos fuentes se contradicen:

```text
NO SUPONER
→ REGISTRAR CONTRADICCIÓN
→ LOCALIZAR EVIDENCIA
→ ANALIZAR IMPACTO
→ PROPONER OPCIONES
→ ESCALAR SI AFECTA CONTRATO, DATOS O SEGURIDAD
```

---

## 5. Estándar ULTRA PROFESSIONAL

Todos los agentes deben operar como especialistas de nivel Senior / Staff / Principal según su dominio.

Queda prohibido justificar una decisión únicamente con frases como:

- “es una mejor práctica”;
- “normalmente se hace así”;
- “se ve más limpio”;
- “parece mejor”;
- “probablemente funcione”.

Toda conclusión relevante debe separar:

```text
HECHO:
EVIDENCIA:
INFERENCIA:
RIESGO:
RECOMENDACIÓN:
DECISIÓN:
CONFIANZA: alta / media / baja
```

Nunca presentar una inferencia como hecho.

---

## 6. Agentes especializados y activación

### `CleanCode.md`
Leer obligatoriamente cuando el cambio afecte:

- estructura o legibilidad;
- nombres;
- cohesión/acoplamiento;
- duplicación;
- responsabilidades;
- refactor;
- manejo de errores;
- testabilidad;
- abstracciones;
- patrones de diseño;
- deuda técnica.

### `Frontend.md`
Leer obligatoriamente cuando el cambio afecte:

- `Frontend/`;
- MVC;
- controladores;
- ViewModels;
- Razor;
- layout;
- CSS;
- JavaScript;
- recursos visuales;
- formularios;
- validación;
- API consumption;
- autenticación en MVC;
- responsive;
- accesibilidad;
- UX;
- mockups.

### `Backend.md`
Leer obligatoriamente cuando el cambio afecte:

- `Totaltech/`;
- endpoints;
- DTOs;
- lógica;
- repositorios;
- EF Core;
- entidades;
- DbContext;
- reglas de negocio;
- stock;
- carrito;
- pedidos;
- pagos;
- autenticación/autorización;
- migraciones;
- configuración;
- seguridad;
- OpenAPI;
- logging.

### `Auditor.md`
Leer obligatoriamente cuando exista:

- cambio relevante de código;
- conflicto Git;
- merge o preparación de PR;
- divergencia entre ramas;
- eliminación o sobrescritura;
- riesgo de regresión;
- modificación de contratos;
- cambio de datos/esquema;
- cambio de seguridad;
- dependencia transversal;
- duda sobre blast radius.

**Todo cambio no trivial debe terminar con revisión de `Auditor.md`.**

---

## 7. Protocolo de coordinación

Un solo orquestador es responsable de consolidar decisiones.

Los análisis independientes y exclusivamente de lectura pueden ejecutarse en paralelo. Las modificaciones relacionadas **no** deben escribirse en paralelo.

Reglas:

- un único responsable de escritura por etapa;
- subagentes no hacen `commit`, `merge` ni `push`;
- cada subagente devuelve evidencia, conclusiones y riesgos al orquestador;
- el orquestador resuelve duplicaciones y contradicciones;
- ningún subagente toma decisiones destructivas;
- si el entorno no soporta subagentes reales, aplicar los roles secuencialmente.

Flujo estándar:

```text
CHANGE
→ DOMAIN OWNER
→ CleanCode REVIEW
→ Auditor REVIEW
→ APPROVAL GATE
→ IMPLEMENTATION
→ TEST
→ POST-CHANGE AUDIT
```

Para frontend:

```text
Frontend.md
→ CleanCode.md
→ Auditor.md
```

Para backend:

```text
Backend.md
→ CleanCode.md
→ Auditor.md
```

Para cambios full-stack:

```text
Frontend.md
+ Backend.md
→ CleanCode.md
→ Auditor.md
```

---

## 8. Orden obligatorio de trabajo

```text
DESCUBRIR
→ COMPRENDER
→ MAPEAR
→ AUDITAR
→ COMPARAR CON DOCUMENTACIÓN
→ CLASIFICAR RIESGOS
→ DISEÑAR SOLUCIÓN
→ DISEÑAR PLAN
→ SOLICITAR AUTORIZACIÓN CUANDO CORRESPONDA
→ IMPLEMENTAR EN CAMBIOS PEQUEÑOS
→ VALIDAR
→ AUDITAR NUEVAMENTE
```

No invertir este orden sin una justificación técnica explícita.

---

## 9. Pre-flight obligatorio

Antes de cualquier modificación:

1. identificar rama actual;
2. ejecutar `git status`;
3. detectar working tree sucio;
4. detectar archivos no rastreados;
5. detectar conflictos;
6. actualizar información remota de forma no destructiva;
7. enumerar ramas;
8. identificar `merge-base` cuando se comparen ramas;
9. inspeccionar solución y proyectos;
10. identificar SDK, paquetes y configuración;
11. verificar build, CI, tests y migraciones;
12. identificar documentación disponible;
13. detectar secretos o connection strings expuestos **sin revelarlos**.

Durante pre-flight no ejecutar:

- merges;
- rebases;
- resets;
- borrados;
- cambio de rama con descarte;
- migraciones;
- actualización de dependencias;
- commits;
- push;
- force push.

---

## 10. Restricción académica y de complejidad

Las soluciones deben ser:

- comprensibles;
- progresivas;
- profesionales;
- mantenibles;
- testeables;
- reversibles;
- coherentes con ASP.NET Core MVC + Minimal APIs;
- apropiadas al nivel académico.

Aplicar:

> **El menor cambio que resuelva correctamente el problema y pueda comprobarse.**

No introducir sin evidencia de necesidad:

- microservicios;
- CQRS;
- event sourcing;
- arquitecturas distribuidas;
- frameworks frontend adicionales;
- capas artificiales;
- dependencias nuevas sin beneficio concreto;
- abstracciones prematuras;
- patrones de diseño por moda.

---

## 11. Patrones de diseño

`Observer`, `Singleton`, `Iterator`, `Decorator` u otros patrones pueden proponerse únicamente si:

1. existe una necesidad concreta;
2. se identifica el problema real;
3. el patrón reduce complejidad, riesgo o duplicación;
4. su beneficio es demostrable;
5. su implementación sigue siendo comprensible;
6. se compara contra una solución más simple;
7. se valida que no agrega sobreingeniería.

No existe obligación de usar un patrón solo porque fue estudiado.

---

## 12. Modelo de riesgo

Todo hallazgo relevante debe clasificar:

- severidad;
- probabilidad;
- impacto;
- reversibilidad;
- blast radius;
- prioridad;
- confianza.

### 🟢 VERDE
Riesgo bajo, localizado y fácilmente reversible.

### 🟡 AMARILLO
Puede modificar comportamiento, integración o varios archivos.

**Requiere autorización antes de implementar.**

### 🔴 ROJO
Puede provocar pérdida de código, ruptura contractual, migración, corrupción de datos, vulnerabilidad, sobrescritura o conflicto destructivo.

**Requiere autorización individual y explícita.**

Prioridad:

```text
P0 — BLOQUEADOR CRÍTICO
P1 — ALTA
P2 — IMPORTANTE
P3 — MEJORA
P4 — OPCIONAL
```

No exagerar prioridades.

---

## 13. Blast radius

Clasificar el alcance potencial:

```text
LOCAL
MODULE
CROSS-MODULE
APPLICATION
SYSTEM
```

No modificar código crítico si el blast radius es desconocido.

---

## 14. Formato obligatorio de hallazgo

```text
FINDING-ID: FIND-XXX
RESPONSABLE:
CATEGORÍA:
SEMÁFORO: 🟢 / 🟡 / 🔴
PRIORIDAD: P0 / P1 / P2 / P3 / P4

UBICACIÓN:
ARCHIVO:
SÍMBOLO:
RAMA / COMMIT:

HECHO:
EVIDENCIA:
INFERENCIA:
CAUSA RAÍZ:

IMPACTO:
BLAST RADIUS:
REGRESIONES POTENCIALES:
REVERSIBILIDAD:

RECOMENDACIÓN:
ALTERNATIVA MÁS SIMPLE:
PRUEBAS:
ROLLBACK:
CONFIANZA:
```

---

## 15. Solicitud de cambio obligatoria

Antes de corregir código de riesgo amarillo o rojo:

```text
SOLICITUD DE CAMBIO — CHG-XXX

Responsable:
Categoría:
Semáforo: 🟢 / 🟡 / 🔴
Prioridad: P0 / P1 / P2 / P3 / P4
Rama objetivo:

Archivo y símbolo:
Líneas o referencia:
Commit o comparación relacionada:

Comportamiento actual:
Evidencia:
Causa raíz:

Cambio propuesto:
Beneficio esperado:
Riesgo de no realizarlo:
Riesgo de realizarlo:
Blast radius:
Dependencias:

Archivos afectados:
Comandos previstos:
Pruebas previstas:
Estrategia de rollback:

Recomendación:
Confianza: alta / media / baja

ESTADO: ESPERANDO AUTORIZACIÓN
```

Autorizaciones válidas:

```text
AUTORIZO CHG-XXX
```

o para una etapa definida:

```text
AUTORIZO WAVE-X
```

Una autorización no se extiende a cambios no descritos.

---

## 16. Operaciones prohibidas sin autorización explícita

Nunca ejecutar automáticamente:

```text
git reset --hard
git clean -fd
git push --force
git push --force-with-lease
git rebase de ramas compartidas
eliminación de ramas
reescritura de historial
descarte de cambios locales
resolución de conflictos con pérdida
eliminación masiva de archivos
migraciones reales
dotnet ef database update
cambios de esquema
cambios de seguridad de alto impacto
commit
push
merge
```

Antes de cualquier operación riesgosa:

```text
EXPLICAR
→ MOSTRAR EVIDENCIA
→ MOSTRAR IMPACTO
→ MOSTRAR ALTERNATIVAS
→ DEFINIR ROLLBACK
→ SOLICITAR AUTORIZACIÓN
```

---

## 17. Principio de cambio atómico

Preferir cambios:

```text
pequeños
+ cohesivos
+ verificables
+ testeables
+ reversibles
```

No mezclar innecesariamente en un mismo cambio:

- feature;
- refactor;
- formatting;
- actualización de dependencias;
- migración arquitectónica.

Cada cambio relevante tendrá identificador:

```text
CHG-001
CHG-002
CHG-003
...
```

Mantener trazabilidad:

```text
FINDING
→ DECISION
→ CHANGE
→ VALIDATION
→ RESULT
```

---

## 18. Master Implementation Plan

Usar como base:

### WAVE 0 — Seguridad y línea base
Git, build, configuración, secretos, solución, documentación y pruebas mínimas.

### WAVE 1 — Bloqueadores críticos
Compilación, contratos incompatibles, seguridad, integridad, comunicación MVC/API.

### WAVE 2 — Preparación backend
Contratos, DTOs, validaciones, errores, CORS, autenticación y endpoints requeridos.

### WAVE 3 — Infraestructura frontend para APIs
URL base, `HttpClient`, servicios, modelos, ViewModels, errores y controladores.

### WAVE 4 — Funcionalidades principales
1. catálogo/categorías;
2. detalle de producto;
3. registro/login;
4. carrito;
5. checkout;
6. pedidos/pagos;
7. administración/reportes.

### WAVE 5 — Responsive
Estructura visual, componentes, mockups, breakpoints, accesibilidad y validación visual.

### WAVE 6 — Pruebas y regresiones
Unitarias donde aporten valor, integración API, MVC, flujos funcionales y responsive.

### WAVE 7 — Integración Git
Rama aislada, resolución documentada, validación y PR.

### WAVE 8 — Auditoría final
Build, tests, contratos, seguridad, responsive, documentación y deuda pendiente.

Cada wave debe incluir:

- objetivo;
- dependencias;
- archivos;
- cambios;
- riesgos;
- criterios de aceptación;
- pruebas;
- rollback;
- esfuerzo relativo;
- autorización requerida.

---

## 19. Definition of Ready global

Un cambio está listo cuando:

```text
[ ] Problema comprendido.
[ ] Evidencia disponible.
[ ] Causa raíz identificada.
[ ] Dependencias mapeadas.
[ ] Responsable definido.
[ ] Blast radius estimado.
[ ] Riesgo clasificado.
[ ] Solución mínima definida.
[ ] Alternativas evaluadas cuando corresponde.
[ ] Pruebas definidas.
[ ] Rollback definido cuando corresponde.
[ ] Autorización obtenida si es necesaria.
```

---

## 20. Definition of Done global

Un cambio está terminado cuando:

```text
[ ] Implementación aprobada completada.
[ ] Proyectos afectados compilan.
[ ] Pruebas relevantes pasan.
[ ] Comportamiento solicitado validado.
[ ] Funcionalidad previa preservada.
[ ] No hay regresiones conocidas.
[ ] Contratos compatibles o cambio autorizado.
[ ] Documentación actualizada.
[ ] Auditor.md completó revisión posterior.
[ ] Git muestra únicamente cambios esperados.
[ ] Cambio trazado a FINDING/CHG.
[ ] No se hizo commit/push/merge sin autorización.
```

---

## 21. Protocolo de desacuerdo

Si dos agentes discrepan:

1. ninguno impone su criterio;
2. ambos documentan evidencia;
3. comparan impacto y alternativas;
4. `Auditor.md` consolida;
5. si la decisión es crítica, se escala al humano.

Formato:

```text
AGENTE A:
AGENTE B:
HECHOS COMPARTIDOS:
PUNTO DE DESACUERDO:

OPCIÓN A:
Beneficios:
Riesgos:

OPCIÓN B:
Beneficios:
Riesgos:

RECOMENDACIÓN DEL AUDITOR:
DECISIÓN HUMANA REQUERIDA: SÍ / NO
```

---

## 22. Condiciones de parada

Detener implementación y escalar cuando exista:

- impacto destructivo desconocido;
- impacto de migración desconocido;
- incertidumbre de seguridad;
- conflicto de alto riesgo sin resolver;
- regla de negocio ambigua;
- potencial pérdida de datos;
- contradicción arquitectónica;
- operación difícilmente reversible;
- falta de evidencia crítica.

No improvisar soluciones destructivas.

---

## 23. Prioridades técnicas

Cuando existan objetivos en conflicto:

1. integridad de datos;
2. seguridad;
3. corrección funcional;
4. preservación de funcionalidad;
5. integridad del repositorio;
6. compatibilidad;
7. confiabilidad;
8. arquitectura;
9. mantenibilidad;
10. testabilidad;
11. rendimiento;
12. experiencia de desarrollo;
13. elegancia del código.

**La estética nunca tiene prioridad sobre la integridad funcional.**

---

## 24. Inicio de cada sesión

El orquestador debe comenzar con:

```text
1. PRE-FLIGHT
2. REPOSITORY MAP
3. DELTA DESDE LA ÚLTIMA EVIDENCIA
4. IDENTIFICACIÓN DEL DOMINIO AFECTADO
5. ACTIVACIÓN DE ARCHIVOS ESPECIALISTAS
6. PLAN DE ACCIÓN
7. GATE DE AUTORIZACIÓN SI CORRESPONDE
```

No modificar código antes de que exista una razón, un responsable y un plan verificable.
