from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
import requests

from .serializers import SetTimeZoneSerializer, LoginServiceSerializer


class TemplateAPIView(APIView):
    """ Help to build CMS System using DRF, JWT and Cookies
        path('some-path/', TemplateAPIView.as_view(template_name='template.html'))
    """
    permission_classes = (AllowAny,)
    template_name = ''

    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        return Response()


class SetUserTimeZone(GenericAPIView):
    serializer_class = SetTimeZoneSerializer
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # response = Response(serializer.data)
        # response.set_cookie(
        #     key=getattr(settings, 'TIMEZONE_COOKIE_NAME', 'timezone'),
        #     value=serializer.data.get('timezone'),
        #     max_age=getattr(settings, 'TIMEZONE_COOKIE_AGE', 86400),
        # )
        url = settings.API_BLOG_URL + '/users/short/'
        print(url)
        data = {
            'user_ids': [1, 2, 3]
        }
        headers = {
            'Authorization': 'X-HTTP-KEY 3sgyqgmW.SftRAyxMLuuJdulTqrewFGUYLmqnWUJh'

        }
        response = requests.post(url, data=data, headers=headers)
        return Response(response.json())


class LoginServiceView(GenericAPIView):

    serializer_class = LoginServiceSerializer

    def post(self, request):
        url = settings.API_BLOG_URL + '/auth/sign-in/'
        print(url)
        response = requests.post(url, data=request.data)
        return Response(response.json())


class LogoutServiceView(GenericAPIView):

    def post(self, request):
        url = settings.API_BLOG_URL + '/auth/logout/'
        response = requests.post(url)
        return Response(response.json())


class ArticleListView(GenericAPIView):

    def get(self, request):
        url = settings.API_BLOG_URL + '/posts/'
        response = requests.get(url)
        return Response(response.json())



