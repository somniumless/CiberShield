const preguntas = document.querySelectorAll('.faq-pregunta');
preguntas.forEach(pregunta => {
    pregunta.addEventListener('click', () => {
        pregunta.classList.toggle('active');
        const respuesta = pregunta.nextElementSibling;
        respuesta.classList.toggle('active');
    });
});