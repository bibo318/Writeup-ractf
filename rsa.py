from pwn import *

# p = 12736417496736655442602617267963357620825841853712732906895398885696709839309257918168226091994953634497776446017624975845723070057111835461641254269269317
# q = 12812745834802942067887996082863564857775464236327866229873820064310547028668532363402551825083254446602822350152834784435994127878640673106783300383715213

# e = 65537

# ct = 36164077670048236315620165241501158490714780378828495489466034792516124438008544795706435407727196245542440722207946911741455419825341977882668518715641221655547701335758290288192516019599540143387244434109169262921709528678398951068201747253902131176016425711977353198578765688585598616779744281471591815486

p = 1299811
q = 1299827

1416088155477,1187894346607,1187894346607,1012248725317,1642686319107, 1299736156328, 1176348111078, 1566932379421, 976078105770,1041712991086,976078105770,164477670995,1176348111078,1533726616075,457718175500, 766162619069 ]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

totient = (p - 1) * (q - 1)
n = p * q
# print(n)
d = modinv(e,totient)
m = pow(ct, d, n)
flag = unhex(hex(m)[2:])
print('hex: '+hex(m))
print('get only hex code: '+hex(m)[2:])
print('unhex it: '+flag.decode())
