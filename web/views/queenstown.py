from django.shortcuts import render

page_title = "Ramada Queenstown"


def page_view(request):
    return render(request, 'queenstown.html', context={})


def std_view(request):
    return render(request, 'qtwn/std.html', context={
        'page_title': page_title
    })


def xstd_view(request):
    return render(request, 'qtwn/xstd.html', context={
        'page_title': page_title
    })


def onebd_view(request):
    return render(request, 'qtwn/1bd.html', context={
        'page_title': page_title
    })


def twobd_view(request):
    return render(request, 'qtwn/2bd.html', context={
        'page_title': page_title
    })


def threebd_view(request):
    return render(request, 'qtwn/3bd.html', context={
        'page_title': page_title
    })


def loft_view(request):
    return render(request, 'qtwn/loft.html', context={
        'page_title': page_title
    })
