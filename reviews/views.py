# Create your views here.
from reviews.models import Review
def get_json_graph():
	#todo: filter by user, product, etc.
	list_review = Review.objects.all()
	
