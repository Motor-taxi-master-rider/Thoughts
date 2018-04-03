#!/usr/bin/env python3
# coding:utf8
from sqlalchemy import create_engine,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()  # 生成一个SqlORM 基类
engine = create_engine(
    "mysql+pymysql://root:admin@127.0.0.1:3306/scrapy_comic", echo=True)
# echo如果为True，那么当他执行整个代码的数据库的时候会显示过程
# 创建一个类继承Base基类


class User(Base):
    # 表名
    __tablename__ = 'user'
    # id字段
    id = Column(String(20), primary_key=True)
    # 名字字段
    name = Column(String(20))
    # 一对多:#内容不是表名而是定义的表结构名字
    books = relationship('Book')


class Book(Base):
    # 表面
    __tablename__ = 'book'
    # id字段
    id = Column(String(20), primary_key=True)
    # 名字字段
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    # ForeignKey是外键 关联user表的id字段
    user_id = Column(String(20), ForeignKey('user.id'))


# 创建所需表
Base.metadata.create_all(engine)

if __name__ == '__main__':
    # 绑定,生成回话
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    # 创建用户
    liuyao = User(id='1', name='liuyao')
    ali = User(id='2', name='ali')
    # 添加字段
    session.add_all([liuyao, ali])
    # 提交
    session.commit()
    # 创建白鹿原这本书，指定谁是拥有者
    Whitedeer = Book(id='1', name='White_deer', user_id='1')
    # 创建三体这本书，指定谁是拥有者
    Threebody = Book(id='2', name='Three_body', user_id='2')
    # 添加字段
    session.add_all([Whitedeer, Threebody])
    # 提交
    session.commit()
