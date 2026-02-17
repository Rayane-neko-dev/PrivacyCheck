from django.shortcuts import render, redirect
from .forms import WebsiteForm

def index(request):
    """
    Pagina principale:
    - Presentazione del GDPR
    - Form per inserire l'URL del sito web
    """
    gdpr_text = """
    Il GDPR (Regolamento Generale sulla Protezione dei Dati) impone ai siti web
    di proteggere i dati personali degli utenti, informare sull'uso dei cookie
    e fornire una politica sulla privacy chiara.
    """
    
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            return redirect(f'/evaluation/?url={url}')
    else:
        form = WebsiteForm()
    
    return render(request, 'core/index.html', {'form': form, 'gdpr_text': gdpr_text})
