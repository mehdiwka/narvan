from django.urls import path
from calculate import views

urlpatterns = [
    path("calculate/", views.calculate),

]