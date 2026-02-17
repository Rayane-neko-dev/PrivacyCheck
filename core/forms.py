from django import forms

class WebsiteForm(forms.Form):
    url = forms.URLField(
        label='Website URL', 
        max_length=200, 
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'})
    )
