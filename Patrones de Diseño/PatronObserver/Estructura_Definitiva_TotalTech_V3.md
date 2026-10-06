# ESTRUCTURA DEFINITIVA DEL PROYECTO TOTALTECH — V3

Para **TotalTech**, la estructura definitiva debería preservar lo que ya funciona, separar con claridad **API, MVC, persistencia, documentación, pruebas y gobierno de agentes**, y evitar convertir el proyecto académico en una arquitectura innecesariamente compleja.

La arquitectura objetivo sería:

```text
TOTALTECH
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│   ├── api/
│   ├── arquitectura/
│   ├── mockups/
│   └── decisiones/
│
├── tests/
│   ├── Totaltech.Tests/
│   └── Frontend.Tests/
│
├── Totaltech/
│   ├── Datos/
│   ├── Endpoints/
│   ├── Entidades/
│   ├── Logica/
│   │   └── DTOs/
│   ├── Repositorios/
│   ├── Migrations/
│   ├── Properties/
│   ├── Program.cs
│   ├── appsettings.json
│   ├── appsettings.Development.json
│   └── Totaltech.csproj
│
├── Frontend/
│   ├── Controllers/
│   ├── Models/
│   │   ├── Api/
│   │   └── ViewModels/
│   ├── Services/
│   │   └── Api/
│   ├── Views/
│   │   ├── Shared/
│   │   ├── Home/
│   │   ├── Auth/
│   │   ├── Productos/
│   │   ├── Carrito/
│   │   ├── Checkout/
│   │   ├── Pedidos/
│   │   └── Admin/
│   ├── wwwroot/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── Properties/
│   ├── Program.cs
│   ├── appsettings.json
│   ├── appsettings.Development.json
│   └── Frontend.csproj
│
├── AGENTS.md
├── CleanCode.md
├── Frontend.md
├── Backend.md
├── Auditor.md
│
├── README.md
├── .gitignore
└── Grupo-N-1---SistemaVentaDeProductosTecnologicos.sln
```

## 1. Arquitectura definitiva

La solución debe quedar conceptualmente dividida en **dos aplicaciones y una capa de pruebas**, no en diez proyectos independientes.

```text
┌──────────────────────────────────────────────┐
│                 FRONTEND MVC                 │
│                                              │
│ Razor → Controller → API Service → HttpClient│
└───────────────────────┬──────────────────────┘
                        │ HTTP / JSON
                        ▼
┌──────────────────────────────────────────────┐
│                TOTALTECH API                 │
│                                              │
│ Endpoint → Lógica → Repositorio → EF Core   │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
                   SQL SERVER
```

Esta separación es fundamental.

### Regla

**`Frontend` no debería referenciar directamente `Totaltech.csproj`.**

No quiero:

```text
Frontend
→ referencia directa
→ Entidades EF
```

Quiero:

```text
Frontend
→ HTTP
→ API
→ JSON
```

Eso hace que el ejercicio cumpla de verdad con:

> el controlador MVC realiza llamadas a las APIs desarrolladas.

---

## 2. Raíz del repositorio

La raíz debe mantenerse limpia.

```text
/
├── AGENTS.md
├── CleanCode.md
├── Frontend.md
├── Backend.md
├── Auditor.md
├── README.md
├── .gitignore
├── Grupo-N-1---SistemaVentaDeProductosTecnologicos.sln
│
├── Totaltech/
├── Frontend/
├── tests/
├── docs/
└── .github/
```

Los cinco agentes quedan deliberadamente en la raíz porque deben ser fáciles de detectar por Codex y otros agentes.

`AGENTS.md` será el **entry point obligatorio**.

---

## 3. Backend definitivo

Mantendría la arquitectura que ya construyeron.

No recomiendo reemplazarla por Clean Architecture, DDD, CQRS ni proyectos adicionales.

```text
Totaltech/
│
├── Datos/
│   └── TotaltechDbContext.cs
│
├── Entidades/
│   ├── Usuario.cs
│   ├── Direccion.cs
│   ├── Producto.cs
│   ├── Categoria.cs
│   ├── Proveedor.cs
│   ├── Carrito.cs
│   ├── DetalleCarrito.cs
│   ├── Pedido.cs
│   ├── DetallePedido.cs
│   ├── Pago.cs
│   ├── Compra.cs
│   ├── Reporte.cs
│   └── Consulta.cs
│
├── Endpoints/
│   ├── AuthEndpoints.cs
│   ├── UsuariosEndpoints.cs
│   ├── DireccionesEndpoints.cs
│   ├── ProductosEndpoints.cs
│   ├── CategoriasEndpoints.cs
│   ├── ProveedoresEndpoints.cs
│   ├── CarritosEndpoints.cs
│   ├── DetalleCarritosEndpoints.cs
│   ├── PedidosEndpoints.cs
│   ├── DetallePedidosEndpoints.cs
│   ├── PagosEndpoints.cs
│   ├── ComprasEndpoints.cs
│   ├── ReportesEndpoints.cs
│   └── ConsultasEndpoints.cs
│
├── Logica/
│   ├── DTOs/
│   │   ├── Auth/
│   │   ├── Usuarios/
│   │   ├── Productos/
│   │   ├── Carritos/
│   │   ├── Pedidos/
│   │   └── Pagos/
│   │
│   ├── UsuariosLogica.cs
│   ├── ProductosLogica.cs
│   ├── CarritosLogica.cs
│   ├── PedidosLogica.cs
│   ├── PagosLogica.cs
│   └── ...
│
├── Repositorios/
│   ├── UsuariosRepositorio.cs
│   ├── ProductosRepositorio.cs
│   ├── CarritosRepositorio.cs
│   ├── PedidosRepositorio.cs
│   ├── PagosRepositorio.cs
│   └── ...
│
├── Migrations/
│
├── Properties/
│   └── launchSettings.json
│
├── Program.cs
├── appsettings.json
├── appsettings.Development.json
└── Totaltech.csproj
```

### Flujo backend obligatorio

```text
HTTP
 ↓
Endpoint
 ↓
Lógica
 ↓
Repositorio
 ↓
DbContext
 ↓
SQL Server
```

### Responsabilidad de cada nivel

**Endpoint**

```text
HTTP
request
response
status code
routing
```

**Lógica**

```text
reglas de negocio
validaciones
coordinación
transacciones
```

**Repositorio**

```text
consultas
persistencia
EF Core
```

**Datos**

```text
DbContext
relaciones
índices
restricciones
```

Esto evita un problema típico:

```text
Endpoint
 ├── validación
 ├── negocio
 ├── consultas SQL
 ├── cálculo
 └── respuesta
```

Eso no debería ocurrir.

---

## 4. Organización de DTOs

Aquí haría una mejora respecto de la estructura actual.

En vez de terminar con:

```text
DTOs/
├── ProductoRequest.cs
├── PagoRequest.cs
├── LoginDto.cs
├── ConfirmarCarritoDto.cs
├── ...
├── ...
└── 40 archivos
```

utilizaría agrupación por dominio:

```text
Logica/
└── DTOs/
    │
    ├── Auth/
    │   ├── LoginRequest.cs
    │   ├── RegistroRequest.cs
    │   └── UsuarioAutenticadoResponse.cs
    │
    ├── Productos/
    │   ├── ProductoRequest.cs
    │   └── ActualizarStockRequest.cs
    │
    ├── Carritos/
    │   ├── CarritoRequest.cs
    │   ├── AgregarProductoCarritoDto.cs
    │   └── ConfirmarCarritoDto.cs
    │
    ├── Pedidos/
    │   └── ...
    │
    └── Pagos/
        ├── PagoRequest.cs
        └── ActualizarEstadoPagoRequest.cs
```

Es organización, no una nueva capa arquitectónica.

---

## 5. Frontend definitivo

Aquí está uno de los cambios arquitectónicos más importantes.

```text
Frontend/
│
├── Controllers/
│   ├── HomeController.cs
│   ├── AuthController.cs
│   ├── ProductosController.cs
│   ├── CarritoController.cs
│   ├── CheckoutController.cs
│   ├── PedidosController.cs
│   └── AdminController.cs
│
├── Models/
│   │
│   ├── Api/
│   │   ├── Auth/
│   │   ├── Productos/
│   │   ├── Carritos/
│   │   ├── Pedidos/
│   │   └── Pagos/
│   │
│   └── ViewModels/
│       ├── Auth/
│       ├── Productos/
│       ├── Carrito/
│       ├── Checkout/
│       ├── Pedidos/
│       └── Admin/
│
├── Services/
│   └── Api/
│       ├── AuthApiService.cs
│       ├── ProductosApiService.cs
│       ├── CategoriasApiService.cs
│       ├── CarritoApiService.cs
│       ├── PedidosApiService.cs
│       └── PagosApiService.cs
│
├── Views/
│   │
│   ├── Shared/
│   │   ├── _Layout.cshtml
│   │   ├── _Header.cshtml
│   │   ├── _Footer.cshtml
│   │   ├── _ValidationScriptsPartial.cshtml
│   │   └── Error.cshtml
│   │
│   ├── Home/
│   │   └── Index.cshtml
│   │
│   ├── Auth/
│   │   ├── Login.cshtml
│   │   ├── Registro.cshtml
│   │   └── RecuperarContrasena.cshtml
│   │
│   ├── Productos/
│   │   ├── Index.cshtml
│   │   └── Detalle.cshtml
│   │
│   ├── Carrito/
│   │   └── Index.cshtml
│   │
│   ├── Checkout/
│   │   ├── Index.cshtml
│   │   └── Confirmacion.cshtml
│   │
│   ├── Pedidos/
│   │   ├── Index.cshtml
│   │   └── Detalle.cshtml
│   │
│   └── Admin/
│       ├── Index.cshtml
│       ├── Productos.cshtml
│       ├── Pedidos.cshtml
│       └── Reportes.cshtml
│
├── wwwroot/
│   │
│   ├── css/
│   │   ├── site.css
│   │   ├── components.css
│   │   └── responsive.css
│   │
│   ├── js/
│   │   ├── site.js
│   │   └── carrito.js
│   │
│   └── images/
│
├── Properties/
│
├── Program.cs
├── appsettings.json
├── appsettings.Development.json
└── Frontend.csproj
```

---

## 6. No más `HomeController` gigante

Algo que impediría en la arquitectura definitiva es colocar:

```text
Index
Login
Register
Productos
Carrito
Checkout
Pedidos
Administración
```

todo dentro de:

```text
HomeController
```

Eso terminaría convirtiéndose en un controlador gigantesco.

Quiero:

```text
HomeController
        │
        └── Home

AuthController
        │
        ├── Login
        ├── Registro
        └── Logout

ProductosController
        │
        ├── Index
        └── Detalle

CarritoController
        │
        ├── Index
        ├── Agregar
        └── Eliminar

CheckoutController
        │
        ├── Index
        └── Confirmar

PedidosController
        │
        ├── Index
        └── Detalle
```

Es muchísimo más fácil de entender.

---

## 7. La pieza nueva clave: `Services/Api`

Aquí debe vivir el consumo HTTP.

Ejemplo conceptual:

```text
ProductosController
        ↓
ProductosApiService
        ↓
HttpClient
        ↓
GET /productos
        ↓
Totaltech API
```

Así el controlador no necesita saber demasiado de `HttpClient`.

No quiero terminar con esto repetido en veinte acciones:

```csharp
var client = _httpClientFactory.CreateClient(...);
var response = await client.GetAsync(...);
var json = ...
var resultado = ...
```

Preferimos:

```csharp
var productos =
    await _productosApiService.ObtenerTodosAsync();
```

El detalle HTTP queda encapsulado.

---

## 8. `ApiModels` ≠ `ViewModels`

Esta separación va a evitar muchos problemas futuros.

### Modelo API

Representa lo que responde TotalTech:

```text
ProductoApiModel

IdProducto
Nombre
Descripcion
Precio
Stock
IdCategoria
IdProveedor
```

### ViewModel

Representa lo que necesita una pantalla:

```text
CatalogoViewModel

Productos
Categorias
TextoBusqueda
CategoriaSeleccionada
MostrarSinResultados
```

Por lo tanto:

```text
API RESPONSE
       ↓
 ApiModel
       ↓
 Controller
       ↓
 ViewModel
       ↓
 Razor
```

Eso mantiene las vistas desacopladas del backend.

---

## 9. Vistas organizadas por funcionalidad

Actualmente existe bastante contenido bajo `Home`.

La estructura final no debería ser:

```text
Views/
└── Home/
    ├── Index
    ├── Login
    ├── Productos
    ├── Carrito
    ├── Checkout
    ├── Registro
    └── ...
```

Debe reflejar los dominios:

```text
Views/
├── Home/
├── Auth/
├── Productos/
├── Carrito/
├── Checkout/
├── Pedidos/
└── Admin/
```

La estructura del proyecto empieza así a representar el negocio.

---

## 10. Layout definitivo

El layout no debería contener toda la interfaz escrita en un único archivo.

Recomiendo:

```text
Shared/
├── _Layout.cshtml
├── _Header.cshtml
├── _Footer.cshtml
└── _ValidationScriptsPartial.cshtml
```

Flujo:

```text
_Layout
│
├── _Header
│
├── @RenderBody()
│
└── _Footer
```

Esto resulta especialmente importante porque:

- login;
- catálogo;
- carrito;
- checkout;
- admin;

van a compartir distintas partes de navegación.

---

## 11. CSS definitivo

No separaría el CSS por cada pequeño componente.

Para el tamaño de TotalTech, esto es suficiente:

```text
css/
├── site.css
├── components.css
└── responsive.css
```

### `site.css`

```text
variables
reset
tipografía
layout general
header
footer
```

### `components.css`

```text
buttons
cards
forms
badges
alerts
product-card
cart-item
```

### `responsive.css`

```text
breakpoints
adaptación de layout
navigation
grids
forms
tables
```

No crear:

```text
button.css
header.css
footer.css
card.css
input.css
login.css
navbar.css
...
```

porque sería exceso para este proyecto.

---

## 12. Breakpoints oficiales

Toda la tienda debería compartir una política única.

```text
320 px   → mobile mínimo
375 px   → mobile estándar
425 px   → mobile grande
768 px   → tablet
1024 px  → laptop/tablet horizontal
1280+ px → desktop
```

No deberían aparecer breakpoints arbitrarios como:

```text
683
747
913
1063
```

salvo que exista una razón visual concreta.

---

## 13. Documentación definitiva

Movería progresivamente la documentación técnica no operativa a:

```text
docs/
│
├── arquitectura/
│   ├── ArquitecturaGeneral.md
│   └── FlujoDeDatos.md
│
├── api/
│   └── ContratosAPI.md
│
├── mockups/
│   └── ...
│
└── decisiones/
    └── ...
```

Pero mantendría en la raíz:

```text
AGENTS.md
CleanCode.md
Frontend.md
Backend.md
Auditor.md
README.md
```

Porque esos archivos gobiernan el repositorio.

---

## 14. Tests

Introduciría tests, pero de forma progresiva.

No intentaría probar absolutamente todo.

```text
tests/
├── Totaltech.Tests/
│   ├── Logica/
│   │   ├── CarritosLogicaTests.cs
│   │   ├── ProductosLogicaTests.cs
│   │   └── PagosLogicaTests.cs
│   │
│   └── Totaltech.Tests.csproj
│
└── Frontend.Tests/
    ├── Services/
    └── Frontend.Tests.csproj
```

### Prioridad

Primero:

```text
Carrito
Stock
Pedido
Pago
Autenticación
```

Después el resto.

No tiene sentido comenzar escribiendo tests para getters triviales.

---

## 15. La solución `.sln`

La solución definitiva sí debe conocer todos los proyectos:

```text
Grupo-N-1---SistemaVentaDeProductosTecnologicos.sln
│
├── Totaltech
├── Frontend
├── Totaltech.Tests
└── Frontend.Tests
```

Como mínimo:

```text
Totaltech
+
Frontend
```

deben quedar dentro de la solución.

Eso también permitirá que CI pueda ejecutar correctamente:

```bash
dotnet restore
dotnet build
dotnet test
```

sobre el sistema completo.

---

## 16. CI definitivo

El workflow actual de escritorio no corresponde con la arquitectura real.

El objetivo debería convertirse en algo mucho más sencillo:

```text
PUSH / PR
    ↓
Checkout
    ↓
Setup .NET
    ↓
Restore
    ↓
Build Totaltech
    ↓
Build Frontend
    ↓
Tests
    ↓
RESULT
```

No necesitamos:

```text
WPF
MSIX
PFX
Windows Application Packaging
```

para TotalTech.

---

## 17. Configuración

La configuración debe quedar:

```text
Totaltech/
├── appsettings.json
└── appsettings.Development.json

Frontend/
├── appsettings.json
└── appsettings.Development.json
```

Frontend:

```json
{
  "ApiBaseUrl": "..."
}
```

Backend:

```text
ConnectionStrings
Logging
AllowedHosts
etc.
```

Los secretos reales:

```text
NO Git
```

Usar:

```text
User Secrets
Environment Variables
```

cuando corresponda.

---

## 18. Dependencias definitivas

Quiero una arquitectura de dependencias muy simple:

```text
Frontend
   │
   └──── HTTP ────► Totaltech API

Totaltech
   │
   └──── EF Core ─► SQL Server
```

Tests:

```text
Totaltech.Tests
       ↓
   Totaltech

Frontend.Tests
       ↓
   Frontend
```

No quiero:

```text
Totaltech → Frontend
Frontend → Totaltech
```

como referencias de proyecto.

---

## 19. Tampoco crearía un proyecto `Shared`

Puede resultar tentador hacer:

```text
Totaltech.Shared
```

para compartir DTOs.

**No lo haría todavía.**

Porque inmediatamente aparecería:

```text
Totaltech
Frontend
Shared
Contracts
Core
Infrastructure
Application
Domain
```

y para un sistema académico de este tamaño estaríamos entrando en sobreingeniería.

Primero aceptar cierto mapeo explícito entre:

```text
API Models
↔
Backend DTOs
```

Si en el futuro la duplicación contractual se convierte realmente en un problema, entonces se evalúa.

---

## 20. Flujo definitivo de catálogo

```text
Usuario
   ↓
GET /Productos
   ↓
ProductosController
   ↓
ProductosApiService
   ↓
HttpClient
   ↓
GET /productos
   ↓
ProductosEndpoints
   ↓
ProductosLogica
   ↓
ProductosRepositorio
   ↓
DbContext
   ↓
SQL Server
```

Respuesta:

```text
SQL
 ↑
Repositorio
 ↑
Lógica
 ↑
Endpoint
 ↑ JSON
ProductosApiService
 ↑
Controller
 ↑
CatalogoViewModel
 ↑
Razor
 ↑
Usuario
```

---

## 21. Flujo definitivo del carrito

```text
Producto
 ↓
Agregar
 ↓
CarritoController
 ↓
CarritoApiService
 ↓
POST /carritos/{id}/productos
 ↓
CarritosEndpoints
 ↓
CarritosLogica
 ↓
Validar:
 ├── carrito
 ├── estado
 ├── producto
 ├── cantidad
 └── stock
 ↓
Repositorio
 ↓
DB
```

El frontend **no decide la validez del stock**.

---

## 22. Flujo definitivo de checkout

```text
Carrito
  ↓
Checkout
  ↓
Dirección
  ↓
Confirmar
  ↓
POST /carritos/{id}/confirmar
  ↓
BACKEND
  │
  ├── validar carrito
  ├── validar usuario
  ├── validar dirección
  ├── validar productos
  ├── validar stock
  │
  ├── BEGIN TRANSACTION
  │
  ├── crear Pedido
  ├── crear DetallePedido
  ├── descontar Stock
  ├── confirmar Carrito
  │
  └── COMMIT
```

Después:

```text
Pedido
 ↓
Pago
 ↓
Estado
```

Es uno de los flujos que más deberemos proteger con tests.

---

## 23. Los agentes dentro de la estructura

La arquitectura de agentes quedaría:

```text
                    AGENTS.md
                       │
          ┌────────────┼─────────────┐
          │            │             │
          ▼            ▼             ▼
     Frontend.md   Backend.md   CleanCode.md
          │            │             │
          └────────────┼─────────────┘
                       ▼
                  Auditor.md
                       │
                       ▼
                 VALIDACIÓN
```

Pero para un cambio real:

```text
REQUERIMIENTO
      ↓
AGENTS.md
      ↓
DOMAIN OWNER
      ↓
CleanCode
      ↓
Auditor
      ↓
IMPLEMENTACIÓN
      ↓
TEST
      ↓
Auditor
```

---

## 24. Estructura funcional final

La aplicación debería evolucionar en este orden:

```text
TOTALTECH
│
├── IDENTIDAD
│   ├── Registro
│   ├── Login
│   └── Sesión
│
├── CATÁLOGO
│   ├── Productos
│   ├── Categorías
│   ├── Búsqueda
│   └── Detalle
│
├── COMPRA
│   ├── Carrito
│   ├── Dirección
│   ├── Checkout
│   ├── Pedido
│   └── Pago
│
└── ADMINISTRACIÓN
    ├── Productos
    ├── Categorías
    ├── Proveedores
    ├── Pedidos
    ├── Compras
    ├── Consultas
    └── Reportes
```

Eso proporciona además el orden natural del desarrollo.

---

## 25. Orden definitivo de implementación

No desarrollaría “pantalla por pantalla” de manera aleatoria.

### WAVE 0

```text
Solución
CI
Build
Configuración
Agentes
Baseline
```

### WAVE 1

```text
Bloqueadores
Seguridad
Contratos
Integridad
```

### WAVE 2

```text
API backend
```

### WAVE 3

```text
HttpClient
Services
ApiModels
ViewModels
```

### WAVE 4

```text
Catálogo
Categorías
Detalle
```

### WAVE 5

```text
Registro
Login
Sesión
```

### WAVE 6

```text
Carrito
```

### WAVE 7

```text
Checkout
Pedido
Pago
```

### WAVE 8

```text
Administración
Reportes
```

### WAVE 9

```text
Responsive integral
Accesibilidad
UX
```

### WAVE 10

```text
Tests
Regresión
Auditoría
Integración Git
```

---

# Arquitectura final

El núcleo de la decisión es éste:

```text
                   TOTALTECH
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
  FRONTEND MVC                 BACKEND API
        │                           │
 Controllers                  Endpoints
        │                           │
 ViewModels                    Logica
        │                           │
 ApiServices                 Repositorios
        │                           │
 HttpClient                      EF Core
        │                           │
        └────── HTTP/JSON ────────►│
                                    │
                                SQL Server
```

Alrededor:

```text
        ┌─────────────────────────────┐
        │          AGENTS.md          │
        │ CleanCode / FE / BE / Audit │
        └─────────────────────────────┘

        ┌─────────────────────────────┐
        │            TESTS            │
        └─────────────────────────────┘

        ┌─────────────────────────────┐
        │             CI              │
        └─────────────────────────────┘
```

## Decisión arquitectónica central

**No necesitamos rehacer TotalTech.**

Necesitamos **ordenar y terminar profesionalmente la arquitectura que ya existe**.

Minimal API + MVC + EF Core es perfectamente suficiente para el proyecto. La mejora importante no está en agregar más capas, sino en conseguir que cada una tenga una responsabilidad inequívoca:

> **Razor muestra → MVC coordina → Service consume → API valida → Lógica decide → Repositorio persiste → EF Core protege relaciones → Auditor controla el cambio.**

Esa sería la estructura que tomaría como **arquitectura definitiva de TotalTech V3** antes de continuar con cualquier implementación profunda.
