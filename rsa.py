import math

p = int(input("Enter p value"))
q = int(input("Enter q value"))

n = p * q
phi = (p - 1) * (q - 1)
e = 2

while (e < phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e = e + 1
print('e', e)

for i in range(1, 10):
    x = 1 + i * phi
    if x % e == 0:
        d = int(x / e)
        break
print('d', d)
msg = int(input("Enter message"))

print("Messsage before encryption:", msg)

c = pow(msg, e)
c = c % n
print("Encrypted data= ", c)

m = pow(c, d)
m = m % n
print("Original Message after decryption=", m)
