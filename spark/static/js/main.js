document.addEventListener("DOMContentLoaded", function () {
    const videoImg = document.getElementById("videoFeed");
    const toggleButton = document.getElementById("toggleCamera");

    let cameraOn = true;
    const videoURL = videoImg.src; // Guarda la URL original

    toggleButton.addEventListener("click", function () {
        cameraOn = !cameraOn;

        if (cameraOn) {
            // Recarga el stream con un parámetro temporal para evitar caché
            videoImg.src = videoURL + "?t=" + new Date().getTime();
            toggleButton.textContent = "Desactivar Cámara";
        } else {
            videoImg.src = ""; // Detiene el stream visualmente
            toggleButton.textContent = "Activar Cámara";
        }
    });
});