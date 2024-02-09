from django.shortcuts import get_list_or_404, get_object_or_404, render, HttpResponse
from django.http.response import Http404
from recipes.models import Recipe
from django.db.models import Q # Consultas complexas na base de dados 


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip() #value # retorna none por padrao e agora retona ''

    if search_term == '': # ou if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
        Q(title__icontains=search_term) | Q(description__icontains=search_term)
        ), is_published=True
        ).order_by('-id') # pode se fazer sem utilizar três Q mas acarreta riscos

    
    # recipes = recipes.order_by('-id')
    # recipes = recipes.filter(is_published=True)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'looking for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes
    })

# Query é uma consulta ao banco de dados || QuerySet é um objeto iterável com os objectos criados