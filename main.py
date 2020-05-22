from flask import Flask, render_template, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def gera_imagem(largura, altura):
    largura = max(largura, 1)
    largura = min(largura, 5000)

    altura = max(altura, 1)
    altura = min(altura, 5000)

    img = Image.new('RGB', (largura, altura), 'lightgray')

    draw = ImageDraw.Draw(img)
    tamanho_imagem = f'{largura}x{altura}'
    l, a = draw.textsize(tamanho_imagem)
    pos_x = (largura-l)/2
    pos_y = (altura-a)/2
    draw.text( ( pos_x, pos_y ), tamanho_imagem, fill="black" )
    
    nome_arquivo = f'imagens/{tamanho_imagem}.png'
    img.save(nome_arquivo)

    return nome_arquivo    

@app.route("/<int:tamanho>/")
def gera_imagem_quadrada(tamanho):

    nome_arquivo = gera_imagem(tamanho, tamanho)

    return send_file(nome_arquivo, mimetype='image/png')

@app.route("/<int:largura>/<int:altura>/")
def gera_imagem_retangular(largura, altura):

    nome_arquivo = gera_imagem(largura, altura)

    return send_file(nome_arquivo, mimetype='image/png')

if __name__ == "__main__":
    app.run(port=8000, debug=True)