# Create your views here.
from functions import analize_text
from django.http import HttpResponse
import json

#wrapper for analize_text until is changed for nltk
def get_features(text):
	return analize_text(text)	

def json_get_features(request,text=None):

	if 'text' in request.GET:
		text = request.GET['text'] 

	elif 'text' in request.POST:
		text = request.POST['text']

	data = {}
	feats = []
	succ = False
	num_feat = 0
	try:
		feats = get_features(text)
		num_feat = len(feats)
		succ = True

	except:
		#TODO: add logging
		pass

	data['success'] = succ
	data['result'] = feats
	data['num_feat'] = num_feat
	return HttpResponse(json.dumps(data),mimetype="application/json")