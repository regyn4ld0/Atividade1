from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
queryset=LogMessage.objects.order_by("-log_date")[:5], # :5 limita os resultados às cinco mensagens mais recentes
context_object_name="message_list",
template_name="hello2/home.html",
)

urlpatterns = [
#path("", views.home, name="home"),
path("",home_list_view,name="home"),
path("hello/<str:name>",views.hello_there,name="hello-there"),
path("about/", views.about, name="about"),
path("contact/", views.contact, name="contact"),
path("log/", views.log_message,name="log"),
]

urlpatterns += staticfiles_urlpatterns()



