"""swiss URL Configuration

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
from django.http import request
from django.urls import path
from django.contrib.auth.models import Group
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout, views as auth_views



from bankapp.views import landing_page, ProfileView, logout_user
from bankapp.models import AccountDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='index'),
    path('dashboard/', ProfileView.as_view(), name='dash'),
    path('transfer/', ProfileView.transfer, name='transfer'),
    path('dashboard/proofofaccount/', ProfileView.proof_of_account, name='poa'),
    path('dashboard/proofofresidence/', ProfileView.proof_of_residence, name='por'),
    path('dashboard/proofofidentity/', ProfileView.proof_of_identity, name='poi'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SWISS OFFSHORE'
admin.site.site_title = 'SWISS OFFSHORE'
admin.site.index_title = 'SWISS OFFSHORE ADMIN CONTROL'

admin.site.unregister(Group)