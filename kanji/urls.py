from django.urls import path
from . import views

urlpatterns= [
path('', views.home),
path('add_kanji/', views.add_kanji, name="addkanji"),
path('delete_kanji/<int:kanji_id>', views.delete_kanji),
path('<int:kanji_id>/', views.kanji_info),
path('radical/<int:radical_id>/', views.radical_info),
path('login/', views.login_page),
path('register/', views.register_page),
path('studyn5/', views.studyn5),
path('studyn5/<int:kanji_id>/', views.updateDetails, name="details"),
path('studyradicals/', views.studyRadicals),
path('studyradicals/<int:radical_id>/',views.updateRadical, name='details_radical'),
path('practicen5', views.practiceN5, name="learnN5"),

]
