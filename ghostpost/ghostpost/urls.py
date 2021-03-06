"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import (
    message_board_view,
    write_post_view,
    upvote,
    downvote,
    just_boast_view,
    order_like_view,
    just_roast_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', message_board_view, name="home"),
    path('message/', write_post_view),
    path('upvote/<int:id>/', upvote),
    path('downvote/<int:id>', downvote),
    path('boast/', just_boast_view),
    path('roast/', just_roast_view),
    path('like/', order_like_view),
]
