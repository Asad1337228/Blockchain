
import hashlib
# print("Hello World")
# m = hashlib.sha256()
# print(m)
# m.update(b"Nobody inspects")
# print(m)

# m.update(b" the spammish repetition")
# print(m)
# m.digest()
# print(m)

# m = hashlib.sha256()

def poluchitHash(IINHASH):
    Hash = hashlib.sha256(IINHASH.encode()).hexdigest()
    return Hash

iin = str(input())
i = 0
hashok = poluchitHash(iin)
print(hashok)
while True:
    # print(str(iin))
    IINHASH = iin + "+" +str(i)
    # print(IINHASH)
    hash_znach = poluchitHash((IINHASH))   
    # if hash_znach[:1] =="0" and hash_znach[:2] !="00"  :
    #     print("С одним нулём",hash_znach)  
    # if hash_znach[:3] =="000":
    #     print("С тремя нулями",hash_znach)
    #     break  
    if hash_znach[:2] == "00":  
        print("Найдено!")
        print("Входное значение:", iin)
        print("Хэш:", hash_znach)
        print("Количество шагов", i)
        break
    i += 1
    
print(IINHASH)