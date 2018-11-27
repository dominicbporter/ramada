from django.shortcuts import render

page_title = "Ramada Auckland"


def page_view(request):
    return render(request, 'auckland.html', context={
        'page_title': page_title
    })


def std_view(request):
    return render(request, 'akl/std.html', context={
        'page_title': page_title
    })


def xstd_view(request):
    return render(request, 'akl/xstd.html', context={
        'page_title': page_title
    })


def onebd_view(request):
    return render(request, 'akl/1bd.html', context={
        'page_title': page_title
    })


def pent_view(request):
    return render(request, 'akl/pent.html', context={
        'page_title': page_title
    })
