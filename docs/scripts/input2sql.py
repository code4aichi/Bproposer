#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import argparse
import pymysql.cursors

class UseMySQL:
    def __init__(self,
                 host='localhost', user='root', password='kenken3922',
                 db='aichifood', charset='utf8mb4'):
        self.connection = pymysql.connect(
            host=host, user=user, passwd=password,
            db=db, charset=charset,cursorclass=pymysql.cursors.DictCursor)

    def newfood(self, food_name):
        cursor = self.connection.cursor()
        sql = 'insert into foods(foodname) value ("'+food_name+'")'
        cursor.execute(sql)
        self.connection.commit()


parser = argparse.ArgumentParser(description='Input foods to MySQL.')
parser.add_argument('filename', type=str, help='filename')


args = parser.parse_args()
fname = args.filename

usemysql = UseMySQL()

for line in open(fname, 'r'):
    food_name = line.replace('\n', '').replace('\r', '')
    print(food_name + ' inputting')
    usemysql.newfood(food_name)
    print(food_name + ' ok')
