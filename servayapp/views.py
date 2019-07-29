from django.shortcuts import render

# Create your views here.
from servayapp.forms import TopicForm, WebpageForm


def index(request):
    return render(request, 'servayapp/index.html')

def polling(request):

    accepted = False

    if request.method == "POST":
        print("done")
    else:
        mydict = {
            'Topic': TopicForm(),
            'webpage': WebpageForm()
        }
        return render(request,'servayapp/question1.html',mydict)