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

    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(host='115.159.151.166', user='root', passwd='123456', port=3306,
                                    db='AIcourse',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    # @classmethod
    # def from_crawler(cls, crawler):
    #     print("进入到from_crawler")

    def open_spider(self, spider):
        print("进入到open_spider")

    def process_item(self, item, spider):
        # sql语句
        insert_sql = """
                insert into Economist(content,theme,title,date,claw_url,paragraphs) VALUES(%s,%s,%s,%s,%s,%s)
                """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (
        item['content'], item['theme'], item['title'], item['date'], item['claw_url'], item['paragraphs']))
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        print("进入到close_spider")
        self.cursor.close()
        self.conn.close()
