import json
from urllib import response
from databasefiles.insert import insertres
from flask import jsonify
import requests


APIKEY = "0cdb9c0f1340ed75"

URL = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=0cdb9c0f1340ed75&lat=35.690921&lng=139.70025&range=5&order=4&count=100&format=json"


def request_hotpepper():
    response = requests.get(URL).text
    jsons = json.loads(response)
    
    jsonify = ({
        "data": []
    })

    datas = jsons["results"]["shop"]
    for data in datas:
        # print(data["name"])
        a = insertres(data["name"])
        if(a == "err"):
            print("err")
        else:
            add_data = ({
                "name":data["name"],
                "id":a,
                "photo":data["photo"]["mobile"]["l"],
                "logo": data["logo_image"]
            })
            jsonify["data"].append(add_data)
    return jsonify

# access
# address
# band
# barrier_free
# budget
# budget_memo
# capacity
# card
# catch
# charter
# child
# close
# coupon_urls
# course
# english
# free_drink
# free_food
# genre
# horigotatsu
# id
# karaoke
# ktai_coupon
# large_area
# large_service_area
# lat
# lng
# logo_image
# lunch
# middle_area
# midnight
# mobile_access
# name
# name_kana
# non_smoking
# open
# other_memo
# parking
# party_capacity
# pet
# photo
# private_room
# service_area
# shop_detail_memo
# show
# small_area
# station_name
# sub_genre
# tatami
# tv
# urls
# wedding
# wifi
