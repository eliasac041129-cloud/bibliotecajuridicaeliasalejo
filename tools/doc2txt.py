#!/usr/bin/env python3
"""Extrae texto de un .doc (Word binario OLE) parseando FIB + piece table (CLX)."""
import sys, struct, olefile

def extract(path):
    ole = olefile.OleFileIO(path)
    doc = ole.openstream('WordDocument').read()

    flags = struct.unpack_from('<H', doc, 0x0A)[0]
    fWhichTblStm = (flags & 0x0200) >> 9
    table_name = '1Table' if fWhichTblStm else '0Table'
    if not ole.exists(table_name):
        table_name = '1Table' if ole.exists('1Table') else '0Table'
    table = ole.openstream(table_name).read()

    fcClx = struct.unpack_from('<I', doc, 0x01A2)[0]
    lcbClx = struct.unpack_from('<I', doc, 0x01A6)[0]
    clx = table[fcClx:fcClx + lcbClx]

    i = 0
    plcpcd = None
    while i < len(clx):
        if clx[i] == 0x01:
            cb = struct.unpack_from('<H', clx, i + 1)[0]
            i += 3 + cb
        elif clx[i] == 0x02:
            lcb = struct.unpack_from('<I', clx, i + 1)[0]
            plcpcd = clx[i + 5:i + 5 + lcb]
            break
        else:
            i += 1
    if plcpcd is None:
        raise RuntimeError('No se encontro Pcdt (piece table)')

    n = (len(plcpcd) - 4) // (4 + 8)
    cps = [struct.unpack_from('<I', plcpcd, k * 4)[0] for k in range(n + 1)]
    pcd_base = (n + 1) * 4

    out = []
    for k in range(n):
        cp_start, cp_end = cps[k], cps[k + 1]
        nchars = cp_end - cp_start
        fc = struct.unpack_from('<I', plcpcd, pcd_base + k * 8 + 2)[0]
        if fc & 0x40000000:
            fc = (fc & 0x3FFFFFFF) // 2
            raw = doc[fc:fc + nchars]
            txt = raw.decode('cp1252', errors='replace')
        else:
            fc = fc & 0x3FFFFFFF
            raw = doc[fc:fc + nchars * 2]
            txt = raw.decode('utf-16-le', errors='replace')
        out.append(txt)

    text = ''.join(out)
    text = text.replace('\r', '\n').replace('\x07', '\n').replace('\x0b', '\n')
    text = text.replace('\x0c', '\n').replace('\x08', '').replace('\x01', '')
    lines = [ln.rstrip() for ln in text.split('\n')]
    ole.close()
    return '\n'.join(lines)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    t = extract(src)
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(t)
    print(f'{src} -> {dst}  ({len(t)} chars, {t.count(chr(10))} lineas)')
