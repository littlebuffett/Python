import hmac
import hashlib
import requests
from time import gmtime, strftime
import urllib
import os
import review

REQUEST_METHOD = "POST"
DOMAIN = "https://api-gateway.coupang.com"

ACCESS_KEY = "쿠팡파트너스 API 키"
SECRET_KEY = "쿠팡파트너스 API 키"

def generateHmac(method, url, secretKey, accessKey):
    path, *query = url.split("?")
    datetimeGMT = strftime('%y%m%d', gmtime()) + 'T' + strftime('%H%M%S', gmtime()) + 'Z'
    message = datetimeGMT + method + path + (query[0] if query else "")

    signature = hmac.new(bytes(secretKey, "utf-8"),
                         message.encode("utf-8"),
                         hashlib.sha256).hexdigest()

    return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey, datetimeGMT, signature)


# 카테고리별 인기 상품 정보 받아오기
def get_best_categories():
    categorie_id = [1001, 1002, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1024, 1025, 1026, 1029, 1030]
    categorie = int(input("카테고리를 선택하세요\
                    \n1:여성패션\
                    \n2:남성패션\
                    \n3:뷰티\
                    \n4:출산/유아동\
                    \n5:식품\
                    \n6:주방용품\
                    \n7:생활용품\
                    \n8:홈인테리어\
                    \n9:가전디지털\
                    \n10:스포츠/레저\
                    \n11:자동차용품\
                    \n12:도서/음반/DVD\
                    \n13:완구/취미\
                    \n14:문구/오피스\
                    \n15:헬스/건강식품\
                    \n16:국내여행\
                    \n17:해외여행\
                    \n18반려동물용품\
                    \n19유아동패션\n:"))

    REQUEST_METHOD = "GET"
    URL = "/v2/providers/affiliate_open_api/apis/openapi/v1/products/bestcategories/" + str(categorie_id[categorie-1])
    authorization = generateHmac(REQUEST_METHOD, URL, SECRET_KEY, ACCESS_KEY) # 일반 url
    url = "{}{}".format(DOMAIN, URL)
    response = requests.request(method=REQUEST_METHOD, url=url,
                                headers={
                                    "Authorization": authorization,
                                    "Content-Type": "application/json"
                                })
    # print(response.json())
    json_res = response.json()
    return json_res['data']

# 키워드 검색 결과 상품 10개 상품정보
def get_products_search(keyword):
    REQUEST_METHOD = "GET"
    URL = "/v2/providers/affiliate_open_api/apis/openapi/v1/products/search?keyword="+urllib.parse.quote(keyword) 
    authorization = generateHmac(REQUEST_METHOD, URL, SECRET_KEY, ACCESS_KEY)
    url = "{}{}".format(DOMAIN, URL)
    response = requests.request(method=REQUEST_METHOD, url=url,
                                headers={
                                    "Authorization": authorization,
                                    "Content-Type": "application/json"
                                })
    json_res = response.json()
    return json_res['data']['productData']

def save_images(data, keyword): # data는 딕셔너리 리스트인 productData
    path = 'AutoPostProject/postData/'+ keyword
    os.mkdir(path)
    for i in data:
        urllib.request.urlretrieve(i['productImage'], path + '/' + str(i['productId']) + '.jpg')

def add_review(products_data):
    for i in products_data:
        i_review = review.get_review(i['productUrl'])
        i['productReview'] = i_review
    
    return products_data
# urls = ['https://www.coupang.com/vp/products/5358757879?itemId=7416308410&vendorItemId=82042278784&q=%EB%85%B8%ED%8A%B8%EB%B6%81&itemsCount=36&searchId=e2ab7be26f0b404ba608775ec6e9e0c6&rank=2&isAddedCart=']
# print(convert_urls(urls))
# print(get_best_categories())

input_keyword = input("상품 키워드를 입력해주세요:")
products_data = get_products_search(input_keyword)
products_data = add_review(products_data)
save_images(products_data, input_keyword)
print(products_data)