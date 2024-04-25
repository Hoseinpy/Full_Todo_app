from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('api/', include('api.urls')),
    
    # Documenting API
    path('api/documention/', schema_view, name='documenting_api')
]
