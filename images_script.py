import pandas as pd
import urllib.request

#------------------------
def url_to_png(i,url,sources,file_path):
    filename="{}-{}.png".format(sources[i],i)
    full_path="{}{}".format(file_path,filename)
    urllib.request.urlretrieve(url,full_path)
    print("{} saved".format(filename))

    return None


FILENAME="Fall 2019 Plumes detected by AVIRIS-NG and GAO provided by NASA-JPL and U.Arizona.csv"
FILE_PATH="images/"
df=pd.read_csv(FILENAME)
continue_from=1081
urls=df["imageurl"][1081:]
sources=df["source_type"][1081:]
j=1081
for i,url in enumerate(urls.values):
    
    url_to_png(j,url,sources,FILE_PATH)
    j+=1
#j=1080 not found