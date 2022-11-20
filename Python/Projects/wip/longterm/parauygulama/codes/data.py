import sqlite3 as sql
import anasayfa_1


conn = sql.connect("NormalDatabase.db")
print("Database Bağlandı.")

cursor = conn.cursor()
print("Cursor Oluşturuldu. ")

cursor.execute("""CREATE TABLE IF NOT EXISTS VERILER(  
    name text,
    age integer
 
 
 ) """)

print("Table Olusturuldu.")

nickname = anasayfa_1.Ui_MainWindow.setupUi()
kategori = str(input("Kategori: "))
harcama = int(input("Harcama: "))


add_Command = """ INSERT INTO VERILER VALUES{} """
data_1 = (nickname, kategori, harcama)


cursor.execute(add_Command.format(data_1))
print("Veri Eklendi")

conn.commit()
conn.close()
