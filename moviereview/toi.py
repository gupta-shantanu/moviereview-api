import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
###################################################################





ERROR_MESSAGE="Couldn't retrieve data, We are working to fix this."
LANGUAGES=['hindi','english','malayalam','tamil','kannada','bengali','marathi','bhojpuri']
digits=re.compile("\d+")


def extract_class_tag(url,tag):
    html_page = requests.get(url)
    soup = BeautifulSoup (html_page.text ,"html.parser")
    return soup.find_all("div", { "class" : tag })
    
    

        
        

class MovieReview:
    
    @staticmethod
    def get_movies_id(lang='hindi'):
        if not lang in LANGUAGES:
            return dict({"Usupported Language":None})
        url="http://timesofindia.indiatimes.com/entertainment/%s/movie-reviews"%(lang)
        result = extract_class_tag(url, "mr_listing_right")
        lst=list()
        for i in result:
            lst.append((i.h2.a.string.lower(),digits.findall(i.h2.a['href'])[-1]))
        return lst
          
    @staticmethod
    def review_by_id(Id):
        result = BeautifulSoup(str(extract_class_tag("http://timesofindia.indiatimes.com/movie-review/%s.cms"%(str(Id)),  "Normal")[0]),"html.parser")
        review=""
        for s in result.stripped_strings:
               review=review+s
        return review
    
    @staticmethod
    def search_info(movie_name,language=None,review=False):
        pattern = re.compile(movie_name,re.IGNORECASE)
        movie_name=movie_name.lower()
        if language:
            lst=MovieReview.get_movies_id(language)
            for i in lst:
                if pattern.search(i[0]):
                    if review:
                        return MovieReview.review_by_id(i[1])
                    return MovieReview.info_by_id(i[1])
            return "Not Found"
        else:
            for l in LANGUAGES:
                t=MovieReview.search_info(movie_name,l)
                if t!="Not Found":
                    return t
            return "Not Found"

    @staticmethod
    def info_by_id(Id):
        info = BeautifulSoup(str(extract_class_tag("http://timesofindia.indiatimes.com/movie-review/%s.cms"%(str(Id)), "flmcasting")),"html.parser")
        k=info.find_all("span", { "class" : "ratingMovie"})
        dic=dict()
        dic['id']=Id
        dic['rating']=k[0].string
        dic['name']=info.h1.contents[0]
        dic['cast'],dic['directors'],dic['genre'],dic['duration']=map(lambda x:x.string,info.find_all("span", { "class" : "casting" }))

        return dic
                    
                             
        
        
            
            
        
        
        
        
        


      
          
      
      
pprint(MovieReview.search_info("gallows"))
