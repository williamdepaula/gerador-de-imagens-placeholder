import sys
import os
from flask import Flask, render_template, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)


def gera_imagem(width, height):
    width = max(width, 1)
    height = max(height, 1)

    width = min(width, 5000)
    height = min(height, 5000)

    filename = 'imagem.png'
    img = Image.new('RGB', (width, height), "lightgray")
    msg = f'{width}x{height}'
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(msg)
    draw.text( ((width-w)/2, (height-h)/2), msg, fill="black")

    img.save(filename)

    return filename


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<int:width>/")
def gera_imagem_quadrada(width):

    filename = gera_imagem(width, width)

    return send_file(filename, mimetype='image/png')


@app.route("/<int:width>/<int:height>/")
def gera_imagem_retangulo(width, height):
    filename = gera_imagem(width, height)

    return send_file(filename, mimetype='image/png')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
