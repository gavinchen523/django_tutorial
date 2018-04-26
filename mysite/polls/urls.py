from django.urls import path

from . import views

app_name = 'polls'
urlpatterns  = [
    #/polls
    path('', views.index, name='index'),
    #/polls/x
    path('<int:question_id>/', views.detail, name='detail'),
    #/polls/x/results
    path('<int:question_id>/results/', views.results, name='results'),
    #/polls/x/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]