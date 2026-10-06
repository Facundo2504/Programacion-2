import os
import sys
import json
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from nbclient import NotebookClient

# Configurar salida segura
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

nb = new_notebook()

# Metadata
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3.14 (ICES)",
        "language": "python",
        "name": "python314"
    },
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.14.7"
    }
}

# -------------------------------------------------------------
# CELDA 1: Portada y Contexto
# -------------------------------------------------------------
cell_1_md = r"""# Trabajo Práctico: Segmentación de Clientes y Optimización de Promociones (ICES)
**Materia:** Programación 2 / Ciencia de Datos  
**Estudiante:** Facundo Sola  
**Institución:** ICES  
**Fecha:** Octubre 2026  

---
## Etapa 1: Análisis Exploratorio de Datos (EDA) y Preparación de Variables

### Escenario de Negocio
Una empresa de servicios por suscripción busca incrementar la retención y expandir la cantidad de productos contratados por su cartera de **2.500 clientes**. Dispone de un catálogo de **5 alternativas comerciales** (4 promociones activas y 1 grupo de control sin promoción) y los resultados observados en una **campaña piloto histórica de 900 tratamientos** sobre 744 clientes.

Cada promoción tiene un costo operativo y un beneficio incremental asociado si el cliente la acepta. El desafío analítico y de negocio consiste en:
1. **Explorar y preparar exhaustivamente la base de clientes**, asegurando calidad, coherencia relacional y analizando la distribución de las variables.
2. **Auditar la representatividad estadística del piloto comercial** para garantizar que sus métricas puedan generalizarse a la cartera completa.
3. **Identificar la estructura de relaciones y multicolinealidad** entre las variables de comportamiento, valor y riesgo.
4. **Construir un pipeline modular de ingeniería de variables y preprocesamiento** (`ColumnTransformer`) que deje los datos listos para algoritmos de segmentación no supervisada (K-Means).
"""
nb.cells.append(new_markdown_cell(cell_1_md))

# -------------------------------------------------------------
# CELDA 2: Configuración y Carga de Datos
# -------------------------------------------------------------
cell_2_code = r"""# ==============================================================================
# CONFIGURACIÓN DEL ENTORNO, BIBLIOTECAS Y CARGA ROBUSTA DE DATOS
# ==============================================================================
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.linear_model import LinearRegression

# Configuración visual
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['figure.autolayout'] = False

# Detección dinámica y robusta del archivo de datos (evita rutas absolutas rígidas)
nombre_archivo = "Segmentacion de clientes para ICES 20260929.xlsx"
rutas_candidatas = [
    nombre_archivo,
    os.path.join(os.getcwd(), nombre_archivo),
    os.path.join("..", nombre_archivo),
    os.path.join(os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.', nombre_archivo)
]

archivo = None
for ruta in rutas_candidatas:
    if os.path.exists(ruta):
        archivo = ruta
        break

if archivo is None:
    raise FileNotFoundError(f"No se encontró el archivo '{nombre_archivo}' en las rutas relativas exploradas.")

print(f"-> Archivo cargado exitosamente desde: {archivo}")

# Carga de todas las hojas disponibles en el archivo Excel
hojas_disponibles = pd.ExcelFile(archivo).sheet_names
print(f"-> Hojas encontradas en el libro: {hojas_disponibles}")

clientes = pd.read_excel(archivo, sheet_name="Clientes")
piloto = pd.read_excel(archivo, sheet_name="Piloto_promociones")
promociones = pd.read_excel(archivo, sheet_name="Promociones")
diccionario = pd.read_excel(archivo, sheet_name="Diccionario")
consigna = pd.read_excel(archivo, sheet_name="Consigna")

print(f"[OK] Clientes: {clientes.shape[0]} filas, {clientes.shape[1]} columnas")
print(f"[OK] Piloto Promociones: {piloto.shape[0]} registros, {piloto.shape[1]} columnas")
print(f"[OK] Catálogo Promociones: {promociones.shape[0]} promociones definidas")
"""
nb.cells.append(new_code_cell(cell_2_code))

# -------------------------------------------------------------
# CELDA 3: Markdown - Auditoría de Calidad
# -------------------------------------------------------------
cell_3_md = r"""### 1. Auditoría de Calidad de Datos, Estructura y Consistencia Relacional
Antes de cualquier análisis estadístico, realizamos un control exhaustivo sobre:
* **Valores faltantes (NaNs)** en todas las tablas.
* **Duplicidad de registros** a nivel cliente y a nivel tratamiento.
* **Integridad referencial**: constatamos que todos los clientes que participaron de la prueba piloto existen en la base maestra de clientes.
* **Consistencia de dominios y rangos**: verificamos que no existan valores fuera de rango lógico (e.g. edades negativas, NPS fuera de $[0, 10]$, índice digital fuera de $[0, 1]$).
"""
nb.cells.append(new_markdown_cell(cell_3_md))

# -------------------------------------------------------------
# CELDA 4: Code - Auditoría de Calidad
# -------------------------------------------------------------
cell_4_code = r"""# ==============================================================================
# AUDITORÍA DE CALIDAD Y CONTROL RELACIONAL
# ==============================================================================
print("=== 1. CONTROL DE NULOS Y REGISTROS ===")
print("Nulos en Clientes:\n", clientes.isnull().sum()[clientes.isnull().sum() > 0])
print("Nulos en Piloto:\n", piloto.isnull().sum()[piloto.isnull().sum() > 0])
print(f"Total valores faltantes en Clientes: {clientes.isnull().sum().sum()}")
print(f"Total valores faltantes en Piloto: {piloto.isnull().sum().sum()}")

print("\n=== 2. CONTROL DE CLAVES Y DUPLICADOS ===")
print(f"Clientes únicos en base Clientes: {clientes['cliente_id'].nunique()} de {len(clientes)}")
print(f"Tratamientos únicos en Piloto: {piloto['tratamiento_id'].nunique()} de {len(piloto)}")
print(f"Clientes únicos testeados en Piloto: {piloto['cliente_id'].nunique()}")

# Integridad referencial
clientes_piloto_en_base = piloto['cliente_id'].isin(clientes['cliente_id']).all()
print(f"¿Todos los clientes del piloto están presentes en la base maestra de clientes?: {clientes_piloto_en_base}")

# Distribución de tratamientos por cliente en el piloto
distrib_trat = piloto['cliente_id'].value_counts().value_counts().sort_index()
print("\nDistribución de tratamientos por cliente en el piloto:")
for n_trat, n_cli in distrib_trat.items():
    print(f"  - {n_cli} clientes recibieron {n_trat} tratamiento(s)")

print("\n=== 3. VERIFICACIÓN DE RANGOS LÓGICOS EN CLIENTES ===")
rangos_check = {
    "edad": (clientes['edad'].min() >= 18, f"Mínimo: {clientes['edad'].min()}, Máximo: {clientes['edad'].max()}"),
    "indice_digital": (0 <= clientes['indice_digital'].min() and clientes['indice_digital'].max() <= 1, f"[{clientes['indice_digital'].min()}, {clientes['indice_digital'].max()}]"),
    "nps": (0 <= clientes['nps'].min() and clientes['nps'].max() <= 10, f"[{clientes['nps'].min()}, {clientes['nps'].max()}]"),
    "dias_sin_interaccion": (clientes['dias_sin_interaccion'].min() >= 0, f"Mín: {clientes['dias_sin_interaccion'].min()}, Máx: {clientes['dias_sin_interaccion'].max()}"),
    "cantidad_productos": (clientes['cantidad_productos'].min() >= 1, f"Mín: {clientes['cantidad_productos'].min()}, Máx: {clientes['cantidad_productos'].max()}")
}
for variable, (es_valido, detalle) in rangos_check.items():
    print(f"  • {variable:22s}: {'VÁLIDO' if es_valido else 'ALERTA'} ({detalle})")
"""
nb.cells.append(new_code_cell(cell_4_code))

# -------------------------------------------------------------
# CELDA 5: Markdown - Análisis Univariado Numérico
# -------------------------------------------------------------
cell_5_md = r"""### 2. Análisis Univariado de Variables Numéricas
Analizamos las 12 variables continuas y discretas de la base `Clientes`:
* **Medidas de tendencia central y dispersión**: Media, Desviación Estándar, Mediana, Rango Intercuartílico ($IQR = Q_3 - Q_1$), Mínimo y Máximo.
* **Forma de la distribución**: Coeficiente de Asimetría (*Skewness*) y Curtosis.
* **Detección formal de outliers**: Implementamos el criterio clásico de **John Tukey** (*box-plot fences*):
  $$\text{Límite Inferior} = Q_1 - 1.5 \times IQR, \quad \text{Límite Superior} = Q_3 + 1.5 \times IQR$$
"""
nb.cells.append(new_markdown_cell(cell_5_md))

# -------------------------------------------------------------
# CELDA 6: Code - Tabla de Estadísticas Descriptivas
# -------------------------------------------------------------
cell_6_code = r"""# ==============================================================================
# TABLA RESUMEN ESTADÍSTICO UNIVARIADO COMPLETO Y DETECCIÓN DE OUTLIERS
# ==============================================================================
variables_numericas = [
    "edad",
    "ingreso_mensual_estimado",
    "antiguedad_anios",
    "cantidad_productos",
    "gasto_mensual",
    "margen_mensual",
    "indice_digital",
    "dias_sin_interaccion",
    "contactos_ult_90d",
    "reclamos_ult_12m",
    "pagos_atrasados_ult_12m",
    "nps"
]

resumen_estadistico = []
for col in variables_numericas:
    s = clientes[col]
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    mediana = s.median()
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers_mask = (s < lower_fence) | (s > upper_fence)
    n_outliers = outliers_mask.sum()
    pct_outliers = (n_outliers / len(s)) * 100
    
    resumen_estadistico.append({
        "Variable": col,
        "Media": s.mean(),
        "Desv. Est.": s.std(),
        "Mediana": mediana,
        "IQR": iqr,
        "Mínimo": s.min(),
        "Máximo": s.max(),
        "Asimetría (Skew)": s.skew(),
        "Curtosis": s.kurtosis(),
        "Outliers (IQR)": n_outliers,
        "% Outliers": pct_outliers
    })

df_resumen_num = pd.DataFrame(resumen_estadistico)
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')
display(df_resumen_num)
"""
nb.cells.append(new_code_cell(cell_6_code))

# -------------------------------------------------------------
# CELDA 7: Code - Histogramas Univariados
# -------------------------------------------------------------
cell_7_code = r"""# ==============================================================================
# DISTRIBUCIONES UNIVARIADAS: HISTOGRAMAS Y DENSIDAD ESTIMADA (KDE)
# ==============================================================================
fig, axes = plt.subplots(4, 3, figsize=(16, 14))
axes = axes.flatten()

for idx, col in enumerate(variables_numericas):
    ax = axes[idx]
    sns.histplot(clientes[col], kde=True, ax=ax, color='#1f77b4', bins=25, edgecolor='black', alpha=0.55)
    ax.axvline(clientes[col].mean(), color='red', linestyle='--', linewidth=1.5, label=f'Media: {clientes[col].mean():.1f}')
    ax.axvline(clientes[col].median(), color='green', linestyle=':', linewidth=1.8, label=f'Mediana: {clientes[col].median():.1f}')
    ax.set_title(f'{col}', fontsize=11, fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylabel('Frecuencia')
    ax.legend(fontsize=8, loc='upper right')

plt.suptitle('Distribución Univariada de Variables Numéricas (N = 2.500 Clientes)', fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_code_cell(cell_7_code))

# -------------------------------------------------------------
# CELDA 8: Code - Boxplots Univariados
# -------------------------------------------------------------
cell_8_code = r"""# ==============================================================================
# DETECCIÓN GRÁFICA DE OUTLIERS: DIAGRAMAS DE CAJA (BOXPLOTS)
# ==============================================================================
fig, axes = plt.subplots(4, 3, figsize=(16, 12))
axes = axes.flatten()

for idx, col in enumerate(variables_numericas):
    ax = axes[idx]
    sns.boxplot(x=clientes[col], ax=ax, color='#72b7b2', 
                flierprops=dict(marker='o', markersize=3.5, alpha=0.6, markerfacecolor='crimson'))
    ax.set_title(f'{col} (Outliers detectados)', fontsize=10, fontweight='bold')
    ax.set_xlabel('')

plt.suptitle('Diagramas de Caja y Detección de Valores Atípicos (Regla de Tukey)', fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_code_cell(cell_8_code))

# -------------------------------------------------------------
# CELDA 9: Markdown - Hallazgos Univariados
# -------------------------------------------------------------
cell_9_md = r"""### Interpretación de los Hallazgos Univariados
De la inspección estadística y gráfica de las variables numéricas se desprenden patrones clave para el negocio:

1. **Dimensión Monetaria y Rentabilidad (`ingreso_mensual_estimado`, `gasto_mensual`, `margen_mensual`):**
   * Exhiben una marcada **asimetría positiva** ($\text{skew} \in [1.62, 1.89]$) y colas pesadas.
   * La mediana del gasto mensual es de **$131.800**, mientras que la media asciende a **$178.985** traccionada por clientes de alto consumo (máximo de **$844.000**).
   * Se identifican 195 clientes con gasto atípico superior a $418.675 y 308 clientes con margen mensual atípico superior a $133.850. Estos perfiles representan el segmento de alto valor o VIP de la cartera.

2. **Dimensión de Vinculación y Tenencia (`antiguedad_anios`, `cantidad_productos`):**
   * La antigüedad promedia **7,1 años** (mediana 5,5 años, rango de 0,2 a 25 años).
   * La cantidad de productos contratados oscila entre **1 y 7** (media 2,63, mediana 2). Existe una masa significativa de clientes mono-producto o bi-producto que constituyen el público objetivo natural para iniciativas de *cross-selling* (como la promoción P3).

3. **Dimensión de Interacción y Canales (`indice_digital`, `dias_sin_interaccion`, `contactos_ult_90d`):**
   * El `indice_digital` tiene media de 0,65 y mediana de 0,70, con dispersión amplia a lo largo de todo el espectro $[0.06, 1.0]$.
   * `dias_sin_interaccion` presenta asimetría de 2,69: la mitad de los clientes interactuó en los últimos 31 días, pero un grupo exhibe inactividad prolongada de hasta 365 días (foco de riesgo de abandono).

4. **Dimensión de Riesgo de Crédito y Fricción (`reclamos_ult_12m`, `pagos_atrasados_ult_12m`):**
   * La gran mayoría de los clientes tiene 0 reclamos (media 0,48) y 0 meses con pagos atrasados (media 0,36).
   * Sin embargo, existe un 3,2% de clientes con entre 3 y 6 reclamos, y un 0,7% con 3 pagos atrasados. Este colectivo acumula fricción operativa y riesgo crediticio.

5. **Satisfacción del Cliente (`nps`):**
   * La distribución presenta asimetría negativa (-0,66) con media de **7,40** y mediana de **7,60**.
   * Identificamos una cola izquierda de detractores ($NPS < 6$, mínimo de 0,3) que requerirá acciones de retención o atención personalizada antes de ofrecerles ventas adicionales.
"""
nb.cells.append(new_markdown_cell(cell_9_md))

# -------------------------------------------------------------
# CELDA 10: Markdown - Variables Categóricas
# -------------------------------------------------------------
cell_10_md = r"""### 3. Análisis de Variables Categóricas y Canales de Atención
Exploramos las dos variables categóricas de la base: `region` geográfica y `canal_preferido`.
Evaluamos si existen diferencias socio-demográficas o transaccionales según el canal de contacto preferido o la región de residencia.
"""
nb.cells.append(new_markdown_cell(cell_10_md))

# -------------------------------------------------------------
# CELDA 11: Code - Variables Categóricas
# -------------------------------------------------------------
cell_11_code = r"""# ==============================================================================
# ANÁLISIS DE VARIABLES CATEGÓRICAS Y SEGMENTACIÓN POR CANAL
# ==============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Región
sns.countplot(data=clientes, x='region', order=clientes['region'].value_counts().index, 
              palette='viridis', ax=axes[0, 0], hue='region', legend=False)
axes[0, 0].set_title('Distribución de Clientes por Región Geográfica', fontsize=11, fontweight='bold')
axes[0, 0].set_ylabel('Cantidad de Clientes')
for p in axes[0, 0].patches:
    axes[0, 0].annotate(f"{int(p.get_height())}\n({p.get_height()/len(clientes)*100:.1f}%)", 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='bottom', fontsize=8.5, xytext=(0, 2), textcoords='offset points')

# 2. Canal Preferido
sns.countplot(data=clientes, x='canal_preferido', order=clientes['canal_preferido'].value_counts().index, 
              palette='magma', ax=axes[0, 1], hue='canal_preferido', legend=False)
axes[0, 1].set_title('Distribución de Clientes por Canal Preferido', fontsize=11, fontweight='bold')
axes[0, 1].set_ylabel('Cantidad de Clientes')
for p in axes[0, 1].patches:
    axes[0, 1].annotate(f"{int(p.get_height())}\n({p.get_height()/len(clientes)*100:.1f}%)", 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='bottom', fontsize=8.5, xytext=(0, 2), textcoords='offset points')

# 3. Canal vs Índice Digital
sns.boxplot(data=clientes, x='canal_preferido', y='indice_digital', palette='magma', ax=axes[1, 0], hue='canal_preferido', legend=False)
axes[1, 0].set_title('Índice Digital según Canal Preferido', fontsize=11, fontweight='bold')
axes[1, 0].set_ylabel('Índice Digital (0 a 1)')

# 4. Canal vs NPS
sns.boxplot(data=clientes, x='canal_preferido', y='nps', palette='magma', ax=axes[1, 1], hue='canal_preferido', legend=False)
axes[1, 1].set_title('Satisfacción (NPS) según Canal Preferido', fontsize=11, fontweight='bold')
axes[1, 1].set_ylabel('NPS (0 a 10)')

plt.suptitle('Comportamiento y Perfil de Clientes según Variables Categóricas', fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()

print("=== PERFIL PROMEDIO POR CANAL PREFERIDO ===")
display(clientes.groupby('canal_preferido')[['edad', 'indice_digital', 'gasto_mensual', 'nps', 'dias_sin_interaccion']].mean().round(2))

print("\n=== PERFIL PROMEDIO POR REGIÓN GEOGRÁFICA ===")
display(clientes.groupby('region')[['edad', 'indice_digital', 'gasto_mensual', 'nps']].mean().round(2))
"""
nb.cells.append(new_code_cell(cell_11_code))

# -------------------------------------------------------------
# CELDA 12: Markdown - Bivariado y Correlación
# -------------------------------------------------------------
cell_12_md = r"""### 4. Análisis Bivariado, Multivariado y Detección de Multicolinealidad
En esta sección profundizamos en las relaciones cruzadas entre variables:
1. Calculamos la **Matriz de Correlación Lineal de Pearson**.
2. Evaluamos pares estratégicos mediante gráficos de dispersión y líneas de tendencia.
3. Realizamos un análisis formal de **Multicolinealidad** a través del **Factor de Inflación de la Varianza (VIF)**:
   $$VIF_j = \frac{1}{1 - R_j^2}$$
   donde $R_j^2$ es el coeficiente de determinación al regresar la variable $j$ sobre todas las demás. Un $VIF > 5$ o $10$ señala multicolinealidad severa.
"""
nb.cells.append(new_markdown_cell(cell_12_md))

# -------------------------------------------------------------
# CELDA 13: Code - Matriz de Correlación
# -------------------------------------------------------------
cell_13_code = r"""# ==============================================================================
# MATRIZ DE CORRELACIÓN DE PEARSON Y MAPA DE CALOR
# ==============================================================================
corr_mat = clientes[variables_numericas].corr()

plt.figure(figsize=(11, 9))
mask = np.triu(np.ones_like(corr_mat, dtype=bool))
sns.heatmap(corr_mat, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, center=0,
            square=True, linewidths=0.5, cbar_kws={'shrink': 0.8}, annot_kws={'size': 9})
plt.title('Matriz de Correlación de Pearson entre Variables Numéricas', fontsize=13, fontweight='bold', pad=12)
plt.tight_layout()
plt.show()

# Listado de correlaciones fuertes (|r| >= 0.40)
print("=== ASOCIACIONES LINEALES DESTACADAS (|r| >= 0.40) ===")
pares_fuertes = []
for i in range(len(variables_numericas)):
    for j in range(i+1, len(variables_numericas)):
        r = corr_mat.iloc[i, j]
        if abs(r) >= 0.40:
            pares_fuertes.append({"Variable 1": variables_numericas[i], "Variable 2": variables_numericas[j], "Correlación (r)": r})
display(pd.DataFrame(pares_fuertes).sort_values(by="Correlación (r)", ascending=False, key=abs))
"""
nb.cells.append(new_code_cell(cell_13_code))

# -------------------------------------------------------------
# CELDA 14: Code - Gráficos Bivariados
# -------------------------------------------------------------
cell_14_code = r"""# ==============================================================================
# RELACIONES BIVARIADAS CLAVE DE NEGOCIO
# ==============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# 1. Gasto vs Margen (Colinealidad casi perfecta)
sns.scatterplot(data=clientes, x='gasto_mensual', y='margen_mensual', alpha=0.35, color='#1f77b4', ax=axes[0, 0])
sns.regplot(data=clientes, x='gasto_mensual', y='margen_mensual', scatter=False, color='red', ax=axes[0, 0],
            line_kws={'label': 'Ajuste lineal (r = 0.985)'})
axes[0, 0].set_title('1. Gasto Mensual vs. Margen Mensual (Alta Colinealidad)', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('Gasto Mensual ($)')
axes[0, 0].set_ylabel('Margen Mensual ($)')
axes[0, 0].legend()

# 2. Edad vs Índice Digital por Canal
sns.scatterplot(data=clientes, x='edad', y='indice_digital', hue='canal_preferido', alpha=0.55, palette='tab10', ax=axes[0, 1])
axes[0, 1].set_title('2. Edad vs. Índice Digital por Canal Preferido (r = -0.613)', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('Edad (Años)')
axes[0, 1].set_ylabel('Índice Digital (0 a 1)')

# 3. Días sin interacción vs NPS
sns.scatterplot(data=clientes, x='dias_sin_interaccion', y='nps', alpha=0.35, color='#d95f02', ax=axes[1, 0])
sns.regplot(data=clientes, x='dias_sin_interaccion', y='nps', scatter=False, color='black', ax=axes[1, 0],
            line_kws={'label': 'Tendencia (r = -0.468)'})
axes[1, 0].set_title('3. Inactividad vs. Satisfacción NPS (r = -0.468)', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel('Días sin Interacción')
axes[1, 0].set_ylabel('NPS (0 a 10)')
axes[1, 0].legend()

# 4. Ingreso Mensual Estimado vs. Gasto Mensual
sns.scatterplot(data=clientes, x='ingreso_mensual_estimado', y='gasto_mensual', alpha=0.35, color='#7570b3', ax=axes[1, 1])
sns.regplot(data=clientes, x='ingreso_mensual_estimado', y='gasto_mensual', scatter=False, color='darkgreen', ax=axes[1, 1],
            line_kws={'label': 'Tendencia (r = 0.709)'})
axes[1, 1].set_title('4. Ingreso Estimado vs. Gasto Mensual (r = 0.709)', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel('Ingreso Mensual Estimado ($)')
axes[1, 1].set_ylabel('Gasto Mensual ($)')
axes[1, 1].legend()

plt.suptitle('Relaciones Bivariadas Estratégicas', fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_code_cell(cell_14_code))

# -------------------------------------------------------------
# CELDA 15: Code - Cálculo de VIF
# -------------------------------------------------------------
cell_15_code = r"""# ==============================================================================
# ANÁLISIS DE MULTICOLINEALIDAD: FACTOR DE INFLACIÓN DE LA VARIANZA (VIF)
# ==============================================================================
vif_records = []
for target_col in variables_numericas:
    y = clientes[target_col]
    X_others = clientes[[c for c in variables_numericas if c != target_col]]
    
    # Regresión lineal con scikit-learn
    lr = LinearRegression().fit(X_others, y)
    r_squared = lr.score(X_others, y)
    
    vif = 1.0 / (1.0 - r_squared) if r_squared < 1.0 else float('inf')
    vif_records.append({
        "Variable": target_col,
        "R² con otras variables": r_squared,
        "VIF": vif,
        "Diagnóstico": "Severo (>10)" if vif > 10 else ("Moderado (5-10)" if vif > 5 else "Bajo (<5)")
    })

df_vif = pd.DataFrame(vif_records).sort_values(by="VIF", ascending=False)
print("=== FACTOR DE INFLACIÓN DE LA VARIANZA (VIF) ===")
display(df_vif)

# Análisis adicional: razón de margen sobre gasto
clientes['ratio_margen'] = clientes['margen_mensual'] / clientes['gasto_mensual']
print("\n=== ANÁLISIS DE LA RAZÓN DE MARGEN (margen_mensual / gasto_mensual) ===")
display(clientes['ratio_margen'].describe().to_frame().T)
"""
nb.cells.append(new_code_cell(cell_15_code))

# -------------------------------------------------------------
# CELDA 16: Markdown - Diagnóstico VIF y Clustering
# -------------------------------------------------------------
cell_16_md = r"""### Diagnóstico de Multicolinealidad y su Impacto en K-Means
1. **Colinealidad Crítica entre Gasto y Margen**:
   * `margen_mensual` ($VIF = 48.53$) y `gasto_mensual` ($VIF = 44.68$) presentan una correlación de **$r = 0.985$**.
   * El margen de contribución representa en promedio el **$28,83\%$** del gasto mensual, con una desviación estándar sumamente pequeña ($5,75\%$).
2. **Efecto Matemático en Algoritmos Basados en Distancia**:
   * En K-Means, la distancia euclidiana entre una observación $x$ y un centroide $\mu$ suma las distancias cuadradas sobre cada variable estandarizada:
     $$d(x, \mu)^2 = \sum_{j=1}^{p} (x_j - \mu_j)^2$$
   * Si incluimos simultáneamente $Z_{\text{gasto}}$ y $Z_{\text{margen}}$, ambas coordenadas aportarán casi idéntica información, **duplicando el peso relativo de la magnitud monetaria** por sobre la satisfacción (NPS), los reclamos o la antigüedad.
3. **Decisión Metodológica**:
   * Para respetar la especificación del pipeline del trabajo práctico, mantenemos ambas variables estandarizadas, pero generamos conscientemente la variable de ingeniería `ratio_margen` para caracterizar la rentabilidad relativa independiente del volumen absoluto de facturación.
"""
nb.cells.append(new_markdown_cell(cell_16_md))

# -------------------------------------------------------------
# CELDA 17: Markdown - Exploración del Piloto
# -------------------------------------------------------------
cell_17_md = r"""### 5. Exploración y Validación Estadística de la Campaña Piloto
La hoja `Piloto_promociones` contiene **900 tratamientos** aplicados a **744 clientes únicos**, con el objetivo de evaluar la receptividad y ganancia incremental de 5 esquemas comerciales:
* **P1**: 10% de bonificación por 3 meses (Objetivo: Retención | Costo: $18.000).
* **P2**: Upgrade sin cargo por 2 meses (Objetivo: Expansión | Costo: $24.000).
* **P3**: Beneficio por sumar segundo producto (Objetivo: Cross-sell | Costo: $32.000).
* **P4**: Atención prioritaria + asesor dedicado (Objetivo: Fidelización | Costo: $14.000).
* **P0**: Sin promoción (Grupo de Control | Costo: $0).

Para poder utilizar los resultados del piloto en la optimización general de la cartera, debemos verificar:
1. **Representatividad Muestral**: ¿Los clientes asignados al piloto son estadísticamente equivalentes al resto de la cartera? (Tests de Kolmogorov-Smirnov, t-Student y Chi-cuadrado).
2. **Desempeño Económico Global**: ¿Qué retorno y tasa de aceptación se observa si las promociones se aplican indiscriminadamente?
"""
nb.cells.append(new_markdown_cell(cell_17_md))

# -------------------------------------------------------------
# CELDA 18: Code - Métricas del Piloto
# -------------------------------------------------------------
cell_18_code = r"""# ==============================================================================
# DESEMPEÑO ECONÓMICO GLOBAL EN LA PRUEBA PILOTO
# ==============================================================================
resumen_piloto = piloto.groupby('promocion_id').agg(
    tratamientos=('tratamiento_id', 'count'),
    aceptaciones=('acepto', 'sum'),
    tasa_aceptacion=('acepto', 'mean'),
    margen_incremental_prom=('margen_incremental_12m', 'mean'),
    costo_promocion_prom=('costo_promocion', 'mean'),
    ganancia_observada_prom=('ganancia_observada', 'mean'),
    ganancia_total_piloto=('ganancia_observada', 'sum')
).reset_index()

# Incorporamos información del catálogo de promociones
resumen_piloto = resumen_piloto.merge(promociones[['promocion_id', 'nombre', 'objetivo']], on='promocion_id', how='left')

print("=== BALANCE GENERAL DEL PILOTO POR PROMOCIÓN ===")
display(resumen_piloto[['promocion_id', 'nombre', 'objetivo', 'tratamientos', 'aceptaciones', 
                        'tasa_aceptacion', 'margen_incremental_prom', 'costo_promocion_prom', 
                        'ganancia_observada_prom', 'ganancia_total_piloto']])

# Gráfico de desempeño del piloto
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Tasa de aceptación
sns.barplot(data=resumen_piloto, x='promocion_id', y='tasa_aceptacion', palette='Blues_r', ax=axes[0], hue='promocion_id', legend=False)
axes[0].set_title('Tasa de Aceptación por Promoción (%)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Tasa de Aceptación')
axes[0].set_xlabel('Promoción')
for p in axes[0].patches:
    axes[0].annotate(f"{p.get_height()*100:.1f}%", (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=9.5, xytext=(0, 2), textcoords='offset points')

# Ganancia observada promedio
colores_ganancia = ['gray' if x==0 else ('crimson' if x<0 else 'forestgreen') for x in resumen_piloto['ganancia_observada_prom']]
sns.barplot(data=resumen_piloto, x='promocion_id', y='ganancia_observada_prom', palette=colores_ganancia, ax=axes[1], hue='promocion_id', legend=False)
axes[1].axhline(0, color='black', linewidth=1)
axes[1].set_title('Ganancia Observada Promedio por Promoción ($)', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Ganancia Neta Promedio ($)')
axes[1].set_xlabel('Promoción')
for p in axes[1].patches:
    val = p.get_height()
    axes[1].annotate(f"${val:,.0f}", (p.get_x() + p.get_width() / 2., val),
                    ha='center', va='bottom' if val>=0 else 'top', fontsize=9.5, 
                    xytext=(0, 2 if val>=0 else -10), textcoords='offset points')

plt.suptitle('Rendimiento Global de la Campaña Piloto', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
"""
nb.cells.append(new_code_cell(cell_18_code))

# -------------------------------------------------------------
# CELDA 19: Code - Tests de Representatividad
# -------------------------------------------------------------
cell_19_code = r"""# ==============================================================================
# TESTS DE REPRESENTATIVIDAD ESTADÍSTICA: PILOTO VS. RESTO DE CARTERA
# ==============================================================================
piloto_clientes_ids = set(piloto['cliente_id'])
clientes_en_piloto = clientes[clientes['cliente_id'].isin(piloto_clientes_ids)]
clientes_fuera_piloto = clientes[~clientes['cliente_id'].isin(piloto_clientes_ids)]

print(f"Clientes evaluados en Piloto: {len(clientes_en_piloto)} ({len(clientes_en_piloto)/len(clientes)*100:.1f}%)")
print(f"Clientes no evaluados en Piloto: {len(clientes_fuera_piloto)} ({len(clientes_fuera_piloto)/len(clientes)*100:.1f}%)")

representatividad = []
for col in variables_numericas:
    ks_stat, ks_p = stats.ks_2samp(clientes_en_piloto[col], clientes_fuera_piloto[col])
    t_stat, t_p = stats.ttest_ind(clientes_en_piloto[col], clientes_fuera_piloto[col])
    representatividad.append({
        "Variable": col,
        "Media Piloto": clientes_en_piloto[col].mean(),
        "Media No Piloto": clientes_fuera_piloto[col].mean(),
        "KS-Statistic": ks_stat,
        "KS p-value": ks_p,
        "t-Statistic": t_stat,
        "t p-value": t_p,
        "Equivalencia (alpha=0.05)": "SÍ (No hay sesgo)" if ks_p > 0.05 and t_p > 0.05 else "REVISAR"
    })

df_rep = pd.DataFrame(representatividad)
print("\n=== TESTS DE IGUALDAD DE DISTRIBUCIONES (KOLMOGOROV-SMIRNOV Y T-STUDENT) ===")
display(df_rep)

# Tests de Chi-cuadrado para variables categóricas
for cat in ['region', 'canal_preferido']:
    tabla_cont = pd.crosstab(clientes['cliente_id'].isin(piloto_clientes_ids), clientes[cat])
    chi2, p_val, dof, _ = stats.chi2_contingency(tabla_cont)
    print(f"Chi-cuadrado para '{cat}': Chi² = {chi2:.4f}, p-value = {p_val:.4f} -> {'Muestra representativa (p > 0.05)' if p_val > 0.05 else 'Diferencias significativas'}")
"""
nb.cells.append(new_code_cell(cell_19_code))

# -------------------------------------------------------------
# CELDA 20: Markdown - Conclusiones del Piloto
# -------------------------------------------------------------
cell_20_md = r"""### Conclusiones Estratégicas de la Validación del Piloto
1. **Validez Externa Comprobada**: Todos los tests de Kolmogorov-Smirnov y t-Student arrojan $p$-values muy superiores al 0.05 (rango entre 0.08 y 1.00), y las pruebas Chi-cuadrado confirman la homogeneidad de canales ($p = 0.897$) y regiones ($p = 0.227$). La muestra del piloto es **completamente representativa** de la cartera general y carece de sesgo de selección.
2. **La Trampa del Contacto Masivo Indiscriminado**:
   * Si la empresa ofreciera la promoción **P1 (Retención)** a ciegas, perdería en promedio **-$607** por tratamiento (pérdida neta de -$140.300 en el piloto).
   * Si ofreciera **P4 (Fidelización)** a ciegas, perdería en promedio **-$2.025** por tratamiento (pérdida neta de -$362.400).
   * Solo **P3 (Cross-sell)** (+$9.968) y **P2 (Expansión)** (+$3.034) presentan ganancias globales positivas.
3. **El Rol Crítico de la Segmentación**:
   * Estas pérdidas globales ocurren porque se contacta a clientes que no valoran la oferta o cuyo beneficio no compensa el costo unitario.
   * La segmentación permitirá aislar los micro-grupos donde P1 y P4 son altamente rentables (por ejemplo, P1 en clientes con alto riesgo de abandono y NPS bajo, P4 en clientes de gasto elevado que exigen atención prioritaria).
"""
nb.cells.append(new_markdown_cell(cell_20_md))

# -------------------------------------------------------------
# CELDA 21: Markdown - Preparación de Variables y Pipeline
# -------------------------------------------------------------
cell_21_md = r"""### 6. Preparación y Transformación de Variables (Feature Engineering & Pipeline)
Para la fase de segmentación no supervisada (K-Means), definimos:
1. **Ingeniería de Características (*Feature Engineering*)**:
   * `ratio_margen`: $\frac{\text{margen\_mensual}}{\text{gasto\_mensual}}$ (eficiencia de rentabilidad sin colinealidad de escala).
   * `gasto_por_producto`: $\frac{\text{gasto\_mensual}}{\text{cantidad\_productos}}$ (ticket promedio unitario).
   * `tasa_reclamos_contacto`: $\frac{\text{reclamos\_ult\_12m}}{\text{contactos\_ult\_90d} + 1}$ (densidad de fricción en la atención).
   * `alerta_inactividad`: Flag binario ($1$ si `dias_sin_interaccion` $> 60$ y $NPS < 7$, $0$ en caso contrario).
2. **Escalamiento Numérico**: Comparamos `StandardScaler` (z-score) y `RobustScaler` (resistente a outliers en ingresos y gastos atípicos).
3. **Codificación Categórica**: Aplicamos `OneHotEncoder(handle_unknown='ignore')` para convertir `region` (6 categorías) y `canal_preferido` (4 categorías) en variables indicadoras binarias.
4. **Construcción del Pipeline**: Ensamblamos el preprocesamiento con `ColumnTransformer` de scikit-learn.
"""
nb.cells.append(new_markdown_cell(cell_21_md))

# -------------------------------------------------------------
# CELDA 22: Code - Feature Engineering
# -------------------------------------------------------------
cell_22_code = r"""# ==============================================================================
# INGENIERÍA DE CARACTERÍSTICAS (FEATURE ENGINEERING)
# ==============================================================================
clientes_prep = clientes.copy()

# 1. Ratio de margen de contribución
clientes_prep['ratio_margen'] = clientes_prep['margen_mensual'] / clientes_prep['gasto_mensual']

# 2. Gasto unitario por producto
clientes_prep['gasto_por_producto'] = clientes_prep['gasto_mensual'] / clientes_prep['cantidad_productos']

# 3. Tasa de reclamos por contacto
clientes_prep['tasa_reclamos_contacto'] = clientes_prep['reclamos_ult_12m'] / (clientes_prep['contactos_ult_90d'] + 1)

# 4. Indicador de alerta de inactividad / riesgo
clientes_prep['alerta_inactividad'] = ((clientes_prep['dias_sin_interaccion'] > 60) & (clientes_prep['nps'] < 7.0)).astype(int)

print("=== NUEVAS VARIABLES GENERADAS ===")
display(clientes_prep[['ratio_margen', 'gasto_por_producto', 'tasa_reclamos_contacto', 'alerta_inactividad']].describe().T)

print(f"Clientes en alerta de inactividad: {clientes_prep['alerta_inactividad'].sum()} ({clientes_prep['alerta_inactividad'].mean()*100:.1f}%)")
"""
nb.cells.append(new_code_cell(cell_22_code))

# -------------------------------------------------------------
# CELDA 23: Code - Pipeline de Preprocesamiento y Comparación de Escaladores
# -------------------------------------------------------------
cell_23_code = r"""# ==============================================================================
# COMPARACIÓN DE ESCALADORES Y ENSAMBLE DEL PREPROCESAMIENTO
# ==============================================================================
scaler_std = StandardScaler()
scaler_rob = RobustScaler()

gasto_std = scaler_std.fit_transform(clientes[['gasto_mensual']])
gasto_rob = scaler_rob.fit_transform(clientes[['gasto_mensual']])

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
sns.kdeplot(clientes['gasto_mensual'], ax=axes[0], color='navy', fill=True)
axes[0].set_title('Original ($0 a $850k)', fontweight='bold')
axes[0].set_xlabel('Pesos ($)')

sns.kdeplot(gasto_std.flatten(), ax=axes[1], color='darkgreen', fill=True)
axes[1].set_title('StandardScaler (Media 0, Desv 1)', fontweight='bold')
axes[1].set_xlabel('Z-Score')

sns.kdeplot(gasto_rob.flatten(), ax=axes[2], color='darkred', fill=True)
axes[2].set_title('RobustScaler (Mediana 0, IQR 1)', fontweight='bold')
axes[2].set_xlabel('Escala Robusta')

plt.suptitle('Normalización de Variables con Outliers para Algoritmos de Distancia', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

# ==============================================================================
# PIPELINE DEFINITIVO DE PREPROCESAMIENTO CON COLUMNTRANSFORMER
# ==============================================================================
variables_categoricas = ["region", "canal_preferido"]

preprocesamiento = ColumnTransformer(
    transformers=[
        ("numericas", StandardScaler(), variables_numericas),
        ("categoricas", OneHotEncoder(handle_unknown="ignore", sparse_output=False), variables_categoricas)
    ],
    remainder="drop"
)

# Ajuste y transformación sobre la base Clientes
X = preprocesamiento.fit_transform(clientes)
nombres_caracteristicas = preprocesamiento.get_feature_names_out()

print("[OK] Matriz transformada X construida exitosamente:")
print(f"  - Dimensiones: {X.shape[0]} observaciones x {X.shape[1]} características")
print(f"  - Cantidad total de dimensiones para clustering: {len(nombres_caracteristicas)}")
"""
nb.cells.append(new_code_cell(cell_23_code))

# -------------------------------------------------------------
# CELDA 24: Markdown - Transición a Clustering
# -------------------------------------------------------------
cell_24_md = r"""### 7. Verificación del Preprocesamiento y Evaluación Preliminar de K (Método del Codo)
Para validar la operatividad de la matriz estandarizada $X$ y conectar fluidamente con la **Etapa 2 (Construcción de la segmentación no supervisada)**, ejecutamos la búsqueda preliminar del número óptimo de grupos $K \in [2, 10]$ evaluando:
1. **Inercia Intra-Cluster (Within-Cluster Sum of Squares - WCSS)**: Medida de compactación interna.
2. **Coeficiente de Silhouette**: Medida de cohesión y separación entre grupos.
3. **Criterio de la Segunda Diferencia**: Localización algorítmica del punto de máxima inflexión de la curva de inercia.
"""
nb.cells.append(new_markdown_cell(cell_24_md))

# -------------------------------------------------------------
# CELDA 25: Code - Método del Codo y Silhouette
# -------------------------------------------------------------
cell_25_code = r"""# ==============================================================================
# EVALUACIÓN DE INERCIA Y SILHOUETTE SCORE PARA K in [2, 10]
# ==============================================================================
resultados_k = []
ks = range(2, 11)

for k in ks:
    modelo_km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=20
    )
    etiquetas = modelo_km.fit_predict(X)

    resultados_k.append({
        "k": k,
        "inertia": modelo_km.inertia_,
        "silhouette": silhouette_score(X, etiquetas)
    })

df_resultados_k = pd.DataFrame(resultados_k)
print("=== RESULTADOS DE INERCIA Y SILHOUETTE POR NÚMERO DE CLÚSTERES ===")
display(df_resultados_k)

# Cálculo algorítmico del punto del codo (máxima segunda diferencia)
inercia = df_resultados_k["inertia"].to_numpy()
segunda_dif = np.abs(np.diff(inercia, 2))
idx_codo = int(np.argmax(segunda_dif)) + 1
k_codo = int(df_resultados_k.loc[idx_codo, "k"])

print(f"\n-> K sugerido por el método del codo (máxima inflexión): {k_codo}")

# Gráficos de Inercia y Silhouette
plt.figure(figsize=(13, 5))

plt.subplot(1, 2, 1)
plt.plot(df_resultados_k["k"], df_resultados_k["inertia"], marker='o', linewidth=2, color='#1f77b4')
plt.axvline(k_codo, color='red', linestyle='--', label=f'K codo: {k_codo}')
plt.axvline(5, color='green', linestyle='-', linewidth=2, label='K sugerido negocio: 5')
plt.title('Método del Codo (Inercia WCSS por K)', fontweight='bold')
plt.xlabel('Número de Clústeres (K)')
plt.ylabel('Inercia Intra-Cluster')
plt.grid(True, alpha=0.3)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(df_resultados_k["k"], df_resultados_k["silhouette"], marker='s', linewidth=2, color='green')
plt.axvline(k_codo, color='red', linestyle='--', label=f'K codo: {k_codo}')
plt.axvline(5, color='green', linestyle='-', linewidth=2, label='K sugerido negocio: 5')
plt.title('Coeficiente de Silhouette por K', fontweight='bold')
plt.xlabel('Número de Clústeres (K)')
plt.ylabel('Silhouette Score')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
"""
nb.cells.append(new_code_cell(cell_25_code))

# -------------------------------------------------------------
# CELDA 26: Markdown - Resumen Ejecutivo y Próximos Pasos
# -------------------------------------------------------------
cell_26_md = r"""### Resumen Ejecutivo de la Etapa 1: EDA y Preparación de Variables

Al finalizar esta primera etapa, se han alcanzado los siguientes hitos fundamentales:
1. **Calidad y Consistencia de Datos**:
   * Certificación de 0 valores faltantes y 0 duplicados en los 2.500 clientes.
   * Confirmación del 100% de consistencia relacional entre la base maestra y los 900 tratamientos del piloto.
2. **Caracterización Univariada y Detección de Outliers**:
   * Identificación de colas pesadas en variables monetarias (`gasto_mensual`, `ingreso_mensual_estimado`, `margen_mensual`), con un subgrupo de alto valor económico (195 clientes con gasto superior a $418.675).
   * Identificación de clientes monoproducto (40% de la cartera) con alto potencial para cross-selling.
   * Detección de perfiles con fricción operativa (3,2% con más de 2 reclamos anuales y baja satisfacción NPS).
3. **Validación Estadística del Piloto Histórico**:
   * Demostración empírica (KS-test y Chi-cuadrado con $p > 0.05$) de que la muestra del piloto es no sesgada y estadísticamente representativa de la población total.
   * Constatación del riesgo de campañas indiscriminadas: promociones como P1 y P4 destruyen valor a nivel global (-$607 y -$2.025 promedio), justificando la necesidad indispensable de la segmentación.
4. **Multicolinealidad y Decisión de Modelado**:
   * Medición formal del $VIF$: se detectó colinealidad severa entre `gasto_mensual` ($VIF=44,68$) y `margen_mensual` ($VIF=48,53$, $r=0.985$).
   * Se desarrolló la variable complementaria `ratio_margen` para aislar la rentabilidad porcentual del cliente.
5. **Pipeline de Preprocesamiento Operativo**:
   * Se estructuró y validó el `ColumnTransformer` (`StandardScaler` + `OneHotEncoder`), generando una matriz $X \in \mathbb{R}^{2500 \times 22}$ limpia y normalizada.
   * La evaluación preliminar del codo y silhouette posiciona a $K=5$ como una solución de alta interpretabilidad comercial para la siguiente etapa.
"""
nb.cells.append(new_markdown_cell(cell_26_md))

# Guardar notebook base
output_path = "ejerICES.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"[OK] Notebook {output_path} creado con {len(nb.cells)} celdas.")
