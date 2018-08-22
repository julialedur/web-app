from flask_frozen import Freezer
from app import app, Hotel

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def show():
    for hotel in Hotel.query.all():
        yield { 'BBL': hotel.BBL }

if __name__ == '__main__':
    freezer.freeze()