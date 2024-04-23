// Function to identify or mark the category selected based on the categories listed
function showProducts(element, category) {
    let smartphoneProducts = document.querySelectorAll('.smartphone-product')
    let foodProducts = document.querySelectorAll('.food-product')

    // Remove 'mark' on selected product categories when choose other category
    let categories = document.querySelectorAll('.category-tipe')
    categories.forEach(function(cat) {
        cat.classList.remove('selected');
    })

    // Add 'selected' class to the choosen category
    element.classList.add('selected');

    if (category === 'Smartphone') {
        smartphoneProducts.forEach(function(product) {
            product.style.display = 'block'
        })
        foodProducts.forEach(function(product) {
            product.style.display = 'none'
        })
    } else if (category === 'Foods') {
        smartphoneProducts.forEach(function(product) {
            product.style.display = 'none'
        })
        foodProducts.forEach(function(product) {
            product.style.display = 'block'
        })
    }
}


// Function to show all products
function showAllProducts() {
    let allProducts = document.querySelectorAll('.item')
    allProducts.forEach(function(product) {
        product.style.display = 'block'
    })

    // Remove mark on selected category when user click 'All'
    let categories = document.querySelectorAll('.category-tipe');
    categories.forEach(function(cat) {
        cat.classList.remove('selected');
    })
}


// Function to shuffle product lists, so user will see 'random product list'
function shuffleProducts() {
    let container = document.getElementById('randomProducts')
    for (let i = container.children.length; i >= 0; i--) {
        container.appendChild(container.children[Math.random() * i | 0]);
    }
}

shuffleProducts()