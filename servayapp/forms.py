from django.forms import ModelForm
from django import forms
from servayapp.models import Webpage, Topic, AccessRecord


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('topic_name',)


class WebpageForm(forms.ModelForm):

    class Meta:
        model = Webpage
        fields = ('topic', 'name', 'url')

class AccessRecord(forms.ModelForm):

    class Meta:
        model = AccessRecord
        fields = ('name','date')