from settings.local import *


ADMIN_TOOLS_APPS = [
    'admin_tools',
    'admin_tools.dashboard'
]

ALLOWED_HOSTS = ["k8s-sv-surveydj-4fb9803733-444906322.ap-southeast-1.elb.amazonaws.com"]

ADMIN_TOOLS_INDEX_DASHBOARD = "settings.admin.dashboard.CustomIndexDashboard"

INSTALLED_APPS = ADMIN_TOOLS_APPS + INSTALLED_APPS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'loaders': [
                    'admin_tools.template_loaders.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

