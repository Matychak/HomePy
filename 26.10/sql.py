# from lib.config import *
# from lib.DB_Manager import db_manager

# user_manager = db_manager(HOSTNAME,USERNAME,PASSWORD)

from lib.config import *
from lib.DB_Manager import db_manager

user_manager = db_manager(HOSTNAME,USERNAME,PASSWORD)
user_manager.menu()