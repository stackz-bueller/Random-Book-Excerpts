from bs4 import BeautifulSoup
import requests as r
import random

base = 'https://www.gutenberg.org'
url = 'https://www.gutenberg.org/ebooks/search/?sort_order=random'
test = r.get(url).content


def get_random_excerpt(url):
    work = r.get(url).text
    words = work.split('.')

    ws = 0
    while (ws < 175):
        rando = random.randint(int(len(words) * 0.35), int(len(words) * 0.65))
        mid = rando + 1
        mid_ = rando + 2
        end = rando + 3
        excerpt = words[rando] + '. ' + words[mid] + '. ' + words[
            mid_] + '. ' + words[end]
        ws = sum(c.isalpha() for c in excerpt)

    return excerpt.replace('\r\n',
                           ' ').replace('_', ' ').replace('\'', "'").replace(
                               "\ ", '').strip()


def get_excerpt():
    s = BeautifulSoup(test, 'lxml')
    book_tags = s.findAll('li', 'booklink')

    book_list = []
    for book in book_tags:
        try:
            title = book.find(class_='title').get_text()
            if title[-1:] == '\n':
                title = title[:-1]
            author = book.find(class_='subtitle').get_text()
            link = book.find('a').get('href')
            book_list.append({
                'title': title,
                'author': author,
                'link': base + link
            })
        except AttributeError:
            print(' ')

    book = random.choice(book_list)

    new_test = r.get(book['link']).content
    s = BeautifulSoup(new_test, 'lxml')

    link_tags = s.findAll('tr', 'even')
    txt_link = link_tags[-2].get('about')
    excerpt = get_random_excerpt(txt_link)

    data = [book['title'], book['author'], excerpt]
    return data


def runner():
    data = get_excerpt()
    dict_ = {'title': data[0], 'author': data[1], 'text': data[2]}
    return dict_
