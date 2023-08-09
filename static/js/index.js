const menuButton = document.getElementById('menu-button');
const menu = document.getElementById('menu');

// Добавляем обработчик события "click" для кнопки меню
menuButton.addEventListener('click', function() {
    if (menu.style.display === 'grid') {
        // Если меню отображено, скрываем его
        menu.style.opacity = '0';
        setTimeout(function() {
            menu.style.display = 'none';
        }, 500); // Задержка для анимации
    } else {
        // Если меню скрыто, отображаем его
        menu.style.display = 'grid';
        setTimeout(function() {
            menu.style.opacity = '1';
        }, 500); // Задержка для анимации
    }
});