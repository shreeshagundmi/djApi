"""djApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from API import views
# from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showapi, name="showapi"),
    path('user_list/', views.user_list, name="UserList"),
    path('user_create/', views.user_create, name="UserCreate"),
    path('validate_user/', views.validate_user, name="validateUser"),
    path('signin/', views.api_signin, name='api_signin'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('login/', views.loginPage, name='loginPage'),
    path('api_signin_username/', views.api_signin_username, name='api_signin_username'),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
