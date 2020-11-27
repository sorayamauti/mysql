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


class Product(Base):
    __tablename__ = 'caseCooler'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    image = Column(String)
    info = Column(String)
    maker_id = Column(Integer)
    size = Column(String)
    fan_numberofrotations = Column(String)
    noise = Column(String)
    air_flow = Column(String)
    

class casecoolermain:
    def MakerID(name):
        """
        とってきた商品のメーカーを調べ、メーカーIDを返す。
        :param name:
        :return:
        """

    def insertcasecooler(item):
        item_list = {}
        item_list["casecooler"] = item
        no = 1
        for i in item_list:
            for length in range(len(item_list[i])):
                id = 11000 + no
                price = Price()
                price.product_id = id
                price.web_id = 201
                price.price = item_list[i][int(length)]["price_tax_exclude"]
                price.url = item_list[i][int(length)]["detail_link"]
                price.category_id = 10
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(price)
                session.commit()

                product = Product()
                product.product_id = id
                product.product_name = item_list[i][int(length)]["name"]
                product.image = item_list[i][int(length)]["image_link"]
                product.info = item_list[i][int(length)]["note"]
                product.maker_id = 111
                product.size = item_list[i][int(length)]["サイズ"]
                product.fan_numberofrotations = item_list[i][int(length)]["ファン回転数"]
                product.noise = item_list[i][int(length)]["ノイズ"]
                product.air_flow = item_list[i][int(length)]["風量"]
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(product)
                session.commit()
                session.close()
                no += 1
