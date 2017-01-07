# SAX概念
* SAX是一种基于事件驱动的API。
* 利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。
* 解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
# 而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。
1. 对大型文件进行处理；
2. 只需要文件的部分内容，或者只需从文件中得到特定信息。
3. 想建立自己的对象模型的时候。
# SAX使用介绍
* 在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
## ContentHandler类方法介绍
## characters(content)方法
* 调用时机：
* 从行开始，遇到标签之前，存在字符，content的值为这些字符串。
* 从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
* 从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。
* 标签可以是开始标签，也可以是结束标签。
## startDocument()方法
* 文档启动的时候调用。
## endDocument()方法
* 解析器到达文档结尾时调用。
## startElement(name, attrs)方法
* 遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
## endElement(name)方法
* 遇到XML结束标签时调用。
## make_parser方法
* 以下方法创建一个新的解析器对象并返回。
* xml.sax.make_parser( [parser_list] )
* 参数说明:
* parser_list - 可选参数，解析器列表
## parser方法
* 以下方法创建一个 SAX 解析器并解析xml文档：
* xml.sax.parse( xmlfile, contenthandler[, errorhandler])
* 参数说明:
* xmlfile - xml文件名
* contenthandler - 必须是一个ContentHandler的对象
* errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
## parseString方法
* parseString方法创建一个XML解析器并解析xml字符串：
* xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
* 参数说明:
* xmlstring - xml字符串
* contenthandler - 必须是一个ContentHandler的对象
* errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
