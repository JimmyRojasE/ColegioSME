from django.urls import path
from .views import inicio, matriculasEst, matriculasApd, login,matriculasMdr,matriculasPdr

urlpatterns = [
    path('', inicio),
    path('matricula-est', matriculasEst),
    path('matricula-apd', matriculasApd),
    path('matricula-mdr', matriculasMdr),
    path('matricula-pdr', matriculasPdr),
    path('login', login)
]