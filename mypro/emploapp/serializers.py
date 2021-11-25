from rest_framework import serializers
from .models import employee, stud, cust
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # stude = serializers.PrimaryKeyRelatedField(many=True, queryset=stud.objects.all())
    stude = serializers.HyperlinkedRelatedField(many=True, view_name='stude-detail', read_only='True')
    emplo = serializers.HyperlinkedRelatedField(many=True, view_name='emplo-detail', read_only='True')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'stude', 'emplo', 'owner']


class employeeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = employee
        fields = '__all__'

    def validate_emp_id(self, value):
        print("running:", value)
        if (value < 101):
            raise serializers.ValidationError("EmpId less than 100")
        return value

class studSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = stud
        fields = '__all__'

    def validate_mark(self, value):
        print("running:", value)
        if(value < 60):
            raise serializers.ValidationError("Mark less than 60")
        return value




class studSerializer1(serializers.ModelSerializer):
    class Meta:
        model = stud
        fields = '__all__'

class custSerializer(serializers.ModelSerializer):
    class Meta:
        model = cust
        fields = '__all__'