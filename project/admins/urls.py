from django.urls import path
from admins.views import RetrieveAdminView, RetrieveUserView, ProfileAdminCreateView




urlpatterns = [
    path('create/', ProfileAdminCreateView.as_view(), name='profile-user-create'),
    path('admin/<int:id>', RetrieveUserView.as_view(), name='profile-admin-retrieve'),
    # path('user/<int:id>', RetrieveUserView.as_view(), name='profile-user-retrieve'),
   


]