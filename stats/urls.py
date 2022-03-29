from django.urls import path

from lotto.views import index
from stats.views import list_draws, overall_stat, update, latest_chart, latest_chart_js

urlpatterns = [
    path('list_draws/', list_draws),
    path('overall_stat/', overall_stat),
    path('latest_chart/', latest_chart),
    path('latest_chart_js/', latest_chart_js),
    path('update/', update),
    path('', index),
]