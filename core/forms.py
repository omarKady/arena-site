from django import forms
from .models import Comment

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)


class CommentForm(forms.ModelForm):
    # (ModelForm) creating form by map its fields to a particular model
    class Meta:
        model = Comment
        fields = ('author', 'text',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs['readonly'] = True