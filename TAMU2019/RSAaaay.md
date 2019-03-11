# TAMU – RSAaaay </br>
**CTF Name:** TAMU ctf</br>
**Challenge Name:** RSAaaay</br>
**Challenge Description:** </br>
```
Hey, you're a hacker, right? I think I am too, look at what I made!
________________________________________
(2531257, 43)
My super secret message: 906851 991083 1780304 2380434 438490 356019 921472
822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268
________________________________________
Problem is, I don't remember how to decrypt it... could you help me out?
```
***Difficulty:*** easy </br>
**Challenge Category:** Crypto</br>
**Challenge Points:** 354</br>
**Solve:** </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We are given (2531257, 43) and I immediately assume it is (n, e), especially since the challenge is named after RSA. We are already given n, e, and c which means all we would need to do is get d in order to have everything needed to decrypt the cipher text.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First step to getting d is getting the totient. After factoring n on https://www.alpertron.com.ar/ECM.HTM we were able to know that Euler’s totient is 2525776.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After this, we need the modular multiplicative inverse. We found some python code to do this on stack overflow, and after plugging in e and the totient m on this python script we were able to get d as 58739.</br>

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now that we have d, all we have left to do is to plug and chug in pow(c, d, n) and later convert the decimal output into ascii letters. This was initially done by hand as we were trying to submit the flag as quickly as we could, however a script was later written to automate the whole process for future reference.</br>

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

d = int(modinv(e, m))

for c in num:
  print(pow(c,d,n))
```
Note: The script outputs each line in decimal, you have to split up the numbers into their respective values within the ascii range, and convert to ascii. So 103105 would be split to 103 105, which would then be converted to ascii. The proper modifications to the script will soon be added so it does this automatically.

> Flag: gigem{Savege_Six_Flying_Tigers}
