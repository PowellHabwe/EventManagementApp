from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    # CreateCheckoutSessionView,

    
)
urlpatterns = [
    path('', PostListView.as_view(), name='events-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('about/', views.about, name='events-about'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
]
