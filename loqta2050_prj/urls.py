"""
URL configuration for loqta2050_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views as home_views


from about import views as about_views



from contact import views as contact_views
 


# from users import views as users_views
# from posts import views as posts_views

from comments import views as comments_views
from categories import views as categories_views
from votes import views as votes_views
from notifications import views as notifications_views
from moderation import views as moderation_views
from search import views as search_views


# URLConf
urlpatterns = [
 
    path('home/',home_views.home, name='home' ),
 
    path('about/', include('about.urls')),

    # path('about/', about_views.about_me, name='about'),

    path('contact/', contact_views.contact_me, name='contact'),
    # path('users/',users_views.users, name='users' ),
    # path('posts/', posts_views.posts, name='posts'),
    path('comments/', comments_views.comments, name='comments'),
    path('categories/', categories_views.categories, name='categories'),
    path('votes/', votes_views.votes, name='votes'),
    path('notifications/', notifications_views.notifications, name='notifications'),
    path('moderation/', moderation_views.moderation, name='moderation'),
    path('search/', search_views.search, name='search'),
    

    path('admin/', admin.site.urls),
]
