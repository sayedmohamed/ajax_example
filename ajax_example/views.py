from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.forms.models import modelform_factory

from ajax_example.models import item

def home(request):
    dropdown_options = item.objects.values("type").distinct()
    add_item_form = modelform_factory(item)
    return render_to_response("basic_template.html",
                                {"dropdown_options": dropdown_options, "add_item_form":add_item_form},
                                context_instance = RequestContext(request)
    )

def ajax_results(request, type=None):
    if request.is_ajax():
        if type:
            matches = item.objects.filter(type__exact = type)
            results = "<h3>Showing results for '" + type + "'</h3>"
            results += "<table>"
            for each in matches:
                results += "<tr><td>" + each.name + "</td></tr>"
            results += "</table>"
            return HttpResponse(results)
    else:
        return HttpResponse("you aint ajax")

def ajax_post_view(request):
    if request.is_ajax():

        if request.method == "POST":
            try:
                itemInDB = item.objects.get(name__exact=request.POST["name"]) #will throw error if does not exist
                return HttpResponse("Error:There is already an item with this name in the database")
            except: #if it isn't there yet
                try:
                    newItem = item(name=request.POST["name"], type=request.POST["type"])
                    newItem.save()
                    return HttpResponse("Successfully added to the database")
                except:
                    return HttpResponse("Error:Item could not be saved.")

        else: #if not POST
            return HttpResponse("Error:Request method is not POST")

    else:
        return HttpResponse("you aint ajax")