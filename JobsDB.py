# Brian Day
# Comp 490 - Development Seminar

import sqlite3
from typing import Tuple

import GithubJobsAPI
import StackOverflowJobsRSS


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
    id TEXT PRIMARY KEY,
    company_url TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT NULL,
    title TEXT NOT NULL,
    job_type TEXT NOT NULL
    );''')
# description TEXT DEFAULT NULL


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO JOBS(id, company_url, company, location, title, job_type)
              VALUES(?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, task)
    return cursor.lastrowid


def insert_github_jobs_into_jobs_db(github_jobs_list):
    conn, cursor = open_db("JobsDB.sqlite")  # Open the database to store information.
    for item in github_jobs_list:  # cycle though the list
        task_1 = (item['id'], item['company_url'], item['company'], item['location'], item['title'], item['type'])
        create_task(conn, task_1)
    close_db(conn)  # close database when all done.
    print("Github jobs available: " + str(len(github_jobs_list)))


def insert_stack_overflow_jobs_into_jobs_db(stack_overflow_jobs_data):
    conn, cursor = open_db("JobsDB.sqlite")  # Open the database to store information.
    for post in stack_overflow_jobs_data:  # cycle though the list
        task_1 = (str(post.guid), post.link, post.author, " ", post.title, " ")
        create_task(conn, task_1)
    close_db(conn)  # close database when all done.


def main():
    github_jobs_list = []
    stack_overflow_jobs_data = StackOverflowJobsRSS.stack_overflow_jobs_search()
    GithubJobsAPI.github_jobs_search(github_jobs_list)  # run the job search to store the job data into the list.
    conn, cursor = open_db("JobsDB.sqlite")  # Open the database to store information.
    setup_db(cursor)
    # methods to do the inserting into db.
    insert_github_jobs_into_jobs_db(github_jobs_list)
    insert_stack_overflow_jobs_into_jobs_db(stack_overflow_jobs_data)
    close_db(conn)


if __name__ == '__main__':
    main()
