from blogapp.views import PersonView
from django.urls import path

urlpatterns = [
    path('persons/', PersonView.as_view(), name='persons')
]
