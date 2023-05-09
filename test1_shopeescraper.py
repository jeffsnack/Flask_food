import requests
import json
import pandas as pd
import time
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
import random
class shopee:
    def __init__(self,keyword='益生菌',page=50):
        #keyword='益生菌'
        #page=50
        self.keyword = keyword
        self.page = page
        self.ecode = 'utf-8-sig'
        self.my_headers = {'accept': 'application/json',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                           'af-ac-enc-dat': 'AAcyLjUuMC0yAAABhPqw6M8AAA8yAuAAAAAAAAAAAuvlR3weVVU60ykHUkkzSmQs+0sol/82EyfDx/bVRcPaaRvYm/EPDX1dVdI5oYrZLxjaGDx26LEgUOjodcncE6Yg6WKu1vXKgkevik2Q4v9VqxQ9eS0l9PEb4Teh1BUvnobnBB1Q6LZ+zG1WkIrxYjgZRuEgJBQZUrOJM/WzXkA0Bp4OcYDekqSusSGiW0OePuYl7F3gdnvQsdSuw2YtunUAOn++EVfp3mJSH6CwQkb+mjiQonyC4myOvxQZPLHIZ3+GtkxBbg/3MkP+4qsvOiuROLSITEZYzRC80owJth3u6ia7CLNTG4n6YRX1KIAmgZ9FoyeX/zYTJ8PH9tVFw9ppG9ibmQjgXUXTpPPKz8uOifIZL3LtUr0qb8Up/lFStMzi/DXP6BE1TRhGpUuMlUW3oQtbJ1YfnFgM6NCI7hOYN49T1mY2C2jMsClKpYZCS3IiePwORGIsK9CwN1RXADveQ87qXL6hI4BMiwjqkLX6eXr43FyqPLAn+EX/M6j/n2SQM5hIqrW9XhLiTEaXFHK8odgVkzNagY60jMbDqdPrdnANmQsNXts5GyAjI8vnGItu2NMBPK5gzPUDad2VMXIPaPl/4tJ6UWEDf1XX/W5ffJijZ0ckfn/aqZ2EUBMC3PvgG/VHkCbuGMzaXlWeRe6wdlHm6bulLTY4m8Qhuucz/q6VcozaSwO/1GXe2Xe6/gfPKa8kRcw/CunlTmb6k/CQFEojN5NwO1tj5RgI6LeacDwoJwsNXts5GyAjI8vnGItu2NPwU5s8NK4u8YHVtX/D9UCK7JI+GvaQBQaPNzaDomSUCKyCYsWyTdGxI4JNqkobJ9bYK+TfV0ZmwYOgnxiJgWgXE3lAIW6HSbZruJCwVQDfyD/17aObFq0w7JbC4v+ZanJ4aocGcmOfvHkaAE2P7Mad98jZ/901tpYwiYTjGF/2xDr16r7zHBobXLhTaV9FwrzudclpBpAZJy+v3NPMjiQY',
                           'content-type': 'application/json',
                           'cookie': '__LOCALE__null=TW; SPC_T_IV=NGdRT29YMEs3ZWhMYzlSZw==; SPC_SI=MLh0YwAAAAA5dmxseWpieU246AIAAAAANGJGRGZqUTg=; SPC_F=w126JfAtgQ4v3OWNDFSEI1GcT8cuQ1UZ; REC_T_ID=a74f292b-784f-11ed-a3a6-0a6880582719; SPC_R_T_ID=tDxOjCDS3y+d3IbptFPlS1McB4gqiE4zTLLdIxVMN7uuti/1Mq+r8Q6jDefYfMK2XOwcNRCa47ts8KkD7uZ9HvIjLwYL9kiPl9oqgX13OIR8U5GLtQKk8uXJjdIm9sCgpOU0KZ+bHlPYfnPFSdBVyAcEdnK1Uz+BdZKJ7diEduE=; SPC_R_T_IV=NGdRT29YMEs3ZWhMYzlSZw==; SPC_T_ID=tDxOjCDS3y+d3IbptFPlS1McB4gqiE4zTLLdIxVMN7uuti/1Mq+r8Q6jDefYfMK2XOwcNRCa47ts8KkD7uZ9HvIjLwYL9kiPl9oqgX13OIR8U5GLtQKk8uXJjdIm9sCgpOU0KZ+bHlPYfnPFSdBVyAcEdnK1Uz+BdZKJ7diEduE=; csrftoken=DWZUZXY9cOKbUoUrZD6iQ0StMEgg8qLz; _gcl_au=1.1.1980051361.1670651905; _fbp=fb.1.1670651905078.210500608; _QPWSDCXHZQA=d7e945cb-dbe5-4cd4-d11d-4ced244cd171; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.88823259.1670651910; _med=refer; _dc_gtm_UA-61915057-6=1; _ga=GA1.1.1738703988.1670651908; shopee_webUnique_ccd=v9OtM7e9E%2BHnnqOiM0oWyA%3D%3D%7CvpeGiWr78lrv8AN6rqwEgswAH3NzT3xd7IuEppCU4bilvPNTe%2BaG%2F4EqXnyh%2FApx9cEsof9ljXefD%2Fd2IGNjBjQzrcinQ%2F9nBQY%3D%7Cv06r0GXydYJPZUM4%7C06%7C3; ds=c1cfafc2060dd6821a70092b2263aee8; cto_bundle=u_kYXV9Na1JScjFxWDIlMkZhajFZd05kM0klMkJWQ3dONGo0bG9udUVSbyUyQjhEODBPd2x0cE5yTkRuNkMxZThlSTFMeGVvbzRSMDFJMHMyaEtlc1ZiT3VDT0xqaU5DTnpjMldYJTJCTTFFMVZsckJPZWoyT1RuZ0pxVEVQdVRkYWklMkZCVzZYSyUyRmpzS3UzellYRkpDbkl6aUNlYU9NdzhnS0ElM0QlM0Q; _ga_RPSBE3TQZZ=GS1.1.1670651907.1.1.1670653221.32.0.0',
                           'referer': 'https://shopee.tw/%E8%8A%B1%E8%A5%AF%E8%A1%AB-50%E6%AC%BE%E5%8F%AF%E9%81%B8-%E9%96%8B%E8%A1%AB-%E8%A5%AF%E8%A1%AB-%E7%94%B7%E7%94%9F%E5%A4%8F%E5%A8%81%E5%A4%B7%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-%E5%BA%A6%E5%81%87%E9%A2%A8%E8%A5%AF%E8%A1%AB-%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-%E4%BA%94%E5%88%86%E8%A2%96%E8%A5%AF%E8%A1%AB-%E7%94%B7%E7%94%9F%E4%B8%8A%E8%A1%A3-%E5%AF%AC%E9%AC%86%E8%8A%B1%E8%A5%AF%E8%A1%AB-%E8%A5%AF%E8%A1%AB-%E6%BC%94%E5%87%BA%E6%9C%8D-i.5695643.16302986550?sp_atk=922fd522-78bf-4c74-b741-b91f88babb79&xptdk=922fd522-78bf-4c74-b741-b91f88babb79',
                           'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"Windows"',
                           'sec-fetch-dest': 'empty',
                           'sec-fetch-mode': 'cors',
                           'sec-fetch-site': 'same-origin',
                           'sz-token': 'v9OtM7e9E+HnnqOiM0oWyA==|vpeGiWr78lrv8AN6rqwEgswAH3NzT3xd7IuEppCU4bilvPNTe+aG/4EqXnyh/Apx9cEsof9ljXefD/d2IGNjBjQzrcinQ/9nBQY=|v06r0GXydYJPZUM4|06|3',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                           'x-api-source': 'pc',
                           'x-csrftoken': 'DWZUZXY9cOKbUoUrZD6iQ0StMEgg8qLz',
                           'x-requested-with': 'XMLHttpRequest',
                           'x-shopee-language': 'zh-Hant'}

    # 進入每個商品，抓取買家留言
    def goods_comments(self,item_id, shop_id):
        url = 'https://shopee.tw/api/v2/item/get_ratings?filter=0&flag=1&itemid='+ str(item_id) + '&limit=59&offset=0&shopid=' + str(shop_id) + '&type=0'
        r = requests.get(url,headers = self.my_headers)
        st= r.text.replace("\\n","^n")
        st=st.replace("\\t","^t")
        st=st.replace("\\r","^r")

        gj=json.loads(st)
        return gj['data']['ratings']

    def scraper(self):
        # 自動下載ChromeDriver
        service = ChromeService(executable_path=ChromeDriverManager().install())

        # 關閉通知提醒
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)

        # 開啟瀏覽器
        driver = webdriver.Chrome(service=service,chrome_options=chrome_options)
        time.sleep(5)

        driver.get('https://shopee.tw/search?keyword=' + self.keyword )
        time.sleep(10)

        print('---------- 開始進行爬蟲 ----------')
        tStart = time.time()#計時開始

        container_product = pd.DataFrame()
        container_comment = pd.DataFrame()
        
        i=0
        for i in range(int(self.page)):
            # 準備用來存放資料的陣列
            itemid = []
            shopid =[]
            name = []
            brand = []
            stock = []
            price = []
            ctime = []
            currency = []
            description = []
            discount = []
            can_use_bundle_deal = []
            can_use_wholesale = []
            tier_variations = []
            hashtag_list = []
            historical_sold = []
            is_cc_installment_payment_eligible = []
            is_official_shop = []
            is_pre_order = []
            is_slash_price_item = []
            liked_count = []
            shop_location = []
            SKU = []
            view_count = []
            cmt_count = []
            five_star = []
            four_star = []
            three_star = []
            two_star = []
            one_star = []
            rating_star = []
            rcount_with_context =[]
            rcount_with_image =[]

            driver.get('https://shopee.tw/search?keyword=' + self.keyword + '&page=' + str(i))

            # 滾動頁面
            for scroll in range(6):
                driver.execute_script('window.scrollBy(0,1000)')
                time.sleep(2)

            #取得商品內容
            for item, thename in zip(driver.find_elements_by_xpath('//*[@data-sqe="link"]'), driver.find_elements_by_xpath('//*[@data-sqe="name"]')):
                #商品ID、商家ID
                getID = item.get_attribute('href')
                theitemid = int((getID[getID.rfind('.')+1:getID.rfind('?')]))
                theshopid = int(getID[ getID[:getID.rfind('.')].rfind('.')+1 :getID.rfind('.')]) 
                itemid.append(theitemid)
                shopid.append(theshopid)

                #商品名稱
                getname = thename.text.split('\n')[0]
                print('抓取： '+getname)
                name.append(getname)

                #價格
                thecontent = item.text
                thecontent = thecontent[(thecontent.find(getname)) + len(getname):]
                thecontent = thecontent.replace('萬','000')
                thecut = thecontent.split('\n')

                if re.search('市|區|縣|鄉|海外|中國大陸|國', thecontent): #有時會沒有商品地點資料
                    if re.search('已售出', thecontent): #有時會沒銷售資料
                        if '出售' in thecut[-3][1:]:
                            theprice = thecut[-4][1:]
                        else:
                            theprice = thecut[-3][1:]

                    else:
                        theprice = thecut[-2][1:]
                else:
                    if re.search('已售出', thecontent): #有時會沒銷售資料
                        theprice = thecut[-2][1:]
                    else:
                        theprice = thecut[-1][1:]

                theprice = theprice.replace('$','')
                theprice = theprice.replace(',','')
                theprice = theprice.replace('售','')
                theprice = theprice.replace('出','')
                theprice = theprice.replace(' ','')
                if ' - ' in theprice:
                    theprice = (int(theprice.split(' - ')[0]) +int(theprice.split(' - ')[1]))/2
                if '-' in theprice:
                    theprice = (int(theprice.split('-')[0]) +int(theprice.split('-')[1]))/2
                price.append(int(theprice))

                # 消費者評論詳細資料
                iteComment = self.goods_comments(item_id = theitemid, shop_id = theshopid)
                if iteComment:
                    #print(iteComment)
                    userid = [] #使用者ID
                    anonymous = [] #是否匿名
                    commentTime = [] #留言時間
                    is_hidden = [] #是否隱藏
                    orderid = [] #訂單編號
                    comment_rating_star = [] #給星
                    comment = [] #留言內容
                    product_SKU = [] #商品規格

                    for comm in iteComment:
                        userid.append(comm['userid'])
                        anonymous.append(comm['anonymous'])
                        commentTime.append(comm['ctime'])
                        is_hidden.append(comm['is_hidden'])
                        orderid.append(comm['orderid'])
                        comment_rating_star.append(comm['rating_star'])
                        try:
                            comment.append(comm['comment'])
                        except:
                            comment.append(None)

                        p=[]
                        for pro in comm['product_items']:
                            try:
                                p.append(pro['model_name'])
                            except:
                                p.append(None)

                        product_SKU.append(p)

                    commDic = {
                        '商品ID':[ theitemid for x in range(len(iteComment)) ],
                        '賣家ID':[ theshopid for x in range(len(iteComment)) ],
                        '商品名稱':[ getname for x in range(len(iteComment)) ],
                        '價格':[ int(theprice) for x in range(len(iteComment)) ],
                        '使用者ID':userid,
                        '是否匿名':anonymous,
                        '留言時間':commentTime,
                        '是否隱藏':is_hidden,
                        '訂單編號':orderid,
                        '給星':comment_rating_star,
                        '留言內容':comment,
                        '商品規格':product_SKU
                        }
                    #資料整合
                    container_comment = pd.concat([container_comment,pd.DataFrame(commDic)], axis=0)




            #暫時存檔紀錄
            container_comment.to_csv('shopeeAPIData'+str(i+1)+'_Comment.csv', encoding = self.ecode)

            print('留言累積' + str(len(container_comment)))
            time.sleep(random.randint(5,10))

        container_comment.to_csv(self.keyword +'_留言資料.csv', encoding = self.ecode, index=False)
        tEnd = time.time()#計時結束
        totalTime = int(tEnd - tStart)
        minute = totalTime // 60
        second = totalTime % 60
        print('資料儲存完成，花費時間（約）： ' + str(minute) + ' 分 ' + str(second) + '秒')


        df = pd.read_excel("Final_圓餅圖關鍵字.xlsx")
        a = df["功效"].tolist()
        a =  [x for x in a if pd.isnull(x) == False and x != 'nan']
        b = df["成分"].tolist()
        b =  [x for x in b if pd.isnull(x) == False and x != 'nan']
        #b
        c = df["風味"].tolist()
        c =  [x for x in c if pd.isnull(x) == False and x != 'nan']
        #c
        d = df["氣味"].tolist()
        d =  [x for x in d if pd.isnull(x) == False and x != 'nan']
        e = df["價格"].tolist()
        e =  [x for x in e if pd.isnull(x) == False and x != 'nan']
        df1 = container_comment
        x = df1["留言內容"].tolist()
        x =  [x for x in x if pd.isnull(x) == False and x != 'nan']

        keyword_list1 = []
        keyword_list2 = []
        keyword_list3 = []
        keyword_list4 = []
        keyword_list5 = []
        for words in x:
            for i in a:
                if i in words:
                    print("有關鍵字", i, words)
                    keyword_list1.append(i)
            for j in b:
                if j in words:
                    print("有關鍵字", j, words)
                    keyword_list2.append(j)
            for w in c:
                if w in words:
                    print("有關鍵字", w, words)
                    keyword_list3.append(w)
            for y in d:
                if y in words:
                    print("有關鍵字", y, words)
                    keyword_list4.append(y)
            for z in e:
                if z in words:
                    print("有關鍵字", z, words)
                    keyword_list5.append(z)
            else:
                print("找不到關鍵字")


        d1 = {}
        d2 = {}
        d3 = {}
        d4 = {}
        d5 = {}
        for f in keyword_list1:
            if keyword_list1.count(f) >= 1:
                d1[f] = keyword_list1.count(f)
        for g in keyword_list2:
            if keyword_list2.count(g) >= 1:
                d2[g] = keyword_list2.count(g)
        for h in keyword_list3:
            if keyword_list3.count(h) >= 1:
                d3[h] = keyword_list3.count(h)
        for m in keyword_list4:
            if keyword_list4.count(m) >= 1:
                d4[m] = keyword_list4.count(m)
        for n in keyword_list5:
            if keyword_list5.count(n) >= 1:
                d5[n] = keyword_list5.count(n)

        aa = sorted(d1.items(), key=lambda x: x[1], reverse=True)

        dfa = pd.DataFrame(aa, columns=['keywords', 'count'])
        dfa.to_excel("功效.xlsx")
        bb = sorted(d2.items(), key=lambda x: x[1], reverse=True)
        dfb = pd.DataFrame(bb, columns=['keywords', 'count'])
        dfb.to_excel("成分.xlsx")
        cc = sorted(d3.items(), key=lambda x: x[1], reverse=True)
        dfc = pd.DataFrame(cc, columns=['keywords', 'count'])
        dfc.to_excel("風味.xlsx")
        dd = sorted(d4.items(), key=lambda x: x[1], reverse=True)
        dfd = pd.DataFrame(dd, columns=['keywords', 'count'])
        dfd.to_excel("氣味.xlsx")
        ee = sorted(d5.items(), key=lambda x: x[1], reverse=True)
        dfe = pd.DataFrame(ee, columns=['keywords', 'count'])
        dfe.to_excel("價格.xlsx")

        o = df["其他"].tolist()
        o =  [x for x in o if pd.isnull(x) == False and x != 'nan']
        del o[0]
        oo = df["Unnamed: 6"].tolist()
        oo =  [x for x in oo if pd.isnull(x) == False and x != 'nan']
        del oo[0]
        ooo = df["Unnamed: 7"].tolist()
        ooo =  [x for x in ooo if pd.isnull(x) == False and x != 'nan']
        del ooo[0]
        oooo = df["Unnamed: 8"].tolist()
        oooo =  [x for x in oooo if pd.isnull(x) == False and x != 'nan']
        del oooo[0]
        ooooo = df["Unnamed: 9"].tolist()
        ooooo =  [x for x in ooooo if pd.isnull(x) == False and x != 'nan']
        del ooooo[0]
        oooooo = df["Unnamed: 10"].tolist()
        oooooo =  [x for x in oooooo if pd.isnull(x) == False and x != 'nan']
        del oooooo[0]

        other = o + oo + ooo + oooo + ooooo + oooooo
        keyword_list6 = []
        for words in x:
            for k in other:
                if k in words:
                    print("有關鍵字", k, words)
                    keyword_list6.append(k)
            else:
                print("找不到關鍵字")


        d6 = {}
        for k in keyword_list6:
            if keyword_list6.count(k) >= 1:
                d6[k] = keyword_list6.count(k)

        oth = sorted(d6.items(), key=lambda x: x[1], reverse=True)
        dfoth = pd.DataFrame(oth, columns=['keywords', 'count'])
        dfoth.to_excel("其他.xlsx")

        list_keywords = ["功效", "成分", "風味", "氣味", "價格", "其他"]
        list_keywords_num = [len(keyword_list1), len(keyword_list2), len(keyword_list3), len(keyword_list4), len(keyword_list5), len(keyword_list6)]
        dfkeys = pd.DataFrame(list_keywords, columns=['keywords'])
        dfkeys = pd.concat([dfkeys, pd.DataFrame(list_keywords_num, columns=['count'])], axis=1)
        dfkeys.to_excel("蝦皮圓餅圖.xlsx")


if __name__ == '__main__':
    d = shopee('益生菌',1)
    d.scraper()