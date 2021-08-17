import os
import random
from datetime import datetime

import mysql.connector
import pymysql

password = os.environ.get('DB_PASSWORD')
CREATE_RECORD = "INSERT INTO actor(first_name, last_name, last_update) VALUES(%s, %s, %s)"
DELETE_RECORD = "DELETE FROM actor WHERE actor_id=%s"
UPDATE_RECORD = "UPDATE actor SET first_name=%s, last_name=%s WHERE actor_id=%s"


def read(id):
    try:
        cnx = mysql.connector.connect(user='shoaib', password=password,
                                      host='127.0.0.1',
                                      database='sakila')
        cur = cnx.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM actor WHERE actor_id=%s", (id,))
        records = cur.fetchall()
        print(records)
        # print('\n'.join([','.join(map(str, i)) for i in records if records]))
    except Exception as e:
        print(e)
    finally:
        cur.close()
        cnx.close()


def create():
    try:
        cnx = mysql.connector.connect(user='shoaib', password=password,
                                      host='127.0.0.1',
                                      database='sakila')
        cur = cnx.cursor(pymysql.cursors.DictCursor)

        # Create data to be inserted
        random_no = random.randint(10000, 20000)
        first_name = f'Shoaib_{random_no}'
        last_name = f'Mansoor_{random_no}'
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = (first_name, last_name, last_update)

        cur.execute(CREATE_RECORD, data)
        cnx.commit()
        print('User added successfully')
        return cur.lastrowid
    except Exception as e:
        print(e)
    finally:
        cur.close()
        cnx.close()


def update(id):
    try:
        cnx = mysql.connector.connect(user='shoaib', password=password,
                                      host='127.0.0.1',
                                      database='sakila')
        cur = cnx.cursor(pymysql.cursors.DictCursor)
        random_no = random.randint(10000, 20000)
        first_name = f'Shoaib_{random_no}'
        last_name = f'Mansoor_{random_no}'
        data = (first_name, last_name, id)

        cur.execute(UPDATE_RECORD, data)
        cnx.commit()
        print('User updated successfully')
    except Exception as e:
        print(e)
    finally:
        cur.close()
        cnx.close()


def delete(id):
    try:
        cnx = mysql.connector.connect(user='shoaib', password=password,
                                      host='127.0.0.1',
                                      database='sakila')
        cur = cnx.cursor(pymysql.cursors.DictCursor)
        data = (id,)

        cur.execute(DELETE_RECORD, data)
        cnx.commit()
        print('User deleted successfully')
    except Exception as e:
        print(e)
    finally:
        cur.close()
        cnx.close()


if __name__ == '__main__':
    record_id = create()
    read(record_id)
    update(record_id)
    delete(record_id)


