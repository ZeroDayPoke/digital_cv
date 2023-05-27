#!/usr/bin/env python3
"""Test connection to database w/ mypy"""
# Path: digital_cv/utils/test_mypy.py

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='cv_user',
                            password='password',
                            db='digital_cv',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
