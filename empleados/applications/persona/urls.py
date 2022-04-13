from django.urls import path

def DesdeApps(self):
    print("=================DESDE LA APP PERSONA===================")

urlpatterns = [
    path('persona/', DesdeApps),
]