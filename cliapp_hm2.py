import psycopg2

conn = psycopg2.connect("dbname=chat_db user=postgres password=qazwsx host=localhost port=5889")
curs = conn.cursor()
# check for client existence
#curs.execute("""
# SELECT COUNT(*) FROM clients
# WHERE
#  email = 'jd@example.host'
# OR
#  phone = '+12345678';
#""")
#result = curs.fetchone()
#print(result
client_id = 10
client_name = "Johny Docker"
client_email = "jd1@example.host"
client_phone = "+5678902314"
client_password = "765432"
def registerClient(client_id, client_name, client_email, client_phone, client_password):
 conn = psycopg2.connect("dbname=chat_db user=postgres password=qazwsx host=localhost port=5889")
 curs = conn.cursor()
# check for client existence
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   email = '{client_email}'
  OR
   phone = '{client_phone}';
 """)
 if curs.fetchone()[0] == 0:
  curs.execute(f"""
   INSERT INTO clients VALUES(
    {client_id},
    {client_name},
    {client_phone},
    {client_email},
    {client_password}
     );
 """)
  conn.commit()
 else:
  print("This email or phone is used, is this your account ? ")
  
client_id = 11
client_name = "Pete Compi"
client_email = "cp@example.host"
client_phone = "+223435123"
client_password = "765432"
registerClient(client_id, client_name, client_email, client_phone, client_password)

def loginClient(client_email, client_password):
 conn = psycopg2.connect("dbname=chat_db user=postgres password=qazwsx host=localhost port=5889")
 curs = conn.cursor()
 curs.execute(f"""
  SELECT * FROM clients
  WHERE
   email = '{client_email}'
  AND
   password = '{client_password}'
  AND
   active = true;
 """)
 client = curs.fetchone()
 if client != None:
  id = client[0]
  curs.execute(f"""
   INSERT INTO sessions (client_id, data, authenticated) VALUES (
   {id},
    '',
   NOW()
     );
 """)
  conn.commit()
 else:
  print("Wrong credentials!")
loginClient(client_email, client_password)

# hm
def logoutClient(client_email):
 conn = psycopg2.connect("dbname=chat_db user=postgres password=qazwsx host=localhost port=5889")
 curs = conn.cursor()
 curs.execute(f"""
  SELECT * FROM clients
  WHERE
   email = '{client_email}'
 """)
 client = curs.fetchone()
 if client != None:
  id = client[0]
  curs.execute(f"""
   DELETE FROM "sessions" WHERE client_id = {id};
 """)
  conn.commit()
 else:
  print("Wrong credentials!")
logoutClient(client_email)
