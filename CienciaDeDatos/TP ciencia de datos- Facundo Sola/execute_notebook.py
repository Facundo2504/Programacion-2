import sys
import nbformat
from nbclient import NotebookClient

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Iniciando ejecución de ejerICES.ipynb con el kernel python314...")
with open("ejerICES.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(nb, timeout=300, kernel_name="python314")
client.execute()

with open("ejerICES.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("[OK] Notebook ejerICES.ipynb ejecutado exitosamente con todas sus celdas y gráficos guardados!")
