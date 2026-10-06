@echo off
masm reg,,reg; > reg.log
link reg; >> reg.log
masm stack,,stack; > stack.log
link stack; >> stack.log
masm compare,,compare; > compare.log
link compare; >> compare.log
masm sample,,sample; > sample.log
link sample; >> sample.log
