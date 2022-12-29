from django.forms import ModelForm, widgets
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'title', 'featured_image', 'description',
                  'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text', 'placeholder': 'Add text'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input input--text', 'placeholder': 'Add Title'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input input--text', 'placeholder': 'Add Description'})
