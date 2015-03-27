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


def main():
    if len(sys.argv) == 1:
        message = 'hi you &#43;'
    else:
        message = ''.join(map(str,sys.argv[1:]))
    mbytes = message.encode("UTF-8")
    print ''.join(['{}\n'.format(to_bits(ord(c))) for c in mbytes])


if __name__ == "__main__":
    main()
