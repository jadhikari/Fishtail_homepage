from django.contrib import admin
from .models import News, Blog, Video, Job, TeamMember, CompanyInfo, Service

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('unique_id','header_ja', 'header_en', 'created_at', 'user')
    search_fields = ('unique_id', 'header_en')
    readonly_fields = ('unique_id', 'created_at', 'updated_at')
    # Exclude the 'user' field so it's not visible in the form
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        # If this is a new object, set the user to the currently logged-in admin user.
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(News)
class NewsAdmin(BaseModelAdmin):
    pass  

@admin.register(Blog)
class BlogAdmin(BaseModelAdmin):  
    pass
    
@admin.register(Video)
class VideoAdmin(BaseModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(BaseModelAdmin):
    pass

@admin.register(TeamMember)
class TeamMemberAdmin(BaseModelAdmin):
    list_display = ('unique_id','name_en', 'name_ja', 'position_en', 'position_ja', 'is_ceo', 'created_at')
    search_fields = ('unique_id','name_en')
    list_filter = ('is_ceo',)
    list_editable = ('is_ceo',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'title_en', 'icon', 'order', 'is_hostel_service', 'created_at')
    search_fields = ('unique_id', 'title_en', 'title_ja', 'title_ne', 'icon')
    readonly_fields = ('unique_id', 'created_at', 'updated_at')
    list_filter = ('is_hostel_service', 'created_at')
    list_editable = ('order', 'is_hostel_service')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('icon', 'order', 'is_hostel_service')
        }),
        ('Title', {
            'fields': ('title_en', 'title_ja', 'title_ne')
        }),
        ('Description', {
            'fields': ('description_en', 'description_ja', 'description_ne')
        }),
    )
    
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'name_en', 'establishment_date', 'representative_en', 'capital', 'office_tel', 'created_at')
    search_fields = ('unique_id', 'name_en', 'name_ja', 'name_ne')
    readonly_fields = ('unique_id', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name_en', 'name_ja', 'name_ne', 'establishment_date', 'representative_en', 'representative_ja', 'representative_ne')
        }),
        ('Company Details', {
            'fields': ('capital', 'employees_num', 'business_portfolio_en', 'business_portfolio_ja', 'business_portfolio_ne')
        }),
        ('Contact Information', {
            'fields': ('office_address_en', 'office_address_ja', 'office_address_ne', 'office_tel', 'office_fax', 'license_details_en', 'license_details_ja', 'license_details_ne')
        }),
        ('About & Mission', {
            'fields': ('about_en', 'about_ja', 'about_ne', 'mission_en', 'mission_ja', 'mission_ne', 'vision_en', 'vision_ja', 'vision_ne', 'values_en', 'values_ja', 'values_ne')
        }),
    )
    
    # Exclude the 'user' field so it's not visible in the form
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        # If this is a new object, set the user to the currently logged-in admin user.
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)