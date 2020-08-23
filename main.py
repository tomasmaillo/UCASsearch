

import lxml.html
import random 
import time
from selenium import webdriver

url = input("url: ")
driver = webdriver.Chrome()
courses = ""
todosleep = True
fname = str(random.randint(0,1000)) + ".txt"
for i in range(10000):
    #print(str(i))

    driver.get(url.replace("pageNumber=1", "pageNumber=" + str(i)))

    tree = lxml.html.fromstring(driver.page_source)

    #results = driver.find_element_by_xpath('course-title')   

    if(todosleep):
        time.sleep(5)
        todosleep = False

    ok = True
    while ok:
        courseName = driver.find_elements_by_class_name('course-title') 
        courseUni = driver.find_elements_by_class_name('provider') 
        coursePoints = driver.find_elements_by_class_name('ucas-points') 
        
        ok = False

        for i in range(len(courseName)):
            try:
                print(courseName[i].text + " ; " + coursePoints[i].text[9:] + " ; " + courseUni[i].text)
                courses += courseName[i].text + " ; " + coursePoints[i].text[9:] + " ; " + courseUni[i].text + "\n"
            except:
                ok = True
                print("error")

        with open(fname,"a+") as f:
            f.write(courses)
        
        courses = ""



print(courses)