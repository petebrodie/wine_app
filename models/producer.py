class Producer:
    
    def __init__(self, name, phone_number, email, country, region, id = None):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.country = country
        self.region = region