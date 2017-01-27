from django.conf.urls import url
from views import index, loginvalidate, registervalidate, success, logout, quotevalidate, faveon, faveoff, userview
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^loginvalidate$', loginvalidate, name='loginvalidate'),
    url(r'^registervalidate$', registervalidate, name='registervalidate'),
    url(r'^success$', success, name='success'),
    url(r'^logout$', logout, name='logout'),
    url(r'^quotevalidate$', quotevalidate, name='quotevalidate'),
    url(r'^faveon$', faveon, name='faveon'),
    url(r'^faveoff$', faveoff, name='faveoff'),
    url(r'^user/(?P<userid>\d+)', userview,name='userview'),
]
