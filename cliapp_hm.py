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
def registerClient(client_id, client_name, client_email, client_phone, client_password)

#hm: client authentication
#ALTER TABLE clients
#ADD COLUMN login boolean DEFAULT false;
# добавляем колонку логин
def loginClient(client_email, client_password):
 conn = psycopg2.connect("dbname=chat_db user=postgres password=qazwsx host=localhost port=5889")
 curs = conn.cursor()
# check for client existence
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   email = '{client_email}';
 """)
 if curs.fetchone()[0] == 0:
  print("This email doesn't exist, please register first. ")
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   email = '{client_email}'
  AND
   password = '{client_password}'
  AND
   active = false
 """)
 elif curs.fetchone()[0] == 1:
  print("Your account is blocked for non-compliance with regulations.")
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   email = '{client_email}'
  AND
   password = '{client_password}'
  AND
   active = true
  AND
   login = true
 """)
 elif curs.fetchone()[0] == 1:
  print("You are already logged in.")
 curs.execute(f"""
  SELECT COUNT(*) FROM clients
  WHERE
   email = '{client_email}'
  AND
   password = '{client_password}'
  AND
   active = true
  AND
   login = false
 """)
 elif curs.fetchone()[0] == 1:
  curs.execute(f"""
  UPDATE clients
  SET login = true
  WHERE email = '{client_email}';
  """)
  print("Account login succeed.")
