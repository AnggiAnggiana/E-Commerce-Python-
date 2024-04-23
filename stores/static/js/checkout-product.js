// Edit User Address
const toggleEdit = () =>  {
    let addressText = document.getElementById("text_address");
    let addressInput = document.getElementById("input_address");
    let saveButton = document.getElementById("saveAddress");
    let editButton = document.getElementById("editAddress");

    if (addressText.style.display === "block") {
        addressText.style.display = "none";
        addressInput.style.display = "block";
        saveButton.style.display = "block";
        editButton.innerText = "Cancel";
        editButton.style.display = "none";
    } else {
        addressText.style.display = "block";
        addressInput.style.display = "none";
        saveButton.style.display = "none";
        editButton.innerText = "Edit";
        editButton.style.display = "block";
    }

    // Set the dynamic marginTop
    adjustContactInfo()
}

const saveAddress = () => {
    let addressText = document.getElementById("text_address")
    let addressInput = document.getElementById("input_address")
    let saveButton = document.getElementById("saveAddress")
    let editButton = document.getElementById("editAddress")

    addressText.innerText = addressInput.value
    addressText.style.display = "block"
    addressInput.style.display = "none"
    saveButton.style.display = "none"
    editButton.innerText = "Edit"
    editButton.style.display = "block"

    // Set the dynamic marginTop
    adjustContactInfo()
}

// Script to set dynamic marginTop adjustment for contact information
const adjustContactInfo = () => {
    let contactInfo = document.getElementById("contact-info")
    let addressText = document.getElementById("text_address")
    let addressInput = document.getElementById("input_address")

    if (addressText.style.display === "block") {
        contactInfo.style.marginTop = "0px";
    } else if (addressInput.style.display === "block") {
        contactInfo.style.marginTop = "-115px";
    } else {
        contactInfo.style.marginTop = "0px";
    }
}

window.onload = adjustContactInfo;

const updateTotalPrice = (quantityId) => {
    let priceElement = document.querySelector('.product-price[data-id="' + quantityId + '"]')
    let priceText = priceElement.innerText.trim().replace('Rp.', '')
    let price = parseFloat(priceText.split('.').join(''))
    console.log('product price:', price);

    let quantity = parseInt(document.getElementById('quantity' + quantityId).innerText)
    console.log('quantity:', quantity);

    let totalPrice = price * quantity
    let totalPriceElement = document.getElementById('totalPrice' + quantityId)
    totalPriceElement.innerText = 'Rp.' + totalPrice.toLocaleString('id-ID', {useGrouping: true})
    totalPriceElement.style.fontWeight = '500'

    // Return totalPrice so can be used out of the function
    // return totalPrice;
    return price;
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
}

// ShippingChoices
document.addEventListener('DOMContentLoaded', function() {
    let shippingField = document.querySelector('.form-1 select')
})

// Hide Delivery Types in a pop up
document.getElementById('pilihButton').addEventListener('click', function() {
    document.getElementById('popupForm').style.display = 'block';
    document.getElementById('pilihButton').style.display = 'none';

    // Hide delivery types when popupForm is displayed
    document.querySelectorAll('.selectedValue, .formattedPrice, .estimatedTime, .estimated-Time').forEach(element => {
        element.style.display = 'none';
    })
});



// Make the 'choose' button in a dynamic positions
document.addEventListener('DOMContentLoaded', function() {
    let showDelivery = document.getElementById('showDelivery');
    let pilihButton = document.getElementById('pilihButton');

    // Function to check if the showDelivery div has content
    function checkShowDeliveryContent() {
        if (showDelivery.innerHTML.trim().length > 0) {
            // If content exists, add margin-left to pilihButton
            pilihButton.style.transform = 'translate(150px, -20px)';
        } else {
            // If no content exists, reset margin-left to default value
            pilihButton.style.marginLeft = '20px';
        }
    }

    // Call the function initially
    checkShowDeliveryContent();

    // Listen for changes in the showDelivery div content
    showDelivery.addEventListener('DOMSubtreeModified', function() {
        // Call the function whenever the content changes
        checkShowDeliveryContent();
    })
})


// START CALCULATE TOTAL PAYMENT



// Total Payment ({Product * quantity} + shippingPayment)
// Quantity id

document.addEventListener('DOMContentLoaded', () => {
    // Product price Id
    let priceElement = document.querySelector('.product-price[data-id]');
    let quantityId = priceElement.dataset.id;
    console.log('id:', quantityId)

    // VERSI 1
    // let productPaymentPrice = updateTotalPrice(quantityId);
    // console.log('product prices:', productPaymentPrice);

    // VERSI 2
    let price = updateTotalPrice(quantityId);
    console.log('price:', price);


    // Get quantity
    let quantityPaymentPrice = parseInt(document.getElementById('quantity' + quantityId).innerText)
    console.log('quantity Price Awal:', quantityPaymentPrice);

    // Add event listener on the + & - button
    document.getElementById('quantity' + quantityId).addEventListener('click', () => {
        let quantityPaymentPrice = updateTotalPrice(quantityId);
        console.log('quantity Price Akhir:', quantityPaymentPrice);
    })

    // quantityElement.addEventListener('click', () => {
    //     let quantityPayment = updateTotalPrice(quantityId);
    //     console.log('quantity Payment:', quantityPayment);
    // })
        // console.log('product Price:', productPaymentPrice);
    // let quantityPaymentPrice = parseInt(document.getElementById('quantity{{ product.id }}').innerText);
    // console.log('product Quantity:', quantityPaymentPrice);

    // Shipping versi 1
    // let shippingPaymentPrice = parseFloat(document.querySelector('#popupForm input[name="delivery_type"]:checked + label + span').innerText.replace(/[^\d.-]/g, ''));
    // console.log('Shipping price:', shippingPaymentPrice)

    // Shipping versi 2
    // let selectedValue = document.querySelector('input[name="delivery_type"]:checked');
    // console.log('The selected option:', selectedValue)
    // // Show selected delivery option
    // if (selectedValue.value === 'Regular') {
    //     console.log('yang dipilih:', selectedValue)
    //     let formattedPrice = selectedValue.nextElementSibling.nextElementSibling.textContent;
    //     console.log('Formatted Price:', formattedPrice);
    // } else if (selectedValue.value === 'Fast') {
    //     console.log('yang dipilih:', selectedValue)
    //     let formattedPrice = selectedValue.nextElementSibling.nextElementSibling.textContent;
    //     console.log('Formatted Price:', formattedPrice);
    // } else if (selectedValue.value === 'Cargo') {
    //     console.log('yang dipilih:', selectedValue)
    //     let formattedPrice = selectedValue.nextElementSibling.nextElementSibling.textContent;
    //     console.log('Formatted Price:', formattedPrice);
    // }

    // // ---------------------//
    // let totalPricePayment = (productPaymentPrice * quantityPaymentPrice) + shippingPaymentPrice;
    // console.log('Total Price Payment:', totalPricePayment)
    // // Show price total in HTML element
    // let showTotalPayment = document.querySelector('.totalPayment');
    // showTotalPayment.innerHTML = '<p>Rp.' + totalPricePayment + '</p>';
})

// END CALCULATE TOTAL PAYMENT

// Show Payment(Midtrans) pop-up display
document.getElementById('showPaymentButton').addEventListener('click', function() {
    // Show the payment form
    document.getElementById('paymentForm').style.display = 'block';

    // Call API to fetch payment method dynamically
    fetchPaymentMethods();
});

// Function to fetch payment methods from API
const fetchPaymentMethods = () => {
    fetch('https://app.sandbox.midtrans.com/snap/v1/transactions')
        .then(response => response.json())
        .then(data => {
            let paymentMethodsDiv = document.getElementById('paymentMethods');
            paymentMethodsDiv.innerHTML = '';
            data.payment_methods.forEach(method => {
                let radioInput = document.createElement('input');
                radioInput.type = 'radio';
                radioInput.name = 'payment_method';
                radioInput.value = method.id; //Use the appropriate identifier from the API response
                let label = document.createElement('label');
                label.htmlFor = method.id;
                label.textContent = method.name //Use the appropriate field from the API response
                let div = document.createElement('div');
                div.classList.add('chooseTypes');
                div.appendChild(radioInput);
                div.appendChild(label);
                paymentMethodsDiv.appendChild(div);
            });
        })
        .catch(error => console.error('Error fetching payment methods:', error));
}

// Event listener for saving selected payment method and close the popUp
document.getElementById('paymentButton').addEventListener('click', function() {
    // Get the selected payment method
    let selectedMethod = document.querySelector('input[name="payment_method"]:checked');
    if (selectedMethod) {
        // Perform action to save the selected payment method
        console.log('Selected payment method:', selectedMethod.value);

        // Close the payment popup
        document.getElementById('paymentForm').style.display = 'none';
    } else {
        alert('Please select a payment method.');
    }
});

// Get data quantity
let quantityProduct = document.getElementById('quantity{{ product.id }}');
let productType = quantityProduct.dataset.productType; //Get productType value

if (productType === 'smartphone') {
    let quantity = quantityProduct;
} else if (productType === 'food') {
    let quantity = quantityProduct;
} else {
    let quantity = 0;
}

// Send data to Django used AJAX
let xhr = new XMLHttpRequest();
xhr.open("POST", "/create_transaction", true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = () => {
    if (xhr.readyState === 4 && xhr.status === 200) {
        let response = JSON.parse(xhr.responseText);
        console.log(response);
    }
};
let data = JSON.stringify({
    product_type: productType,
    quantity: quantity, //Send quantity value to server
});
xhr.send(data);
