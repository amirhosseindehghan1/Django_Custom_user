from django.urls import path
from Account.views import MyUserView

urlpatterns = [
    path('account/', MyUserView.as_view()),
    path('account/<int:id>/', MyUserView.as_view())
]