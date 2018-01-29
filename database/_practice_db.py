# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_range(low,high):
	try:	
		conn =sqlite3.connect(db_file)
		cursor = conn.cursor()
		#cursor.execute('select name from user where score >= ? and score <= ? order by score asc', (low,high))
		cursor.execute('select name from user where score between {} and {} order by score'.format(low,high))
	except Exception as e: print e
	finally:
		values = cursor.fetchall()
		cursor.close()
		conn.close()
	return [value[0] for value in values]


def get_score_in(low, high):
	conn_t = sqlite3.connect(db_file)
	cursor_t = conn_t.cursor()
	cursor_t.execute(('select * from user'))
	values = cursor_t.fetchall()
	for value in values:
		if value[2] >=low and value[2]<=high:
			print value[1]
	cursor_t.close()
	conn_t.close()



assert get_score_range(80, 95) == ['Adam'], get_score_range(80, 95)
assert get_score_range(60, 80) == ['Bart', 'Lisa'], get_score_range(60, 80)
assert get_score_range(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_range(60, 100)

print('PASS')
'''
get_score_range(80, 95)
get_score_range(60, 80)
get_score_range(60, 100)
'''
