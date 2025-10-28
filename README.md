# Fishtail - Job Portal & News Management System

A comprehensive Django-based web application for managing job postings, news articles, blogs, and team information with multi-language support and rich text editing capabilities.

## 🚀 Features

### Core Functionality
- **Job Portal Management**: Create, edit, and manage job postings with detailed descriptions
- **News Management**: Publish and manage news articles with image support
- **Blog System**: Content management for blog posts
- **Team Management**: Manage team member profiles with social media links
- **Company Information**: Comprehensive company profile management
- **Video Management**: Organize and manage video content

### Technical Features
- **Multi-language Support**: English, Japanese, and Nepali language support
- **Rich Text Editing**: Advanced text editor powered by CKEditor 5
- **User Management**: Custom user model with authentication
- **Image Upload**: Support for image uploads in news, blogs, and team profiles
- **Responsive Design**: Mobile-friendly interface
- **Unique ID System**: Automatic generation of unique 6-character alphanumeric IDs
- **Translation System**: Built-in internationalization (i18n) support

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6
- **Database**: SQLite (development), PostgreSQL/MySQL (production ready)
- **Rich Text Editor**: django-ckeditor-5
- **Image Processing**: Pillow
- **Frontend**: HTML, CSS, JavaScript
- **Internationalization**: Django i18n framework

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Fishtail
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Compile Translation Files
```bash
python manage.py compilemessages
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
Fishtail/
├── fishtail/                 # Main project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── accounts/                 # User management app
│   ├── models.py            # Custom user model
│   ├── views.py             # User views
│   └── admin.py             # User admin interface
├── core/                     # Main application
│   ├── models.py            # Core models (News, Blog, Job, etc.)
│   ├── views.py             # Core views
│   ├── urls.py              # Core URL patterns
│   ├── admin.py             # Admin interface
│   ├── templates/           # HTML templates
│   └── static/             # Static files (CSS, images)
├── locale/                  # Translation files
│   ├── ja/                  # Japanese translations
│   └── ne/                  # Nepali translations
├── media/                   # User uploaded files
├── templates/               # Global templates
├── static/                  # Static files directory
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## 🗄️ Database Models

### News Model
- Multi-language headers (Japanese, English, Nepali)
- Rich text content with CKEditor 5
- Optional image upload
- Automatic unique ID generation

### Job Model
- Job posting management
- Multi-language support
- Attraction points and detailed descriptions
- Rich text content editing

### Blog Model
- Blog post management
- Multi-language headers and content
- Image support
- Rich text editing capabilities

### Team Member Model
- Team member profiles
- Social media links (Twitter, Facebook, Instagram)
- Multi-language name and position fields
- Profile image support

### Company Info Model
- Comprehensive company information
- Multi-language support for all fields
- Business portfolio and office details
- Mission and about sections

## 🌐 Multi-language Support

The application supports three languages:
- **English (en)**: Default language
- **Japanese (ja)**: Japanese language support
- **Nepali (ne)**: Nepali language support

### Language Switching
Users can switch languages using the built-in language switcher. The system automatically detects the user's preferred language and displays content accordingly.

## 🎨 Admin Interface

The Django admin interface provides comprehensive management capabilities:
- User management
- Content management for all models
- Rich text editing with CKEditor 5
- Image upload and management
- Multi-language content editing

Access the admin interface at: `http://127.0.0.1:8000/admin/`

## 🔧 Configuration

### CKEditor 5 Configuration
The application uses CKEditor 5 with custom configurations for different content types:
- Default toolbar for basic editing
- Extended toolbar for advanced formatting
- Image upload and management
- Table support with custom styling

### Static Files
- Static files are served from the `static/` directory
- Media files are served from the `media/` directory
- Proper configuration for development and production environments

## 🚀 Deployment

### Production Settings
For production deployment, update the following settings:
- Set `DEBUG = False`
- Configure proper database (PostgreSQL/MySQL)
- Set up static file serving
- Configure media file serving
- Set up proper security settings

### Environment Variables
Consider using environment variables for sensitive settings:
- `SECRET_KEY`
- `DATABASE_URL`
- `DEBUG`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

- **v1.0.0**: Initial release with basic functionality
- **v1.1.0**: Added multi-language support
- **v1.2.0**: Upgraded to CKEditor 5
- **v1.3.0**: Enhanced admin interface

---

**Fishtail** - Empowering businesses with comprehensive job portal and news management solutions.