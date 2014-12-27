#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def hello(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('hello.html',  context_instance=context)

#def hello(request):
    #return render(request, 'hello.html')
#def hello(request):
    #return render(request, 'base.html')