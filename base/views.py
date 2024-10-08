from django.shortcuts import render, HttpResponse
from translate import Translator 
# Create your views here.
def home(request):
    context={}
    if request.method == "POST":
        text = request.POST.get("text")
        language = request.POST.get("language")
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        context['translation'] = translation
    return render(request, 'base/home.html', context)