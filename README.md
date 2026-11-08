# iNova Store

Tienda online de iPhones con interfaz tipo Apple Store, desarrollada con Flask.

## Características
- Catálogo de iPhones (iPhone 13 - 18, Pro y Pro Max)
- Filtros por modelo, precio y más
- Carrito de compras con localStorage
- Detalle de producto con variantes (color/capacidad)
- Promociones configurables
- Diseño responsive con paleta pastel
- Contenido en español

## Estructura del proyecto
```
├── app/              # Aplicación Flask modular
│   ├── routes/       # Blueprints (main, api)
│   ├── static/       # CSS, JS, imágenes
│   ├── templates/    # Plantillas HTML
│   ├── utils/        # Utilidades
│   └── data/         # Datos de productos y promociones
├── api/              # Para despliegue serverless
├── app.py            # Punto de entrada
├── wsgi.py           # Para WSGI
├── vercel.json       # Configuración Vercel
└── requirements.txt  # Dependencias
```

## Desarrollo local
```bash
pip install -r requirements.txt
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

## Despliegue en Vercel
El proyecto está listo para desplegarse directamente en Vercel usando `vercel.json`.
