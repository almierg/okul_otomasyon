import sqlite3 as sql


adi =input("isim giriniz")
par =input("şifre giriniz")


con = sql.connect("kayitlar2.db")
cur = con.cursor()
#cur.execute("CREATE TABLE If not exists ogrenci(kuladi TEXT,sifre TEXT)") tablo yoksa oluşturuyor
cur.execute("INSERT INTO ogrenci VALUES(?,?)", (adi, par))# personellere kayıt yapıcaksak personeller yazmayı unutma


con.commit()
con.close()
