from .models import SpaceMarines
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_orders(request, orders, results):
    page = request.GET.get('page')
    paginator = Paginator(orders, results)

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        orders = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        orders = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, orders


def search_index(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    orders = SpaceMarines.objects.filter(Q(title__iregex=search_query) |
                                         Q(description__iregex=search_query))

    return orders, search_query
