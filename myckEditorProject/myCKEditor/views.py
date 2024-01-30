from django.http import JsonResponse
from django.shortcuts import render
from .models import myCKEditor

def myCKEditor_home(request):
    return render(request,"home.html")


def generateCode(request):
    try:
        myCKEditor.objects.all().delete()
        content = request.GET.get('content','')
        data = myCKEditor.objects.create(html_data=content)
        data.save()
        last_inserted_data = myCKEditor.objects.order_by('-id').first()
        # 'id' is assumed to be the primary key field, you can replace it with any other field if needed
    except myCKEditor.DoesNotExist:
        # Handle the case where no data exists
        last_inserted_data = None
    return JsonResponse({'message': last_inserted_data.html_data})
