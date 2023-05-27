#!/usr/bin/env python3
"""Test local MySQL connection"""
# Path: digital_cv/utils/test_mysqldb.py

import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="cv_user",
                     passwd="password",
                     db="digital_cv")

cursor = db.cursor()

# Execute SQL
cursor.execute("SELECT DATABASE();")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database : %s " % data)

# disconnect from server
db.close()
