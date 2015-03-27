import sys

def to_bits(v):
    rtn = []
    for i in xrange(8):
        rtn.append(v & 1)
        v >>= 1
    return tuple(reversed(rtn))

def to_byte(b):
    v = 0
    for bit in b:
        v = (v<<1)|bit
    return v

def _and(a,b):
    rtn = None
    if a == 0:
        if b == 0:
            rtn = 0
        else:
            rtn = 0
    else:
        if b == 0:
            rtn = 0
        else:
            rtn = 1
    return rtn

def _or(a,b):
    rtn = None
    if a == 0:
        if b == 0:
            rtn = 0
        else:
            rtn = 1
    else:
        rtn = 1
    return rtn

def _not(a):
    return 0 if a else 1

def nand(a,b):
    rtn = None
    if a == 0:
        rtn = 1
    else:
        if b == 1:
            rtn = 0
        else:
            rtn = 1
    return rtn

def nor(a,b):
    rtn = None
    if a == 0:
        if b == 0:
            rtn = 1
        else:
            rtn = 0
    else:
        rtn = 0
    return rtn
        

def xor(a,b):
    rtn = None
    if a == 0:
        if b == 0:
            rtn = 0
        else:
            rtn = 1
    else:
        if b == 0:
            rtn = 1
        else:
            rtn = 0
    return rtn

def nxor(a,b):
    rtn = None
    if a == 0:
        if b == 0:
            rtn = 1
        else:
            rtn = 0
    else:
        if b == 0:
            rtn = 0
        else:
            rtn = 1
    return rtn

def main():
    if len(sys.argv) == 1:
        message = 'hi you &#43;'
    else:
        message = ''.join(map(str,sys.argv[1:]))
    mbytes = message.encode("UTF-8")
    print mbytes
    print ''.join(['{}\n'.format(to_bits(ord(c))) for c in mbytes])


if __name__ == "__main__":
    main()
