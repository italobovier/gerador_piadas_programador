# Importa bibliotecas
import pyjokes
from deep_translator import GoogleTranslator

# Inicializa o tradutor
tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    # Obtém uma piada em inglês
    piada = pyjokes.get_joke()

    # Traduz a piada para o português
    piada_traduzida = tradutor.translate(piada)
    
    # Exibe a piada traduzida
    print(piada_traduzida)
    
    # Pergunta se o usuário deseja gerar outra piada
    repetir = input('Gerar outra piada (s/n)? ').strip().lower()
    
    if repetir != 's':
        print('Obrigado por usar o programa! Até a próxima!')
        break
