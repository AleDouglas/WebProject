from django.db.models.indexes import Index
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import IndexView, DashboardView, BlogView, BlogDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('dashboard', DashboardView.as_view(), name='Dashboard'),
    path('blog', BlogView.as_view(), name='Blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]