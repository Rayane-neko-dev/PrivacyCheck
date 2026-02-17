from django.shortcuts import render
import requests

def report(request):
    url = request.GET.get('url', None)
    results = {}
    suggestions = []

    if url:
        # Controllo HTTPS
        results['HTTPS abilitato'] = 'Sì' if url.startswith('https://') else 'No'
        if not url.startswith('https://'):
            suggestions.append("Utilizzare HTTPS per proteggere i dati degli utenti.")

        # Recupera HTML del sito
        try:
            r = requests.get(url, timeout=5)
            html = r.text.lower()
        except:
            html = ''
            suggestions.append("Impossibile recuperare il sito, controllare l'URL.")

        # Privacy Policy
        results['Privacy Policy'] = 'Presente' if 'privacy' in html or 'confidentiality' in html else 'Assente'
        if results['Privacy Policy'] == 'Assente':
            suggestions.append("Aggiungere una politica sulla privacy chiara.")

        # Cookie / tracking
        results['Cookie utilizzati'] = 'Sì' if 'cookie' in html else 'No'
        results['Script di tracciamento'] = 'Sì' if 'analytics' in html or 'track' in html else 'No'

        # Conformità GDPR complessiva
        compliant = results['HTTPS abilitato'] == 'Sì' and results['Privacy Policy'] == 'Presente'
        results['Conforme al GDPR'] = '✅ Sì' if compliant else '❌ No'

        if not compliant:
            suggestions.append("Assicurarsi che il sito rispetti le norme GDPR.")
    
    return render(request, 'evaluation/report.html', {
        'url': url, 
        'results': results,
        'suggestions': suggestions
    })
