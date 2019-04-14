# PlaidCTF 2019 - can you guess me<br>
**CTF Name:** PlaidCTF 2019 </br>
**Challenge Name:** can you guess me</br>
**Challenge Description:**</br></br>
Here's the source to a guessing game: [here](https://play.plaidctf.com/files/can-you-guess-me-53d1aa54ca7d7151fcd2c48ce36d1bdb.py)</br>

You can access the server at</br>

nc canyouguessme.pwni.ng 12349</br></br>
**Challenge Category:** Misc</br>
**Challenge Points:** 100</br>
**Solve:**</br>
We open the python file to see the code that's running on the server</br>
```python
#! /usr/bin/env python3

from sys import exit
from secret import secret_value_for_password, flag, exec

print(r"")
print(r"")
print(r"  ____         __   __           ____                     __  __       ")
print(r" / ___|__ _ _ _\ \ / /__  _   _ / ___|_   _  ___  ___ ___|  \/  | ___  ")
print(r"| |   / _` | '_ \ V / _ \| | | | |  _| | | |/ _ \/ __/ __| |\/| |/ _ \ ")
print(r"| |__| (_| | | | | | (_) | |_| | |_| | |_| |  __/\__ \__ \ |  | |  __/ ")
print(r" \____\__,_|_| |_|_|\___/ \__,_|\____|\__,_|\___||___/___/_|  |_|\___| ")
print(r"                                                                       ")
print(r"")
print(r"")

try:
    val = 0
    inp = input("Input value: ")
    count_digits = len(set(inp))
    if count_digits <= 10:          # Make sure it is a number
        val = eval(inp)
    else:
        raise

    if val == secret_value_for_password:
        print(flag)
    else:
        print("Nope. Better luck next time.")
except:
    print("Nope. No hacking.")
    exit(1)
```
Seemed simple enough I thought, we just had to dissect the code and see where the vulnerability lie that would give us the right value for our ```secret_value_for_password``` variable.

I first did exactly that and statically analyzed the code, seeing where the exploit could be. My teammate [Owen](https://github.com/owenflannagan) mentioned something about exec being imported, and after some research I learned about how vulnerable python's ```eval()``` statement was. 
I looked for some articles and started trying to dump ```dir()``` which would maybe lead me in the right direction. I typed in ```print(dir())``` which showed me what valid attributes were being held in the object. It was at this point that my other team mate Kevin proposed printing out the flag, however nothing would happen as the command was 10 lines long.</br>
After some trial and error, my other teammate [Owen](https://github.com/owenflannagan) ended up solving the challenge! </br>
He stated that he simply put in ```print(vars())``` and it returned the value of the flag within the vars(). This was also another idea proposed by Kevin, yet we didn't realize that it would work being that the parentheses used in the command would only equal to one element in the ```set()``` part of the code, making the length equal to 10! I had to see this for myself and ran that through and indeed we do see the flag.
![](PLAID2019/cygm.PNG)
I wrote a script to clean the output and make the process much more painless, it's in the folder under solver.py </br>

flag = ```PCTF{hmm_so_you_were_Able_2_g0lf_it_down?_Here_have_a_flag}```
