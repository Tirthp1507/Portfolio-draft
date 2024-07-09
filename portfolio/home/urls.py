import home
from django.contrib import admin
from django.urls import include, path
from home import views

admin.site.site_header = "DEVELOPER TIRTH"
admin.site.site_title = "Welcome to Tirth's Dashboard"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),

]
