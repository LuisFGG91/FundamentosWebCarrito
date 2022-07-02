from ast import Param
from tokenize import group
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render,get_object_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse ,QueryDict
from django import template
from django.urls import reverse
from django.views import View 
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.usuarios.form import ListForm, UsuarioForm
from django.contrib.auth.models import Group
from apps.usuarios.models import User
# from apps.usuarios.models import User
# Función imaginaria para manejar un archivo cargado.
# from somewhere import handle_uploaded_file
from django.contrib import messages
from .models import *
from django.urls import reverse 


class perfilesView(LoginRequiredMixin, UserPassesTestMixin,View):
	login_url = '/login/'
	redirect_field_name = 'redirect_to'
	context = {'segment': 'perfiles'}
	def test_func(self):
		return self.request.user.groups.filter(name="Administrador").exists()
	def get(self, request, action=None, id=None):
		if request.is_ajax():
			if id and action == 'editar':
				edit_row = self.edit_row(id)
				return JsonResponse({'edit_row': edit_row}) 
			elif id and not action:
				edit_row = self.get_row_item(id)
				return JsonResponse({'edit_row': edit_row})
		if id and action == 'editar':
			context, template = self.editar(request, id)
		elif action == 'new':
			context, template = self.new(request)
		else:
			context, template = self.list(request)
		if not context:
			html_template = loader.get_template('page-500.html')
			return HttpResponse(html_template.render(self.context, request))
			
		return render(request, template, context)	
	def post(self, request, action=None, id=None ):
		self.new_instance(request)
		return redirect('users')	
	def put(self, request, id=None, action=None):
		is_done, message = self.update_instance(request,id, True)
		edit_row = self.get_row_item(id)
		return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})
	def delete(self, request, id=None, action=None):
		#transaction = self.get_object(pk)
		#transaction.delete()
		redirect_url = None
		if action == 'single':
			messages.success(request, 'Item deleted successfully')
			redirect_url = reverse('importaciones')
		response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
		return JsonResponse(response)
	""" Get pages """
	def list(self, request):
		self.context['form'] = ListForm()
		group = Group.objects.all()
		self.context['Usuarios'] = group
		return self.context, 'usuario/usuarios/list.html' 
    
	def new(self, request):
		self.context['formAction'] = "Nuevo"
		self.context['formUsuario'] = UsuarioForm()
		return self.context, 'usuario/usuarios/edit.html'
		#return self.context, 
		
		""" Get Ajax pages """
	def editar(self, request, pk):
		usuario = self.get_object_usuario(pk)
		usuario = self.get_object_usuario(usuario.usuario)
		user = self.get_object_user(usuario.user)
		self.context['formAction'] = "Editar"
		self.context['formUsuario'] = UsuarioForm(instance=usuario)
		return self.context, 'usuario/usuarios/edit.html'		
	def edit_row(self, pk):
		usuarios = self.get_object(pk)
		form = UsuarioForm(instance=usuarios)
		context = {'instance': usuarios, 'form': form}
		return render_to_string('usuario/usuarios/edit_row.html', context)
	def get_object_usuario(self, pk):
		queryset = User.objects
		usuario = get_object_or_404(queryset, id=pk)
		return usuario		
	def get_row_item(self, pk):
		transaction = self.get_object(pk)
		edit_row = render_to_string('usuario/usuarios/edit_row.html', {'instance': transaction})
		return edit_row
	def update_instance(self, request, pk, is_urlencode=False):
    
		usuario = self.get_object_usuario(pk)
		form_data_usuario = QueryDict(request.body) if is_urlencode else request.POST
		usuarioForm = usuarioForm(form_data_usuario, instance=usuario)
		if usuarioForm.is_valid():
			usuarioForm.save(commit=False)		
			messages.success(request, 'usuario Creado correctamente.')
		else:
			messages.error(request, 'Error al insertar usuario. Revise los datos.')
		return redirect('users')	
			#return self.context, 
	def new_instance(self, request, is_urlencode=False):
		form_data_usuario = QueryDict(request.body) if is_urlencode else request.POST
		usuarioForm = usuarioForm(form_data_usuario)
		if usuarioForm.is_valid():
			usuarioForm.save(request)		
			messages.success(request, 'usuario Creado correctamente.')
		else:
			messages.error(request, 'Error al insertar usuario. Revise los datos.')
		return redirect('users')	
			#return self.context, 