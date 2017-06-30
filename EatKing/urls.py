from django.conf.urls import url
from . import views,auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
# auth
	url(r'^login$', auth_views.login, name='login'),
	url(r'^authenticate$', auth_views.authenticate, name='authenticate'),
    url(r'^signup$', auth_views.signup, name='signup'),
    url(r'^signup/submit$', auth_views.signup_submit, name='signup-submit'),
    url(r'^logout$', auth_views.logout, name='logout'),
]