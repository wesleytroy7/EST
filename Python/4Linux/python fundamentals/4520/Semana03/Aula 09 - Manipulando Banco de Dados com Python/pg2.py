import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=pagila user=postgres password=wesley')
    cur = con.cursor()
except Exception as e:
    print('Erro')
    exit()

cur.execute("INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES (202, 'wesley', 'GUINESS', '2300-02-15 09:34:33');")
con.commit()

cur.close()
con.close()