from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, create_engine
)
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('mysql+pymysql://user:pass@mysql/db?charset=utf8')


class Price(Base):
    __tablename__ = 'Price'
    product_id = Column(Integer, primary_key=True)
    web_id = Column(Integer)
    price = Column(Integer)
    url = Column(String)
    category_id = Column(Integer)


class SSD(Base):
    __tablename__ = 'SSD'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    image = Column(String)
    info = Column(String)
    maker_id = Column(Integer)
    connection = Column(String)
    capacity = Column(Integer)
    size = Column(String)
    max_write = Column(Integer)
    max_read = Column(Integer)

class ssdmain:
    def MakerID(name):
        """
        とってきた商品のメーカーを調べ、メーカーIDを返す。
        :param name:
        :return:
        """

    def insertssd(item):
        item_list = {}
        item_list["SSD"] = item
        no = 1
        for i in item_list:
            for length in range(len(item_list[i])):
                id = 40000 + no
                price = Price()
                price.product_id = id
                price.web_id = 201
                price.price = item_list[i][int(length)]["price_tax_exclude"]
                price.url = item_list[i][int(length)]["detail_link"]
                price.category_id = 4
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(price)
                session.commit()

                product = SSD()
                product.product_id = id
                product.product_name = item_list[i][int(length)]["name"]
                product.image = item_list[i][int(length)]["image_link"]
                product.info = item_list[i][int(length)]["note"]
                product.maker_id = 105
                product.connection = item_list[i][int(length)]["接続"]
                product.capacity = item_list[i][int(length)]["容量"]
                product.size = item_list[i][int(length)]["サイズ"]
                product.max_write = item_list[i][int(length)]["最大書込速度"]
                product.max_read = item_list[i][int(length)]["最大読込速度"]
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(product)
                session.commit()
                session.close()
                no += 1