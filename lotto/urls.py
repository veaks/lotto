from django.contrib import admin
from django.urls import path, include

import stats
from lotto.views import index
from stats.views import list_draws, overall_stat, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stats.urls')),
]
