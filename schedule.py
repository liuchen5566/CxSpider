from apscheduler.schedulers.blocking import BlockingScheduler

import toolkit as tool
from weibo.hot_ranking import crawler as weibo_hot_ranking  # 微博热搜榜实时爬虫

if __name__ == "__main__":
    # 启动MySQL数据库连接
    mysql = tool.mysql_connect("CxSpider")

    # 定义任务框架
    scheduler = BlockingScheduler()  # 定义BlockingScheduler

    # 添加爬虫任务
    scheduler.add_job(weibo_hot_ranking, "interval", seconds=5 * 60,
                      kwargs={"test": True, "mysql": mysql, "table_name": "weibo"})  # 微博热搜榜实时爬虫

    # 启动任务框架
    scheduler.start()
