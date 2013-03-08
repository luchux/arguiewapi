# Create your views here.
from reviews.models import Review, ReviewForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def get_json_graph():
	#todo: filter by user, product, etc.
	list_review = Review.objects.all()


# TODO: if we enable loging add 
#this decoreator @login_required(login_url='/login/')
def index(request):
	all_reviews = Review.objects.all()
	form = ReviewForm(request.user) 
	return render_to_response('reviews/index.html',{'review_list':all_reviews, 'form':form}, context_instance=RequestContext(request))