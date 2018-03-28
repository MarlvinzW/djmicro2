from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Your API')

API_PREFIX = r'api/v1'

urlpatterns = [
    path(f'{API_PREFIX}/docs/', swagger_view),
    path(f'{API_PREFIX}/hello/', views.api_hello),
]
