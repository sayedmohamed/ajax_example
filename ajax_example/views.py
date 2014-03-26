from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse

from ajax_example.models import item

def home(request):
    dropdown_options = item.objects.values("type").distinct()
    return render_to_response("basic_template.html",
                                {"dropdown_options": dropdown_options},
                                context_instance = RequestContext(request)
    )

def ajax_results(request, type=None):
    if request.is_ajax():
        if type:
            matches = item.objects.filter(type__exact = type)
            results = ""
            for each in matches:
                results += "<tr><td>" + each.name + "</td></tr>"
            return HttpResponse(results)
    else:
        return HttpResponse("you aint ajax")
