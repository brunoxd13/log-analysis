#!/usr/bin/env python3

ARTICLE_QUERY = """
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

AUTHOR_QUERY = """
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

LOG_QUERY = """
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
