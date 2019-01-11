# -*- coding: utf-8 -*-

import os, sqlite3

def sqlite3_create_table(db_name,create_sql):
    '''创建sqlite3数据表'''
    db_file = os.path.join(os.path.dirname(__file__), db_name)
    if os.path.isfile(db_file):
        os.remove(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(create_sql)
    cursor.close()
    conn.commit()
    conn.close()
    print("创建表成功...")

def sqlite3_insert_table(db_name,insert_sql):
    db_file = os.path.join(os.path.dirname(__file__), db_name)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    rowcount = cursor.execute(insert_sql).rowcount
    cursor.close()
    conn.commit()
    conn.close()
    if rowcount>0:
        print("插入数据成功")
    return rowcount

def sqlite3_get_user_by_name_score(db_name,select_sql,select_params):
    db_file = os.path.join(os.path.dirname(__file__), db_name)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    result_list = cursor.execute(select_sql,select_params);
    list=result_list.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    print(result_list)
    return list;

if __name__ == '__main__':
    sqlite3_create_table('test.db','create table user(id varchar(20) primary key, name varchar(20), score int)')
    i=1;
    for i in range(10):
        sql="insert into user values ({}, {}, {})".format(i,i,i)
        # print(sql)
        result = sqlite3_insert_table('test.db',sql)
        if result>1:
            print("插入成功")
    result_list = sqlite3_get_user_by_name_score('test.db','select * from user where id=?',('1',))
    print("查询结果:",result_list)
    print("查询数",result_list.__len__())
    if result_list.__len__() > 0:
        print("第一条数据",result_list[0].__len__())
        assert 3 == result_list[0].__len__()
    count = sqlite3_get_user_by_name_score('test.db','select count(1) from user',())
    print("总记录数",count)
