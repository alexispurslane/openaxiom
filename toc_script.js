document.addEventListener('DOMContentLoaded', function() {
    const toc = document.getElementById('TOC');
    
    if (toc) {
        // Create toggle button
        const toggleButton = document.createElement('button');
        toggleButton.id = 'toc-toggle';
        toggleButton.textContent = 'Table of Contents';
        toggleButton.setAttribute('aria-expanded', 'true');
        
        // Insert toggle button at the beginning of TOC
        toc.insertBefore(toggleButton, toc.firstChild);
        
        // Add click event to toggle collapsed state
        toggleButton.addEventListener('click', function() {
            toc.classList.toggle('collapsed');
            const isCollapsed = toc.classList.contains('collapsed');
            toggleButton.setAttribute('aria-expanded', isCollapsed ? 'false' : 'true');
        });
    }
});