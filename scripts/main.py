#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from bottle import route, get, post, run, HTTPResponse, request
import simplejson as json
import pymysql.cursors

#MariaDBを参照するためのクラス。initを除いて、各関数はHTTP POST/GETに紐づいて呼び出される。
class useMySQL:
    def __init__(self,
                 host='localhost', user='kenken9', password='8b58S3jGp3Tp',
                 db='aichifoods', charset='utf8mb4'): self.connection = pymysql.connect(
            host=host, user=user, passwd=password,
            db=db, charset=charset,cursorclass=pymysql.cursors.DictCursor)

    #全食材情報を吐く関数
    def get_allfood(self):
        cursor = self.connection.cursor()
        sql = 'select id, regionname, foodname from test2'
        cursor.execute(sql)
        return cursor.fetchall()

    #新たな食材情報を登録する関数
    def newfood(self, region_name, food_name):
        cursor = self.connection.cursor()
        sql = 'insert into foods(regionname, foodname) value ("'+region_name+','+food_name+'")'
        cursor.execute(sql)
        self.connection.commit()

@route('/')
def index():
    return ""

#食材更新リクエスト(POST)が届いた場合の処理
@post('/api/new')
def new():
    regionname = request.forms.regionname
    foodname = request.forms.foodname
    usemysql = useMySQL()
    usemysql.newfood(regionname, foodname)
    body = json.dumps({
        'message' : 'OK',
        'regionname' : regionname,
        'foodname' : foodname
    })
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    r.set_header('Access-Control-Allow-Origin', '*')
    return r

#GETに対する食材情報返答処理。DBを参照し全食材情報をJSONに乗せて投げ返す。
@get('/api/foods')
def foods():
    usemysql = useMySQL()
    #全食材情報をDBから取得。DB情報をそのまま変数foodsへ代入。(get_allfood()参照
    foods = usemysql.get_allfood()
    body = json.dumps({
            'message' : 'OK',
            'foods' : foods
        })
    r = HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'application/json')
    r.set_header('Access-Control-Allow-Origin', '*')
    return r

run(host='0.0.0.0', port=8080, debug=True)
