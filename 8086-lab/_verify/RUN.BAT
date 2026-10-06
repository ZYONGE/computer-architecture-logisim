@echo off
debug reg.exe < reg.dbg > reg.dbo
debug stack.exe < stack.dbg > stack.dbo
compare.exe < c1.in > c1.out
compare.exe < c2.in > c2.out
compare.exe < c3.in > c3.out
sample.exe < s.in > s.out
