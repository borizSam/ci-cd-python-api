# CI/CD Pipeline Demo — FastAPI + PyTest + Docker + GitHub Actions

Este proyecto es una demostración completa de un flujo **CI/CD moderno**, utilizando:

- **FastAPI** → API ligera y rápida
- **PyTest** → pruebas automatizadas
- **Docker** + **Docker Compose** → empaquetado y despliegue local
- **GitHub Actions** → integración continua (CI)
- **TestClient / requests** → validación de endpoints

El objetivo es mostrar cómo automatizar validaciones, construir imágenes reproducibles y asegurar calidad continua antes de desplegar software, siguiendo prácticas DevOps.

---

## 📁 Estructura del proyecto

```
ci-cd-python-api/
│
├── app/
│ ├── main.py # Lógica principal de la API FastAPI
│ ├── requirements.txt # Dependencias necesarias
│ └── init.py
│
├── tests/
│ └── test_api.py # Pruebas automatizadas con PyTest
│
├── conftest.py # Ajustes del path para PyTest
│
├── Dockerfile # Imagen Docker de la API
├── docker-compose.yml # Despliegue local con Docker Compose
│
├── README.md
└── .github/
└── workflows/
└── ci.yml # Pipeline CI con GitHub Actions
```

---


## ▶️ Ejecutar la API localmente (sin Docker)

### 1. Crear entorno virtual

```
python3 -m venv venv
source venv/bin/activate
```

### 2.Instalar dependencias
```
pip install -r app/requirements.txt
```
### 3. Ejecutar FastAPI
```
uvicorn app.main:app --reload --port 8000
```

Endpoints accesibles:
```
http://localhost:8000
```
```
http://localhost:8000/health
```
## ▶️ Ejecutar tests

Ejecutar pruebas automatizadas con PyTest:
```
pytest -q
```

Los tests validan que los endpoints devuelvan:

Código de estado 200

Respuesta JSON esperada

### Ejecutar el proyecto con Docker
#### 1. Build manual
```
docker build -t ci-cd-python-api:latest .
docker run -p 8000:8000 ci-cd-python-api:latest
```
#### 2. Con Docker Compose (recomendado)
```
docker-compose up --build
```

La API estará disponible en:
```
http://localhost:8000

http://localhost:8000/health
```
### ⚙️ CI/CD con GitHub Actions

Cada vez que haces push o un pull request hacia main, GitHub Actions ejecuta el pipeline:

Etapas del workflow:

- Checkout del repositorio

- Configurar Python 3.10

- Instalar dependencias

- Ejecutar tests

- Subir artefactos (resultados JUnit)

- Construir imagen Docker


Este proceso permite validar automáticamente la calidad del código y asegurar que la API siempre se puede construir desde cero.