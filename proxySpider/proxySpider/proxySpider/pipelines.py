# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  json

class AnjukespiderPipeline(object):
    def process_item(self, item, spider):
        """
        将代理服务器写入本地的json文件
        """
        with open('proxy.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dict(item), ensure_ascii=False)+'\n')
        return item
