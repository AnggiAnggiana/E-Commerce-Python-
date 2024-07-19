// Calculate Product based on quantity
const updateTotalPrice = (quantityId) => {
    let priceElement = document.querySelector('.product-price[data-id="' + quantityId + '"]')
    let priceText = priceElement.innerText.trim().replace('Rp.', '')
    let price = parseFloat(priceText.split('.').join(''))
    // console.log('product price:', price);

    let quantity = parseInt(document.getElementById('quantity' + quantityId).innerText)
    // console.log('quantity:', quantity);

    // let totalPrice = price
    let totalPrices = price * quantity
    // let totalPriceElement = document.getElementById('totalPrice' + quantityId)
    let totalPricesElement = document.getElementById('totalPrice' + quantityId)
    // totalPriceElement.innerText = 'Rp.' + totalPrice.toLocaleString('id-ID', {useGrouping: true})
    totalPricesElement.innerText = 'Rp.' + totalPrices.toLocaleString('id-ID', {useGrouping: true})
    // totalPriceElement.style.fontWeight = '500'
    totalPricesElement.style.fontWeight = '500'

    // Return totalPrice so can be used out of the function
    // return totalPrice;
    return totalPrices;
}

// Script to calculate total price as decrease
const decreaseQuantity = (quantityId) => {
    let quantityElement = document.getElementById('quantity_input_' + quantityId)
    let quantityButton = document.getElementById('quantity' + quantityId)
    let currentQuantity = parseInt(quantityElement.value)
    if (currentQuantity > 1) {
        currentQuantity -= 1
        quantityElement.value = currentQuantity
        quantityButton.innerHTML = currentQuantity
        // console.log('quantity_now: ', currentQuantity)
    }
    
    updateTotalPrice(quantityId)
}

// Script to calculate total price as increase
const increaseQuantity = (quantityId) => {
    let quantityElement = document.getElementById('quantity_input_' + quantityId)
    let quantityButton = document.getElementById('quantity' + quantityId)
    let currentQuantity = parseInt(quantityElement.value)
    currentQuantity += 1
    quantityElement.value = currentQuantity
    quantityButton.innerHTML = currentQuantity
    // console.log('quantity_now: ', currentQuantity)

    // To increase the quantity
    updateTotalPrice(quantityId)
    return currentQuantity;
}

