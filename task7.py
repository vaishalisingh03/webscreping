import json
import pprint
f = open("movie_details.json","r")
read = f.read()
data = json.loads(read)
def anlayse_movie_directors(movie):
    i = 0
    count_of_director = {}
    while i < len(movie):    
        j = 0
        count = 0
        while j < len(movie[i]["Director:"]):
            count=0
            k=0
            while k<len(movie):
                for l in movie[k]["Director:"]:
                    if movie[i]["Director:"][j]==l:
                        count=1
                k+=1
            count_of_director[movie[i]["Director:"]]=count
            j+=1
        i+=1
    return count_of_director
pprint.pprint(anlayse_movie_directors(data))