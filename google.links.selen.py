# This script tests the latest version of the google.com web page
# - tests validity of each link found on page
# - saves a list of links found to a date stamped file, to provide a continuous comparison
# - prints invalid links
# - uses selenium webdriver
# - uses requests lib

from selenium import webdriver
import requests
from datetime import datetime


subListOfUrls = []

def fetch_url(url):
    # print "link test: "
    response = requests.get(url)
    assert response.status_code == 200
    if response.status_code != 200:
        print "INVALID LINK: ", url
    else:
        print url


def dumpResults(data):
    
    outF = open('GoogleLinks'+datetime.now().strftime("%Y%m%d-%H%M%S")+'.txt', "w")
    for line in data:
        print >>outF, line
    outF.close()

def main():
    global subListOfUrls
    driver = webdriver.Firefox()
    driver.get('http://google.com')
    print "Testing links in Google Page:"
    
    # Find all Links in the page, and save the list to a file
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        url = elem.get_attribute("href")
        if "javascript:void(0)" in url or "mailto" in url :
            print "INVALID LINK URL: ", url
            continue

        subListOfUrls.append(url)   # add every valid url to subList
        fetch_url(url)

    dumpResults(subListOfUrls)

if __name__== "__main__":
    main()