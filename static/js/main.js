// iNova Store - Main JavaScript

let cart = [];

// Initialize cart from localStorage
function initCart() {
    const savedCart = localStorage.getItem('inovaCart');
    if (savedCart) {
        cart = JSON.parse(savedCart);
    }
    updateCartBadge();
}

// Update cart badge
function updateCartBadge() {
    const badge = document.querySelector('.cart-badge');
    if (badge) {
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        badge.textContent = totalItems;
    }
}

// Save cart to localStorage
function saveCart() {
    localStorage.setItem('inovaCart', JSON.stringify(cart));
    updateCartBadge();
}

// Format price in COP
function formatPrice(price) {
    return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 0
    }).format(price).replace('COP', 'COP');
}

// Carousel functionality
function initCarousel() {
    const carousel = document.querySelector('.carousel');
    if (!carousel) return;
    
    const container = carousel.querySelector('.carousel-container');
    const slides = carousel.querySelectorAll('.carousel-slide');
    const prevBtn = carousel.querySelector('.carousel-prev');
    const nextBtn = carousel.querySelector('.carousel-next');
    const indicators = carousel.querySelectorAll('.carousel-indicator');
    
    let currentSlide = 0;
    const totalSlides = slides.length;
    
    function goToSlide(n) {
        currentSlide = (n + totalSlides) % totalSlides;
        container.style.transform = `translateX(-${currentSlide * 100}%)`;
        
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentSlide);
        });
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            goToSlide(currentSlide - 1);
            resetAutoPlay();
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            goToSlide(currentSlide + 1);
            resetAutoPlay();
        });
    }
    
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            goToSlide(index);
            resetAutoPlay();
        });
    });
    
    // Auto play
    let autoPlayInterval;
    function startAutoPlay() {
        autoPlayInterval = setInterval(() => {
            goToSlide(currentSlide + 1);
        }, 4000);
    }
    
    function resetAutoPlay() {
        clearInterval(autoPlayInterval);
        startAutoPlay();
    }
    
    if (totalSlides > 1) {
        startAutoPlay();
        carousel.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
        carousel.addEventListener('mouseleave', startAutoPlay);
    }
}

// Product color selector
function initProductCards() {
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach(card => {
        const colorOptions = card.querySelectorAll('.color-option');
        const productImage = card.querySelector('.product-image');
        const priceCurrent = card.querySelector('.price-current');
        const addToCartBtn = card.querySelector('.btn-add-cart');
        
        colorOptions.forEach(option => {
            option.addEventListener('click', () => {
                if (option.classList.contains('disabled')) return;
                
                // Update active color
                colorOptions.forEach(opt => opt.classList.remove('active'));
                option.classList.add('active');
                
                // Update image if data-image exists
                const newImage = option.getAttribute('data-image');
                if (newImage && productImage) {
                    productImage.src = newImage;
                }
                
                // Update price if data-price exists
                const newPrice = option.getAttribute('data-price');
                if (newPrice && priceCurrent) {
                    priceCurrent.textContent = formatPrice(parseInt(newPrice));
                }
            });
        });
        
        if (addToCartBtn) {
            addToCartBtn.addEventListener('click', () => {
                const productId = card.getAttribute('data-product-id');
                const productName = card.querySelector('.product-name').textContent;
                const activeColor = card.querySelector('.color-option.active');
                const color = activeColor ? activeColor.getAttribute('data-color') : '';
                const colorHex = activeColor ? activeColor.style.backgroundColor : '';
                const capacity = card.querySelector('.product-capacity').textContent.replace('Almacenamiento: ', '');
                const priceText = card.querySelector('.price-current').textContent;
                const price = parseInt(priceText.replace(/[^0-9]/g, ''));
                const image = productImage ? productImage.src : '';
                
                // Add to cart
                const existingItem = cart.find(item => 
                    item.product_id === productId && 
                    item.color === color && 
                    item.capacity === capacity
                );
                
                if (existingItem) {
                    existingItem.quantity += 1;
                } else {
                    cart.push({
                        product_id: productId,
                        name: productName,
                        color: color,
                        colorHex: colorHex,
                        capacity: capacity,
                        price: price,
                        image: image,
                        quantity: 1
                    });
                }
                
                saveCart();
                showNotification('Producto agregado al carrito');
            });
        }
    });
}

// Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 90px;
        right: 20px;
        background-color: var(--verde-menta);
        color: var(--gris-oscuro);
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 10000;
        font-weight: 600;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 2000);
}

// Mobile menu
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    
    if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', () => {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
            if (navMenu.style.display === 'flex') {
                navMenu.style.flexDirection = 'column';
                navMenu.style.position = 'absolute';
                navMenu.style.top = '70px';
                navMenu.style.left = '0';
                navMenu.style.right = '0';
                navMenu.style.backgroundColor = 'var(--blanco-calido)';
                navMenu.style.padding = '1rem';
                navMenu.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
            }
        });
    }
}

// Search functionality
function initSearch() {
    const searchInput = document.querySelector('.nav-search input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            // This would filter products on catalog page
            console.log('Searching for:', query);
        });
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize all functions when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initCart();
    initCarousel();
    initProductCards();
    initMobileMenu();
    initSearch();
});
