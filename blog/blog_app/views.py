from django.shortcuts import render, get_object_or_404, redirect

#import models
from .models import Author, Article

#import form
from .forms import FeedbackForm

# Create your views here.



def main_page(request): 
    #get all article obj in database
    article = Article.objects.all()
    author = Article.objects.all()
    context = {'articles': article, 'author': author}
    #send the httprequest with the template, dictionary means the article in template is the article object
    return render(request, 'html/main_page.html', context) # CHANGE MAIN_PAGE.HTML -> LAYOUT.HTML

def about_page(request):
    return render(request, 'html/about.html')

def contact_page(request):
    return render(request, 'html/contact_page.html')

'''
#handle feedback
def feedback_data(request):
    #Handle Post request - method that change the database
    if request.method == 'POST':Ch
        form = FeedbackForm(request.POST)
        #Handle valid data form
        if form.is_valid():
            username = form.cleaned_data['username']
            feedback = form.cleaned_data['feedback']

            return redirect('thank_you.html')
    else:
        form = FeedbackForm()

    context = {'form': form}
    return render(request, 'html/feedback.html', context)
'''
def contact_page(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()  # Handle form submission
            return redirect('thank_you.html')  # Redirect to a success page
    else:
        feedback_form = FeedbackForm()

    # Static contact data (you can modify this)
    contact_info = {
        'name': 'Kamuning',
        'email': 'you@example.com',
        'phone': '+123456789',
        'address': 'Cat Bldg., Common street, Kamuning, Quezon city, NCR '
    }

    context = {
        'contact_info': contact_info,
        'feedback_form': feedback_form,
    }
    return render(request, 'html/contact_page.html', context)


#Thank you msg after feedback submission
def thank_you(request):
    return render(request, 'html/thank_you.html')

def article_page(request, article_id):
    #get_object_or_404 obtain single object or throw 404 if no record is found.
    article = get_object_or_404(Article, pk=article_id)  #pk means primary key, the unique code of a specific record
    context = {'article': article}
    return render(request, 'html/article_page.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'html/author_detail.html', {'author': author})