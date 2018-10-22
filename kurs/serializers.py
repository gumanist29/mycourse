from .models import Category, Course, Branch, Contact
from rest_framework import serializers


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Category
        fields = ('name', 'image')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    category = CategorySerializer(many=True)
    

    class Meta:
        model = Course
        fields = ('ids', 'description', 'category', 'logo', 'contacts', 'branches')

    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        categories = validated_data.pop('category')



        
        course = Course.objects.create(**validated_data)
        for contact in contacts:
            Contact.objects.create(course=course,**contact)
            print(Contact)
        for branch in branches:
            Branch.objects.create(course=course, **branch)
            print(Branch)
        return course
