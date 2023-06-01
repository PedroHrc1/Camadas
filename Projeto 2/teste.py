import random



#Client
C1 = b'\x00\x00\x00\x00' 
C2 = b'\x00\x00\xAA\x00' 
C3 = b'\xAA\x00\x00' 
C4 = b'\x00\xAA\x00' 
C5 = b'\x00\x00\xAA' 
C6 = b'\x00\xAA' 
C7 = b'\xAA\x00' 
C8 = b'\x00' 
C9 = b'\xFF' 


bytes_val = len(C1).to_bytes(1, byteorder='big')
print(bytes_val)

c1_new = bytes_val + C1

lista_comandos = [C1, C2, C3, C4, C5, C6, C7, C8, C9]

lista_com_select = []

n_comandos = random.randint(10, 30)
print("n_comandos = {}" .format(n_comandos))

i = 0

while i < n_comandos:
    comando = random.choice(lista_comandos)
    comando = len(comando).to_bytes(1, byteorder='big') + comando 

    lista_com_select.append(comando)
    i += 1

arraydebites = bytearray()
for c in lista_com_select:
    arraydebites += c

print(arraydebites)

print(f"tamanho {arraydebites[0]}")




#Server



tamanho_do_byte = arraydebites[0]


tamanho_do_array = len(arraydebites)
print(f"tamanho do array = {tamanho_do_array}")

lista_com_rec = []

i = 0

while i < tamanho_do_array:
    n = 0
    #print(i)
    tamanho_do_byte = arraydebites[i]
    prov_bit = b''

    while n <= tamanho_do_byte:
        #print(arraydebites[i].to_bytes(1, byteorder='big'))
        prov_bit += arraydebites[i].to_bytes(1, byteorder='big')
        n += 1
        i += 1
    
    
    lista_com_rec.append(prov_bit)


print(lista_com_rec)

# print(lista_com_select)


# print(f"len do byte = {lista_com_select[0]}")

# print(f"len do byte = {lista_com_select[0][0]}")