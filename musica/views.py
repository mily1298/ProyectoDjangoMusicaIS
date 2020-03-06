from django.shortcuts import render
from django.views import View


class Index(View):
    template = "musica/index.html"

    def get(self, request):
        return render(request, self.template)


class TopSongs(View):
    template = "musica/top_songs.html"

    def get(self, request):
        return render(request, self.template)
