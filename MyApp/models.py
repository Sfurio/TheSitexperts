from django.db import models

class SiteRequest(models.Model):
    WEBSITE_CHOICES = [
        ('online-store', 'Online Store'),
        ('portfolio', 'Portfolio'),
        ('blog', 'Blog'),
        ('corporate', 'Corporate Website'),
        ('other', 'Other'),
    ]

    FEATURE_CHOICES = [
        ('ecommerce', 'E-commerce (shopping cart, checkout)'),
        ('blog', 'Blog/Articles'),
        ('gallery', 'Photo/Video Gallery'),
        ('contact_form', 'Contact Form'),
        ('seo', 'SEO Optimization'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    website_type = models.CharField(max_length=50, choices=WEBSITE_CHOICES)
    website_features = models.CharField(max_length=255, blank=True)  # Stores as a CSV string
    budget = models.CharField(max_length=100, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    def get_website_features_list(self):
        """Return website features as a list."""
        return self.website_features.split(',') if self.website_features else []
