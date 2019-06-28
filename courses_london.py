# courses_london.py
# manual: https://towardsdatascience.com/building-a-web-scraper-in-python-fb8f48597ec3
# problems: multi line statements, old syntax and class reference in tutorial



from bs4 import BeautifulSoup
import urllib.request as ur


# loop through the 7 pages of undergraduate courses
for i in range(0, 6):

    # read and open url
    urltoscrape = 'https://www.city.ac.uk/courses?level=Undergraduate&p=' + str(i * 10 + 1)
    r = ur.urlopen(urltoscrape).read()
    soup = BeautifulSoup(r, "lxml")

    # attributes for each course
    courselist = soup.find_all("div", attrs=
        {"class": "course-finder__results__item course-finder__results__item--undergraduate"})

    # loop through each course
    for courselistItem in courselist:

        # get course name
        try:
            cnelement = courselistItem.find("div", attrs={"class": "col-sm-24 col-md-18 col-lg-20"})
            cname = cnelement.find('a').text

        except Exception as e:
            cname= ""

        # get course duration
        try:
            cdurelement = courselistItem.find("div", attrs={"class": 'course-finder__results__item__md course-'
                'finder__results__item__md--duration'})
            cdur = cdurelement.find_all("span")[2].text

        except Exception as e:
            cdur = ""

        print(cname)
        print(cdur)
        print('-----------------------')









