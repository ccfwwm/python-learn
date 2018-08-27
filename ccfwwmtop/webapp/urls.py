
from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    # ex: /webapp/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /webapp/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /webapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]