from flask_frozen import Freezer
from index import app

freezer = Freezer(app)

if __name__=='__main__':
    freezer.freeze()
