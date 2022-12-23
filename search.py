# Author: Dhriti Madireddy
# Email: dmadireddy@umass.edu
# Spire ID: 33858902

import urllib.request
import re
import string
import sys


# Task 2: Fetch Articles
def read_article_file(url):
    req = urllib.request.urlopen(url)
    text = req.read()
    text = text.decode('UTF-8')
    return text


# Task 3: Split the Articles
def text_to_article_list(text):
    # Reference: https://pynative.com/python-regex-split/
    articles = re.split('<NEW ARTICLE>', text, flags=re.IGNORECASE)
    for article in articles:
        if len(article) == 0:
            articles.remove(article)
    return articles


# Task 4: Splitting and Scrubbing
def split_words(text):
    words = []
    split_lines = text.splitlines()
    # Reference: https://www.geeksforgeeks.org/iterate-over-words-of-a-string-in-python/
    for line in split_lines:
        word = line.split()
        words += word
    return words


def scrub_word(text):
    return text.strip(string.punctuation)


def scrub_words(text):
    scrubbed_words = []
    for words in text:
        word_stripped_space = words.strip()
        word = scrub_word(word_stripped_space)
        word_lower = word.lower()
        scrubbed_words.append(word_lower)
    return scrubbed_words


# Task 5: Building an Article Index
def build_article_index(article_list):
    article_index = {}
    for (index, article) in enumerate(article_list):
        split_word = split_words(article)
        for word in split_word:
            scrub_word1 = scrub_word(word).lower()
            if scrub_word1 in article_index:
                article_index[scrub_word1].add(index)
            else:
                if scrub_word1 == "":
                    continue
                article_index[scrub_word1] = {index}
    return article_index

# Task 6: Finding Words
def find_words(keywords, index):
    intersect_docs = set()
    for keyword in keywords:
        if keyword in index:
            if len(intersect_docs) != 0:
                intersect_docs.intersection_update(index[keyword])
            else:
                intersect_docs.update(index[keyword])
    return intersect_docs


if __name__ == "__main__":
    if sys.argv[2] == "find":
        for num in find_words(split_words(sys.argv[3]), build_article_index(text_to_article_list(read_article_file(sys.argv[1])))):
            print(num, end = " ")
    elif sys.argv[2] == "print":
        articles = text_to_article_list(read_article_file(sys.argv[1]))
        print(articles[int(sys.argv[3])])