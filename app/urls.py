from django.urls import path
from .views import Home_view, about_view, services_view, pricing_view, blog_view, contact_view,\
    signin_view, blog_single_view,Signup_view,user_profile

urlpatterns = [
    path('', Home_view.as_view(),name='home'),
    path('about/', about_view),
    path('services/', services_view.as_view(),name='services'),
    path('pricing/', pricing_view),
    path('blog/', blog_view),

    path('blog/<int:pk>/', blog_single_view.as_view(), name='blog_detail'),
    path('contact/', contact_view.as_view(),name='contact'),
    path('signup/', Signup_view.as_view(),name='register'),
    path('signin/', signin_view.as_view(),name='login'),
    path('profile/', user_profile,name='profile'),
]
