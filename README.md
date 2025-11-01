# 🧠 LiveCount: Detección en tiempo real con Django + YOLOv3

Este proyecto combina el framework web **Django** con el modelo de detección de objetos **YOLOv3** para realizar conteo en tiempo real desde imágenes o video. 
Incluye una interfaz web sencilla y scripts de integración con el modelo preentrenado.

---

## 🚀 Instalación rápida

### 1. Clona el repositorio 

###bash
git clone https://github.com/Naomi-1998/opencv-ey.git
cd livecount


2️⃣ Descarga los archivos del modelo YOLOv
- Accede al siguiente enlace de Google Drive:
📁 https://drive.google.com/drive/folders/1X93Ww24QlVKvQ_2dSUSpWGv13KTkGBMA?usp=drive_link
- Descarga los archivos yolov3.cfg y yolov3.weights.
- Coloca ambos archivos directamente en la carpeta raíz del proyecto (livecount/), al mismo nivel que manage.py y db.sqlite3.


3️⃣ Crea y activa un entorno virtual (opcional pero recomendado)
🪟 En sistemas Windows
    python -m venv env
    env\Scripts\activate


4️⃣ Instala las dependencias necesarias
📦 Instala Django
    pip install django


📷 Descargar la de pependencia OpenCV para procesar imágenes o video
    pip install opencv-python


5️⃣ Ejecuta el servidor de desarrollo
    python manage.py runserver


📁 Estructura del proyect
livecount/
├── livecount/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── spark/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       ├── main.js
│   │       └── scripts.js
│   ├── templates/
│   │   └── home.html
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── __init__.py
├── yolov3.cfg
├── yolov3.weights
├── db.sqlite3
└── manage.py



    
