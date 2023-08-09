    function handlePageRefresh() {
        console.log("Страница была обновлена!");
        // Получаем элемент iframe
        const youtubePlayer = document.getElementById('youtubePlayer');

        // Извлекаем идентификатор видео из URL
        const videoId = youtubePlayer.src.split('/').pop();
        // Создаем прямую ссылку на видео
        const directVideoUrl = `https://www.youtube.com/watch?v=${videoId}`;
        // Ваш API ключ YouTube Data API
        const apiKey = 'AIzaSyD2VHl37fzQGH5ruIiJ0Gtdkk61mqlt7F0';

        // Формируем URL для запроса к YouTube Data API
        const apiUrl = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${apiKey}`;

        // Выполняем запрос к YouTube Data API
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Получаем URL превью видео (максимального качества доступного на YouTube)
                const previewUrl = data.items[0].snippet.thumbnails.maxres.url;

                // Создаем элемент img для отображения превью видео
                const imgElement = document.createElement('img');
                imgElement.src = previewUrl;
                var mediaQuery = window.matchMedia('(max-width: 1024px)');

                // Функция для обработки изменения состояния медиа-запроса
                function handleMediaQueryChange(mediaQuery) {
                    if (mediaQuery.matches) {
                        // Применяем свойства только если медиа-запрос срабатывает
                        imgElement.style.width = '320px';
                        imgElement.style.height = '180px';
                    } else {
                       // Если медиа-запрос не срабатывает, можем применить другие стили или оставить без изменений
                        imgElement.style.width = '160px';
                        imgElement.style.height = '90px';
                    }
                }
                handleMediaQueryChange(mediaQuery);
                mediaQuery.addListener(handleMediaQueryChange);
                // Добавляем imgElement в контейнер previewContainer
                const previewContainer = document.getElementById('videoPreview');
                previewContainer.appendChild(imgElement);
            })
            .catch(error => {
                console.error('Произошла ошибка при получении превью видео:', error);
            });
        console.log("Прямая ссылка на видео:", directVideoUrl);
    }
    // Добавляем слушатель события "beforeunload" к объекту window
    window.addEventListener('DOMContentLoaded', handlePageRefresh);


    const videoPreview = document.getElementById('videoPreview');
    videoPreview.addEventListener('click', function () {
        const videoPreviewContainer = document.getElementById('videoPreviewContainer');
        videoPreviewContainer.hidden = false;
        const imagePreviewContainer = document.getElementById('imagePreviewContainer');
        imagePreviewContainer.hidden = true;
    });


    const thumbnails = document.querySelectorAll('.thumbnail');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function(event) {
        // Заменяем содержимое div на изображение
        const videoPreviewContainer = document.getElementById('videoPreviewContainer');
            videoPreviewContainer.hidden = true;
            const imagePreviewContainer = document.getElementById('imagePreviewContainer');
            imagePreviewContainer.hidden = false;
            imagePreviewContainer.innerHTML = '';
            imagePreviewContainer.appendChild(event.target.cloneNode());
        });
    });

    // Функция для переключения информации по системам
    function showSystemInfo(system) {
        const systemInfos = document.querySelectorAll('.system-info');
        systemInfos.forEach(info => {
            info.style.display = 'none';
        });
        document.getElementById('system-info-' + system).style.display = 'block';
    }

    // Обработчики событий для кнопок
    const systemButtons = document.querySelectorAll('.system-button');
    systemButtons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedSystem = button.getAttribute('data-system');
            showSystemInfo(selectedSystem);
        });
    });

// Добавление css файла в IFRAME
window.onload = () => {


}

