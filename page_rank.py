'''
I have a short task for you, you will build a very simple web search engine in python.
Implement a method index(urls), which – given a list of input URLs – 

–  downloads each web page 

–  strips tags in the resultingHTML

–  normalizes the text data (e.g., using string.lower() and the module stemming.porter2) 

–  computes and stores a sparse bag-of-words representation of each page (e.g., using python dictionaries) 

run your method to index a list of URLs

Implement a method search(query), which – given a sequence of query words – out- puts a ranked list of web pages in the index based on the cosine distance measure between the bag-of-words representations of queries and web pages. 

Search your index with a few queries like “colosseum”, “hungary”, or “tower”. What results/problems do you observe? State three steps with which you could improve your search results. Ping me incase of any query. You can use numpy or any other library you want.
'''


# Step-1 :- 
# Make a list of urls

urls = [
    'https://en.wikipedia.org/wiki/Castle',
    'https://en.wikipedia.org/wiki/Alcázar_of_Segovia',
    'https://en.wikipedia.org/wiki/Charles_III_of_Spain',
    'https://en.wikipedia.org/wiki/Ferdinand_VI_of_Spain'
    ]
def retrieve_page(url):
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    xyz = soup.find_all('p')
    a = ''
    for x in xyz:
        a += (x.get_text())
    return a 
    
def index(urla):
    # STep-2 Extract text
    text = retrieve_page(urla).lower()
        
    #Step-3 -Convert to array and then stem 
    import numpy as np
    data = np.array(text.split(' '))
    
    
    # Step -4 Stemming data
    
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    bag_of_words = [stemmer.stem(x) for x in data]
    data = bag_of_words
    
    return data


def cosine_sim(text1, text2):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    text1 = ''.join(str(text) for text in text1)
    tfidf = vectorizer.fit_transform([text1,text2])

    return ((tfidf * tfidf.T).A)[0,1]
    
def search(dict):
    
    query = input("Enter the search word:- ").lower()
    prob = []
    for i in range(0,len(dict)):
        prob.append(cosine_sim(str(dict[i]),query))
    print(prob)
def run():
    dict = {}
    for i in range(0,len(urls)):
        dict[i] = index(urls[i])
    search(dict)    

if __name__ == "__main__":
    run()
    
