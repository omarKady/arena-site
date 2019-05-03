from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns =[
    path('', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:pk>/openleague/', views.openleague, name='openleague'),
    path('<int:pk>/opennews/', views.opennews, name='opennews'),
    path('<int:pk>/clubpage/', views.clubpage, name='clubpage'),
    path('<int:pk>/clubnews/', views.clubnews, name='clubnews'),
    path('<int:pk>/openallclubs/', views.openallclubs, name='openallclubs'),
    path('<int:pk>/newsdetail/', views.newsdetail, name='newsdetail'),
    path('<int:pk>/leaguerank/', views.leaguerank, name='leaguerank'),
    path('<int:pk>/leaguematchs/', views.leaguematchs, name='leaguematchs'),
    path('<int:pk>/clubmatchs/', views.clubmatchs, name='clubmatchs'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.successcontact, name='successcontact'),
    path('news/<int:pk>/comment/', views.add_comment_to_news, name='add_comment_to_news'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
