// jQuery 4.0 Standard: Usar shorthand $(function(){}) en lugar de $(document).ready()
$(function() {
    
    // ==========================================
    // 0. INYECCIÓN DE CONTENIDO (DOM MANIPULATION)
    // ==========================================
    
    // --- A. Texto About Me ---
    const aboutParagraphs = [
        "Land surveying Technician and Full Stack Java, JavaScript & Python developer with a solid base in web technologies such as <strong>HTML, CSS and JavaScript. Experienced in Bootstrap, MySQL, JQuery, Java, Spring Boot Node.js, express.js PostgreSQL, Python, React, Django and SQLite.</strong>",
        "I am a professional who is committed to permanent development, with strong technical skills and work ethics, focused on creating efficient solutions to complex challenges.",
        "My innate curiosity drives me to constantly explore new technologies and approaches, ensuring that I keep my knowledge up to date in a dynamic and constantly evolving environment. Among my strengths, I can highlight my open-mindedness and flexibility in my approach to work, which allows me to tackle projects from different perspectives and adapt quickly to change when necessary. Also, my perseverance and determination drive me to successfully achieve my goals, as I face challenges head-on until I find effective solutions.",
        "I stand out for my analytical skills and critical thinking, with a meticulous approach at every stage of development. Persistence is one of my greatest strengths as I face challenges with determination to find effective solutions.",
        "I am eager to contribute to the success of challenging and dynamic projects."
    ];

    const aboutContainer = $('#about-content');
    if (aboutContainer.length) {
        const elements = aboutParagraphs.map(text => $('<p>').html(text));
        aboutContainer.append(elements);
    }

    // --- B. Formulario de Contacto ---
    // Inyectamos el HTML completo del formulario
    const contactFormHTML = `
        <form action="https://formspree.io/f/mandqroa" class="w-75 mx-auto" id="contact-form" method="post">
            <div class="mb-3">
                <label for="contact-name" class="form-label">Name: </label>
                <input type="text" class="form-control" id="contact-name" name="nombre" placeholder="Your Name" required>
            </div>
            <div class="mb-3">
                <label for="contact-subject" class="form-label">Subject:</label>
                <input type="text" class="form-control" id="contact-subject" name="asunto" placeholder="Subject" required>
            </div>
            <div class="mb-3">
                <label for="contact-email" class="form-label">Email: </label>
                <input type="email" class="form-control" id="contact-email" name="correo" placeholder="name@example.com" required>
            </div>
            <div class="mb-3">
                <label for="contact-message" class="form-label">Message:</label>
                <textarea name="message" id="contact-message" class="form-control" placeholder="Your message here..." required></textarea>
            </div>
            <div class="py-3">
                <input type="submit" class="btn btn-light text-uppercase" value="Send">
            </div>
        </form>
    `;

    const formContainer = $('#contact-form-container');
    if (formContainer.length) {
        formContainer.html(contactFormHTML);
    }

    // ==========================================
    // 1. FUNCIONALIDADES UI
    // ==========================================

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
    sections.addClass('fade-in-section');

    function checkVisibility() {
        const triggerBottom = $(window).height() * 0.85; 
        sections.each(function() {
            const top = this.getBoundingClientRect().top;
            if (top < triggerBottom) {
                $(this).addClass('is-visible');
            }
        });
    }

    $(window).on('scroll', checkVisibility);
    checkVisibility(); 

    // ==========================================
    // 2. VALIDACIÓN (Debe ir DESPUÉS de la inyección)
    // ==========================================
    
    // Al inyectar el form antes, JQuery puede encontrar '#contact-form' sin problemas
    $("#contact-form").on('submit', function(event) {
        const nombreVal = $("#contact-name").val();
        const asuntoVal = $("#contact-subject").val();
        const mensajeVal = $("#contact-message").val();
        
        const nombre = nombreVal ? nombreVal.trim() : "";
        const asunto = asuntoVal ? asuntoVal.trim() : "";
        const mensaje = mensajeVal ? mensajeVal.trim() : "";
        
        // Validación básica
        if (nombre.length < 8 || asunto.length < 8 || mensaje.length < 15) {
            event.preventDefault(); 
            alert("Por favor revisa los campos:\n- Nombre: mínimo 8 caracteres\n- Asunto: mínimo 8 caracteres\n- Mensaje: mínimo 15 caracteres");
            return false;
        }
        return true;
    });

});