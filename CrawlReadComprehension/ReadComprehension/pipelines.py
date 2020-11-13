# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ReadcomprehensionPipeline(object):
    pass


class MysqlPipeline(object):
    connect = pymysql.connect.__defaults__

    def __init__(self, mysql_uri, mysql_port, mysql_user, mysql_passwd, mysql_db):
        self.mysql_uri = mysql_uri
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
        self.mysql_db = mysql_db
        # 获取游标

    @classmethod
    def from_crawler(cls, crawler):
        # return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))
        return cls(mysql_uri="115.159.151.166", mysql_port="3306", mysql_user="root", mysql_passwd="123456",
                   mysql_db="AIcourse")

    print("进入到from_crawler")

    def open_spider(self, spider):
        pass
        # self.connect = pymysql.connect(
        #     host=self.mysql_uri,
        #     port=self.mysql_port,
        #     user=self.mysql_user,
        #     passwd=self.mysql_passwd,
        #     db=self.mysql_db,
        #     charset='utf8'
        # )

    def process_item(self, item, spider):
        # self.cur.execute('select * from ""')
        print("进入到process_item")
        return item

    def close_spider(self, spider):
        # self.connect.cursor.close()
        # self.connect.close()
        print("进入到close_spider")
