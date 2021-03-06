from wikibags.models import WikiArticle
from wordindex.tasks import populate_from_bag

import requests
from bs4 import BeautifulSoup

import re
from nltk.tokenize.nist import NISTTokenizer

from django.db.utils import IntegrityError

ENDPOINT = "https://en.wikipedia.org/w/api.php?action=parse&{key}={wiki_id}&format=json"
WIKI_PAGE = "https://en.wikipedia.org/wiki/{name}/"

NIST = NISTTokenizer()

def get_article_tokens(data):
    try:
        html = data['parse']['text']['*']
    except KeyError:
        raise ValueError("Invalid wiki json")
    
    soup = BeautifulSoup(html, 'lxml')
    text_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5'])
    
    for tag in text_tags:
        
        text = tag.get_text(separator=' ')
        text = re.sub(r"\[[\ ]{0,}[0-9|edit|citation needed]{1,}[\ ]{0,}\]", "", text)
        tokens = NIST.tokenize(text, lowercase=True)
        for token in tokens:
            if token:
                yield (tag.name, token)

def create_wikiarticle(wiki_id):
    if wiki_id.isdigit():
        response = requests.get(ENDPOINT.format(wiki_id=wiki_id, key="pageid"))
        redirect = False
    else:
        response = requests.get(ENDPOINT.format(wiki_id=wiki_id, key="page"))
        redirect = True
    if response.ok:
        data = response.json()
        if 'error' in data:
            raise ValueError("Not Found", response.json()['error'])
        try:
            wiki_id = data['parse']['pageid']
            title = data['parse']['title']
            page = data['parse']['sections'][0]['fromtitle']
        except KeyError:
            raise ValueError("Wiki API in unexpected format")
        bag = {}
        bag_size = 0
        header_bag = {}
        header_bag_size = 0
        for tag, token in get_article_tokens(data):
            if tag == 'p':
                bag_size += 1
                bag.setdefault(token, 0)
                bag[token] += 1
            else:
                header_bag_size += 1
                header_bag.setdefault(token, 0)
                header_bag[token] += 1
        wikiarticle = WikiArticle(
            wiki_id=wiki_id,
            title=title,
            page=page.lower(),
            bag_size=bag_size,
            bag=bag,
            header_bag_size=header_bag_size,
            header_bag=header_bag
        )
        try:
            wikiarticle.save()
            populate_from_bag(bag, WIKI_PAGE.format(name=page))
        except IntegrityError:
            raise IntegrityError(wiki_id)
        if not redirect:
            return wikiarticle
        raise IntegrityError(wiki_id)
    else:
        raise ValueError("Invalid response:", response.status)
        

def get_or_create_wikiarticle(wiki_id):
    if wiki_id.isdigit():
        wikis = WikiArticle.objects.filter(wiki_id=wiki_id)
        if wikis.exists():
            return wikis[0]
    else:
        wikis = WikiArticle.objects.filter(page=wiki_id.lower())
        if wikis.exists():
            raise IntegrityError(wikis[0].wiki_id)
    
    return create_wikiarticle(wiki_id)