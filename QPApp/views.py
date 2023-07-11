from django.shortcuts import render
from .models import QPModel


def search_view(request):
    search_query = ""
    results = []

    if request.method == 'POST':
        search_query = request.POST.get('subject_name', '').replace(" ", "%20")
        results = QPModel.objects.filter(name__icontains=search_query).values_list('name', flat=True)

    return render(request, 'search.html', {'search_query': search_query, 'results': results})

