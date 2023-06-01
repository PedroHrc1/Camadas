

#Cliente

imageR = "pequeno.png"

txBuffer = open(imageR, 'rb').read() #isso é um array de bytes
       
print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))


x = b'\x01'

header = bytearray()

header += b'\x00' * 12

eop_hs = bytearray()

eop_hs += b'\x00\x00\x01'

print(header)

print(int.from_bytes(x, byteorder='big'))


imagem = len(txBuffer)# numero de bits
pacotes_completos = imagem // 114
pacote_restante = imagem % 114

if pacote_restante == 0 : 
    total_de_pacotes = pacotes_completos
else:
    total_de_pacotes = pacotes_completos + 1

print("numero de pacotes:{}".format(total_de_pacotes))
print("tamanho ultimo pacote:{}".format(pacote_restante))

#print(total_de_pacotes.to_bytes(1, byteorder='big'))






eop = bytearray()

eop += b'\xbb\xbb\xbb'

for i in range(0, total_de_pacotes):
    pacote_full = bytearray()

    #Payload

    payload = txBuffer[i*114:(i+1)*114]
    print("-"*50)
    print("pacote completo:{}".format(payload))
    print("-"*50)
    print("tamanho do pacote:{}".format(len(payload)))
    print("-"*50)

    #Header
    header = bytearray()

    header +=  total_de_pacotes.to_bytes(4, byteorder='big') #Qtd de pacotes total

    header +=  len(payload).to_bytes(4, byteorder='big') #Tamanho do payload

    #Numero do Payload
    n_p = i + 1
    header +=  n_p.to_bytes(4, byteorder='big') #Numero do pacote

    #fim

    pacote_full += header + payload + eop

    

    

    

#print("header:{}".format(header))

