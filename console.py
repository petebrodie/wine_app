import pdb
from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_repository.delete_all()
producer_repository.delete_all()

producer1 = Producer("Cloudy Bay", "6435209147", "info@cloudybay.co.nz", "New Zealand", "Marlborough")
producer_repository.save(producer1)

producer2 = Producer("Châteaux Codéclan", "1312902600", "python3@codeclan.com", "Scotland", "Edinburgh")
producer_repository.save(producer2)

producer3 = Producer("Penfolds", "1300095930", "info@penfolds.co.au", "Australia", "Barossa Valley")
producer_repository.save(producer3)

producer4 = Producer("Campo Viejo", "34941279900", "info.bodegas@pernod-ricard.com", "Spain", "Rioja")
producer_repository.save(producer4)

producer5 = Producer("Royal Tokaji", "3647548500", "zsolt@royal-tokaji.hu", "Hungary", "Tokaj")
producer_repository.save(producer5)

producer6 = Producer("Pol Roger", "3332659800", "polroger@polroger.fr", "France", "Champagne")
producer_repository.save(producer6)

producer7 = Producer("Freixenet", "3355191", "info@freixenet.com", "Italy", "Veneto")
producer_repository.save(producer7)


wine1 = Wine("Sauvignon Blanc", "Light, crisp and refreshing", 9.15, 22.99, 12, producer1)
wine_repository.save(wine1)

wine2 = Wine("Pinot Noir", "Floral, with black cherry and bramble", 8.87, 19.50, 3, producer1)
wine_repository.save(wine2)

wine3 = Wine("Merlot", "Intense and complex, sometimes hard to swollow", 6.91, 17.50, 5, producer2)
wine_repository.save(wine3)

wine4 = Wine("Cabernet Sauvignon", "dark and mysterious", 10.27, 26.00, 1, producer2)
wine_repository.save(wine4)

wine5 = Wine("Shiraz", "Full bodied, rich and fruity", 13.79, 35, 8, producer3)
wine_repository.save(wine5)

wine6 = Wine("Tempranillo", "Easy-drinking, jammy red wine", 4.84, 9.99, 0, producer4)
wine_repository.save(wine6)

wine7 = Wine("Furmint", "Honey and orange notes with some spice", 9.68, 25.00, 2, producer5)
wine_repository.save(wine7)

wine8 = Wine("Chardonnay", "Rich, apricot and lemon notes with a long savory finish ", 19.57, 49.99, 6, producer6)
wine_repository.save(wine8)

wine9 = Wine("Prosecco", "Simple, light and citrussy", 6.01, 14.99, 1, producer7)
wine_repository.save(wine9)

wine10 = Wine("Cava", "Light, red berry fruit with hint of vanilla", 6.46, 15.99, 1, producer7)
wine_repository.save(wine10)




pdb.set_trace()