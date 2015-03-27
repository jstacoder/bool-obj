from bool_obj import _and, _or,_not,nand,nor,xor,nxor

def test_and1():
    assert _and(0,0) == 0
def test_and2():
    assert _and(0,1) == 0
def test_and3():
    assert _and(1,0) == 0
def test_and4():
    assert _and(1,1) == 1
    

def test_or1():
    assert _or(0,0) == 0
def test_or2():
    assert _or(0,1) == 1
def test_or3():
    assert _or(1,0) == 1
def test_or4():
    assert _or(1,1) == 1

def test_not1():
    assert _not(1) == 0

def test_not2():
    assert _not(0) == 1

def test_nand1():
    assert nand(0,0) == 1
def test_nand2():
    assert nand(0,1) == 1
def test_nand3():
    assert nand(1,0) == 1
def test_nand4():
    assert nand(1,1) == 0

def test_nor1():
    assert nor(0,0) == 1
def test_nor2():
    assert nor(0,1) == 0
def test_nor3():
    assert nor(1,0) == 0
def test_nor4():
    assert nor(1,1) == 0

def test_xor1():
    print xor(0,0)
    assert xor(0,0) == 0
def test_xor2():
    print xor(0,1)
    assert xor(0,1) == 1
def test_xor3():
    print  xor(1,0) 
    assert xor(1,0) == 1
def test_xor4():
    print  xor(1,1)
    assert xor(1,1) == 0


def test_nxor1():
    assert nxor(0,0) == 1
def test_nxor2():
    assert nxor(0,1) == 0
def test_nxor3():
    assert nxor(1,0) == 0
def test_nxor4():
    assert nxor(1,1) == 1

