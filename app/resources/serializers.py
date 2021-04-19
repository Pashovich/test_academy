from rest_framework import serializers

from .models import Resources


class ResourcesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    unit = serializers.CharField()
    price = serializers.IntegerField(min_value=0)
    amount = serializers.IntegerField(min_value=0)
    cost = serializers.IntegerField(min_value=0, required=False, read_only=True)
    date = serializers.DateField(format='%Y-%m-%d')
    id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['cost'] = validated_data['price'] * validated_data['amount']
        return Resources.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.cost = instance.amount * instance.price
        instance.save()
        return instance
