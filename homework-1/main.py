"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

PASS = os.environ.get('PG_PASS')
DATA_PATH = os.path.abspath("../homework-1/north_data")


def get_data(is_id_data=False, file_name=""):

    result = []
    if os.path.exists(os.path.join(DATA_PATH, file_name)):
        with open(os.path.join(DATA_PATH, file_name), mode="r", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                if count:
                    temp_list = [str(count)] if is_id_data else []
                    for item in row:
                        temp_list.append(item)
                    result.append(tuple(temp_list))
                count += 1
    return result


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=PASS)
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", get_data(False, 'customers_data.csv'))
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", get_data(True, 'employees_data.csv'))
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", get_data(False, 'orders_data.csv'))
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customers")

finally:
    conn.close()
