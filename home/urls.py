from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.pageIndex, name="Index"),
   path('chonchuyende/', views.pageChonChuyenDe, name="ChonChuyenDe"),
   path('chonchuyende/chonexercise/', views.pageChonExercise, name="ChonExercise"),
   path('chonchuyende/chonexercise/baitapABCD/', views.pageChonABCD, name="ABCD"),
   path('chonchuyende/chonexercise/baitapQUESTION_ABCD/', views.pageChonQuestion_ABCD, name="QUESTION_ABCD"),
   path('chonchuyende/chonexercise/baitapTIMVASUALOISAI/', views.pageTimVaSuaLoiSai, name="TIMVASUALOISAI"),
   path('chonchuyende/chonexercise/baitapTEXT/', views.pageChonTEXT, name="TEXT"),
   path('chonchuyende/chonexercise/baitapBIENDOICAU/', views.pageChonBIENDOICAU, name="BIENDOICAU"),
   path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]
