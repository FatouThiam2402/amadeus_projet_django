from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_in/',views.sign_in, name='signin')
]

