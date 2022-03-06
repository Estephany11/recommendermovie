from . import views
from .models import Movie
from django.shortcuts import render
from .forms import formulario

# HINT: Create a view to provide movie recommendations list for the HTML template
def home(request):
    context=generate_movies_forhome()

    return render(request, 'movierecommender/home.html', context)

def generate_movies_forhome():
    context={}
    movies = Movie.objects.all()[:30]
    context['movie_list'] = movies
    return context


##### FILTERING MOVIES:

def filtered(request):
    if request.method == "GET":

        context=generate_movies_filtered()
        return render(request, 'movierecommender/filtered.html', context)


def generate_movies_filtered():
    context={}

    movies = Movie.objects.filter(
        genres='romance'
        ).order_by('-vote_count')[:30]
    context['movie_list'] = movies
    return context

############################### BACKEND ################################
# Funcion 1. se actualiza con el contexto de funcion 2
def movie_recommendation_view(request):
    if request.method == "GET":
        #the context/ data to be presented in the html template
        context= generate_movies_context()
        #render a html with specified template and context
        return render(request, 'movierecommender/movie_list.html', context)

# Funcion 2.
def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie counts
    recommended_count = Movie.objects.filter(
        recommended=True
    ).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(
            watched=False
        ).order_by('-vote_count')[:30]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended=True
        ).order_by('-vote_count')[:30]
    context['movie_list'] = movies
    return context

############################### BACKEND ################################
