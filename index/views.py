# REST framework 允许使用基于函数的视图。它提供了一套简单的api_view装饰器来包装你的函数视图
# 以确保它们接收 Request（而不是 Django HttpRequest）实例并允许它们返回 Response（而不是 Django HttpResponse）
# 并允许你配置该请求的处理方式。

from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


# 普通函数方式生成视图,根据id读取数据
@api_view(['GET'])
def product_get(request, pk):
    if request.method == 'GET':
        queryset = Product.objects.filter(id=pk).all()
        # many=True 序列化实例
        serializer = ProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)


# @api_view(['POST'])
# def product_post(request):
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             # 保存数据库
#             serializer.save()
#             # 返回对象response由Django rest Framework实现，status用于设置响应状态码
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# APIView 方式生成视图,分页读取数据
class product_class(APIView):
    # GET请求
    def get(self, request):
        queryset = Product.objects.all()
        # 分页查询, 需要在setting.py中设置REST_FRAMEWORK属性
        pg = PageNumberPagination()
        page_roles = pg.paginate_queryset(queryset=queryset,
                                          request=request,
                                          view=self)
        # 序列化分页实例
        serializer = ProductSerializer(instance=page_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 获取请求数据
        serializer = ProductSerializer(data=request.data)
        # 验证数据
        if serializer.is_valid():
            # 保存数据库
            serializer.save()
            # 返回对象response由Django rest Framework实现，status用于设置响应状态码
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
