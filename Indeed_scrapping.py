#Indeed data scrapping:

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
from datetime import datetime
import numpy as np


# In[2]:

career = input("Enter the Job:") #use raw_input because input just takes the python expression and does eval on them
careerplus = career.replace(" ","+")
#careerplusnotrail = careerplus.strip()
URL = "https://www.indeed.com/jobs?q="+careerplus+"&explvl=entry_level"

page = requests.get(URL)

soup = BeautifulSoup(page.text,"html.parser")
print(soup.prettify())


# In[3]:

def extractjobtitle(soup):
    jobs=[]
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name ="a", attrs ={ "data-tn-element":"jobTitle"}):
            jobs.append(a["title"]) 
    jobsList = np.array(jobs).tolist()
    return (jobsList)
    
            
list_1=extractjobtitle(soup)            



# In[4]:

def extractcompany(soup): 
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        company = div.find_all(name="span", attrs={"class":"company"})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
        else:
            secondary = div.find_all(name="span", attrs={"class":"result-link-source"})
            for span in secondary:
                companies.append(span.text.strip())
    companiesList = np.array(companies).tolist()
    return(companiesList)
 
list_2 = extractcompany(soup)      


# In[5]:

def extractlocation (soup):
    location = []
    spans = soup.find_all(name="span", attrs = {"class":"location"})
    for span in spans:
        location.append(span.text) #the content of the span tag
    locationList = np.array(location).tolist()
    return (locationList)
list_3 = extractlocation(soup)    


# In[6]:

rows =zip(list_1,list_2,list_3)

with open('C:\\Users\\SHYAM\\Desktop\\index.csv','a') as csv_file:
        writer = csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)


# In[7]:
'''
datas = pd.read_csv('C:\\Users\\SHYAM\\Desktop\\index.csv', parse_dates=True)
datas.head()


# In[8]:

datas[datas['Location'].str.contains('IL')]

'''
# In[ ]:
