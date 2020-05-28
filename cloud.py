import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup

def is_wanted_element(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    return True

def words_in_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(is_wanted_element, texts)  
    return u" ".join(t.strip() for t in visible_texts)

# enter a url to make a word cloud
url = 'https://en.wikipedia.org/wiki/Lauterbrunnen'
page = requests.get(url)
html = page.content
words = words_in_html(html)
# print(words)

wordcloud = WordCloud(width=1000, height=700, max_font_size=70).generate(words)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()