#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#  Date: 2014-03-12 16:39:57
#
#  Copyright 2014 chaubeau <chaubeau01@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  Desc :
#
import MySQLdb
import threading
import sys

def db_op_thread_func( i, num_of_op ):
    conn=MySQLdb.connect(host="127.0.0.1",port=5659, user="root",passwd="123456",db="io")
    cursor = conn.cursor()
    sql = "select sleep(100)"

    for j in range(0, int(num_of_op) ):
        cursor.execute( sql )
        print "thread", i, ":", " num:", j

    conn.close()

if __name__ == "__main__":
    args = sys.argv
    num_of_thd  = args[1]
    num_of_op   = args[2]
    threads = []
    for i in range( 0, int(num_of_thd) ):
        threads.append( threading.Thread( target=db_op_thread_func,args=(i, num_of_op ) ) )

    for t in threads:
        t.start()

    for t in threads:
        t.join()

