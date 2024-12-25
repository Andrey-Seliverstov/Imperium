from django.shortcuts import render, get_object_or_404, redirect
from .models import SpaceMarines
from .forms import SpaceMarinesForm, ReviewForm
from .utils import search_index, paginate_orders
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    orders, search_query = search_index(request)
    custom_range, orders = paginate_orders(request, orders, 3)

    context = {
        'orders': orders,
        'search_query': search_query,
        'custom_range': custom_range
    }

    return render(request, 'Space_Marines/index.html', context)


def order(request, pk):
    legion = get_object_or_404(SpaceMarines, id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.order = legion
        review.owner = request.user.profile
        review.save()
        messages.success(request, 'Комментарий добавлен')
        return redirect('order', pk=legion.id)

    context = {
        'order': legion,
        'form': form
    }
    return render(request, 'Space_Marines/order.html', context)


def create_order(request):
    form = SpaceMarinesForm()

    if request.method == 'POST':
        form = SpaceMarinesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'Space_Marines/form-template.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    num = get_object_or_404(SpaceMarines, id=pk)
    form = SpaceMarinesForm(instance=num)

    if request.method == 'POST':
        form = SpaceMarinesForm(request.POST, request.FILES, instance=num)
        if form.is_valid():
            form.save()
            return redirect('order', pk=pk)

    context = {'form': form}
    return render(request, 'Space_Marines/update-order.html', context)


@login_required(login_url='login')
def delete_order(request, pk):
    num = get_object_or_404(SpaceMarines, id=pk)
    if request.method == 'POST':
        num.delete()
        messages.success(request, 'Record was deleted successfully')
        return redirect('index')
    context = {'object': num}
    return render(request, 'Space_Marines/delete-order.html', context)
