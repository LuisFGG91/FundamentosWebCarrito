from ast import Param
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View 
from django.views.generic import TemplateView 

import json
from django.contrib import messages
from django.db import connections
 
from .models import *

import datetime 
import calendar

import urllib.request, json 
import urllib.parse

from apps.dashboard.utils import set_pagination

from django.urls import reverse 
 
'''
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('errores/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('errores/page-500.html')
        return HttpResponse(html_template.render(context, request))
'''

class DashboardView(View):
	context = {'segment': 'dashboard'}
	def get(self, request, action=None, id=None):
		if request.headers.get('x-requested-with') == 'XMLHttpRequest':
			if id and action == 'detalle':
				edit_row = self.edit_row(id)
				return JsonResponse({'edit_row': edit_row}) 
			elif id and not action:
				edit_row = self.get_row_item(id)
				return JsonResponse({'edit_row': edit_row})
		
		if id and action == 'detalle':
			context, template = self.detalle(request, id)
		elif action == 'buscar':
			context, template = self.buscar(request)
		else:
			context, template = self.list(request)
		if not context:
			html_template = loader.get_template('errores/page-500.html')
			return HttpResponse(html_template.render(self.context, request))
			
		return render(request, template, context)	

	def post(self, request, action=None, id = None):

			mensaje =""
			respot =""
			if action == "CargaFolio":
				if request.method == "POST":
					try:
						connection = connections['dsad']
						cursor = connection.cursor()
						sql = ' exec [Dps_TraeFoliosDisponibles]'
						cursor.execute(sql)

					except:
						respot = 'warning'
						mensaje ="your token is not correct"
				else:
					respot = 'warning'
					mensaje ="your token is not correct"
				
			return JsonResponse({'valid': respot, 'message': mensaje})

	def put(self, request, action=None, id = None):
		is_done, message = self.update_instance(request, id , True)
		edit_row = self.get_row_item(id)
		return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

	def delete(self, request, action=None, id=None):
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
		
		return self.context, 'dashboard/dashboard/dashboard.html' 
