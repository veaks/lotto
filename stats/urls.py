from django.urls import path

from lotto.views import index
from stats.views import list_draws, overall_stat, update

urlpatterns = [
    path('list_draws/', list_draws),
    path('overall_stat/', overall_stat),
    path('update/', update),
    path('', index),
]