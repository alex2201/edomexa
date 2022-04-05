# Create your views here.
from django.http.response import JsonResponse, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse

from edomexa.models import SiteSection, Post
import edomexa.constants as c


def index(request):
    context = {
        'navbar_options': c.create_navbar_options(''),
        'sections': c.HOMEPAGE_SECTIONS,
        'municipios': c.MUNICIPIOS,
        'tipo_lugar': c.TIPO_LUGAR,
    }
    return render(request, 'edomexa/index.html', context)


def site_section(request, section_id):
    section = c.HOMEPAGE_SECTIONS[section_id]

    if section is None:
        return Http404()

    sectionDB = SiteSection.objects.get(pk=section[0])

    if sectionDB is None:
        return Http404()

    postsDB = sectionDB.post_set.all()
    p_sections = [x.postsection_set.all() for x in postsDB]
    context = {
        'navbar_options': c.create_navbar_options(request.path),
        'section': sectionDB,
        'posts': p_sections,
    }

    return render(request, 'edomexa/seccion.html', context)


def post_detail(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    sections = post.postsection_set.all()

    context = {
        'navbar_options': c.create_navbar_options(request.path),
        'p_id': post_id,
        'post': post,
        'sections': sections,
    }
    return render(request, 'edomexa/detalle_seccion.html', context)


def submit_form_place(request):
    print(request.POST)
    data = request.POST
    municipio = ''

    for m in c.MUNICIPIOS:
        if m[0] == data['seleccion-municipio']:
            municipio = m[1]
            break

    context = {
        'nombre': data['nombre-lugar'],
        'municipio': municipio,
        'tipo': data['tipo-lugar-group'],
        'descripcion': data['texto-lugar-descripcion'],
    }
    html_string = render_to_string('edomexa/registro_ubicacion.html', context=context)
    send_mail('Nuevo registro de lugar', '', 'no-reply@edomexa.com', c.EMAIL_LIST, html_message=html_string)
    return JsonResponse({'status': 200, 'message': 'form received'})


def submit_form_person(request):
    data = request.POST

    context = {
        'nombre': data['nombre-persona'],
        'apellidos': data['apellidos-persona'],
        'facebook': data['facebook'],
        'instagram': data['instagram'],
        'tiktok': data['tiktok'],
    }
    html_string = render_to_string('edomexa/registro_persona.html', context=context)
    send_mail('Nuevo registro de persona', '', 'no-reply@edomexa.com', c.EMAIL_LIST, html_message=html_string)
    return JsonResponse({'status': 200, 'message': 'form received'})


def nosotros(request):
    context = {
        'navbar_options': c.create_navbar_options(request.path),
    }
    return render(request, 'edomexa/nosotros.html', context)
