#!/usr/bin/env python3

import psycopg2
from queries import ARTICLE_QUERY, AUTHOR_QUERY, LOG_QUERY


class DataBaseUtils():
    def connect_to_database(self, db_name):
        """Connects to the news database and return a database cursor."""
        try:
            database = psycopg2.connect("dbname=%s" % db_name)
            return database.cursor()
        except:
            print("Failed to connect to database.")
            return None


class LogAnalyzer():
    def most_popular_three_articles(self, db_cursor):
        """
        Query and print out the 3 most popular articles.

        Args:
            db_cursor: psycopg2 PostgreSQL database cursor object.
        """

        db_cursor.execute(ARTICLE_QUERY)
        results = db_cursor.fetchall()

        print('------ Three most popular articles of all time ------')
        print('=====================================================')

        for result in results:
            print('"{title}" - {count} views'.format(
                title=result[0], count=result[1]))

        print('')

    def most_popular_authors(self, db_cursor):
        """Query and print out the most popular authors.

        Args:
            db_cursor: psycopg2 PostgreSQL database cursor object.
        """

        db_cursor.execute(AUTHOR_QUERY)
        results = db_cursor.fetchall()

        print('------ Most popular authors of all time ------')
        print('==============================================')

        for result in results:
            print('{author} - {count} views'.format(
                author=result[0], count=result[1]))

        print('')

    def days_greater_than_1pc_errors(self, db_cursor):
        """Query and print out days where the error rate is greater than 1%.

        Args:
            db_cursor: psycopg2 PostgreSQL database cursor object.
        """

        db_cursor.execute(LOG_QUERY)
        results = db_cursor.fetchall()

        print('------ Days with greater than 1% errors ------')
        print('==============================================')

        for result in results:
            print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
                date=result[0], error_rate=result[1]))

        print('')


if __name__ == "__main__":

    db_instance = DataBaseUtils().connect_to_database("news")

    if db_instance:
        log = LogAnalyzer()

        log.most_popular_three_articles(db_instance)
        log.most_popular_authors(db_instance)
        log.days_greater_than_1pc_errors(db_instance)

        db_instance.close()
