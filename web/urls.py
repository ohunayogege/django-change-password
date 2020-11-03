from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'forgot-password', views.forgot_password, name='forgot-password'),
	url(r'forgot-password-ajax', views.forgot_password_ajax, name='forgot_password_ajax'),
]