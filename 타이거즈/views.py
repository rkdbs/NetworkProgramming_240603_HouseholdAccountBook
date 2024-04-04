from django.shortcuts import render

group = {
    'members': [
        {
            'group_name': '타이거즈',
            'name': '도영',
            # 'img_src': 'https://i.namu.wiki/i/4uojHDCernMm1AizC-WejbubtlOEdkzCmpeAGjoVXF2dNS_NwiOKYGZNwy7OX4jYszCuRF25X-LcJDzZgLL5Cw.webp'
            'img_src': '타이거즈/images/도영.jpg'
        },
        {
            'group_name': '타이거즈',
            'name': '의리',
            # 'img_src': 'https://i.namu.wiki/i/Ve5oqGUntB90OlWUoWGWq2NRqOOjrkAnJUvQvIHQe0cDd-0_XIqWmiSr1xMZllHwDzZPhOI3MPDi54c7HUA2fg.webp'
            'img_src': '타이거즈/images/의리.jpeg'
        },
        {
            'group_name': '타이거즈',
            'name': '영철',
            # 'img_src': 'https://i.namu.wiki/i/J59_Y_Qxedf7ElhdyPB7khFLmq6hFj95S_K_J_LUlOvjDgxfLX92xy89EamxIBSbQq-cMloPcZY59CSklcLPjA.webp'
            'img_src': '타이거즈/images/영철.jpg'
        }
    ]
}


def show_도영(request):
    context = list(filter(lambda member: '도영' in member['name'], group['members']))[0]
    # context = group['members'][0]
    # return render(request, '타이거즈/도영.html')
    return render(request, '타이거즈/멤버.html', context=context)

def show_의리(request):
    context = list(filter(lambda member: '의리' in member['name'], group['members']))[0]
    # context = group['members'][1]
    # return render(request, '타이거즈/의리.html')
    return render(request, '타이거즈/멤버.html', context=context)

def show_멤버(request, 멤버):
    context = list(filter(lambda member: 멤버 in member['name'], group['members']))[0]
    return render(request, '타이거즈/멤버.html', context=context)

def show_멤버리스트(request):
    context = group     # {'mamber': [{멤버1}, {멤버2},]}
    return render(request, '타이거즈/멤버리스트.html', context=context)