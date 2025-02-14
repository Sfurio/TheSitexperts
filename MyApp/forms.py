from django import forms
from .models import SiteRequest

class SiteRequestForm(forms.ModelForm):
    FEATURE_CHOICES = [
        ('ecommerce', 'E-commerce (shopping cart, checkout)'),
        ('blog', 'Blog/Articles'),
        ('gallery', 'Photo/Video Gallery'),
        ('contact_form', 'Contact Form'),
        ('seo', 'SEO Optimization'),
    ]

    website_features = forms.MultipleChoiceField(
        choices=FEATURE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = SiteRequest
        fields = ['full_name', 'email', 'phone', 'website_type', 'website_features', 'budget', 'additional_notes']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'website_type': forms.Select(attrs={'class': 'form-control'}),
            'budget': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your budget'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your vision'}),
        }

    def clean_website_features(self):
        """Convert list of selected features into a comma-separated string."""
        return ",".join(self.cleaned_data['website_features'])
