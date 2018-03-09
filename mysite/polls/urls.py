from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('specifics/<int:pergunta_id>/', views.detalhe, name='detalhe'),
    # /polls/5/resultados
    path('<int:pergunta_id>/resultados/', views.resultados, name='resultados'),
    # /polls/5/voto
    path('<int:pergunta_id>/voto/', views.voto, name='voto'),
]