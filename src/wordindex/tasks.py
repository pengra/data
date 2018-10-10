from wordindex.models import WordIndex, Word, Webpage


def populate_from_wikibags():
    from data.settings import INSTALLED_APPS
    assert "wikibags" in INSTALLED_APPS
    assert WordIndex.objects.all().count() == 0
    from wikibags.models import WikiArticle
    for article in WikiArticle.objects.all():
        populate_from_bag(article.bag, article.link)


def populate_from_bag(bag, url):
    pages = Webpage.objects.filter(url=url)
    if pages.exists():
        page = pages[0]
    else:
        page = Webpage.objects.create(url=url)
    
    for word, count in bag.items():
        words = Word.objects.filter(word=word)
        if words.exists():
            wordEntry = words[0]
        else:
            wordEntry = Word()

        wordEntry.word = word
        if wordEntry.count is None:
            wordEntry.count = 0
        wordEntry.count += count
        wordEntry.save()

        wordIndex = WordIndex(
            word=wordEntry,
            url=page,
            count=count
        )
        wordIndex.save()
    
