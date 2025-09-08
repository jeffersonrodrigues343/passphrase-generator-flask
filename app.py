from flask import Flask, render_template
import random
from wordlist import words # importa nosso array "wordlist"

#inicializa a aplicação Flask
app = Flask(__name__)

@app.route('/') # Define a rota principal da nossa aplicação
def gerar_passphrase():
        """
        Esta função é executada quando o cliente acessa a página.
        """


        # 1. Escolhe 4 palavras aleatórias da nossa lista
        palavras_escolhidas = random.choices(words,k=4)

        # 2. Junta as palavras com um hífen para formar a passphrase
        passphrase_gerada = "-".join(palavras_escolhidas)

        # 3. Renderiza o arquivo HTML e passa a passphrase gerada para ele
        return render_template('index.html', passphrase=passphrase_gerada)

  #Permite que o script seja executado diretamente no 'python app.py'
if __name__=='__main__':
     app.run(debug=True)