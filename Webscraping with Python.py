# -*- coding: utf-8 -*-
import nltk
from nltk import FreqDist
import urllib
import codecs
from bs4 import BeautifulSoup

url = "http://lavica.fesb.unist.hr/mat1/predavanja/index.html"
handle = urllib.urlopen(url)
html =  handle.read()

soup = BeautifulSoup(html, 'html.parser')
nodes = []

for link in soup.find_all('a'):
    nodes.append(link.get('href'))
    
nodes = nodes[5:-2]

for node in nodes:
    url = "http://lavica.fesb.unist.hr/mat1/predavanja/" + str(node)
    handle = urllib.urlopen(url)
    html =  handle.read()
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    outputfile = "output/" + str(node)[:-5] + ".txt"
    my_file = codecs.open(outputfile, "w", "utf-8")
    with my_file as file:
        file.write(text)
my_file.close()

for node in nodes:
    file_name = "output/" + str(node[:-5]) + ".txt"
    my_file = codecs.open(file_name, "r", "utf-8")
    my_file_string = ""
  
    for line in my_file:
        my_file_string += line

    my_file_string = my_file_string.lower()
    my_file_string = "".join(c for c in my_file_string if c not in ('!','.',':',')','(',','))

    words = nltk.tokenize.word_tokenize(my_file_string)
    fdist = dict(FreqDist(words))

    output_file_name = "output/" + str(node[:-5]) +"freqdist.txt"

    with codecs.open(output_file_name, 'w', "utf-8") as f:
        for key, value in fdist.items():
            f.write('%s:%s\n' % (key, value))
    my_file.close()
    f.close()