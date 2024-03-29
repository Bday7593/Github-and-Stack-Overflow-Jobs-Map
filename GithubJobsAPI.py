# Brian Day
# Comp 490 - Development Seminar

import requests


def store_data(data, my_list):
    for item in data.json():  # going through each dictionary item on the json page.
        my_list.append(item)


def github_jobs_search():
    my_list = []
    page = 1  # the page the url search is on.
    while True:
        url1 = 'https://jobs.github.com/positions.json?page=' + str(page)  # re-assign URL for Github Jobs.txt
        raw_data = requests.get(url1)  # requesting the URL and saving it as a data type
        print("PAGE = " + str(page))
        store_data(raw_data, my_list)
        if len(my_list) % 50 != 0 or page == 10:
            return my_list
        else:
            page = page + 1

# takes a list of dictionaries and saved them to a text file
# def write_jobs_to_file(basic_list):
#  print("WITHIN write_jobs_to_file()")
# with open('Github Jobs.txt', 'w') as output:  # open the file and close it when actions are done.
#    json.dump(basic_list, output)  # write the list of dictionaries to the file
