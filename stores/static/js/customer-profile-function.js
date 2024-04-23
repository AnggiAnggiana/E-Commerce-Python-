// Change profile picture
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('file-upload').addEventListener('change', function() {
        let file = this.files[0]
        if (file) {
            let reader = new FileReader()
            reader.onload = function(e) {
                document.querySelector('.size-profile-picture').src = e.target.result
            }
            reader.readAsDataURL(file)
        }
    })
})