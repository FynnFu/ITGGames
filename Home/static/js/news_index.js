document.addEventListener('DOMContentLoaded', function() {
    const upButtons = document.querySelectorAll('.up-i');

    upButtons.forEach(function(button) {
        var news_id = $(button).closest('.news').data('news-id');
        var isUpVoted = getCookie(`upvoted_${news_id}`);

        if (isUpVoted === 'true') {
            $(button).closest('.news').find('.up').css('color', 'green');
        }
    });

    const  downButtons = document.querySelectorAll('.down-i');

    downButtons.forEach(function(button) {
        var news_id = $(button).closest('.news').data('news-id');
        var isDownVoted = getCookie(`downvoted_${news_id}`);

        if (isDownVoted === 'true') {
            $(button).closest('.news').find('.down').css('color', 'red');
        }
    });
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}

const upButtons = document.querySelectorAll('.up-i');

upButtons.forEach(function(button) {
    button.addEventListener('click', function() {
            var news_id = $(this).closest('.news').data('news-id');
            var upSpan = $(this).closest('.news').find('.up span');
            var downSpan = $(this).closest('.news').find('.down span');
            var upI = $(this).closest('.news').find('.up');
            var downI = $(this).closest('.news').find('.down');

            var isUpVoted = getCookie('upvoted_' + news_id);
            var isDownVoted = getCookie('downvoted_' + news_id);


            $.ajax({
                url: upUrl,
                type: "POST",
                data: {
                    id: news_id,
                    isUpVoted: isUpVoted,
                    isDownVoted: isDownVoted,
                    csrfmiddlewaretoken: csrfToken,
                },
                success: function (data) {
                    upSpan.text(data.up_count);
                    if (isUpVoted) {
                        document.cookie = `upvoted_${news_id}=; path=/`;
                        upI.css('color', '');
                    } else {
                        document.cookie = `upvoted_${news_id}=true; path=/`;
                        upI.css('color', 'green');
                        if (isDownVoted) {
                            document.cookie = `downvoted_${news_id}=; path=/`;
                            downI.css('color', '');
                            downSpan.text(data.down_count);
                        }
                    }
                    console.log(`Sequence updated successfully. Cookie: ${isUpVoted}`);
                    },
                error: function (data) {
                    console.log("Error updating sequence.");
                },
            });
    });
});


const downButtons = document.querySelectorAll('.down-i');

downButtons.forEach(function(button) {
    button.addEventListener('click', function() {
            var news_id = $(this).closest('.news').data('news-id');
            var upSpan = $(this).closest('.news').find('.up span');
            var downSpan = $(this).closest('.news').find('.down span');
            var upI = $(this).closest('.news').find('.up');
            var downI = $(this).closest('.news').find('.down');

            var isUpVoted = getCookie('upvoted_' + news_id);
            var isDownVoted = getCookie('downvoted_' + news_id);

            $.ajax({
                url: downUrl,
                type: "POST",
                data: {
                    id: news_id,
                    isUpVoted: isUpVoted,
                    isDownVoted: isDownVoted,
                    csrfmiddlewaretoken: csrfToken,
                },
                success: function (data) {
                    downSpan.text(data.down_count);
                    if (isDownVoted) {
                        document.cookie = `downvoted_${news_id}=; path=/`;
                        downI.css('color', '');
                    } else {
                        document.cookie = `downvoted_${news_id}=true; path=/`;
                        downI.css('color', 'red');
                        if (isUpVoted) {
                            document.cookie = `upvoted_${news_id}=; path=/`;
                            upI.css('color', '');
                            upSpan.text(data.up_count);
                        }
                    }
                    console.log(`Sequence updated successfully. Cookie: ${isDownVoted}`);
                    },
                error: function (data) {
                    console.log("Error updating sequence.");
                },
            });
        });
});





const thumbnails = document.querySelectorAll('.thumbnail');
const imagePreviewContainer = document.getElementById('imagePreviewContainer');


    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function(event) {
            imagePreviewContainer.hidden = false;
            imagePreviewContainer.innerHTML = '';
            imagePreviewContainer.appendChild(event.target.cloneNode());

        });
    });

    function handlePageRefresh() {
        console.log("Страница была обновлена!");
                    imagePreviewContainer.appendChild(thumbnails[0].cloneNode());


    }
    // Добавляем слушатель события "beforeunload" к объекту window
    window.addEventListener('DOMContentLoaded', handlePageRefresh);
