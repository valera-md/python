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

hm: client authentication
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


#python3 -m venv env - через модудь venv создай environment
#source env/bin/activate - запуск environment
#app (python) -> ORM -> adapter (psycopg-binary) -> postgresql
# ORM - object relational mapping, типа библиотеки, паттерны приненим
ORM будем использовать в основной логике, для того чтобы функциями туда передовать какие-то действия, данные или получать результат оттуда.
#pip install psycopg2-binary - установка psycopg2 в environment
#sudo docker-composer up - запуск файла docker-compose.yml, который запускает или создаёт и запускает контейнер
# в пайтоне многострочный текст пишется в тройных кавычках """ """, не важно какого характера
# когда мы вносим изменения типа insert, update, delete обязательно нужно выполнять commit, моментально применять эти измненения
# psql -U postgres -h localhost -p 5889 - подключение к движку postgresql, к пользователю postgres в контейнере docker
# \c chat_db - подключение к базе данных chat_db
# SELECT * FROM clients
# https://www.psycopg.org/docs/usage.html