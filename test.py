#!/usr/bin/env python

from Extractor import Extractor

extractor = Extractor()

# 获取问题列表（保存在数据库leetcode.db中，若希望获取问题状态（是否ac），需首先登录）
# extractor.login('foo@bar.com', '123456')
extractor.update_problem_list()

# 导出问题列表为中文CSV文件
extractor.save_problem_list('problems.csv')

