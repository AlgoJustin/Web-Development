#import modul
import sqlite3

#connect to the database
conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

#Question #1. How many artists are represented in the database? 
#Baca data
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()

print('Jumlah artis dalam database:', len(data))
#460

#Question #2. How many women (Female) are in the database?
#Membaca data di kolom "Gender" untuk mencari berapa nilai "Female"
cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
data = cursor.fetchall()

print('Jumlah perempuan:', len(data))
#63

#Question #3. How many people in the database were born before 1900?
#Membaca data pada kolom "Birth Year" dengan kondisi < 1900
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()

print('Born before 1900:', len(data))
#122

#Question #4*. What is the name of the oldest artist?


#Opsi solusi #1 gunakan alat Python standar

cursor.execute('SELECT * FROM artists WHERE "Birth Year" <1900')
data = cursor.fetchall()
oldest = {'name': '', 'birthday': 1900}
# Membandingkan setiap tahun yang paling kecil samapai menemukan yg tertua
for person in data:
    if person[4] < oldest['birthday']:
        oldest['name'] = person[1]
        oldest['birthday'] = person[4]
print('The oldest:', oldest)

#Opsi solusi #2 SQL saja
#Pakai "order by" yang mengurutkan nilai terkecil samapi terbesar
cursor.execute('SELECT name FROM artists WHERE "Birth Year" < 1900 order by "Birth Year"')
data = cursor.fetchall()
#Memakai index pertama
print('The oldest:', data[0][0])

#Thomas Bewick, 1753

conn.commit()