from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_POST
from django.shortcuts import reverse
from django.views.decorators.csrf import csrf_exempt
import requests
class Index(View):
    def get(self, request):
        #auth.logout(request)
        print(request.user)
        return render(request=request,template_name='front/app.html')

class DetailView(View):
    def get(self, request, pk):
        data = requests.get('http://127.0.0.1:8000/v1/entry-detail/' + pk).json()
        information = []
        information.append(data['name'])
        information.append(data['city'])
        information.append(data['school'])
        information.append(data['address'])
        information.append(data['distance'])
        information.append(data['time'])
        information.append(data['contact'])
        information.append(data['score'])
        information.append(data['comments'])
        information.append(data['sell'])
        information.append(data['pk'])
        print(information)
        return render(request, 'front/detail.html',{'information': information})

    def patch(self, request, pk):
        # user = auth.authenticate(username='admin', password='666666')
        return JsonResponse({'status':'ok'})
    # @csrf_exempt
    # def dispatch(self, request, *args, **kwargs):
    #     return super(DetailView, self).dispatch(request, *args, **kwargs)

@require_POST
def login(request):
    user = auth.authenticate(username='admin',password='666666')
    if user is not None:
        auth.login(request, user)
        return JsonResponse({"status":"success"})
    else:
        return JsonResponse({"status":"fail"})

@login_required
@require_POST
def logout(request):
    auth.logout(request)
    return JsonResponse({"status":"success"})
