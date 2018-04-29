#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 鼠标动作链，有些时候，我们需要再页面上模拟一些鼠标操作，比如双击、右击、拖拽甚至按住不动等，我们可以通过导入 ActionChains 类来做到：

from selenium import webdriver
# 导入 ActionChains 类
# from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
# find_element_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# 样式1 by ID. <div id="coolestWidgetEvah">...</div>
element = driver.find_element_by_id("coolestWidgetEvah")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# element = driver.find_element(by=By.ID, value="coolestWidgetEvah")

# 样式2 by Class Name <div class="cheese"><span>Cheddar</span></div><div class="cheese"><span>Gouda</span></div>
cheeses = driver.find_elements_by_class_name("cheese")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheeses = driver.find_elements(By.CLASS_NAME, "cheese")

# 样式3 by Tag Name <iframe src="..."></iframe>
frame = driver.find_element_by_tag_name("iframe")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# frame = driver.find_element(By.TAG_NAME, "iframe")

# 样式4 by Name <input name="cheese" type="text"/>
cheese = driver.find_element_by_name("cheese")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheese = driver.find_element(By.NAME, "cheese")

# 样式5 by Link Text <a href="http://www.google.com/search?q=cheese">cheese</a>
cheese = driver.find_element_by_link_text("cheese")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheese = driver.find_element(By.LINK_TEXT, "cheese")

# 样式6 By Partial Link Text <a href="http://www.google.com/search?q=cheese">search for cheese</a>>
cheese = driver.find_element_by_partial_link_text("cheese")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")

# 样式7 By CSS <div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>
cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

# 样式8 By XPath  <input type="text" name="example" /> or <INPUT type="text" name="other" />
inputs = driver.find_elements_by_xpath("//input")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# inputs = driver.find_elements(By.XPATH, "//input")
