# Create your views here.
from django.http.response import JsonResponse, Http404
from django.shortcuts import render
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


# TODO: Validate form
def submit_form_place(request):
    print(request.POST)
    return JsonResponse({'status': 200, 'message': 'form received'})


def nosotros(request):
    context = {
        'navbar_options': c.create_navbar_options(request.path),
    }
    return render(request, 'edomexa/nosotros.html', context)
