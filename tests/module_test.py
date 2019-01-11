#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

from sample.baseModule import baseModule
from sample.xmlModule import domModule
from sample.xmlModule import saxModule

import xml.sax

def test_module():
    print("=================== baseModule ===================")
    baseModule.hello()
    baseModule.aTest()
    baseModule.typeTest()
    baseModule.data2Json()
    baseModule.json2data()
    baseModule.inputFunction()

if __name__ == '__main__':
    print("=================== domModule ===================")
    handler = domModule.MovieHandler('movies.xml')
    handler.parseXml()

    print("=================== saxModule ===================")
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = saxModule.MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("movies.xml")


