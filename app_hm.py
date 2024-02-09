import psycopg2
import random

# hm1: insert 10 products with random values

# 1. connect
conn = psycopg2.connect("dbname=e-shop-python user=postgres password=1234")
# 2. prepare the query
#sql = """
#BEGiN;
#INSERT INTO "money" VALUES (131, 15000, 'EURO');
#INSERT INTO "products" VALUES (131, 'Product #131', 131);
#INSERT INTO "stock" VALUES (2131, 131, 10000);
#COMMIT;
#"""
#product_id = 151
#product_price = 17.00
#product_quantity = 1000

#sql = f"""
#BEGiN;
#INSERT INTO "money" VALUES ({product_id}, {int(product_price * 100)}, 'EURO');
#INSERT INTO "products" VALUES ({product_id}, 'Product {product_id}', {product_id});
#INSERT INTO "stock" VALUES (2{product_id}, {product_id}, {product_quantity});
#COMMIT;
#"""
for i in range(10):
 product_id = random.randint(100, 1000)
 product_price = int(random.uniform(10, 100) * 100) / 100
 product_quantity = random.randint(1000, 10000)

 sql = f"""
 BEGiN;
 INSERT INTO "money" VALUES ({product_id}, {int(product_price * 100)}, 'EURO');
 INSERT INTO "products" VALUES ({product_id}, 'Product {product_id}', {product_id});
 INSERT INTO "stock" VALUES (2{product_id}, {product_id}, {product_quantity});
 COMMIT;
 """

#sql = """SELECT * FROM "products" JOIN "stock" ON "stock".product_id = "products".id JOIN "money" ON "products".price_id = "money".id;"""
# 3. create a cursor
 cursor = conn.cursor()
# 4. send the request
 cursor.execute(sql)
# 5. get the data
#result = cursor.fetchall()
#print(result)
