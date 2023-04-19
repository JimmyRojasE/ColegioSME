from django.urls import path
from .views import inicio, matriculasEst, matriculasApd, login

urlpatterns = [
    path('', inicio),
    path('matricula-est', matriculasEst),
    path('matricula-apd', matriculasApd),
    path('login', login)
]