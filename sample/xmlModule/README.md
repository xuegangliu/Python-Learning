# python对XML的解析方式

- [SAX (simple API for XML )](#SAX概念)

python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

- [DOM(Document Object Model)]()

将XML数据在内存中解析成一个树，通过对树的操作来操作XML。

## SAX概念

- SAX是一种基于事件驱动的API。

- 利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。

- 解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;