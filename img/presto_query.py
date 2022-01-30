# !/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
# from google.cloud import bigquery


# client = bigquery.Client()
# query = """
#     SELECT name, SUM(number) as total_people
#     FROM `bigquery-public-data.usa_names.usa_1910_2013`
#     WHERE state = 'TX'
#     GROUP BY name, state
#     ORDER BY total_people DESC
#     LIMIT 20
# """
# query_job = client.query(query)  # Make an API request.
# print("The query data:")
# for row in query_job:
#     # Row values can be accessed by field name or index.
#     print("name={}, count={}".format(row[0], row["total_people"]))
import prestodb

# presto 查询
conn = prestodb.dbapi.connect(
    # host='ip-178-31-12-97.ec2.internal',
    # port=8889,
    host='cluster-d83e-m-0',
    port=8060,
    user="hive",
    catalog="hive"
)
cur = conn.cursor()
# cur.execute("select event_name,count(1) from triwin_source.user_event_history where event_date='2021-05-07' group by event_name")
cur.execute("show schemas")
print("success")
res_list = []

rows = cur.fetchall()
for i in rows:
    res_list.append(i)
print(res_list)
