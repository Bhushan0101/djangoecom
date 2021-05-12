from .models import Category


def menu_links(request):
    links = Category.objects.all()
    links = {
        'links': links
    }
    return links
