from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate




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

def registred(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            errors = "Заполните все поля"
            return render(request, 'registration_form.html', {'errors': errors, "STATIC_URL": settings.STATIC_URL})

        if password != confirm_password:
            errors = "Пароли не совпадают"
            return render(request, 'registration_form.html', {'errors': errors, "STATIC_URL": settings.STATIC_URL})

        if User.objects.filter(username=username).exists():
            errors = "Пользователь с таким именем уже существует"
            return render(request, 'registration_form.html', {'errors': errors, "STATIC_URL": settings.STATIC_URL})

        User.objects.create_user(username=username, password=password)
        
        return redirect('/login')
    else:
        return render(request, 'registration_form.html', {"STATIC_URL": settings.STATIC_URL})
    
def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            errors = "Заполните все поля"
            return render(request, 'login_form.html', {'errors': errors, "STATIC_URL": settings.STATIC_URL})

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('/article/new')
        else:
            errors = "Неверные имя пользователя или пароль"
            return render(request, 'login_form.html', {'errors': errors, "STATIC_URL": settings.STATIC_URL})
    else:
        return render(request, 'login_form.html', {"STATIC_URL": settings.STATIC_URL})

def logout_func(request):
    logout(request)
    return redirect('/login')
    