import csv
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from googletrans import Translator
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User








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




def Aone(request):
    query = request.GET.get('q', '').lower()
    data = []
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/aone.csv')

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
    return render(request, 'second.html', context)


def Atwo(request):
    query = request.GET.get('q', '').lower()
    data = []
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/atwo.csv')

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
    return render(request, 'atwo.html', context)


def Btwo(request):
    query = request.GET.get('q', '').lower()
    data = []
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/btwo.csv')

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
    return render(request, 'btwo.html', context)

def Cone(request):
    query = request.GET.get('q', '').lower()
    data = []
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/cone.csv')
 
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
    return render(request, 'cone.html', context)


@csrf_exempt
def add_word(request):
    if request.method == 'POST':
        english = request.POST.get('english')
        georgia = request.POST.get('georgia')
        level = request.POST.get('level')

        csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')

        try:
            os.makedirs(os.path.dirname(csv_file), exist_ok=True)
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if os.stat(csv_file).st_size == 0:
                    writer.writerow(['english', 'georgia', 'level'])
                writer.writerow([english, georgia, level])
        except Exception as e:
            return JsonResponse({'error': f'CSV write error: {e}', 'path': csv_file}, status=500)

        return JsonResponse({'success': True, 'word': english, 'georgia': georgia, 'level': level, 'path': csv_file})

    return HttpResponseBadRequest('POST მეთოდი აუცილებელია')


@csrf_exempt
def add_btwo(request):
    if request.method == 'POST':
        english = request.POST.get('english')
        georgia = request.POST.get('georgia')
        level = request.POST.get('level')

        csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/btwo.csv')

        try:
            os.makedirs(os.path.dirname(csv_file), exist_ok=True)
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if os.stat(csv_file).st_size == 0:
                    writer.writerow(['english', 'georgia', 'level'])
                writer.writerow([english, georgia, level])
        except Exception as e:
            return JsonResponse({'error': f'CSV write error: {e}', 'path': csv_file}, status=500)

        return JsonResponse({'success': True, 'word': english, 'georgia': georgia, 'level': level, 'path': csv_file})

    return HttpResponseBadRequest('POST მეთოდი აუცილებელია')




def dashboard(request):
    translated_text = ''
    if request.method == 'POST':
        text_to_translate = request.POST.get('text_to_translate')
        target_lang = request.POST.get('target_lang', 'ka')  
        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_lang)
        translated_text = translation.text

    return render(request, 'dashboard.html', {
        'translated_text': translated_text,
    })

def sign(request):
    if request.method == 'POST':
        name = request.POST['Username']  
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=name).exists():
            return render(request, 'sign.html', {'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'sign.html', {'error': 'Email is already registered'})

        if password1 != password2:
            return render(request, 'sign.html', {'error': 'Passwords do not match'})

        user = User.objects.create_user(username=name, email=email, password=password1)
        user.save()

        login(request, user)  

        return redirect('admin:index')  

    return render(request, 'sign.html')


def long(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")  
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'long.html', {"form": form})     