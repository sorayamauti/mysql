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


class Cpu(Base):
    __tablename__ = 'Motherboard'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    image = Column(String)
    info = Column(String)
    maker_id = Column(Integer)
    socket = Column(String)
    chipset = Column(String)
    Supported_memory = Column(String)
    Maximum_memory = Column(Integer)
    foamfactor = Column(String)

class mothermain:
    def MakerID(name):
        """
        とってきた商品のメーカーを調べ、メーカーIDを返す。
        :param name:
        :return:
        """

    def insertmother(item):
        item_list = {}
        item_list["motherBoard"] = item
        no = 1
        for i in item_list:
            for length in range(len(item_list[i])):
                id = 20000 + no
                price = Price()
                price.product_id = id
                price.web_id = 201
                price.price = item_list[i][int(length)]["price_tax_exclude"]
                price.url = item_list[i][int(length)]["detail_link"]
                price.category_id = 2
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(price)
                session.commit()

                product = Cpu()
                product.product_id = id
                product.product_name = item_list[i][int(length)]["name"]
                product.image = item_list[i][int(length)]["image_link"]
                product.info = item_list[i][int(length)]["note"]
                product.maker_id = 103
                product.socket = item_list[i][int(length)]["ソケット形状"]
                product.chipset = item_list[i][int(length)]["チップセット"]
                product.Supported_memory = item_list[i][int(length)]["対応メモリ"]
                product.Maximum_memory = item_list[i][int(length)]["メモリ最大"]
                product.foamfactor = item_list[i][int(length)]["フォームファクタ"]
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(product)
                session.commit()
                session.close()
                no += 1