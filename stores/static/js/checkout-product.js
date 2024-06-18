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
    return totalPrice;
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

// ShippingChoices
document.addEventListener('DOMContentLoaded', () => {
    let shippingField = document.querySelector('.form-1 select')
})

// Hide Delivery Types in a pop up
document.getElementById('pilihButton').addEventListener('click', () => {
    document.getElementById('popupForm').style.display = 'block';
    document.getElementById('pilihButton').style.display = 'none';

    // Hide delivery types when popupForm is displayed
    document.querySelectorAll('.selectedValue, .formattedPrice, .estimatedTime, .estimated-Time').forEach(element => {
        element.style.display = 'none';
    })
});


// Make the 'choose' button in a dynamic positions
document.addEventListener('DOMContentLoaded', () => {
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
    const observer = new MutationObserver((mutationsList) => {
        // Call the function whenever the content changes
        checkShowDeliveryContent();
    });

    // Configure the observer to listen for changes
    const config = { childList: true, subtree: true };

    // Start observing the target for configured mutations
    observer.observe(showDelivery, config);
})


// Show Payment(Midtrans) pop-up display
document.getElementById('showPaymentButton').addEventListener('click', () => {
    // Show the payment form
    document.getElementById('paymentForm').style.display = 'block';

    // VERSI NEW
    const paymentButton = document.querySelector('.payment-button')
    
    // Send data (product/items & totalPrice) when checkout(beli) button is clicked
    paymentButton.addEventListener('click', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const objectData = {};
        formData.forEach((value, key) => {
            objectData[key] = value;
        });
        console.log(objectData);

        // Modify into JSON format
        const requestData = {
            ...objectData,
            items: JSON.parse(objectData.items),
        };

        // Getting transaction tokens with ajax/fetch
        try {
            // const response = await fetch('/create_transaction', {
            const response = await fetch('http://localhost:5000/create_transaction', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestData),
            });
            const result = await response.json();
            const token = result.transaction_token;
            // console.log(token)
            window.snap.pay(token);
        } catch (error) {
            console.log(error.message)
        }
    })
});


// Event listener for saving selected payment method and close the popUp
document.getElementById('paymentButton').addEventListener('click', () => {
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

