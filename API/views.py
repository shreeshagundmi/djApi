from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import userSerializer
from .decorators import define_usage
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

from .models import Crud_Users

@login_required(login_url="loginPage")

@api_view(['GET'])
# Create your views here.
def showapi(request):

    api_urls = {
        'List':'/user_list',
        'create':'/user_create',
        'update':'/user_update/<str:pk>/',
        'delete': '/user_delete/<str:pk>/',
        'authuser': '/authuser/',
    }

    return Response(api_urls)

@api_view(['GET'])
def user_list(request):
    list = Crud_Users.objects.all()
    serializer = userSerializer(list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def validate_user(request):
    # serializer = userSerializer(data=request.data)
    # serializer = self.get_serializer(self.get_queryset(), many=True)
    # response = Response(data=serializer.data, headers={'indent': '    '})
    # user = authenticate(request, username=request.cleaned_data['username'], password=request.cleaned_data['password'])
    print(request.query_params)
    return Response(request)

#URL /signin/

@define_usage(params={'username': 'String', 'password': 'String'},
              returns={'authenticated': 'Bool', 'token': 'Token String'})
@api_view(['POST'])
@permission_classes((AllowAny,))
def api_signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except:
        return Response({'error': 'Please provide correct username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'authenticated': True, 'token': "Token " + token.key,'SessionKey':request.session.session_key})
    else:
        return Response({'authenticated': False, 'token': None})



@csrf_protect
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('addandshow')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('showapi')
        else:
            messages.info(request, request)
    # return request
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('showapi')



@define_usage(params={'username': 'String'},
              returns={'authenticated': 'Bool', 'token': 'Token String'})
@api_view(['POST'])
@permission_classes((AllowAny,))
def api_signin_username(request):
    try:
        username = request.data['username']
    except:
        return Response({'error': 'Please provide correct username'},
                        status=HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
        uservalid = authenticate(request, username=user)

        if uservalid is not None:
            login(request, uservalid)
            token,created = Token.objects.get_or_create(user=user)
            return Response(
                {'authenticated': True, 'token': token.key, 'SessionKey': request.session.session_key})
        else:
            return Response({'authenticated': False, 'token': None})
    except User.DoesNotExist:
        return Response({'error': 'user Doesnot Exist'},
                        status=HTTP_400_BAD_REQUEST)

