from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
db = SQLAlchemy(app)

class Hotel(db.Model):
  __tablename__ = 'hotelsts'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  return render_template("list.html")


@app.route("/hotels/")
def list():
  hotels = Hotel.query.all()
  return render_template("list.html", hotels=hotels)


@app.route("/hotels/<BBL>/")
def show(BBL):
  hotel = Hotel.query.filter_by(BBL=BBL).first()
  return render_template("show.html", hotel=hotel)

""" @app.route("/hotels/cool-fun-hotel/")
def show():
  hotel = Hotel.query.filter_by(index = 1).first()
  return render_template("show.html", hotel=hotel) """


if __name__ == "__main__":
  app.run(debug=True)