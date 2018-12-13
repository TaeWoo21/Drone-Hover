# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('game_rank.db')
curs = conn.cursor()
curs.execute('create table game_rank (name, time )')
curs.execute("insert into game_rank values ('Ali', 28)")
values = [('Brad',54), ('Ross', 34), ('Muhammad', 28), ('Bilal', 44)]
curs.executemany('insert into game_rank values(?,?)', values)
conn.commit()
conn.close() 
