from django.shortcuts import render

def show_도영(request):
    context = {
        'group_name': '타이거즈',
        'name': '도영',
        'img_src': 'https://i.namu.wiki/i/4uojHDCernMm1AizC-WejbubtlOEdkzCmpeAGjoVXF2dNS_NwiOKYGZNwy7OX4jYszCuRF25X-LcJDzZgLL5Cw.webp'
    }
    # return render(request, '타이거즈/도영.html')
    return render(request, '타이거즈/멤버.html', context=context)

def show_의리(request):
    context = {
        'group_name': '타이거즈',
        'name': '의리',
        'img_src': 'https://i.namu.wiki/i/Ve5oqGUntB90OlWUoWGWq2NRqOOjrkAnJUvQvIHQe0cDd-0_XIqWmiSr1xMZllHwDzZPhOI3MPDi54c7HUA2fg.webp'
    }
    # return render(request, '타이거즈/의리.html')
    return render(request, '타이거즈/멤버.html', context=context)