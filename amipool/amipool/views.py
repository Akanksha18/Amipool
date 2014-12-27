
#from django.http import HttpResponse

from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

from forms import ContactForm

from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')


def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        #books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html')
      
    else:
      return render(request, 'search_form.html', {'error': True})
    
      
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
  
  
def thanks(request):
    return HttpResponse("Thank you for mailing us")


def gmap(request):
    return render(request, 'map.html')


def aka(request):
    
    return render(request, 'aka.html')
