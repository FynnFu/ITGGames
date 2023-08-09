const copyUrlButton = document.getElementById('copy_url')

copyUrlButton.addEventListener('click', function () {
    const currentUrl = window.location.href;

    const tempTextarea = document.createElement('textarea');
    tempTextarea.value = currentUrl;
    document.body.appendChild(tempTextarea);
    tempTextarea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextarea);

    var spanElement = copyUrlButton.querySelector('span');
    var iElement = copyUrlButton.querySelector('i');
    iElement.classList.replace('fa-clipboard', 'fa-circle-check');
    spanElement.textContent = 'Copied';
    setTimeout(function() {
        spanElement.textContent = 'Copy URL';
        iElement.classList.replace('fa-circle-check', 'fa-clipboard');
    }, 1500); // 1.5 секунды
});

document.addEventListener('DOMContentLoaded', function() {
    const sortSelect = document.getElementById('sort-by');

    // Получаем текущее значение параметра sort_by из URL
    const urlParams = new URLSearchParams(window.location.search);
    const currentSortBy = urlParams.get('sort_by');

    // Устанавливаем выбранный вариант в элементе select
    if (currentSortBy) {
        for (let i = 0; i < sortSelect.options.length; i++) {
            if (sortSelect.options[i].value === currentSortBy) {
                sortSelect.options[i].selected = true;
                break;
            }
        }
    }

    sortSelect.addEventListener('change', function() {
        const selectedValue = this.value;

        // Создаем новый URL с GET параметром sort_by
        const currentUrl = new URL(window.location.href);
        currentUrl.searchParams.set('sort_by', selectedValue);

        // Перенаправляем пользователя на новый URL
        location.replace(currentUrl);
    });




});

document.addEventListener('DOMContentLoaded', function() {
    const sortSelectDirection = document.getElementById('sort-direction');

    // Получаем текущее значение параметра sort_direction из URL
    const urlParams = new URLSearchParams(window.location.search);
    const currentSortDirection = urlParams.get('sort_direction');

    // Устанавливаем выбранный вариант в элементе select
    if (currentSortDirection) {
        for (let i = 0; i < sortSelectDirection.options.length; i++) {
            if (sortSelectDirection.options[i].value === currentSortDirection) {
                sortSelectDirection.options[i].selected = true;
                break;
            }
        }
    }

    sortSelectDirection.addEventListener('change', function() {
        const selectedValue = this.value;

        // Создаем новый URL с GET параметром sort_direction
        const currentUrl = new URL(window.location.href);

        currentUrl.searchParams.set('sort_direction', selectedValue);

        // Перенаправляем пользователя на новый URL
        location.replace(currentUrl);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const newsElements = document.querySelectorAll('.news');
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5, // Порог видимости
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                // Новость стала видимой
                const newsId = entry.target.getAttribute('data-news-id');
                markNewsAsViewed(newsId);
            }
        });
    }, options);

    newsElements.forEach(function(newsElement) {
        observer.observe(newsElement);
    });

    function markNewsAsViewed(newsId) {
        $.ajax({
            url: markNewsViewedUrl,
            method: 'POST',
            data: {
                newsId: newsId,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(data) {
                const newsElement = document.querySelector(`.news[data-news-id="${newsId}"]`);
                const viewsSpan = newsElement.querySelector('.views span');
                viewsSpan.textContent = data.views_count;
                console.log('News marked as viewed.');
            },
            error: function(data) {
                console.log('Error marking news as viewed.');
            },
        });
    }
});