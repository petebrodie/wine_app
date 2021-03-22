from db.run_sql import run_sql
from models.wine import Wine
from models.producer import Producer
import repositories.producer_repository as producer_repository 


def save(wine):
    sql = """
        INSERT INTO wines
        (grape_variety, 
        description, 
        cost_price, 
        retail_price, 
        stock, 
        producer_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *
    """

    values = [
        wine.grape_variety, 
        wine.description, 
        wine.cost_price, 
        wine.retail_price, 
        wine.stock, 
        wine.producer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    wine.id = id
    return wine


def select(id):
    wine = None
    sql = "SELECT * FROM wine WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        producer = producer_repository.select(result['producer_id'])
        wine = Wine(
            result['grape_variety'], 
            producer, 
            result['description'], 
            result['cost_price'], 
            result['retail_price'], 
            result['stock'], 
            result['producer'])
    return wine


def select_all():
    wine = []
    sql = "SELECT * FROM wine"
    results = run_sql(sql)

    for row in results:
        producer = producer_repository.select(row['producer_id'])
        wine = Wine(
            row['grape_variety'],
            producer,
            row['description'],
            row['cost_price'],
            row['retail_price'], 
            row['stock'], 
            row['producer'])
        wine.append(wine)
    return wine



def delete_all():
    sql = "DELETE FROM wine"
    run_sql(sql)



def delete(id):
    sql = "DELETE FROM wine WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def update(wine):
    sql = """
        "UPDATE wine SET 
        (grape_variety, 
        producer_id, 
        description, 
        cost_price, 
        retail_price, 
        stock, 
        producer) 
        = (%s, %s, %s, %s, %s, %s, %s) 
        WHERE id = %s
        """
    values = [
        wine.grape_variety, 
        wine.producer.id, 
        wine.description, 
        wine.cost_price, 
        wine.retail_price, 
        wine.stock, 
        wine.producer, 
        wine.id]
    run_sql(sql, values)
        
    