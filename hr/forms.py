from django.forms import ModelForm
from . models import Job

class AddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class EditJobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

