eval() Function Demo

print(eval('25'))                  # ➜ 25 (int)
print(eval('10.8'))                # ➜ 10.8 (float)
print(eval('False'))               # ➜ False (bool)
print(eval('3+4j'))                # ➜ (3+4j) (complex)
print(eval('Hyd'))                 #  NameError (Hyd not defined)
print(eval("    'Hyd'   "))        # ➜ 'Hyd' (str, with spaces trimmed)
print(eval('3 + 4 * 5'))           # ➜ 23 (4*5=20 + 3 = 23)
print(eval('[10 , 20 , 15 , 18]')) # ➜ [10, 20, 15, 18] (list)
print(eval('{10,20,15,18,20,12,18}'))  # ➜ {10, 12, 15, 18, 20} (set, duplicates removed)
print(eval('(10 , 20 , 30)'))      # ➜ (10, 20, 30) (tuple)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  # ➜ {10: 'Sec'} (duplicate key, last wins)
print(eval(4 + 5))                 # ➜ 9 (evaluates 4+5 first, then passes 9 to eval → int)


---

Tricky eval() Program

print(eval("    'hyd'   "))       # ➜ 'hyd'
hyd = 'Sec'
print(eval('hyd'))                # ➜ 'Sec'
sec = '25'
print(eval('sec'))                # ➜ '25' (str)
print(eval(sec))                  # ➜ 25 (int)
cyb = 10.8
print(eval('cyb'))                # ➜ 10.8
print(eval(cyb))                  # ➜ 10.8 (float)


---
 eval with print inside

print(eval('print("Hyd")'))       # Prints: Hyd ➜ Then returns None ➜ Output: Hyd\nNone


---
 bool() vs eval() Trick

print(bool('False'))              # ➜ True (non-empty string)
print(eval('False'))              # ➜ False (boolean False)
print(bool(''))                   # ➜ False (empty string)
print(eval('  ""  '))             # ➜ "" ➜ empty string
print(eval(''))                   #  SyntaxError (empty input)
print(eval('  " "   '))           # ➜ ' ' (space)
print(eval(' '))                  #  SyntaxError (invalid literal)


---

 Advantage of eval(input())

x = eval(input('Enter any input : '))
print(type(x))
print(x)

Advantage: You can enter int, float, list, tuple, etc., and it automatically detects type.

Example input:

Enter any input: [1, 2, 3]
➜ <class 'list'>
➜ [1, 2, 3]


---

 Better way to take string input

a = input('Enter any string: ')
print(len(a))   # Length of input
print(a)

b = eval(input('Enter any string: '))
print(len(b))   # Works only if you enter string with quotes → 'Hyd'
print(b)

Note: eval(input()) for strings needs quotes in input: 'Hyd'


---

 sep= Argument Demo

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, sep=',')         # ➜ 25,10.8,Hyd
print(a, b, c, sep='\t')        # ➜ 25    10.8    Hyd
print(a, b, c, sep='---')       # ➜ 25---10.8---Hyd
print(a, b, c, sep='\n')        # ➜ prints each on new line
print(a, b, c)                  # ➜ 25 10.8 Hyd
print(a, b, c, separator=':')   #  TypeError (wrong keyword: should be sep)


---

 end= and sep= Combined

a, b, c = 25, 10.8, 'Hyd'
print(a, b, c, end='---')               # ➜ 25 10.8 Hyd---
print(a, b, c, sep=',,,')              # ➜ 25,,,10.8,,,Hyd
print(a, b, c, sep=':::', end='\t\t\t')# ➜ 25:::10.8:::Hyd\t\t\t
print(a, b, c)                         # ➜ 25 10.8 Hyd


---

 Empty print() Calls

print('Hyd')
print()           # prints empty line
print('Sec')
print()           # prints empty line
print('Cyb')


---

 Print List, Tuple, Set

l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
s = {10, 20, 30, 40}
print(l, t, s)  # ➜ [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}


---

 % Formatting - Type Demo

a = 25
b = '%f' % a
print(b)               # ➜ 25.000000
print(type(b))         # ➜ str

x = 10.8
y = '%d' % x
print(y)               # ➜ 10 (int part only)
print(type(y))         # ➜ str

m = [10, 20, 15, 18]
n = '%s' % m
print(n)               # ➜ [10, 20, 15, 18]
print(type(n))         # ➜ str


---

Float Formatting with Width & Precision

a = 10.9274
print('%8.2f' % a)     # ➜ '   10.93' (3 spaces)
print('%9.1f' % a)     # ➜ '     10.9'
print('%10.3f' % a)    # ➜ '    10.927'
print('%.2f' % a)      # ➜ '10.93'
print('%.6f' % a)      # ➜ '10.927400'
print('%f' % a)        # ➜ '10.927400'


---

 String Formatting

a = 'Hyd'
print('%7s' % a)       # ➜ '    Hyd'
print('%-7s' % a)      # ➜ 'Hyd    '
print('%2s' % a)       # ➜ 'Hyd' (width < string → ignored)
print('%s' % a)        # ➜ 'Hyd'
print('%s', a)         # ➜ ('%s', 'Hyd') (prints tuple)
print('%s' a)          #  SyntaxError
print('%s', %a)        #  SyntaxError
print(a)               # ➜ 'Hyd'


---

 List Formatting Errors

a = [10, 20, 30, 40]
print('%s' % a)        # ➜ '[10, 20, 30, 40]'
print('%s', a)         # ➜ ('%s', [10, 20, 30, 40])
print('%s' a)          # Error
print('%s', %a)        # Error
print('%l' % a)        # Error (%l not valid)
print(a)               # ➜ [10, 20, 30, 40]


---

 Multiple Value Formatting

a = 25
b = 10.9274
c = 'Hyd'

print('%d    %f    %s' % (a, b, c))   # ➜ 25    10.927400    Hyd
print('%i    %g    %s' % (a, b, c))   # ➜ 25    10.9274    Hyd
print('%s    %s    %s' % (a, b, c))   # ➜ 25    10.9274    Hyd
print('%d    %g    %s', a, b, c)      # ➜ ('%d    %g    %s', 25, 10.9274, 'Hyd')
print('%d    %g    %s' a, b, c)       # Error
print('%d    %g    %s',  %(a, b, c))  # Error (comma not allowed before %)
print('%d    %g    %s' % a % b % c)   # Error (chaining % is invalid)
print('%d' % a, '%f' % b, '%s' % c)   # ➜ 25 10.927400 Hyd
