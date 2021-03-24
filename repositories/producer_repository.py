from db.run_sql import run_sql

from models.producer import Producer
from models.wine import Wine

def save(producer):
    sql = """
        INSERT INTO 
        producers (name, phone_number, email, country, region) 
        VALUES (%s, %s, %s, %s, %s) 
        RETURNING *
        """
    values = [
        producer.name, 
        producer.phone_number, 
        producer.email, 
        producer.country, 
        producer.region]
    results = run_sql(sql, values)
    producer.id = results[0]['id']
    return producer


def select(id):
    producer = None
    sql = """
        SELECT *
        FROM producers
        WHERE id = %s
        """
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        producer = Producer( 
            result['name'], 
            result['phone_number'], 
            result['email'], 
            result['country'], 
            result['region'],
            result['id'])
    return producer



def select_all():
    producers = []
    sql = "SELECT * FROM producers"
    results = run_sql(sql)

    for row in results:
        producer = Producer(
            row['name'],
            row['phone_number'],
            row['email'],
            row['country'],
            row['region'],
            row['id'])
        producers.append(producer)
    return producers



def delete_all():
    sql = "DELETE FROM producers"
    run_sql(sql)



def delete(id):
    sql = """
        DELETE FROM producers
        WHERE id = %s
        """
    values = [id]
    run_sql(sql, values)



def update(producer):
    sql = """
        UPDATE producers
        SET (name, phone_number, email, country, region)
        = (%s, %s, %s, %s, %s,)
        WHERE id = %s
        """
    values = [
        producer.name,
        producer.phone_number,
        producer.email, 
        producer.country,
        producer.region,
        producer.id]
    run_sql(sql, values)