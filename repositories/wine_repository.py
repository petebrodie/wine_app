from db.run_sql import run_sql
from models.wine import Wine
from models.producer import Producer
import producer_repository 


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