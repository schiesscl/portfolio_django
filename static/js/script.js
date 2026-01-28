// jQuery 4.0 Standard: Usar shorthand $(function(){})
$(function() {
    
    // --- 0. INYECCIÓN DE CONTENIDO (DOM MANIPULATION + I18N) ---
    
    // A. Texto About Me (gettext() para traducción)
    const aboutParagraphs = [
        gettext("Land surveying Technician and Full Stack Java, JavaScript & Python developer with a solid base in web technologies such as <strong>HTML, CSS and JavaScript. Experienced in Bootstrap, MySQL, JQuery, Java, Spring Boot Node.js, express.js PostgreSQL, Python, React, Django and SQLite.</strong>"),
        gettext("I am a professional who is committed to permanent development, with strong technical skills and work ethics, focused on creating efficient solutions to complex challenges."),
        gettext("My innate curiosity drives me to constantly explore new technologies and approaches, ensuring that I keep my knowledge up to date in a dynamic and constantly evolving environment. Among my strengths, I can highlight my open-mindedness and flexibility in my approach to work, which allows me to tackle projects from different perspectives and adapt quickly to change when necessary. Also, my perseverance and determination drive me to successfully achieve my goals, as I face challenges head-on until I find effective solutions."),
        gettext("I stand out for my analytical skills and critical thinking, with a meticulous approach at every stage of development. Persistence is one of my greatest strengths as I face challenges with determination to find effective solutions."),
        gettext("I am eager to contribute to the success of challenging and dynamic projects.")
    ];

    const aboutContainer = $('#about-content');
    if (aboutContainer.length) {
        aboutContainer.append(aboutParagraphs.map(text => $('<p>').html(text)));
    }

    // B. Formulario de Contacto (gettext() para traducción)
    const lblName = gettext("Name:");
    const phName = gettext("Your Name");
    const lblSubject = gettext("Subject:");
    const phSubject = gettext("Subject");
    const lblEmail = gettext("Email:");
    const phEmail = "name@example.com";
    const lblMessage = gettext("Message:");
    const phMessage = gettext("Your message here...");
    const btnSend = gettext("Send");

    const contactFormHTML = `
        <form action="https://formspree.io/f/mandqroa" class="w-75 mx-auto" id="contact-form" method="post">
            <div class="mb-3">
                <label for="contact-name" class="form-label">${lblName}</label>
                <input type="text" class="form-control" id="contact-name" name="nombre" placeholder="${phName}" required>
            </div>
            <div class="mb-3">
                <label for="contact-subject" class="form-label">${lblSubject}</label>
                <input type="text" class="form-control" id="contact-subject" name="asunto" placeholder="${phSubject}" required>
            </div>
            <div class="mb-3">
                <label for="contact-email" class="form-label">${lblEmail}</label>
                <input type="email" class="form-control" id="contact-email" name="correo" placeholder="${phEmail}" required>
            </div>
            <div class="mb-3">
                <label for="contact-message" class="form-label">${lblMessage}</label>
                <textarea name="message" id="contact-message" class="form-control" placeholder="${phMessage}" required></textarea>
            </div>
            <div class="py-3">
                <input type="submit" class="btn btn-light text-uppercase" value="${btnSend}">
            </div>
        </form>
    `;

    const formContainer = $('#contact-form-container');
    if (formContainer.length) {
        formContainer.html(contactFormHTML);
    }

    // --- 1. UI Y FUNCIONALIDAD ---

    $('[data-bs-toggle="tooltip"]').tooltip();
    
    // Selector de Temas
    const body = $('body');
    const btnDefault = $('#btn-theme-default');
    const btnAlt = $('#btn-theme-alt');

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

    const savedTheme = localStorage.getItem('portfolioTheme');
    if (savedTheme) { setThemeState(savedTheme); }

    btnDefault.on('click', () => { setThemeState('default'); localStorage.setItem('portfolioTheme', 'default'); });
    btnAlt.on('click', () => { setThemeState('alternative'); localStorage.setItem('portfolioTheme', 'alternative'); });

    // Scroll Fade-In
    const sections = $('#projects, #skills, #contact');
    sections.addClass('fade-in-section');

    function checkVisibility() {
        const triggerBottom = $(window).height() * 0.85; 
        sections.each(function() {
            if (this.getBoundingClientRect().top < triggerBottom) { $(this).addClass('is-visible'); }
        });
    }
    $(window).on('scroll', checkVisibility);
    checkVisibility(); 

    // --- 2. VALIDACIÓN DE FORMULARIO ---
    
    $("#contact-form").on('submit', function(event) {
        const nombreVal = $("#contact-name").val();
        const asuntoVal = $("#contact-subject").val();
        const mensajeVal = $("#contact-message").val();
        
        const nombre = nombreVal ? nombreVal.trim() : "";
        const asunto = asuntoVal ? asuntoVal.trim() : "";
        const mensaje = mensajeVal ? mensajeVal.trim() : "";
        
        if (nombre.length < 8 || asunto.length < 8 || mensaje.length < 15) {
            event.preventDefault();
            alert(gettext("Please check the fields:\n- Name: minimum 8 characters\n- Subject: minimum 8 characters\n- Message: minimum 15 characters"));
            return false;
        }
        return true;
    });
});
