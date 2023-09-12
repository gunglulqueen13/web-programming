from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.conf import settings


def archive(request):
    data = {"posts": Article.objects.all(), "STATIC_URL": settings.STATIC_URL}
    return render(request, "archive.html", data)


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        data = {"STATIC_URL": settings.STATIC_URL, "post": post}
        return render(request, "article.html", data)
    except Article.DoesNotExist:
        raise Http404


@login_required
def create_post(request):
    if request.method == "POST":
        form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
        }
        if form["text"] and form["title"]:
            if Article.objects.filter(title=form["title"]).exists():
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form, "STATIC_URL": settings.STATIC_URL})
            article = Article.objects.create(
                text=form["text"], title=form["title"], author=request.user)
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form, "STATIC_URL": settings.STATIC_URL})
    else:
        return render(request, 'create_post.html', {"STATIC_URL": settings.STATIC_URL})
