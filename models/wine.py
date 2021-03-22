class Wine:

    def __init__(self, grape_variety, description, cost_price, retail_price, stock, producer, id = None):
        self.id = id
        self.grape_variety = grape_variety
        self.description = description
        self.cost_price = cost_price
        self.retail_price = retail_price
        self.stock = stock
        self.producer = producer
        