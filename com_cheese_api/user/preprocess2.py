from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Okt
from lxml import html
import pytagcloud
import sys

r = lambda: random.randint(0,255)

# 글씨의 랜덤 색깔
color = lambda: (r(), r(), r())

# 최대 100개의 명사 단어 갯수를 찾아냄.
def get_tags(text, ntags=100, multiplier=3):
    spliter = Okt()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return [{'color':color(), 'tag':n,  'size': (c*multiplier)/2}\
            for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname='Nobile', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

# Main

def main():
    text_file = open('com_cheese_api/user/data/users.csv', 'r')
    text = text_file.read()
    tags = get_tags(text)
    draw_cloud(tags, 'wordcloud.png')

    text_file.close()

if __name__ == "__main__":
    main()