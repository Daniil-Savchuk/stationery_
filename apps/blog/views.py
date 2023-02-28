from django.shortcuts import render
from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag, Comment
from apps.blog.forms import CreateCommentForm


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {
        'current': "Категории"
    }
    return render(request, 'blog/category_list.html', {"categories": blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    comments = Comment.objects.filter(article=articles).filter(is_checked=True)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': category.name
    }

    error = None
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=articles)
        user = request.user
        if not user.is_authenticated:
            data.update(name=user.username, email=user.email, is_checked=True)
        request.POST = data
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            form.save()
            breadcrumbs = {'current': 'Комментарий создан'}
            return render(request, 'blog/comments.html', {'article': articles, 'breadcrumbs': breadcrumbs})
        else:
            error = form.errors

    return render(
        request,
        'blog/article_list.html',
        {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs, 'error': error, 'comments': comments}
    )


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        reverse('blog_article_list', args=category_id): category.name,
        'current': article.title
    }
    return render(
        request,
        'blog/article_view.html',
        {"category": category, "article": article, 'breadcrumbs': breadcrumbs}
    )


def tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag_articles = Article.objects.filter(tag=tag)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': tag.name
    }
    return render(request, 'blog/tag_view.html', {'tag': tag, 'articles': tag_articles, 'breadcrumbs': breadcrumbs})
