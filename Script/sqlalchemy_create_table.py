#!/usr/bin/env python3
#coding:utf8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker
Base = declarative_base() #生成一个SqlORM 基类
engine = create_engine("mysql+pymysql://root:admin@127.0.0.1:3306/scrapy_comic",echo=True)
#echo如果为True，那么当他执行整个代码的数据库的时候会显示过程
#创建一个类继承Base基类
class Host(Base):
    #表名为hosts
    __tablename__ = 'hosts'
    #表结构
    #primary_key等于主键
    #unique唯一
    #nullable非空
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)

Base.metadata.create_all(engine) #创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    #bind绑定
    #创建与数据库的会话session class
    #注意,这里返回给session的是个class,不是实例
    session = SessionCls()
    #插入字段
    h1 = Host(hostname='qd115',ip_addr='115.29.51.8')
    h2 = Host(hostname='ubuntu',ip_addr='139.129.5.191',port=80)
    h3 = Host(hostname='mysql',ip_addr='121.42.195.15',port=3306)
    #添加一个
    #session.add(h3)
    #可以添加多个字段
    session.add_all( [h1,h2,h3])
    #修改字段名字,只要没提交,此时修改也没问题
    #h2.hostname = 'ubuntu_test'
    #支持数据回滚
    #session.rollback()
    #提交
    session.commit()
