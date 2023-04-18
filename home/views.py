import re

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import re_path
from django.views import View
from django.views.static import serve


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'home/index.html')


# class Aha(View):
#     def get(self, request, path):
#         print("salam")
#         print(path)
#         generated_path = re_path(
#             r"^%s(?P<path>.*)$" % re.escape(path.lstrip("/")), serve, kwargs={"document_root": settings.MEDIA_ROOT}
#         ),
#         print("------------")
#         print(generated_path)
#         return HttpResponse("salam")
