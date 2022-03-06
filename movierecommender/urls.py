from django.urls import path
from . import views

app_name ="movierecommender"

urlpatterns = [
    # route is a string contains a URL pattern
    path(route='', view=views.home, name= 'home'),
    path(route='filtered/', view=views.filtered, name='filtered'),
    path(route='recommendations/', view = views.movie_recommendation_view, name='recommendations'),
]
