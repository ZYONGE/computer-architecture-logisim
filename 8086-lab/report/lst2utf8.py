#!/usr/bin/env python3
"""MASM .LST(CP949) -> UTF-8 변환.
MASM은 긴 줄을 바이트 단위로 줄바꿈해서 한글(2바이트)이 줄 경계에서 쪼개진다.
윗줄 끝에 홀로 남은 선행 바이트와, 아랫줄 첫 글자 자리의 후행 바이트를 다시 붙인 뒤 디코딩한다."""
import sys

def dangling_lead(line: bytes) -> bool:
    i = 0
    while i < len(line):
        if line[i] >= 0x81:
            if i + 1 >= len(line):
                return True
            i += 2
        else:
            i += 1
    return False

def convert(src, dst):
    raw = open(src, 'rb').read().replace(b'\r\n', b'\n').replace(b'\x0c', b'')
    lines = raw.split(b'\n')
    for n in range(len(lines) - 1):
        if dangling_lead(lines[n]):
            nxt = lines[n + 1]
            k = len(nxt) - len(nxt.lstrip(b'\t'))      # 줄바꿈 들여쓰기(탭) 건너뛰기
            lines[n] += nxt[k:k + 1]                    # 후행 바이트를 윗줄로
            lines[n + 1] = nxt[:k] + nxt[k + 1:]
    text = b'\n'.join(lines).decode('cp949')            # 실패하면 예외 → 변환 오류를 숨기지 않음
    open(dst, 'w', encoding='utf-8').write(text)

for name in sys.argv[1:]:
    convert(name + '.LST', 'report/' + name.lower() + '.lst.txt')
    print('ok:', name)
