from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import med_detailview,add_med,update_med,del_meds
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name='blog-home'),
    path('buy', views.buy, name='buy'),
    path('login/', auth_views.LoginView.as_view(template_name='mtfD/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mtfD/logout.html'), name='logout'),
    path('buyer/', views.buyer, name='buyer'),
    path('saler/', views.saler, name='saler'),
    path('agent/', views.agent, name='agent'),
    path('profile/', views.profile, name='profile'),
    path('detail/<int:pk>/', med_detailview.as_view(),name='detail'),
    path('detail/<int:pk>/upd', update_med.as_view(),name='update'),
    path('del/<int:pk>/', del_meds.as_view(),name='del'),
    path('add/', add_med.as_view(),name='add'),
    path('password_reset',
        auth_views.PasswordResetView.as_view(template_name='mtfD/pasre.html'), name='pasre'),
    path('password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name='mtfD/pasred.html'), name='password_reset_done'),        
    path('password_reset_confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='mtfD/pasrec.html'), name='password_reset_confirm'),
    path('password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='mtfD/pasreco.html'), name='password_reset_complete'),
]