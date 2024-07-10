let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.primerCarrusel img');
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    const offset = -currentSlide * 100;
    document.querySelector('.primerCarrusel').style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}



// Auto-slide
setInterval(() => {
    nextSlide();
}, 3000); // Cambia de imagen cada 3 segundos



function formularioCambio(){
    var x = document.getElementsByClassName("form")
    x[0].innerHTML =("<h1>Gracias por su compra..</h1>")
}
document.addEventListener("DOMContentLoaded", function() {
    let currentSlide = 0;
    const slides = document.querySelectorAll(".slide");

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.remove("active");
            if (i === index) {
                slide.classList.add("active");
            }
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    setInterval(nextSlide, 2000); // Cambia de imagen cada 3 segundos
});