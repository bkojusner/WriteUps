# TAMU – RSAaaay </br>
** CTF Name: ** TAMU ctf</br>
** Challenge Name: ** RSAaaay</br>
** Challenge Description: ** </br>
Hey, you're a hacker, right? I think I am too, look at what I made! </br>
________________________________________
(2531257, 43) </br>
My super secret message: 906851 991083 1780304 2380434 438490 356019 921472 </br>822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268</br>
________________________________________
Problem is, I don't remember how to decrypt it... could you help me out? </br>
Difficulty: easy
** Challenge Category: ** Crypto</br>
** Challenge Points: ** 354</br>
** Solve: ** </br>
We are given (2531257, 43) and I immediately assume it is (n, e), especially since the challenge is named after RSA. We are already given n, e, and c which means all we would need to do is get d in order to have everything needed to decrypt the cipher text. 
First step to getting d is getting the totient. After factoring n on https://www.alpertron.com.ar/ECM.HTM we were able to know that Euler’s totient is 2525776. 
After this, we need the modular multiplicative inverse. We found some python code to do this on stack overflow, and after plugging in e and the totient m on this python script we were able to get d as 58739. 

```python
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
```

Now that we have d, all we have left to do is to plug and chug in pow(c, d, n) and later convert the decimal output into ascii letters. This was initially done by hand as we were trying to submit the flag as quickly as we could, however a script was later written to automate the whole process for future reference.

```python
n = int(input("Enter n: "))
e = int(input("Enter e: "))
num = list(map(int, input("Enter c: ").split()))
m = int(input("Enter totient: "))

#Get D
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

d = int(modinv(43, 2525776))

for c in num:
  print(pow(c,d,n))
```

> Flag; gigem{Savege_Six_Flying_Tigers}






