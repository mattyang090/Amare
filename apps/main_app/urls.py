from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^login_reg_page$', views.login_reg_page),
    url(r'^register_user$', views.register_user),
    url(r'^login_user$', views.login_user),
    url(r'^help_suicide$', views.help_suicide),
    url(r'^help_homeless$', views.help_homeless),
    url(r'^help_disability$', views.help_disability),
    url(r'^help_social$', views.help_social),
    url(r'^help_violence$', views.help_violence),
    url(r'^log_out$', views.log_out),
    url(r'^donation$', views.donation),
    
]