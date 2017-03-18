__author__ = 'minin'

import unittest

signsList = '(,.:;!?-); '


class MyTests(unittest.TestCase):

    def setUp(self):
        pass

#extract_words section
    def test_extract_words_1(self):
        self.assertEqual(extract_words('Hello,Hello, my dear!'), ['hello', 'hello', 'my', 'dear'])

    def test_extract_words_2(self):
        self.assertEqual(extract_words('to understand recursion you need first to understand recursion...'), ['to', 'understand', 'recursion', 'you', 'need', 'first', 'to', 'understand', 'recursion'])

    def test_extract_words_3(self):
        self.assertEqual(extract_words('Mom! Mom! Are you sleeping?!!!'), ['mom', 'mom', 'are', 'you', 'sleeping'])

    def test_extract_words_4(self):
        self.assertEqual(extract_words('Mike-Paul mike'), ['mike', 'paul', 'mike'])

    def test_extract_words_5(self):
        self.assertEqual(extract_words('Mike, Paul mike'), ['mike', 'paul', 'mike'])

#extract_words section
    def test_find_most_frequent_1(self):
        self.assertEqual(find_most_frequent('Hello,Hello, my dear!'), ['hello'])

    def test_find_most_frequent_2(self):
        self.assertEqual(find_most_frequent('to understand recursion you need first to understand recursion...'), ['recursion', 'to', 'understand'])

    def test_find_most_frequent_3(self):
        self.assertEqual(find_most_frequent('Mom! Mom! Are you sleeping?!!!'), ['mom'])

    def test_find_most_frequent_4(self):
        self.assertEqual(find_most_frequent('Mike-Paul mike'), ['mike'])


def extract_words(text):
    word = ''
    wordlist = []
    text += '.'
    for letter in text.lower():
        if signsList.count(letter) == 0:
            word += letter
        else:
            if word != '':
                wordlist.append(word)
            word = ''

    return wordlist


def find_most_frequent(text):
    sentence = extract_words(text)
    array, result = [], []

    for word in sentence:
        array.append(sentence.count(word))

    for word in sentence:
        if (sentence.count(word) == max(array)) & (result.count(word) == 0):
            result.append(word)

    return sorted(result)

unittest.main()
#print find_most_frequent('to understand recursion you need first to understand recursion...')
#print extract_words('Mike-Paul-mike')