document.addEventListener("DOMContentLoaded", function() {
    // Find all navbar links in the header
    const navLinks = document.querySelectorAll('.bd-header .navbar-nav a.nav-link');
    
    navLinks.forEach(link => {
        // If the link text is "Tutorials", force the active styling
        if (link.textContent.trim().toLowerCase() === 'tutorials') {
            link.style.setProperty('color', 'var(--pst-color-text-base)', 'important');
            link.style.setProperty('font-weight', '600', 'important');
            link.classList.add('active');
        }
    });
});

