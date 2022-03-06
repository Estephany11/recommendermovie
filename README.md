Movie Recommender app using Django. It consist of a database with more than 20,000 movies, where you can save your movie watch history and review the recommended movies. 

The recommendation algorithm is content filtering based that use Jaccard similarity to calculate similarity between two set.

Algorithm: first query watched movies and undwatched movies, then, for each unwatched movi, calculate the max similarity between all watched movies. If its max similarity is greater than a treshold, then we update its recommended field. 


1 - Create your own watched movie history: 

  In /admin login with superuser credentials. Select movies you have watched and mark them. Repeat the process
 
2 - Generate recommendations:

  Run make_recommendations.py 


IBM Cognitive class based project
