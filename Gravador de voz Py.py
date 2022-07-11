# Importando as bibliotecas necessárias para a execução do algoritmo
import sounddevice
from scipy.io.wavfile import write
print('-=-'*15)
print(f'{"GRAVADOR DE VOZ EM PYTHON":^45}')
print('-=-'*15)

#Frequência de amostragem
fs = 44100
# Definindo o tempo de gravação
tempo = int(input('Por quantos segundos deseja gravar sua linda voz?: '))

print('\nGravando sua linda voz.......\n')
#Capturando a gravação
gravacao = sounddevice.rec(int(tempo*fs), samplerate=fs, channels=2)
sounddevice.wait()

#Salva arquivo da gravação
write('gravacao.wav', fs, gravacao)



