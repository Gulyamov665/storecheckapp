from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from store.forms import *
from store.models import *


@login_required(login_url='/users/sign-in')
def index(request):
    skus = Sku.objects.all()
    detail = Details.objects.all()
    united = United.objects.all()
    visit = Visit.objects.all()
    user = request.user.id
    form = VisitForm(request.POST or request.FILES or None)


    if request.method == 'POST':
        trade = request.POST.get('trade')
        territory = request.POST.get('territory')
        comment = request.POST.get('comment')
        sku_names = [x.sku_name for x in Sku.objects.all()]
        detail_names = [t.name for t in Details.objects.all()]
        sku_ids = []
        detail_ids = []
        for x in sku_names:
            sku_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print('0')
        for t in detail_names:
            detail_ids.append(int(request.POST.get(t))) if request.POST.get(t) else print('0')

        visit = Visit.objects.create(
            trade_id=trade,
            territory_id=territory,
            user_id=user,
            comment=comment
        )
        for x in sku_ids:
            visit.sku.add(Sku.objects.get(id=x))
        for t in detail_ids:
            visit.detail.add(Details.objects.get(id=t))
        form.is_valid()
        return redirect('store:home')
   
    return render(request, 'home.html', {
        'visit': visit,
        'skus': skus,
        'details': detail, 
        'form': form,
        'uniteds': united,
    })


@login_required(login_url='/users/sign-in')
def create_trade(request):
    trade_form = TradeForm(request.POST or None, request.FILES or None)
    if trade_form.is_valid():
        trade_form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_trade.html', {
        'trade_form': trade_form
    })


@login_required(login_url='/users/sign-in')
def create_territory(request):
    territory_form = TerritoryForm(request.POST or None, request.FILES or None)
    if territory_form.is_valid():
        territory_form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_territory.html', {
        'territory_form': territory_form,
    })


@login_required(login_url='/users/sign-in')
def create_sku(request):
    sku_form = SkuForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and sku_form.is_valid():
        instance = sku_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_sku.html', {
        'sku_form': sku_form
    })


@login_required(login_url='/users/sign-in')
def edit_sku(request, pk):
    sku = get_object_or_404(Sku, pk=pk)
    form = SkuForm(request.POST or None, request.FILES or None, instance=sku)
    if form.is_valid():
        form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/edit_page.html', {
        'form': form
    })


def del_sku(request, pk):
    author = Sku.objects.get(pk=pk).delete()
    return redirect('store:home')


def create_deatil(request):
    form_detail = DetailForm(request.POST or None)
    if request.method == 'POST' and form_detail.is_valid():
        instance = form_detail.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_detail.html', {
        'form_detail': form_detail
    })
