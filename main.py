import lxml.html
import random 
import time
from selenium import webdriver

# Make sure that the URL says "pageNumber=1"  (you can also change it manually)
# Most probably digital.ucas.com
url = input("url: ")

# Install and include chrome driver in the same folder
driver = webdriver.Chrome()

courses = ""

todosleep = True

# To have a unique output file name
fname = str(random.randint(0,1000)) + ".txt"

# You might have to stop the loop manualy, there isnt a check for the end of the list
for i in range(10000):

    # Next page (havent tested for number 0 lol)
    driver.get(url.replace("pageNumber=1", "pageNumber=" + str(i)))

    # Gives you a chance to change any settigns before the process begins (helps you change from different grading systems)
    if(todosleep):
        time.sleep(5)
        todosleep = False

    ok = True
    while ok:
        # Details of different elements
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
                print("error") # Sometimes stuff goes wrong

        # Append on every page to not loose all data in the case of an error
        with open(fname,"a+") as f:
            f.write(courses)
        
        courses = ""

print("Done")