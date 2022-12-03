from django.urls import path
from . import views
urlpatterns=[
    path ("get",views.getdata),
    path ("add",views.adddata),
    path ("delete/<int:pk>",views.deletedata),
    path("update/<int:pk>",views.updatedata),
    path("retrieve/<int:pk>",views.getlist)
]
