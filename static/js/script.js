// jQuery 4.0 Standard: Usar shorthand $(function(){}) en lugar de $(document).ready()
$(function() {

    // 1. Activar Tooltips (Bootstrap 5)
    $('[data-bs-toggle="tooltip"]').tooltip();
    
    // --- Lógica del Selector de Temas ---
    const body = $('body');
    const btnDefault = $('#btn-theme-default');
    const btnAlt = $('#btn-theme-alt');

    // Función única para cambiar el tema visualmente
    function setThemeState(themeName) {
        if (themeName === 'alternative') {
            body.addClass('theme-alternative');
            btnAlt.addClass('active');
            btnDefault.removeClass('active');
        } else {
            body.removeClass('theme-alternative');
            btnDefault.addClass('active');
            btnAlt.removeClass('active');
        }
    }

    // Cargar tema guardado al iniciar (Persistencia)
    const savedTheme = localStorage.getItem('portfolioTheme');
    if (savedTheme) {
        setThemeState(savedTheme);
    }

    // Eventos de clic
    // JQUERY 4.0 UPDATE: Se prefieren .on('click') sobre .click()
    btnDefault.on('click', function() {
        setThemeState('default');
        localStorage.setItem('portfolioTheme', 'default');
    });

    btnAlt.on('click', function() {
        setThemeState('alternative');
        localStorage.setItem('portfolioTheme', 'alternative');
    });

    // --- Animación Fade-In al hacer Scroll ---
    const sections = $('#projects, #skills, #contact');
    
    // Les agregamos la clase base CSS
    sections.addClass('fade-in-section');

    // Función para verificar si un elemento está en pantalla
    function checkVisibility() {
        const triggerBottom = $(window).height() * 0.85; // Se activa al 85% de la pantalla

        sections.each(function() {
            // Optimización: 'this' ya es el elemento DOM nativo
            const top = this.getBoundingClientRect().top;
            
            if (top < triggerBottom) {
                $(this).addClass('is-visible');
            }
        });
    }

    // Ejecutar al cargar y al hacer scroll
    $(window).on('scroll', checkVisibility);
    checkVisibility(); // Ejecutar un chequeo inicial

    // Validación del formulario
    // JQUERY 4.0 UPDATE: Se prefiere .on('submit') sobre .submit()
    $("#contact-form").on('submit', function(event) {
        const nombreVal = $("#contact-name").val();
        const asuntoVal = $("#contact-subject").val();
        const mensajeVal = $("#contact-message").val();
        
        // JQUERY 4.0 UPDATE: Usar .trim() nativo de JS en lugar de utilidades deprecadas
        // Esto evita que espacios en blanco pasen como válidos
        const nombre = nombreVal ? nombreVal.trim() : "";
        const asunto = asuntoVal ? asuntoVal.trim() : "";
        const mensaje = mensajeVal ? mensajeVal.trim() : "";
        
        // Validación básica
        if (nombre.length < 8 || asunto.length < 8 || mensaje.length < 15) {
            event.preventDefault(); // Método estándar para evitar el envío
            alert("Por favor revisa los campos:\n- Nombre: mínimo 8 caracteres\n- Asunto: mínimo 8 caracteres\n- Mensaje: mínimo 15 caracteres");
            return false;
        }
        return true;
    });

});