from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView

from .forms import UploadForm
from .models import Game, MultipleImageGame, DynamicPage, MultipleImageNews, News


# Create your views here.
def home(request):
    news_list = News.objects.all()
    sort_by = request.GET.get('sort_by', 'up')
    sort_direction = request.GET.get('sort_direction', 'ascending')
    sort_by_list = [
        {
            'value': 'up',
            'text': 'Up'
        },
        {
            'value': 'down',
            'text': 'Down'
        },
        {
            'value': 'views',
            'text': 'Views'
        },
        {
            'value': 'created_date',
            'text': 'Created Date'
        }
    ]

    if sort_direction == 'ascending':
        news_list = news_list.order_by(f'-{sort_by}')
    elif sort_direction == 'descending':
        news_list = news_list.order_by(f'{sort_by}')
    context = {
        'news_list': news_list,
        'sort_by_list': sort_by_list
    }

    return render(request, 'home.html', context)


def news(request, slug):
    news_obj = get_object_or_404(News, slug=slug)
    context = {
        'news': news_obj
    }
    return render(request, 'news.html', context)


def dynamic_page(request, slug):
    page = DynamicPage.objects.get(slug=slug)
    context = {
        'page': page
    }
    return render(request, 'dynamic_page.html', context)


def games(request):
    games_models = Game.objects.all()
    context = {
        'games': games_models
    }
    return render(request, 'games.html', context)


def genre(request, slug):
    return render(request, 'genre.html')


def game(request, slug):
    game_models = Game.objects.get(slug=slug)
    context = {
        'game': game_models
    }
    return render(request, 'game.html', context)


def page_not_found(request, exception):
    return HttpResponse("Page Not Found")


def upload_images_game(request, slug):
    if request.method == "POST":
        game = Game.objects.get(slug=slug)
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImageGame.objects.create(game=game, images=image)
    images = Game.objects.get(slug=slug).multipleimagegame_set.all()
    game_obj = Game.objects.get(slug=slug)
    return render(request, 'upload_game.html', {'images': images, 'game': game_obj})


def upload_images_news(request, slug):
    if request.method == "POST":
        news = News.objects.get(slug=slug)
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImageNews.objects.create(news=news, images=image)
    images = News.objects.get(slug=slug).multipleimagenews_set.all()
    news_obj = News.objects.get(slug=slug)
    return render(request, 'upload_news.html', {'images': images, 'news': news_obj})


def update_sequence_game(request):
    if request.method == 'POST':
        image_ids = request.POST.getlist('ids[]')
        for index, image_id in enumerate(image_ids, start=1):
            try:
                image = MultipleImageGame.objects.get(pk=image_id)
                image.sequence = index
                image.save()
            except MultipleImageGame.DoesNotExist:
                pass

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def update_sequence_news(request):
    if request.method == 'POST':
        image_ids = request.POST.getlist('ids[]')
        for index, image_id in enumerate(image_ids, start=1):
            try:
                image = MultipleImageNews.objects.get(pk=image_id)
                image.sequence = index
                image.save()
            except MultipleImageNews.DoesNotExist:
                pass

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def up_update(request):
    if request.method == 'POST':
        news_id = request.POST.get('id')
        isUpVoted = request.POST.get('isUpVoted')
        isDownVoted = request.POST.get('isDownVoted')
        try:
            news = News.objects.get(pk=news_id)
            if isUpVoted:
                news.up = news.up - 1
            else:
                if isDownVoted:
                    news.up = news.up + 1
                    news.down = news.down - 1
                else:
                    news.up = news.up + 1
            news.save()
            updated_up = news.up
            updated_down = news.down
        except News.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid id.'})

        return JsonResponse({'status': 'success', 'up_count': updated_up, 'down_count': updated_down})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def down_update(request):
    if request.method == 'POST':
        news_id = request.POST.get('id')
        isUpVoted = request.POST.get('isUpVoted')
        isDownVoted = request.POST.get('isDownVoted')
        print(news_id)
        try:
            news = News.objects.get(pk=news_id)
            if isDownVoted:
                news.down = news.down - 1
            else:
                if isUpVoted:
                    news.down = news.down + 1
                    news.up = news.up - 1
                else:
                    news.down = news.down + 1
            news.save()
            updated_up = news.up
            updated_down = news.down
        except News.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid id.'})

        return JsonResponse({'status': 'success', 'up_count': updated_up, 'down_count': updated_down})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def view_news(request):
    if request.method == 'POST':
        news_id = request.POST.get('newsId')
        try:
            news = get_object_or_404(News, pk=news_id)

            # Обновляем список просмотренных новостей в сессии
            viewed_news = request.session.get('viewed_news', [])
            if news_id not in viewed_news:
                viewed_news.append(news_id)
                request.session['viewed_news'] = viewed_news
                news.views = news.views + 1
                news.save()
            views_count = news.views
        except News.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid id.'})

        return JsonResponse({'status': 'success', 'views_count': views_count})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# def user_viewed_news(request):
#     viewed_news = request.session.get('viewed_news', [])
#     news_list = News.objects.filter(id__in=viewed_news)
#     return render(request, 'viewed_news.html', {'news_list': news_list})


# def sort_news(request):
#     if request.method == 'POST':
#         sort_by = request.POST.get('sort_by', 'up')  # Параметр сортировки по умолчанию
#         news_list = News.objects.all()
#
#
#
#         # Преобразуйте QuerySet в список
#         news_list_data = [
#             {
#                 'title': news.title,
#                 'short_text': news.short_text,
#                 'main_image': news.main_image.url if news.main_image else None,
#                 'up': news.up,
#                 'down': news.down,
#                 'views': news.views,
#                 'created_date': news.created_date.date,
#             }
#             for news in news_list
#         ]
#
#         return JsonResponse({'status': 'success', 'news_list': news_list_data})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
