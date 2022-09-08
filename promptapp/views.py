from django.shortcuts import render, redirect 
from .models import Prompt
from .form import PromptForm
# Create your views here.
def prompts(request):
    choas = Prompt.objects.all()
    penit = PromptForm
    
    context = {
        'choas': choas,
        'penit': penit,
    }
    if request.method == 'POST':
        store = PromptForm(request.POST)
        
        if store.is_valid:
            
            store.save()
    
    return render(request, 'promptapp/home.html', context)


def delete(request, pk):
    choas = Prompt.objects.get(id = pk)
    penit = PromptForm
    
    context = {
        'choas':choas,
        'penit': penit
    }
    if request.method == 'POST':
        choas.delete()
        return redirect('/')
    return render(request, 'promptapp/delete.html',context)


def update(request, pk):
    choas = Prompt.objects.get(id = pk)
    penit = PromptForm(instance=choas)
    
    if request.method == 'POST':
        penit = PromptForm(request.POST, instance=choas)
        if penit.is_valid:
            penit.save()
            return redirect('/')
        
    context = {
        'penit' : penit,
        'choas': choas
    }
    return render(request, 'promptapp/update.html', context)
    