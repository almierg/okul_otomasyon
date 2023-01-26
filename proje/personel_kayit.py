import sqlite3 as sql

adi =input("isim giriniz")
par =input("şifre giriniz")

con = sql.connect("personel_kayitlari.db")
cur = con.cursor()
cur.execute("CREATE TABLE If not exists personel(kuladi TEXT,sifre TEXT)")
cur.execute("INSERT INTO personel VALUES(?,?)", (adi, par))

con.commit()
con.close()