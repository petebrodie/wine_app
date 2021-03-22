import pdb
from models.wine import Wine
from models.producer import Producer

import repositories.wine_repository as wine_repository
import repositories.producer_repository as producer_repository

wine_repository.delete_all()
producer_repository.delete_all()





