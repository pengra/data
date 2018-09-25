from wikibags.models import WikiArticle

import requests
from bs4 import BeautifulSoup

import re
from nltk.tokenize.nist import NISTTokenizer

ENDPOINT = "https://en.wikipedia.org/w/api.php?action=parse&pageid={wiki_id}&format=json"
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
        text = re.sub(r"\[[\ ]{0,}[0-9|edit]{1,}[\ ]{0,}\]", "", text)
        tokens = NIST.tokenize(text, lowercase=True)
        for token in tokens:
            if token:
                yield (tag.name, token)

def create_wikiarticle(wiki_id):
    response = requests.get(ENDPOINT.format(wiki_id=wiki_id))
    if response.ok:
        data = response.json()
        title = data['parse']['title']
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
        wikiarticle = WikiArticle.objects.create(
            wiki_id=wiki_id,
            title=title,
            bag_size=bag_size,
            bag=bag,
            header_bag_size=header_bag_size,
            header_bag=header_bag
        )
        return wikiarticle
    else:
        raise ValueError("Invalid response:", response.status)
        

def get_or_create_wikiarticle(wiki_id):
    wikis = WikiArticle.objects.filter(wiki_id=wiki_id)
    if wikis.exists():
        return wikis[0]
    return create_wikiarticle(wiki_id)