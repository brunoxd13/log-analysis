#!/usr/bin/env python3

import psycopg2


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
        query = """
                SELECT
                    articles.title,
                    count(*) AS num
                FROM
                    log,
                    articles
                WHERE
                    log.path = '/article/' || articles.slug
                GROUP BY
                    articles.title
                ORDER BY
                    count(*) DESC
                LIMIT 3
        """

        db_cursor.execute(query)
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
        query = """
                SELECT
                    authors.name,
                    count(*) AS num
                FROM
                    log,
                    articles,
                    authors
                WHERE
                    log.path = '/article/' || articles.slug AND
                    articles.author = authors.id
                GROUP BY
                    authors.name
                ORDER BY
                    num DESC
        """

        db_cursor.execute(query)
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
        query = """
                SELECT
                    errors.date,
                    errors.num/total.num::float*100 AS error_rate
                FROM
                    (SELECT
                        time::timestamp::date AS date,
                        count(status) AS num
                    FROM
                        log
                    GROUP BY
                        date, status
                    HAVING
                        status='404 NOT FOUND'
                    ) AS errors,

                    (SELECT
                        time::timestamp::date AS date,
                        count(*) AS num
                    FROM
                        log
                    GROUP BY
                        date
                    ) AS total
                WHERE
                    errors.date = total.date AND
                    errors.num/total.num::float*100 > 1.0
        """

        db_cursor.execute(query)
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
