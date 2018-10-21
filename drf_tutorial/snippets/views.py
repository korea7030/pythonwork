from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from .models import Snippet
from .permissions import IsOnwerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer

from django.http import Http404
# from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

"""
요청(Request) 객체
 - HttpRequest객체를 확장
 - 핵심은 request.data 속성
   request.POST : 폼 데이터만 다루며, 'POST' 메서드에서만 사용 가능
   request.data : 아무 데이터나 다룰 수 있고, 'POST'뿐만 아니라 
                  'PUT'과 'PATCH' 메서드에서도 사용 가능
응답(Response) 객체
 - TemplateResponse 타입
 - 렌더링 안된 content를 client에게 return할 content 형태로 변환
 
API 뷰 감싸기
 - @api_view decorator : 함수기반 뷰
 - APIView : 클래스 기반 뷰
"""
# Create your views here.
# class JSONResponse(HttpResponse):
#     """
#     Return HttpResponse type after convert contents
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    show all list or make snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    else:
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JSONResponse(serializer.data, status=201)
        # return JSONResponse(serializer.errors, status=400)

        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    snippet retrieve or update or delete
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        # return JSONResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(snippet, data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JSONResponse(serializer.data)
        # return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
class based view
"""
# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # """
    # show all list or make snippet
    # """
    ## class based view without mixin
    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ## class based view with mixin
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     """
#     snippet retrieve or update or delete
#     """
    ## class based view without mixin
    # def get_object(self, pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    ## class based view with mixin
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOnwerOrReadOnly, )
    #
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    """
    this viewsets support list and create, retrieve, update, destroy
    add highlight function
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOnwerOrReadOnly)

    # 기본적으로 GET요청에 응답, method 인자 설정 시 POST요청도 가능
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# 리팩토링 - viewset
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list and detail function viewset
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# API 최상단 엔드 포인트 만들기
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })