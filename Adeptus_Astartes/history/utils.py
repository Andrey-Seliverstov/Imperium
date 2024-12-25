from .models import History


def search_history(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if search_query:
        events = History.objects.filter(millennium__iexact=search_query)
    else:
        events = History.objects.order_by('millennium')

    return events, search_query

