import psycopg2 as pg2

conn = pg2.connect(database="Tarot",user="postgres",password="password")

# cur = conn.cursor()
# # cur.execute("SELECT base_meaning FROM card_meaning")
# cur.execute("SELECT card FROM test02")
# print(cur.fetchone())

cursor = conn.cursor()

# cursor.execute("SELECT card FROM card_meaning")
# for row in cursor:
#     print(row)

cursor.execute("SELECT card FROM card_meaning")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

conn.close()

