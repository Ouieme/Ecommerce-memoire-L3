from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics

from .mixins import MultipleFieldLookupMixin
from .models import Admin
from .serializers import ProfileAdminSerializer,AdminSerializer
from  Comptes.serializers import ProfileUserSerializer


# Create your views here.
class ProfileAdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = ProfileAdminSerializer

    def perform_create(self, serializer):
        # Get the current user from the request object

        user = User.objects.create_user(self.request.data.get('username'), self.request.data.get('email'),
                                        self.request.data.get('password'),
                                        first_name=self.request.data.get('firstname'),
                                        last_name=self.request.data.get('lastname'))


        serializer.save(user=user,nom=self.request.data.get('nom'), type_Admin=self.request.data.get('type_Admin'))

# update

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Retrieve the existing Admin instance

        # Update the user fields
        user_data = {
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'first_name': request.data.get('firstname'),
            'last_name': request.data.get('lastname')
        }
        user_serializer = User(instance.user, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        # Update the Admin fields
        admin_data = {
            'nom': request.data.get('nom'),
            'type_Admin': request.data.get('type_Admin')
        }
        serializer = self.get_serializer(instance, data=admin_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)



# Create an admin object and associate it with the user

class RetrieveAdminView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = ProfileAdminSerializer
    lookup_fields = ['type_Admin']

class RetrieveUserView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUserSerializer
    lookup_fields = ['id']

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F


from django.shortcuts import render
from .models import Admin

def admin_details(request, admin_id):
    admin_instance = Admin.objects.get(id=admin_id)

    # Accessing the username of the associated User object
    username = admin_instance.user.username

    # Accessing the type_Admin field value
    type_admin = admin_instance.type_Admin

    context = {
        'username': username,
        'type_admin': type_admin
    }

    return render(request, 'admin_details.html', context)

class AdminDetailsView(APIView):
    def get(self, request, admin_id):
        admin_instance = Admin.objects.get(id=admin_id)
        serializer = AdminSerializer(admin_instance)
        return Response(serializer.data)
