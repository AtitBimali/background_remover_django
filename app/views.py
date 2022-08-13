
from django.shortcuts import render, HttpResponse
import requests
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')

from app.models import Course
from .forms import CourseForm
# from django.core.files.storage import FileSystemStorage
def UploadImage(request):
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('Wait a few Seconds')       
    else:
        form = CourseForm()
    context = {'form':form,}
    return render(request, 'app/upload.html', context)

def output(request):
        
        img = Course.objects.latest('id')
        a = img.image.url
        print(a)
        response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(f'.{a}', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': f'{API_KEY}'},
        )
        if response.status_code == requests.codes.ok:
            with open('media/no-bg.png', 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)
        Course.objects.update(
            result='no-bg.png',
            
        )
        output = Course.objects.latest('result')
        
        context={
            'output':output
        }
        if not context:
            return HttpResponse('Please Go Back and Pick an Image First')
        
        
        return render(request,'app/output.html',context)
def delete_ev():
    abc = Course.objects.all()
    abc.delete()
