1)Write a function that takes a dictionary with numeric values and returns the keys of the top 3 highest values.

from operator import itemgetter
A = {'a':10, 'b':843, 'c': 39,'d':5,'e':300}
def values(dict):
    
    newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)[:3])
    return newA
print (values(A))

2)Write a function that takes two lists of strings as input, and returns a single list of unique strings common to both lists.
list1=['this','this','n','that']
list2=['this','not','that','that']
def common_elements(list1, list2):
    for element in list1:
        if element in list2:
            return list(element)
print (common_elements(list1, list2))

3)Write a function that, using the Star Wars API (swapi.co), takes a character name, and returns a list with the names of the films that character was in.
import requests 
import urllib.parse

#number of pages in JSON feed
page_list = [cheat,more,legacy,novel,bhauballi,prediator]
def Star_Wars(page_list):
    
    for i in range(len(page_list)):
        try:
            pages = page_list[i]
    
            endpoint = "https://swapi.co/api/people/?"
    
            type = 'json'
    
            #specifies api parameters
            url = endpoint + urllib.parse.urlencode({"format": type, "page": pages})
            #print(url_2)
    
            #gets info
            json_data = requests.get(url).json()
            number_of_char = json_data['count']
    
            #list to store names
            st_names = []
    
            count = 0
            while count <= number_of_char:
                print(json_data['results'][count]['name'])
                st_names.append([json_data['results'][count]['name']])
                count = count + 1
    
    #error handling 
        except KeyError:
             print('Key error \n')
             pass
        except IndexError:
            print('Index error \n')
            pass
print Star_Wars(page_list)

4)Write a function that finds the longest repeated substring of a string (for example, running this function with the input of "abccdebccfs" should return “bcc”).

def largest_substring(string):
    l = list(string)
    d = deque(string[1:])
    match = []
    longest_match = []
    while d:
        for i, item in enumerate(d):
            if l[i]==item:
                match.append(item)
            else:
                if len(longest_match) < len(match):
                    longest_match = match
                match = []
        d.popleft()
    return ''.join(longest_match)
