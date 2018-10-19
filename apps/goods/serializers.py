#/usr/bin/env python3
#coding=utf-8
from rest_framework import serializers
from .models import Goods, GoodsCategory

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

#Serialzer还可以嵌套使用，覆盖外键字段
class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'