from django.shortcuts import render
from django.views.generic import ListView

from 브레드이발소.models import Character


class CharacterListView(ListView):
    model = Character
    # character_list = Character.objects.all() # DB에 Character 데이터 다 가져오자
    # return render(request, '브레드이발소/character_list.html', context={'character_list': character_list}) # 모델_list.html에 모델_list라는 키로 DB에 가져온 데이터 넣어서 render 하자
