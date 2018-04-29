#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 我们已经知道了怎样向文本框中输入文字，但是有时候我们会碰到<select> </select>标签的下拉框。直接点击下拉框中的选项不一定可行。
#
# Example : <select id="status" class="form-control valid" onchange="" name="status">
#             <option value=""></option>
#             <option value="0">未审核</option>
#             <option value="1">初审通过</option>
#             <option value="2">复审通过</option>
#             <option value="3">审核不通过</option>
#          </select>

from selenium import webdriver
driver = webdriver.PhantomJS()
# 导入 Select 类
from selenium.webdriver.support.ui import Select
# 找到 name 的选项卡
select = Select(driver.find_element_by_name('status'))

# index 索引从 0 开始
# value是option标签的一个属性值，并不是显示在下拉框中的值
# visible_text是在option标签文本的值，是显示在下拉框的值

select.select_by_index(1)
select.select_by_value("0")
select.select_by_visible_text(u"未审核")

# 全部取消选择怎么办呢？很简单:

select.deselect_all()