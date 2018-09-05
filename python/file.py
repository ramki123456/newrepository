#!/usr/bin/env python
"""
x = "As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality"
words = x.split(" ")
words.sort()

last_word = ""
for word in words:
    if word != last_word:
        count = [i for i, w in enumerate(words) if w == word]
        #print count
        print(word + " is repeated " + str(len(count)) + " times.")
    last_word = word"""

'''ip=10.1.1.1 color=red house=big
ip=10.1.1.2 color=green house=small
ip=10.1.1.3 animal = dog house=beach
ip=10.1.1.4 color=yellow house=motorhome

with open("/home/brahma/Desktop/file.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if "refer" in part:
                print part

def searcher(outf, inf, string):
    with open(outf, 'a') as f1:
        if string in open(inf).read():
            f1.write(string)'''


'''import re, os


path = raw_input("please enter your path:"")
freddys_library = os.listdir(path)

for book in freddys_library:
    if book.endswith('.txt'):
        file = os.path.join(path, book)
        text=open(file, 'r')
        
        for line in text:
            re_pattern = r'\b(?:refer)\b'
            print len(re.findall(re_pattern, line)), re.findall(re_pattern, line)'''
            

'''for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(file)'''


def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True
print is_palindrome('string')