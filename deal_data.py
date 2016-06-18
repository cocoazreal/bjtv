from __future__ import division
import MySQLdb
import time
import datetime



def get_date():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="067116", db="bjtv", charset="utf8")
    cursor = conn.cursor()
    sql = 'select idsite,`_date` from local_action'
    cursor.execute(sql)
    for x in cursor.fetchall():
        timestamp = x[1]
        idsite = x[0]
        timestruct = time.localtime(timestamp)
        year = time.strftime("%Y", timestruct)
        month = time.strftime("%m", timestruct)
        week = time.strftime("%W", timestruct)
        day = time.strftime("%d", timestruct)
        date = time.strftime("%Y-%m-%d %H:00:00", timestruct)

        sql1 = 'select datetime from day_data'
        cursor.execute(sql1)
        all_date = list()
        for each in cursor.fetchall():
            all_date.append(each[0])
        if date not in all_date:
            print date
            sql2 = "insert into day_data(idsite, datetime,`day`,week,`month`,`year`) values(%s,%s,%s,%s,%s,%s)"
            query = (idsite, date, day, week, month, year)
            cursor.execute(sql2, query)
    conn.commit()
    cursor.close()
    conn.close()


def get_data(idsite):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="067116", db="bjtv", charset="utf8")
    cursor = conn.cursor()
    sql = "select `datetime` from day_data where idsite='%s'"
    cursor.execute(sql % idsite)
    i = 0
    for x in cursor.fetchall():
        timestamp = int(time.mktime(time.strptime(x[0], '%Y-%m-%d %H:%M:%S')))
        other_timestamp = timestamp + 3600
        sql1 = "select ip,idvisit,cookie from local_action where `_date` >= %s and `_date` < %s"
        time_data = (timestamp, other_timestamp)
        cursor.execute(sql1, time_data)
        data = cursor.fetchall()
        ip = set()
        pv = list()
        uv = set()
        new_uv = set()
        for each in data:
            # print i
            pv.append(each[0])
            ip.add(each[0])
            uv.add(each[1])
            if each[2] != '1':
                print each[2]
                new_uv.add(each[1])
            i += 1
        sql2 = 'update day_data set ip=%s, pv=%s, uv=%s , new_uv=%s,`timestamp`= %s where datetime=%s'
        all_data = (len(ip), len(pv), len(uv), len(new_uv), timestamp, x[0])
        cursor.execute(sql2, all_data)

    conn.commit()
    cursor.close()
    conn.close()
    pass

def deal_url():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="067116", db="bjtv", charset="utf8")
    cursor = conn.cursor()



    pass


if __name__ == '__main__':
    get_data('1587d8ce70f85bc2e79f0bc6cd5cef64')

