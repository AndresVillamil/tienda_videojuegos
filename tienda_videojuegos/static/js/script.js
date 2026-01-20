document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('toggle-theme');
    const html = document.documentElement;
    const STORAGE_KEY = 'bs-theme';

    if (!btn) return;

    // Aplicar tema guardado al cargar
    const savedTheme = localStorage.getItem(STORAGE_KEY);
    if (savedTheme) {
        html.setAttribute('data-bs-theme', savedTheme);
    }

    btn.addEventListener('click', function () {
        const currentTheme = html.getAttribute('data-bs-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        html.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem(STORAGE_KEY, newTheme);
    });
});
