document.addEventListener('DOMContentLoaded', () => {
    let categoryField = document.querySelector('.form1 select')
    let smartphoneField = document.getElementById('smartphoneForm')
    let smartphoneCategoriesForm = document.querySelector('.form14 select')
    let foodField = document.getElementById('foodForm')

    categoryField.addEventListener('change', function() {
        console.log(categoryField.value)
        // console.log(smartphoneCategoriesForm.value)
        if (categoryField.value === 'Smartphone') {
            console.log('ini smartphone')
            smartphoneField.style.display = 'block'
            foodField.style.display = 'none'
        } else if (categoryField.value === 'Foods') {
            console.log('ini makanan')
            foodField.style.display = 'block'
            smartphoneField.style.display = 'none'
        } else {
            smartphoneField.style.display = 'none'
            foodField.style.display = 'none'
        }
    })
})