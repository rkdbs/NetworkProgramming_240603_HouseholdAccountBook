from django.urls import path
from 타이거즈 import views

app_name = '타이거즈'

urlpatterns = [
    # path('도영/', views.show_도영, name='도영'),
    # path('의리/', views.show_의리, name='의리'),
    path('<멤버>/', views.show_멤버, name='멤버'),
]