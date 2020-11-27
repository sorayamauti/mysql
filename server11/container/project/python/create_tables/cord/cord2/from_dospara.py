# coding:UTF-8

import requests
from bs4 import BeautifulSoup
import re
import string
import os

URI_home = "https://www.dospara.co.jp"

sep = os.sep
parent_dir = os.path.dirname(__file__)
req_file_path = "{0}{1}required.txt".format(parent_dir, sep)

with open(req_file_path, "r", encoding="utf-8") as f:
    row = f.readlines()

category_information = {}

for f in row:
    dct = {}
    lst = f.split()
    cat = lst.pop(0)
    dct["link"] = lst.pop(0)
    dct["info"] = lst
    category_information[cat] = dct

# 余計な英字を削除用
varidation_list = list(string.ascii_letters)

# ここに置いた属性は型変換される
int_set = {"コア数", "スレッド数", "TDP", "メモリ最大", "最大書込速度", "最大読込速度", "容量"}
float_set = {}


def get_parts(parts_name="ALL"):
    '''
    :param parts_name:
    :return: parts_list
    '''

    def fetch_items(_uri) -> list:
        """
        :param _uri: 参照するドスパラのURI
        :return data: リスト<辞書>
        """

        r = requests.get(_uri)
        soup = BeautifulSoup(r.content, 'lxml')
        items = soup.find("table", class_="table itemSearchTable")
        items = items.find_all("tr", class_="")[1:]

        data = []

        for i, elem in enumerate(items):
            if i % 2 == 0:
                _temp = {}
                # 商品名
                _temp["name"] = elem.find("a").getText()
                # 商品コード
                _temp["item_code"] = elem.find("span").getText().split("：")[1]
                # 詳細リンクURL
                _temp["detail_link"] = "{}{}".format(URI_home, elem.find("a")["href"])

            else:
                txt = elem.find_all("td")
                note = txt[3].getText()
                note = note.replace("\r", "")
                note = note.replace("\n", "")
                note = note.strip(" ")

                # 画像URL
                image_url = elem.find("td", class_="photo")
                _temp["image_link"] = image_url.find("img")["src"]

                # 価格
                _temp["price_tax_exclude"] = int(re.sub(r'\D', '', txt[1].getText()))

                # 商品説明
                # 追記:有用な情報をさらにnoteのほかに属性として追加する
                if len(note) == 0:
                    _temp["note"] = None
                else:
                    _temp["note"] = note

                # 追加情報
                info_lst = note.split("●")[1:]
                info_dct = {}

                for i in info_lst:
                    spl = i.split("：")
                    info_dct[spl[0]] = spl[1]

                for r in required_scheme_lst:
                    if r in int_set:
                        _temp[r] = 0
                    elif r in float_set:
                        _temp[r] = 0.0
                    else:
                        _temp[r] = ""

                for k, it in info_dct.items():
                    # 我々にとって必要な属性が説明文内にあるなら
                    if k in required_scheme_lst:
                        # 型変換が必要なら
                        try:
                            if k in int_set:
                                value = re.sub("[a-z]|[A-Z]|[ぁ-ん]|[ァ-ン]|/", "", it)
                                value = int(value)
                            elif k in float_set:
                                value = re.sub("[a-z]|[A-Z]|[ぁ-ん]|[ァ-ン]|/", "", it)
                                value = float(value)
                            else:
                                value = it
                        except TypeError as ty:
                            print(ty)
                        except Exception as e:
                            continue

                        _temp[k] = value
                # 11/02追記:セット商品っぽいものを除外するためnoteがNoneなら追加しないようにした
                if _temp["note"] is not None:
                    data.append(_temp)

        # 次ページが有るか参照
        _next = soup.find("dl", class_="pageNav")
        _next = _next.find("li", class_="next")
        _next = _next.find("a")

        if _next is None:
            return data
        else:
            _next = _next["href"]
            link = "{}{}".format(URI_home, _next)
            return data + fetch_items(link)

    if parts_name == "ALL":
        item_list_all = {}

        print("全パーツ取得しています...")
        for name in category_information.keys():
            required_scheme_lst = category_information[name]["info"]
            uri = "{}{}".format(URI_home, category_information[name]["link"])
            try:
                item_list = fetch_items(uri)
            except Exception as e:
                item_list = None
            item_list_all[name] = item_list

            try:
                print("{}:{}件".format(name, len(item_list)))
            except:
                print("{}:{}件".format(name, 0))
        return item_list_all
    else:
        print("{}を取得します".format(parts_name))
        required_scheme_lst = category_information[parts_name]["info"]
        uri = "{}{}".format(URI_home, category_information[parts_name]["link"])
        # print("参照URL:{}".format(uri))

        try:
            item_list = fetch_items(uri)
        except Exception as e:
            print(e)
            return None
        return item_list


if __name__ == "__main__":
    category = "ALL"
    # category = "motherBoard"  # required.txtを参照
    item_list = get_parts(category)
