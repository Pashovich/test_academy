from django.urls import path
from resources.views import ResourcesView, TotalCostView


app_name = "resources"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('resources', ResourcesView.as_view()),
    path('total_cost', TotalCostView.as_view())
]