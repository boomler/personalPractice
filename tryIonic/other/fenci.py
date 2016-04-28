#!/usr/bin/env python
#-*-coding=utf-8-*-
# coding=utf-8
import jieba
f = open("rawData.data","r").read()
stop_words =[ i for i in  open('stop_words.txt').readlines()]
seg_list = jieba.cut(f)
for word in seg_list:
	if word not in stop_words:
		print word,