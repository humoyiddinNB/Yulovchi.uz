from django.urls import path

from .views import homePageView, PostView, AboutView, ProjectsView, ContactView, ProjectDetailView, post_view, post_like

urlpatterns = [
    path('', homePageView, name='homepage'),
    path('posts/', PostView.as_view(), name='posts'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('project/detail/<int:id>/', ProjectDetailView.as_view(), name='project_detail'),

    path('post/<int:post_id>/view/', post_view, name='post_view'),
    path('post/<int:post_id>/like/', post_like, name='post_like'),
]