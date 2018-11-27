from django.shortcuts import render

page_title= "Ramada Christchurch"


def page_view(request):
    return render(request, 'christchurch.html', context={
        'page_title': page_title
    })


def std_view(request):
    return render(request, 'chch/std.html', context={
        'page_title': page_title
    })


def onebd_view(request):
    return render(request, 'chch/1bd.html', context={
        'page_title': page_title
    })

def twobd_view(request):
    return render(request, 'chch/2bd.html', context={
        'page_title': page_title
    })
