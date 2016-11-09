"""lagrangian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
### default

######
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login

###################
###### import my apps
from home import views as home_views
from fermi import views as fermi_views
from demo import views as demo_views
from dashboard import views as dashboard_views
from enterprise import views as enterprise_views
#####################

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_views.home,name="home"),
    url(r'^fermi/', fermi_views.base,name="fermi"),
    url(r'^archive/', fermi_views.archive,name="archive"),
    url(r'^lambda/', home_views.lamb,name="lambda"),
    url(r'^dashboard', dashboard_views.dashboard,name="dashboard"),
    url(r'^kinetic', dashboard_views.kinetic,name="kinetic"),
    url(r'^potential', dashboard_views.potential,name="potential"),
    url(r'^demo/', demo_views.demo,name="demo"),
    url(r'^demo_drones/', demo_views.drones,name="demo_drones"),
    url(r'^demo_intelligence/', demo_views.intelligence,name="demo_intelligence"),
    url(r'^demo_police/', demo_views.police_home,name="demo_police"),
    url(r'^demo_police_graph/', demo_views.police_graph,name="demo_police_graph"),
    url(r'^demo_police_fermi/', demo_views.police_fermi,name="demo_police_fermi"),
    url(r'^demo_police_dashboard/', demo_views.police_dashboard,name="demo_police_dashboard"),
   
    # url(r'^demo/intelligence/login/', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
   
    
    url(r'^demo_news/', demo_views.news,name="demo_news"),
    url(r'^enterprise/', enterprise_views.enterprise,name="enterprise"),

    url('^', include('django.contrib.auth.urls')), ## for login urls
    url(r'^$', home_views.home), #default
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # for json uploads