from django.urls import path
from Posts import views as post_view

urlpatterns = [
    path('', post_view.HomePage.as_view(),name="Home"),
    path('post/<int:pk>', post_view.PostDetaileView.as_view(),name="post-detail"),
    path('new-post', post_view.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update', post_view.PostUpdaeView.as_view(),name="post-update"),
    path('user/<str:username>', post_view.UserPostDetaileView.as_view(),name="user-post-detail"),
]