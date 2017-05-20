from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def edit_docs(request):
	t = get_template('edit.html')
	html = t.render()
	return HttpResponse(html)