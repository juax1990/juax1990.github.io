document.getElementById("registroForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let archivo = document.getElementById("archivo").files[0];
    let mensajeError = document.getElementById("mensajeError");

    if (archivo) {
        let extension = archivo.name.split('.').pop().toLowerCase();
        if (["jpg", "jpeg", "pdf"].includes(extension)) {
            mensajeError.textContent = "";
            alert("Datos enviados ¡Bienvenido!");
        } else {
            mensajeError.textContent = "Solo se permiten archivos JPG, JPEG o PDF.";
        }
    } else {
        mensajeError.textContent = "Por favor, sube un archivo válido.";
    }
});

// Menú hamburguesa
const menuToggle = document.getElementById("menu-toggle");
const menu = document.querySelector(".menu");

menuToggle.addEventListener("click", () => {
    menu.classList.toggle("show");

    if (menu.classList.contains("show")) {
        menuToggle.textContent = "✖"; // Mostrar la X
    } else {
        menuToggle.textContent = "☰"; // Mostrar hamburguesa
    }
});

// Botón Ir Arriba
const btnTop = document.getElementById("btnTop");

window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        btnTop.classList.add("show");
    } else {
        btnTop.classList.remove("show");
    }
};

btnTop.addEventListener("click", function() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});
 