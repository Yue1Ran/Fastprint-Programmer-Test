from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm 


def produk_list(request):
    produk = Produk.objects.filter(status__nama_status__iexact="bisa dijual")  
    return render(request, 'produk/list.html', {
        'produk': produk
    })
def tambah_produk(request):
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'produk/form.html', {'form': form})


def edit_produk(request, id):
    produk = get_object_or_404(Produk, pk=id)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'produk/form.html', {'form': form})


def hapus_produk(request, id):
    produk = get_object_or_404(Produk, pk=id)
    produk.delete()
    return redirect('list')


