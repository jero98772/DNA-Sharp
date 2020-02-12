import re, sys
"""
cheat sheet
Command 	Brainfuck equivalent 	C-equivalent 	Symbols for symbol form
ATAT 	> 	pointer++ / newpointer++ *** 	>
ATGC 	< 	pointer-- / newpointer-- *** 	<
ATTA 	+ 		+
ATCG 	- 		-
GCAT 	. (Output as ASCII) 		.
GCGC 	, (ASCII input) 		,
GCTA 	[ 		[
GCCG 	] 		]
TAAT * 		*pointer = *newpointer 	= or := ****
TAGC * 		*pointer += *newpointer 	+=
TATA * 		*pointer -= *newpointer 	-=
TACG * 		*pointer *= *newpointer 	*=
CGAT * 		*pointer /= *newpointer 	/=
CGGC 		. (Output as integer value) 	~
CGTA 		, (Integer input) 	?
CGCG 		- (NOP) 	X** 
"""
fname = sys.argv[1]
#the argument give the name of file 
with open(fname, "r") as f:
    code = f.read()
#open file
code = re.sub("[^ATCG]","",code)
#regular expreion [^ATCG] repalse "" in file or string
code = [code[i:i+4] for i in range(0,len(code),4)]
#select in size of instruccion with length 4
pos = 0
#position in code can use for debug an error 
pnt = 0
#ponter is a index of code, where is in code
tape = [0]
#tape is a secence
def npointfunc(action):
    global pos, pnt, tape
    oldpnt = tape[pnt]

    pos += 1
    
    while code[pos] != "CGCG":
        eval(code[pos].lower()+'()')

    newpnt = tape[pnt]
    tape[pnt] = oldpnt

    exec('tape[pnt]'+action+'newpnt')

def atat():
    global pos, pnt, tape
    pnt += 1
    
    if len(tape)==pnt:
        tape += [0]
    
    pos += 1

def atgc():
    global pos, pnt, tape
    pnt -= 1
    
    if pnt < 0:
        raise RuntimeError("Pointer fell off tape at position "+str(pos))
    
    pos += 1
    
def atta():
    global pos, pnt, tape
    tape[pnt] += 1
    
    pos += 1
    
def atcg():
    global pos, pnt, tape
    tape[pnt] -= 1
    
    pos += 1

def gcta():
    global pos, pnt, tape
    
    if tape[pnt] == 0:
        while code[pos] != "GCCG":
            pos += 1
        pos += 1

    else:
        pos += 1
        tpos = pos
        while tape[pnt] > 0:
            pos = tpos
            while code[pos] != "GCCG":
                eval(code[pos].lower()+'()')

        pos += 1
    
def gcat():
    global pos, pnt, tape
    
    print(chr(tape[pnt]),end='')
    
    pos += 1
    
def gcgc():
    global pos, pnt, tape
    
    tape[pnt] = ord(input())
    
    pos += 1
    
def cggc():
    global pos, pnt, tape
    
    print(tape[pnt],end='')
    
    pos += 1
    
def cgta():
    global pos, pnt, tape
    
    tape[pnt] = int(input())
    
    pos += 1

def taat():
    npointfunc('=')

def tagc():
    npointfunc('+=')

def tata():
    npointfunc('-=')

def tacg():
    npointfunc('*=')

def cgat():
    npointfunc('/=')

def cgcg():
    global pos, pnt, tape
    
    pos += 1

while pos < len(code):
    comm = code[pos]
    print(eval(comm.lower() + "()"))
    
