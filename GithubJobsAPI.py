# Brian Day
# Comp 490 - Development Seminar
import json

import requests


def store_data(data):
    data_counter = 0
    for item in data.json():  # going through each dictionary item on the json page.
        data_counter = data_counter + 1
        # Append the item from the dictionary onto the jobs_list
        jobs_list.append(item)


def github_jobs_search():
    page = 1  # the page the url search is on.
    is_page_full = 1
    while is_page_full == 1:
        url1 = 'https://jobs.github.com/positions.json?page=' + str(page)  # re-assign URL for Github Jobs.txt
        raw_data = requests.get(url1)  # requesting the URL and saving it as a data type
        print("PAGE = " + str(page))
        store_data(raw_data)
        if len(jobs_list) % 50 != 0:
            break
        else:
            page = page + 1


# takes a list of dictionaries and saved them to a text file
def write_jobs_to_file(basic_list):
    print("WITHIN write_jobs_to_file()")
    with open('Github Jobs.txt', 'w') as output:  # open the file and close it when actions are done.
        json.dump(basic_list, output)  # write the list of dictionaries to the file


# in future projects - but sure to have all code in functions rather than 'loose' like below
jobs_list = []  # defining a list to store the items from the json dictionary.
github_jobs_search()
write_jobs_to_file(jobs_list)

counts = 0
for job in jobs_list:
    print(job['company'])
    print(job['location'])
    print()
    counts = counts + 1
print(str(counts) + " jobs available.")
