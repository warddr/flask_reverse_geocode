from flask import Flask
import reverse_geocode

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/geo_lookup/<lat>/<lon>")
def geo_lookup(lat, lon):
    coord = (float(lat), float(lon))
    return reverse_geocode.get(coord)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
