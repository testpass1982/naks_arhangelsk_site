from django.urls import include, path, re_path

import mainapp.views as mainapp

urlpatterns = [
    path("", mainapp.index, name="index"),
    path("about/", mainapp.about, name="about"),
    path("contact/", mainapp.contact, name="contact"),
    path("staff/", mainapp.staff, name="staff"),
    path("documents/", mainapp.documents, name="documents"),
    path("news/", mainapp.news, name="news"),
    path("detailview/<slug:content>/<slug:pk>", mainapp.details, name="detailview"),
    path("create/<slug:content_type>", mainapp.create_factory, name="create"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("messages/", mainapp.messages, name="messages"),
    path("services/", mainapp.services, name="services"),
    path("reestrsp/", mainapp.reestrsp, name="reestrsp"),
]
