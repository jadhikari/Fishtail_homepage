
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . import models  
from datetime import datetime
from django.utils.translation import get_language, gettext as _


def home(request):
    # Fetch recent news items (latest 7) for the home page
    recent_news = models.News.objects.exclude(unique_id="").order_by('-created_at')[:5]
    context = {
        'recent_news': recent_news
    }
    return render(request, 'core/home.html', context)

def about(request):
    try:
        company_info = models.CompanyInfo.objects.get()
    except models.CompanyInfo.DoesNotExist:
        company_info = None
    return render(request, "core/about.html", {"company_info": company_info})

def services(request):
    services_list = models.Service.objects.all().order_by('order', 'created_at')
    return render(request, "core/services.html", {"services": services_list})

def news_home(request):
    """Fetch the latest, trending, and all news for display."""
    all_news = models.News.objects.exclude(unique_id="").order_by('-created_at')
    
    # Get top news (most recent)
    top_news = all_news.first() if all_news.exists() else None
    
    # Get latest news list (excluding top news if it exists)
    if top_news:
        latest_news_list = all_news[1:]
    else:
        latest_news_list = all_news
    
    # Get trending news (top 5)
    trending_news = all_news[:5]

    # Pagination for latest_news (6 per page)
    paginator = Paginator(latest_news_list, 6)
    page_number = request.GET.get('page')
    latest_news = paginator.get_page(page_number)

    context = {
        'top_news': top_news,
        'latest_news': latest_news,
        'trending_news': trending_news
    }
    return render(request, 'core/news.html', context)

def news_detail(request, unique_id):
    """Fetch a specific news article by unique_id."""
    news = get_object_or_404(models.News, unique_id=unique_id)
    return render(request, 'core/news_detail.html', {'news': news})

def team_view(request):
    """View to display all team members."""
    # Get CEO member
    ceo = models.TeamMember.objects.filter(is_ceo=True).first()
    
    # Get other team members (exclude CEO if found)
    if ceo:
        team_members = models.TeamMember.objects.exclude(unique_id=ceo.unique_id).order_by('created_at')
    else:
        team_members = models.TeamMember.objects.all().order_by('created_at')
    
    return render(request, "core/team.html", {"ceo": ceo, "team_members": team_members})

def contact(request):
    try:
        company_info = models.CompanyInfo.objects.get()
    except models.CompanyInfo.DoesNotExist:
        company_info = None
    
    if request.method == 'POST':
        from django.contrib import messages
        
        try:
            # Save contact message
            models.ContactMessage.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                purpose=request.POST.get('purpose'),
                message=request.POST.get('message')
            )
            
            messages.success(request, _('Thank you for your message! We have received your inquiry and will contact you soon.'))
            
        except Exception as e:
            messages.error(request, _('Sorry, there was an error submitting your message. Please try again later.'))
    
    return render(request, 'core/contact.html', {'company_info': company_info})

def job_list_view(request):
    query = request.GET.get('q', '')
    lang = get_language()  # will return 'en', 'ja', or 'ne'

    # Dynamically pick the translated header field based on current language
    header_field = f'header_{lang}'
    
    job_list = models.Job.objects.all()

    if query:
        filter_kwargs = {f'{header_field}__icontains': query}
        job_list = job_list.filter(**filter_kwargs)

    job_list = job_list.order_by('-created_at')

    paginator = Paginator(job_list, 10)
    page = request.GET.get('page', 1)

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'core/job_list.html', {'jobs': jobs, 'query': query})

def job_detail_view(request, unique_id):
    # Retrieve the job object based on the unique_id
    job = get_object_or_404(models.Job, unique_id=unique_id)
    
    
    context = {
        'job': job
    }
    return render(request, 'core/job_detail.html', context)

def hostel_view(request):
    hostels = models.Hostel.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'core/hostel.html', {'hostels': hostels})

def hostel_booking(request, unique_id):
    """Handle hostel booking form submission"""
    hostel = get_object_or_404(models.Hostel, unique_id=unique_id, is_active=True)
    
    if request.method == 'POST':
        from django.contrib import messages
        from django.shortcuts import redirect
        
        booking = models.BookingRequest.objects.create(
            hostel=hostel,
            customer_name=request.POST.get('customer_name'),
            phone_number=request.POST.get('phone_number'),
            current_address=request.POST.get('current_address'),
            email=request.POST.get('email'),
            message=request.POST.get('message', ''),
            user=request.user if request.user.is_authenticated else None
        )
        
        messages.success(request, _('Thank you for your booking request! Our staff will contact you soon via email or phone to confirm your reservation.'))
        return redirect('hostel')
    
    return render(request, 'core/hostel.html', {'hostels': models.Hostel.objects.filter(is_active=True)})


