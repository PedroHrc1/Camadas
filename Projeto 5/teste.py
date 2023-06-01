from crc import Crc16, Calculator

inicio = False

server_id = b'\xEE'

img_id = b'\xcc'

eop = b'\xAA\xBB\xCC\xDD'

#Numero total de Pacotes

imageR = "pequeno.png"

txBuffer = open(imageR, 'rb').read() #isso é um array de bytes

imagem = len(txBuffer)  # numero de bits
pacotes_completos = imagem // 114
pacote_restante = imagem % 114

if pacote_restante == 0 : 
    total_de_pacotes = pacotes_completos
else:
    total_de_pacotes = pacotes_completos + 1

print("numero de pacotes:{}".format(total_de_pacotes))



handshake = b'\x01' + server_id + b'\x00' + total_de_pacotes.to_bytes(1, byteorder='big') + b'\x00' + img_id + b'\x00'*4 + eop

print(handshake)

i = 1

pacote_full = bytearray()
pacote_full_arrumado = bytearray()

payload = txBuffer[i*114:(i+1)*114]

#CRC
expected = b'\x00' + b'\x00'
calculator = Calculator(Crc16.CCITT, optimized=True)
expected = calculator.checksum(payload).to_bytes(2, byteorder='big')


len(payload).to_bytes(1, byteorder='big')
pacote_full += b'\x03' + b'\x00' + b'\x00' + total_de_pacotes.to_bytes(1, byteorder='big') + i.to_bytes(1, byteorder='big') + len(payload).to_bytes(1, byteorder='big') + b'\x00'*2 + expected + payload + eop

# print(pacote_full)

print(expected)