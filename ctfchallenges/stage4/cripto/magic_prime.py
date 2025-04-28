#!/usr/bin/env python3
from Crypto.Util.number import bytes_to_long, getPrime
from secrets import token_bytes, randbelow

# Definimos la flag
FLAG = "CAUC{17_w45n7_45_d1ff1cul7_45_1_7h0u6h7}"

# Convertimos la flag a bytes y la rellenamos
flag_bytes = FLAG.encode()
padded_flag = flag_bytes + token_bytes(128 - len(flag_bytes))
padded_flag_int = bytes_to_long(padded_flag)

# Generamos tres primos para crear un RSA con 3 factores
p, q, r = getPrime(512), getPrime(512), getPrime(512)
N = p * q * r
e = 65537  # Usando un exponente público común

# Calculamos phi (función de Euler) y la clave privada
phi = (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phi)

# Genni likes squares y SBG likes cubes
value_for_genni = p**2 + (q + r * padded_flag_int)**2
value_for_sbg = p**3 + (q + r * padded_flag_int)**3

# Valores para el Oblivious Transfer
x0 = randbelow(N)
x1 = randbelow(N)

# Mostramos los valores públicos
print("Welcome to the Squares vs Cubes challenge!")
print(f"N = {N}")
print(f"e = {e}")
print(f"x0 = {x0}")
print(f"x1 = {x1}")

print("\nDo you prefer squares or cubes? Choose wisely!")
print("Send me a value v, and I'll help you calculate either Genni's or SBG's value.")
print("(This is an implementation of 1-out-of-2 Oblivious Transfer)")

try:
    # El usuario debe enviar v = x_i + k^e mod N para algún k aleatorio
    v = int(input('Send me v: '))
    
    # Calculamos los mensajes usando Oblivious Transfer
    m0 = (pow(v - x0, d, N) + value_for_genni) % N
    m1 = (pow(v - x1, d, N) + value_for_sbg) % N
    
    print(f"m0 = {m0}  # Genni's value (squares)")
    print(f"m1 = {m1}  # SBG's value (cubes)")
    
    print("\nCan you extract the flag from these values?")
    
except Exception as e:
    print(f"Error: {e}")
