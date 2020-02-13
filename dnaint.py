import re, sys
"""
cheat sheet and remeber note
The DNA Sharp Programing Language works with a series of sets of 4 where the instructions are [^ ATGC] and has no instruction limit

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
    # funtion is a indual intruccion 
    global pos, pnt, tape
    #Take the global variables to make them own in fuction
    oldpnt = tape[pnt]

    pos += 1
    #read the code moving in the secuence
    while code[pos] != "CGCG":
        #while instruccion are difernt to CGCG
        eval(code[pos].lower()+'()')
        #pass the code to python interpreter
    newpnt = tape[pnt]
    tape[pnt] = oldpnt
    #extract the intruccion of sequence  and the old instruccion go to secence
    exec('tape[pnt]'+action+'newpnt')
#ponter
def atat():
    #sum 1 to pointer ,ponter is a regitrer address in memory and sum 1 is move in memory
    global pos, pnt, tape
    pnt += 1
    #if length of tape == pnt add a other element to array
    if len(tape) == pnt:
        tape += [0]
    
    pos += 1

def atgc():
    #this is to go back a record or a pointer
    global pos, pnt, tape
    pnt -= 1
    
    if pnt < 0:
        raise RuntimeError("Pointer fell off tape at position "+str(pos))
    
    pos += 1
    
def atta():
    #this is going to add 1 value of a ponter
    global pos, pnt, tape
    tape[pnt] += 1
    
    pos += 1
    
def atcg():
    #This goes back 1 number  in the pointer
    global pos, pnt, tape
    tape[pnt] -= 1
    
    pos += 1
#input /output
def gcta():
    #read pointer
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
    #print char in part of sequense 
    global pos, pnt, tape
    
    print(chr(tape[pnt]),end='')
    
    pos += 1
    
def gcgc():
    #key board input
    global pos, pnt, tape
    
    tape[pnt] = ord(input())
    
    pos += 1
    
def cggc():
    #print a part of sequence
    global pos, pnt, tape
    
    print(tape[pnt],end='')
    
    pos += 1

def cgta():
    #int input
    global pos, pnt, tape
    
    tape[pnt] = int(input())
    
    pos += 1
#arimetic operators betten part of sequence and new pointer
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
    #pass
    global pos, pnt, tape
    
    pos += 1
try :    
    while pos < len(code):
        comm = code[pos]
        print(eval(comm.lower() + "()"))

        #print('syntaxis error with ', eval(comm.lower())
except:
    comm = code[pos]
    print("error in ",comm )
