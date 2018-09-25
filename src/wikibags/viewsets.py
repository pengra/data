from rest_framework import viewsets, permissions, response
from wikibags.serializers import WikiArticleSerializer
from wikibags.models import WikiArticle
from wikibags.tasks import get_or_create_wikiarticle

from django.db.utils import IntegrityError
from django.shortcuts import redirect

class WikiArticleViewset(viewsets.ModelViewSet):
    queryset = WikiArticle.objects.all()
    serializer_class = WikiArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'wiki_id'

    def list(self, request):
        data = {"help": [
            "Look up a wikipedia article analysis. E.g. https://data.pengra.io/wikibags/14003441/",
            "Check out the docs @ https://pengra.github.io/data/wikibags"
        ]}
        return response.Response(data=data, status=200)

    def retrieve(self, request, wiki_id=None):
        "Grab WikiArticles if it doesn't exist."
        try:
            wiki = get_or_create_wikiarticle(wiki_id)
        except ValueError as e:
            return response.Response(data=str(e), status=500)
        except IndexError as e:
            return response.Response(status=404)
        except IntegrityError as e:
            return redirect("wikiarticle-detail", wiki_id=e.args[0])

        serializer = self.serializer_class(wiki)
        return response.Response(serializer.data)
        