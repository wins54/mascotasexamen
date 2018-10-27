from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import DesempenoForm, MascotaForm
from mascotas.models import Desempeno, Categoria, Mascota
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def desempeno_nueva(request):
    if request.method == "POST":
        formulario = DesempenoForm(request.POST)
        if formulario.is_valid():
            desempeno = Desempeno.objects.create(
                nombre=formulario.cleaned_data['nombre'], anio=formulario.cleaned_data['anio'])
            for mascota_id in request.POST.getlist('mascotas'):
                categoria = Categoria(
                    mascota_id=mascota_id, desempeno_id=desempeno.id)
                categoria.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Desmpeño Guardada Exitosamente')
            return redirect('post_list')
    else:
        formulario = DesempenoForm()
    return render(request, 'mascotas/mascota_editar.html', {'formulario': formulario})


@login_required
def desempeno_nueva1(request, pk):
    post = get_object_or_404(Mascota, pk=pk)
    formulario = MascotaForm(request.POST or None, instance=post)
    if formulario.is_valid():
        formulario.save()
        return redirect('post_list')
    return render(request, 'mascotas/mascota_nuevo.html', {'formulario': formulario})


def post_list(request):
    posts = Categoria.objects.all()
    mascota = Mascota.objects.all()
    return render(request, 'mascotas/post_list.html', {'posts': posts, 'mascota': mascota})


@login_required
def post_remove(request, pk):
    Mascota.objects.filter(pk=pk).delete()
    return redirect('post_list')


@login_required
def post_remove1(request, pk):
    Desempeno.objects.filter(pk=pk).delete()
    return redirect('post_list')


@login_required
def mascota_create(request):
    if request.method == "POST":
        formulario = MascotaForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect(post_list)
    else:
        formulario = MascotaForm()
    return render(request, 'mascotas/mascota_nuevo.html', {'formulario':  formulario})
