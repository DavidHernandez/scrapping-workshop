import requests
from lxml.html import fromstring

def make_request():
    url = 'https://2022.drupalcamp.es/programa'
    response = requests.get(url)

    if not response.ok:
        raise Exception

    return response.text

def extract_authors(html):
    dom = fromstring(html)
    author_xpath = '//div[@class="schedule-wrapper"]//span[@class="author"]'
    
    authors = [e.text_content() for e in dom.xpath(author_xpath)]
    return authors 

html = make_request()
authors = extract_authors(html)

print(authors)
