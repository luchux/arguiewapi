# Create your views here.
from reviews.models import Review, ReviewForm
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth.models import User
# TODO: if we enable loging add
# this decoreator @login_required(login_url='/login/')


def index(request):
    all_reviews = Review.objects.all()
    form = ReviewForm(request.user)
    return render_to_response('reviews/index.html', {'review_list': all_reviews, 'form': form}, context_instance=RequestContext(request))

# TODO: if we enable loging add decorator
# @login_required(login_url='/login/')


def add(request):
    user = User.objects.get(username='luchux')
    if request.method == 'POST':
        form = ReviewForm(user, request.POST)
        form.save()
        return redirect("/")
    else:
        form = ReviewForm(user)
        return render(request, "reviews/add.html", {"form": form})
