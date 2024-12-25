from django.shortcuts import render, get_object_or_404, redirect
from .models import History
from .forms import HistoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import search_history


def history(request):
    events, search_query = search_history(request)

    context = {
        'events': events,
        'search_query': search_query
    }

    return render(request, 'history/millennium.html', context)


def detail(request, mil_num):
    try:
        num = History.objects.get(millennium=mil_num)
    except History.DoesNotExist:
        return redirect('history')

    context = {'num': num}

    return render(request, 'history/details.html', context)


def create_record(request):
    form = HistoryForm()

    if request.method == 'POST':
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('history')

    context = {'form': form}
    return render(request, 'history/form-template.html', context)


@login_required(login_url='login')
def update_record(request, mil_num):
    num = get_object_or_404(History, millennium=mil_num)
    form = HistoryForm(instance=num)

    if request.method == 'POST':
        form = HistoryForm(request.POST, request.FILES, instance=num)
        if form.is_valid():
            form.save()
            return redirect('detail', mil_num=num.millennium)

    context = {'form': form}
    return render(request, 'history/update-record.html', context)


@login_required(login_url='login')
def delete_record(request, mil_num):
    num = get_object_or_404(History, millennium=mil_num)
    if request.method == 'POST':
        num.delete()
        messages.success(request, 'Record was deleted successfully')
        return redirect('history')
    context = {'object': num}
    return render(request, 'history/delete-record.html', context)