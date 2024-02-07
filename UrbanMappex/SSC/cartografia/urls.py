from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [

    path('home/',login_required(views.home), name='home'),
    path('cartografia/', permission_required('app.can_view_cartografia')(login_required(views.geosis)), name='cartografia'),
    path('reset_session/', views.reset_session, name='reset_session'), 
]