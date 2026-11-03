# iNova Store - Tienda Online de iPhone

Tienda online especializada en la venta de iPhones en Colombia, con diseño estilo Apple Store.

## Características

- **Diseño moderno y minimalista** con paleta de colores pastel
- **Catálogo completo** de iPhone con filtros avanzados
- **Carrito de compras funcional** con persistencia en localStorage
- **Página de detalles** con galería de imágenes y selector de variantes
- **Sistema de inventario** por variante (color/capacidad)
- **Promociones configurables** (solo ofertas reales)
- **Responsive** para desktop, tablet y móvil
- **Checkout de demostración**
- **Búsqueda en tiempo real**

## Tecnologías

- Flask (Python)
- HTML5, CSS3, JavaScript
- Tailwind CSS (paleta personalizada)
- Lucide Icons

## Instalación y uso

1. Instalar dependencias:
```bash
pip install flask
```

2. Ejecutar la aplicación:
```bash
python app.py
```

3. Abrir en el navegador: `http://127.0.0.1:5000`

## Estructura del proyecto

```
├── app.py              # Aplicación Flask principal
├── data/
│   ├── products.json   # Datos de productos e inventario
│   └── promotions.json # Promociones configurables
├── static/
│   ├── css/style.css   # Estilos con paleta pastel
│   ├── js/main.js      # JavaScript funcional
│   └── images/         # Imágenes locales
└── templates/          # Plantillas HTML
    ├── base.html
    ├── index.html
    ├── catalog.html
    ├── product_detail.html
    ├── cart.html
    ├── checkout.html
    ├── offers.html
    └── contact.html
```

## Datos de demostración

- Los productos, precios e inventario son **datos de ejemplo**
- Las promociones son configurables en `data/promotions.json`
- El checkout es una **demostración** - no procesa pagos reales
- El inventario usa localStorage (para demostración en un solo navegador)

## Personalización

Para personalizar con datos reales:
1. Editar `data/products.json` con tus productos, precios e inventario
2. Editar `data/promotions.json` con tus promociones reales
3. Configurar número de WhatsApp en `templates/checkout.html` y `templates/contact.html`
4. Para producción, integrar base de datos y pasarela de pagos

## Características del carrito

- Agregar múltiples productos
- Mismo producto en diferentes colores/capacidades
- Actualizar cantidades
- Eliminar productos
- Persistencia en localStorage
- Validación de stock
- Cálculo de totales en COP

## Filtros disponibles

- Por precio (mínimo/máximo)
- Por modelo
- Por generación
- Por capacidad
- Por estado
- Por disponibilidad
- Ordenamiento por precio y popularidad
