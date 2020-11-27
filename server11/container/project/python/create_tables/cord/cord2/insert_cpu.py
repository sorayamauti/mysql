# coding:UTF-8

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
    __tablename__ = 'Cpu'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    image = Column(String)
    info = Column(String)
    maker_id = Column(Integer)
    socket = Column(String)
    clock = Column(String)
    thread = Column(Integer)
    core = Column(Integer)
    TDP = Column(Integer)


class cpumain:
    def MakerID(name):
        """
        とってきた商品のメーカーを調べ、メーカーIDを返す。
        :param name:
        :return:
        """
        
        CpuDict = {'intelCPU': 101, 'amdCPU': 102}
        for i in CpuDict.keys():
            if i in name:
                return CpuDict[i]

    def insertcpu(item):
        item_list = {}
        item_list["cpu"] = item
        no = 1
        for i in item_list:
            for length in range(len(item_list[i])):
                id = 10000 + no
                price = Price()
                price.product_id = id
                price.web_id = 201
                price.price = item_list[i][int(length)]["price_tax_exclude"]
                price.url = item_list[i][int(length)]["detail_link"]
                price.category_id = 1
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(price)
                session.commit()

                product = Cpu()
                product.product_id = id
                product.product_name = item_list[i][int(length)]["name"]
                product.image = item_list[i][int(length)]["image_link"]
                product.info = item_list[i][int(length)]["note"]
                product.maker_id = cpumain.MakerID(i)
                product.socket = item_list[i][int(length)]["ソケット形状"]
                product.clock = item_list[i][int(length)]["動作クロック"]
                product.thread = item_list[i][int(length)]["スレッド数"]
                product.core = item_list[i][int(length)]["コア数"]
                product.TDP = item_list[i][int(length)]["TDP"]
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(product)
                session.commit()
                session.close()
                no += 1
