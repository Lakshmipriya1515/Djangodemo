
from shop.models import Category


def menu_links(request):
    t=Category.objects.all()
    return {'links':t}

