from bs4 import BeautifulSoup
import requests as r
import random

base = 'https://www.gutenberg.org'
url = 'https://www.gutenberg.org/ebooks/search/?sort_order=random'
test = r.get(url).content

# Fuction that grabs excerpt from book txt file, url positional varible need
def get_random_excerpt(url):
    work = r.get(url).text
    words = work.split('.')

    ws = 0
    while (ws < 400):
        rando = random.randint(int(len(words) * 0.5), int(len(words) * 0.65))
        excerpt = [words[rando + i] for i in range(0, 14)]
        string_ = '. '.join(excerpt)
        ws = sum(c.isalpha() for c in string_)
    return string_ + '. '

# Function that pulls random book info and link through html parse
def get_random_book():
    s = BeautifulSoup(test, 'lxml')
    book_tags = s.findAll('li', 'booklink')

    book_list = []
    for book in book_tags:
        try:
            title = book.find(class_='title').get_text().rstrip('\\n')
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

    data = [book['title'], book['author'], excerpt, book['link']]
    return data

# Function that zips random book data and hard-coded keys
def runner():
    data = get_random_book()
    keys = ['title', 'author', 'text', 'link']
    dict_ = dict(zip(keys, data))
    return dict_
