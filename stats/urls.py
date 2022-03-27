from django.urls import path

from stats.views import list_draws, overall_stat, update

urlpatterns = [
    path('list_draws/', list_draws, name='list_draws'),
    path('overall_stat/', overall_stat, name='overall_stat'),
    path('update/', update, name='update'),
]