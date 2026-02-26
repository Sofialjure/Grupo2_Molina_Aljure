# 📁 Nombre del Proyecto

## 🧭 Introducción
Este repositorio contiene los trabajos y proyectos desarrollados con fines académicos y de aprendizaje, enfocados en el fortalecimiento de habilidades en programación, bases de datos y uso de herramientas modernas de desarrollo.  
Aquí se documenta el proceso, la estructura y los resultados de cada proyecto de manera organizada y clara.

---

## 📌 Descripción del Proyecto
Data-Dogs es un proyecto de ETL (Extract, Transform, Load) orientado al análisis estadístico de datos sobre razas de perros, utilizando información obtenida desde una API pública especializada en caninos.

El proyecto extrae datos crudos de la API, los normaliza, los almacena en formatos estructurados (CSV y JSON) y posteriormente genera visualizaciones estadísticas avanzadas, permitiendo analizar características como esperanza de vida, peso promedio, categorías de tamaño y distribución poblacional de las razas.

Este enfoque facilita el análisis exploratorio de datos (EDA) y la obtención de conclusiones estadísticas a partir de información real.

---

## 🎯 Objetivos del Proyecto
Desarrollar un pipeline ETL que permita extraer, limpiar, estructurar y visualizar datos de razas de perros, generando información estadística clara y reutilizable.

### 🎯 Objetivos específicos

- Extraer automáticamente todas las razas disponibles desde la API.

- Normalizar los datos crudos en un esquema estructurado.

- Generar datasets limpios en formatos CSV y JSON.

- Calcular métricas estadísticas relevantes (promedios, categorías, diferencias).

- Crear visualizaciones estadísticas agrupadas en imágenes consolidadas.

- Mantener un flujo reproducible y organizado para análisis futuros.

---

## 🛠️ Herramientas Utilizadas
- 🧑‍💻 **VS Code**
- 🐍 **Python**
- 🐳 **Docker**
- 🐧 **WSL**
- 🗄️ **PostgreSQL**
- 📊 **Jupyter Notebook**

---

## 🗂️ Estructura del Proyecto
```
data-dogs/
│
├── data/
│   ├── dogs_normalized.csv
│   ├── dogs_normalized.json
│   ├── dogs_statistical_analysis.png
│   └── dogs_statistical_analysis_extra.png
│
├── logs/
│   └── etl.log
│
├── scripts/
│   ├── extractor.py
│   └── visualizador.py
│
├── venv/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 👤 Autor
> 📌 **Jhon Sebastián Molina Fierro**
> 📌 **Maria Sofia Aljure Herrera**

