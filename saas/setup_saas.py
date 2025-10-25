import os
import subprocess
from pathlib import Path

print("🚀 Iniciando creación automática del proyecto SaaS con Sass...")

# --- Directorios base ---
BASE_DIR = Path(__file__).resolve().parent
VENV_DIR = BASE_DIR / "venv"
PROJECT_NAME = "myproject"
PROJECT_DIR = BASE_DIR / PROJECT_NAME

# --- 1. Crear entorno virtual ---
if not VENV_DIR.exists():
    print("🧩 Creando entorno virtual...")
    subprocess.run(["python", "-m", "venv", "venv"], check=True)
    print(f"👉 Activa tu entorno con:\n   {VENV_DIR}\\Scripts\\activate")
else:
    print("✅ Entorno virtual ya existe.")

# --- 2. Instalar dependencias ---
print("📦 Instalando Django y django-sass-processor...")
subprocess.run([str(VENV_DIR / "Scripts" / "pip"), "install", "django", "django-sass-processor"], check=True)

# --- 3. Crear proyecto Django ---
if not PROJECT_DIR.exists():
    print("🛠  Creando nuevo proyecto Django...")
    subprocess.run([str(VENV_DIR / "Scripts" / "python"), "-m", "django", "startproject", PROJECT_NAME, str(BASE_DIR)], check=True)
else:
    print("✅ Proyecto Django ya existe.")

# --- 4. Crear apps principales ---
os.chdir(PROJECT_DIR)
for app in ["Home", "accounts"]:
    if not (PROJECT_DIR / app).exists():
        print(f"🧱 Creando aplicación: {app}")
        subprocess.run([str(VENV_DIR / "Scripts" / "python"), "manage.py", "startapp", app], check=True)

# --- 5. Modificar settings.py ---
settings_path = PROJECT_DIR / PROJECT_NAME / "settings.py"
print("⚙️  Configurando settings.py...")

settings_content = settings_path.read_text(encoding="utf-8")
if "sass_processor" not in settings_content:
    settings_content = settings_content.replace(
        "INSTALLED_APPS = [",
        'INSTALLED_APPS = [\n    "sass_processor",'
    )
    settings_content += """

# --- Configuración de archivos estáticos y Sass ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
SASS_PROCESSOR_ROOT = BASE_DIR / "static"
"""
    settings_path.write_text(settings_content, encoding="utf-8")

print("✅ settings.py configurado correctamente.")

# --- 6. Crear estructura de archivos estáticos ---
static_sass_dir = PROJECT_DIR / "static" / "sass"
static_css_dir = PROJECT_DIR / "static" / "css"
templates_dir = PROJECT_DIR / "templates"
static_sass_dir.mkdir(parents=True, exist_ok=True)
static_css_dir.mkdir(parents=True, exist_ok=True)
templates_dir.mkdir(parents=True, exist_ok=True)

# --- 7. Crear archivo style.scss con requisitos ---
style_scss = static_sass_dir / "style.scss"
style_scss.write_text("""// === VARIABLES ===
$color-principal: #d62828;
$color-secundario: #003049;
$color-fondo: #f8f9fa;
$padding-base: 1.5rem;
$radius-base: 10px;

// === ANIDACIÓN ===
body {
  background-color: $color-fondo;
  font-family: 'Segoe UI', sans-serif;

  header {
    background-color: $color-principal;
    color: white;
    padding: $padding-base;

    nav {
      ul {
        list-style: none;
        li {
          display: inline-block;
          margin-right: 10px;

          a {
            text-decoration: none;
            color: white;

            &:hover {
              color: yellow;
            }
          }
        }
      }
    }
  }

  footer {
    background-color: $color-secundario;
    color: white;
    text-align: center;
    padding: $padding-base;
    border-radius: $radius-base;
  }
}

// === INTERPOLACIÓN ===
$estado: success;
$color-estado: green;

.alert-#{$estado} {
  color: white;
  background-color: $color-estado;
  padding: $padding-base;
}

$tipo: error;
$color-tipo: red;

.alert-#{$tipo} {
  color: white;
  background-color: $color-tipo;
  padding: $padding-base;
}
""", encoding="utf-8")

print("🎨 style.scss creado con variables, anidación e interpolación.")

# --- 8. Crear plantilla base.html ---
base_html = templates_dir / "base.html"
base_html.write_text("""{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Plataforma SaaS</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<header>
  <nav>
    <ul>
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Cuenta</a></li>
      <li><a href="#">Salir</a></li>
    </ul>
  </nav>
</header>

<main style="padding: 2rem;">
  <h1>Bienvenido a tu plataforma SaaS 🚀</h1>
  <div class="alert-success">Operación exitosa ✅</div>
  <div class="alert-error">Ha ocurrido un error ❌</div>
</main>

<footer>
  <p>© 2025 - Plataforma SaaS</p>
</footer>

</body>
</html>
""", encoding="utf-8")

print("🧩 Plantilla base.html creada correctamente.")

# --- 9. Compilar Sass a CSS ---
print("🧵 Compilando style.scss a style.css...")
try:
    subprocess.run(["sass", str(style_scss), str(static_css_dir / "style.css")], check=True)
    print("✅ Compilación Sass completada.")
except Exception:
    print("⚠️  No se pudo compilar Sass automáticamente. Puedes hacerlo manualmente con:")
    print("   sass static/sass/style.scss static/css/style.css")

# --- 10. Migraciones iniciales ---
print("🛠  Ejecutando migraciones iniciales...")
subprocess.run([str(VENV_DIR / "Scripts" / "python"), "manage.py", "migrate"], check=True)

print("\n🎉 Proyecto SaaS con Sass creado correctamente.")
print("👉 Ejecuta ahora:")
print(f"   {VENV_DIR}\\Scripts\\activate")
print("   python manage.py runserver")
