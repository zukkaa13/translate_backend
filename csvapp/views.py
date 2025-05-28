import csv
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from googletrans import Translator

def combined_csv_view(request):
    query = request.GET.get('q', '').lower()
    data = []
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')

    # CSV-ის წაკითხვა და მონაცემების შევსება data-ში
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            # თუ ძებნის სიტყვაა და ის მოიძებნება, ვავსებთ results-ს
            if query and query in row['english'].lower():
                results.append(row)

    context = {
        'data': data,
        'query': query,
        'results': results if query else None,
    }
    return render(request, 'csv_template.html', context)

    

@csrf_exempt
def add_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        georgia = request.POST.get('georgia')
        level = request.POST.get('level')

        if not word or not level:
            return JsonResponse({'error': 'სიტყვა და დონე აუცილებელია'}, status=400)

        csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')
        file_exists = os.path.isfile(csv_file)

        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists or os.stat(csv_file).st_size == 0:
                writer.writerow(['english', 'georgia', 'level'])
            writer.writerow([word, georgia, level])

        return JsonResponse({'success': True, 'word': word, 'georgia': georgia, 'level': level})

    return HttpResponseBadRequest('POST მეთოდი აუცილებელია')



def dashboard(request):
    translated_text = ''
    if request.method == 'POST':
        text_to_translate = request.POST.get('text_to_translate')
        target_lang = request.POST.get('target_lang', 'ka')  # default - ქართულად
        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_lang)
        translated_text = translation.text

    return render(request, 'dashboard.html', {
        'translated_text': translated_text,
    })
