from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.results, name='results'),
    # ext: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]