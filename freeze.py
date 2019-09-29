from flask_frozen import Freezer
from dateotw import app

app.config['FREEZER_BASE_URL'] = 'https://johnjung.github.io/design_after_the_end_of_the_world/'
freezer = Freezer(app)

if __name__=='__main__':
    freezer.freeze()
