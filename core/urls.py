from django.db.models.indexes import Index
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import IndexView, DashboardView, BlogView, BlogDetailView, AboutMeView, AdminPageView, AdminPostView, AdminPostDelete, AdminAllPost, AdminEditPost, ErrorPage

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('errorPage/1232sdfad', ErrorPage.as_view(), name='errorPage'),
    path('dashboard', DashboardView.as_view(), name='Dashboard'),
    path('blog', BlogView.as_view(), name='Blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('sobremim', AboutMeView.as_view(), name='SobreMim'),
    path('adminPage', AdminPageView.as_view(), name='AdminPage'),
    path('adminPage/allpost', AdminAllPost.as_view(), name='all_post_view'),
    path('adminpage/createPost/', AdminPostView.as_view(), name='post_new'),
    path('adminpage/deletepost/<int:pk>/confirm', AdminPostDelete.as_view(), name='post_delete'),
    path('adminpage/editpost/<int:pk>/edit', AdminEditPost.as_view(), name='post_edit'),
]