from pwn import *

#target = process('./k3Y')
conn = remote('20.42.99.115', 3143)

payload = ""
payload += '3345399721'

#target.sendline(payload)
conn.sendline(payload)
#target.interactive()
conn.interactive()
