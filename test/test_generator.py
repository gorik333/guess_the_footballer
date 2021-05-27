import os
import sys
sys.path.append(os.getcwd())

from football import gen_player, parse_html, process_data
import ssl
import urllib.request
import urllib.parse

ctx = ssl.create_default_context()

from random import choice

def test_gen():
    temp = gen_player()
    assert len(temp)>0

def test_parse():
    random_player = choice(list(open('players.txt', encoding='utf-8'))).replace('\n', '')

    url = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(random_player)
    html = urllib.request.urlopen(url, context=ctx)
    result = parse_html(html)

    assert len(result)==2


def test_parse_example():
    url = 'https://en.wikipedia.org/wiki/Lionel_Messi'
    html = urllib.request.urlopen(url, context=ctx)
    result = parse_html(html)

    assert result[1] == "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Lionel_Messi_20180626_%28cropped%29.jpg/220px-Lionel_Messi_20180626_%28cropped%29.jpg"

def test_request():
    url = 'https://en.wikipedia.org/wiki/Lionel_Messi'
    html = urllib.request.urlopen(url, context=ctx)

    assert html.getcode() == 200

def test_false_request():
    url = 'https://en.wikipdsfdfedia.org/wiki/Lionel_Messi'
    try:
        html = urllib.request.urlopen(url, context=ctx)
    except OSError as err:
        assert 1

def test_request_random():
    random_player = choice(list(open('players.txt', encoding='utf-8'))).replace('\n', '')

    url = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(random_player)
    html = urllib.request.urlopen(url, context=ctx)

    assert html.getcode() == 200
