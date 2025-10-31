import random
import string
from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import get_language
from django.core.exceptions import ValidationError


def generate_random_id():
    """Generates a random 6-character alphanumeric string."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class BaseModel(models.Model):
    unique_id = models.CharField(max_length=6, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_random_id()
            # Ensure the generated ID is unique for the model.
            ModelClass = self.__class__
            while ModelClass.objects.filter(unique_id=self.unique_id).exists():
                self.unique_id = generate_random_id()
        super().save(*args, **kwargs)
    
    def get_translated_field(self, field_base_name):
        lang = get_language()
        field_name = f"{field_base_name}_{lang}"
        # Attempt to get the field in the current language
        if hasattr(self, field_name):
            value = getattr(self, field_name)
            if value:
                return value
        # Fallback to English if available
        field_name_en = f"{field_base_name}_en"
        if hasattr(self, field_name_en):
            value = getattr(self, field_name_en)
            if value:
                return value
        # Fallback to Japanese as the default
        field_name_ja = f"{field_base_name}_ja"
        if hasattr(self, field_name_ja):
            return getattr(self, field_name_ja)
        return None

class News(BaseModel):
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = CKEditor5Field()
    content_en = CKEditor5Field(blank=True, null=True)
    content_ne = CKEditor5Field(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('header')
    
    def get_translated_content(self):
        return self.get_translated_field('content')

    def __str__(self):
        return self.get_translated_header()
    
class Blog(BaseModel):
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = CKEditor5Field()
    content_en = CKEditor5Field(blank=True, null=True)
    content_ne = CKEditor5Field(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('header')
    
    def get_translated_content(self):
        return self.get_translated_field('content')

    def __str__(self):
        return self.get_translated_header()

class Video(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField()

    def get_translated_header(self):
        return self.get_translated_field('header')

    def __str__(self):
        return self.get_translated_header()
    
class Job(BaseModel):
    header_ja = models.CharField(max_length=255)
    header_en = models.CharField(max_length=255, blank=True, null=True)
    header_ne = models.CharField(max_length=255, blank=True, null=True)
    attract_point_ja = models.CharField(max_length=255)
    attract_point_en = models.CharField(max_length=255, blank=True, null=True)
    attract_point_ne = models.CharField(max_length=255, blank=True, null=True)
    content_ja = CKEditor5Field()
    content_en = CKEditor5Field(blank=True, null=True)
    content_ne = CKEditor5Field(blank=True, null=True)

    def get_translated_header(self):
        return self.get_translated_field('header')

    def get_translated_attract_point(self):
        return self.get_translated_field('attract_point')

    def get_translated_content(self):
        return self.get_translated_field('content')

    def __str__(self):
        return self.get_translated_header()



class TeamMember(BaseModel):
    name_ja = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    position_ja = models.CharField(max_length=100)
    position_en = models.CharField(max_length=100)
    position_ne = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    blog_ja = CKEditor5Field(blank=True, null=True)
    blog_en = CKEditor5Field(blank=True, null=True)
    blog_ne = CKEditor5Field(blank=True, null=True)
    is_ceo = models.BooleanField(default=False, help_text="Mark this member as CEO")

    def get_translated_name(self):
        return self.get_translated_field('name')
    
    def get_translated_position(self):
        return self.get_translated_field('position')
    
    def get_translated_blog(self):
        return self.get_translated_field('blog')

    def __str__(self):
        return self.get_translated_name()

class Service(BaseModel):
    icon = models.CharField(max_length=50, help_text="Bootstrap Icons class name (e.g., 'bi-house-door')")
    title_ja = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_ne = models.CharField(max_length=255, blank=True, null=True)
    description_ja = CKEditor5Field()
    description_en = CKEditor5Field(blank=True, null=True)
    description_ne = CKEditor5Field(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower number appears first)")
    is_hostel_service = models.BooleanField(default=False, help_text="Mark as specialized hostel service")
    
    def get_translated_title(self):
        return self.get_translated_field('title')
    
    def get_translated_description(self):
        return self.get_translated_field('description')

    def __str__(self):
        return self.get_translated_title()
    
    class Meta:
        ordering = ['order', 'created_at']

class CompanyInfo(BaseModel):
    name_en = models.CharField(max_length=255)
    name_ja = models.CharField(max_length=255)
    name_ne = models.CharField(max_length=255)
    establishment_date = models.DateField()
    representative_en = models.CharField(max_length=255)
    representative_ja = models.CharField(max_length=255, blank=True, null=True)
    representative_ne = models.CharField(max_length=255, blank=True, null=True)
    capital = models.CharField(max_length=20)
    employees_num = models.PositiveIntegerField()
    business_portfolio_en = CKEditor5Field()
    business_portfolio_ja = CKEditor5Field(blank=True, null=True)
    business_portfolio_ne = CKEditor5Field(blank=True, null=True)
    office_address_en = CKEditor5Field()
    office_address_ja = CKEditor5Field(blank=True, null=True)
    office_address_ne = CKEditor5Field(blank=True, null=True)
    office_tel = models.CharField(max_length=20)
    office_fax = models.CharField(max_length=20, blank=True, null=True)
    license_details_en = CKEditor5Field()
    license_details_ja = CKEditor5Field(blank=True, null=True)
    license_details_ne = CKEditor5Field(blank=True, null=True)
    about_en = CKEditor5Field()
    about_ja = CKEditor5Field(blank=True, null=True)
    about_ne = CKEditor5Field(blank=True, null=True)
    mission_en = CKEditor5Field()
    mission_ja = CKEditor5Field(blank=True, null=True)
    mission_ne = CKEditor5Field(blank=True, null=True)
    vision_en = CKEditor5Field()
    vision_ja = CKEditor5Field(blank=True, null=True)
    vision_ne = CKEditor5Field(blank=True, null=True)
    values_en = CKEditor5Field()
    values_ja = CKEditor5Field(blank=True, null=True)
    values_ne = CKEditor5Field(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        if CompanyInfo.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of CompanyInfo is allowed.")
        super().save(*args, **kwargs)
    
    def get_translated_name(self):
        return self.get_translated_field('name')

    def get_translated_representative(self):
        return self.get_translated_field('representative')

    def get_translated_business_portfolio(self):
        return self.get_translated_field('business_portfolio')

    def get_translated_office_address(self):
        return self.get_translated_field('office_address')

    def get_translated_license_details(self):
        return self.get_translated_field('license_details')
        
    def get_translated_about(self):
        return self.get_translated_field('about')

    def get_translated_mission(self):
        return self.get_translated_field('mission')

    def get_translated_vision(self):
        return self.get_translated_field('vision')

    def get_translated_values(self):
        return self.get_translated_field('values')

    def __str__(self):
        return self.get_translated_name()
