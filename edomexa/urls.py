from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-place', views.submit_form_place, name='submit-place'),
    path('section/<str:section_id>', views.site_section, name='site_section'),
    path('detalles-post/<int:post_id>', views.post_detail, name='detalles-post'),
    path('nosotros', views.nosotros, name='nosotros'),
]
