import json
from collections import Counter

with open('cpp.sarif') as f:
    data = json.load(f)

SUB_NULLCHECK = 'is not checked for null, but'
VAL_NULLCHECK = 'Result of call is not checked for null'

SUB_NONLOCAL = 'may be assigned to a non-local variable.'
VAL_NONLOCAL = 'A stack address  may be assigned to a non-local variable.'

SUB_PNTMISMATCH = 'This pointer might have type'
VAL_PNTMISMATCH = 'A pointer might have mismatching type.'

SUB_UNREACHABLE = ' is unreachable'
VAL_UNREACHABLE = 'Unreachable code.'

SUB_UNUSED = ' is not used.'
VAL_UNUSED = 'Code is not used.'

SUB_UNREAD = ' is never read.'
VAL_UNREAD = 'Variable is never read.'

SUB_TOOMANY = 'Block with too many statements ('
VAL_TOOMANY = 'Block with too many statements.'

SUB_LONGSWITCH = 'Switch has at least one case that is too long'
VAL_LONGSWITCH = 'Switch has at least one case that is too long'

SUB_NONINIT = 'may not be initialized at this access.'
VAL_NONINIT = 'A variable may not be initialized at this access.'

SUB_MULT = "Multiplication result may overflow"
VAL_MULT = "Multiplication result may overflow."

SUB_PASSPOINTER = 'consider passing a const pointer/reference instead.'
VAL_PASSPOINTER = 'Parameter too big, consider passing a const pointer/reference instead.'

SUB_LOOPALOC = 'Stack allocation is inside a '
VAL_LOOPALOC = 'Stack allocation is inside a loop.'

SUB_GLOBALHIDE = 'global variable](1) with the same name.'
VAL_GLOVALHIDE = 'Global variable hides another variable with the same name.'

SUB_VIRTOVER = 'If you intend to statically call this virtual function'
VAL_VIRTOVER = 'Call to virtual function which is overriden.'

SUB_VIRTCALL = ' that calls virtual function '
VAL_VIRTCALL = 'Call to virtual function.'

SUB_USERINPUT = 'This argument to a file access function is derived from [user input'
VAL_USERINPUT = 'Using unsanitized user data for file access.'

SUB_NULLREDUNDANT = 'This null check is redundant because'
VAL_NULLREDUNDANT = 'Null check is redundant.'

# substring: value
SUB_ITEMS = {
    SUB_NONLOCAL: VAL_NONLOCAL,
    SUB_NULLCHECK: VAL_NULLCHECK,
    SUB_NONINIT: VAL_NONINIT,
    SUB_PNTMISMATCH: VAL_PNTMISMATCH,
    SUB_UNREACHABLE: VAL_UNREACHABLE,
    SUB_UNUSED: VAL_UNUSED,
    SUB_UNREAD: VAL_UNREAD,
    SUB_TOOMANY: VAL_TOOMANY,
    SUB_LONGSWITCH: VAL_LONGSWITCH,
    SUB_MULT: VAL_MULT,
    SUB_PASSPOINTER: VAL_PASSPOINTER,
    SUB_LOOPALOC: VAL_LOOPALOC,
    SUB_GLOBALHIDE: VAL_GLOVALHIDE,
    SUB_VIRTOVER: VAL_VIRTOVER,
    SUB_VIRTCALL: VAL_VIRTCALL,
    SUB_USERINPUT: VAL_USERINPUT,
    SUB_NULLREDUNDANT: VAL_NULLREDUNDANT,
}

VAL_SWITCH = 'This switch statement should either handle more cases, or be rewritten as an if statement.'
VAL_NEGMOD = 'Possibly invalid test for oddness. This will fail for negative numbers.'
VAL_LONGENUM = 'Enumeration types should be used instead of integers to select from a limited series of choices.'
VAL_NEGSUB = 'Unsigned subtraction can never be negative.'
VAL_NEGBIT = 'Usage of a logical not (!) expression as a bitwise operator.'
VAL_NONREAD = 'This variable is read, but may not have been written. It should be guarded by a check that the [call to sscanf](1) returns at least 1.'
VAL_FLOATEQ = 'Equality checks on floating point values can yield unexpected results.'
VAL_COMPLEX = 'Complex condition: too many logical operations in this expression.'
VAL_COMPARE = 'Comparison as an operand to another comparison.'
VAL_COMPARE_TRUE = 'Comparison is always true because end <= -1.'
VAL_RAWARRAY = 'Raw arrays should not be used in interfaces. A container class should be used instead.'
VAL_ENUMINIT = 'In an enumerator list, the = construct should not be used to explicitly initialize members other than the first, unless all items are explicitly initialized.'
VAL_FORMATCONST = 'The format string argument to snprintf should be constant to prevent security issues and other potential errors.'
VAL_HEADGUARD = 'This header file should contain a header guard to prevent multiple inclusion.'
VAL_NOMATCH = 'No matching copy assignment operator in class Iterator. It is good practice to match a copy constructor with a copy assignment operator.'

# 1:1 match
VAL_ITEMS = [
    VAL_SWITCH,
    VAL_NEGSUB,
    VAL_LONGENUM,
    VAL_NEGMOD,
    VAL_NEGBIT,
    VAL_NONREAD,
    VAL_FLOATEQ,
    VAL_COMPLEX,
    VAL_COMPARE,
    VAL_COMPARE_TRUE,
    VAL_RAWARRAY,
    VAL_ENUMINIT,
    VAL_FORMATCONST,
    VAL_HEADGUARD,
    VAL_NOMATCH,
]

res = Counter()

for item in data['runs'][0]['results']:
    item_msg = item['message']['text']

    if item_msg in VAL_ITEMS:
        res[item_msg] += 1
        continue

    found = False
    for submsg, msg in SUB_ITEMS.items():
        if submsg in item_msg:
            res[msg] += 1
            found = True
            break

    if found:
        continue

    print("")
    print(item['message'])

print('''
|Error description | Occurances|
|------------------|-----------|''')

for k, v in res.most_common():
    print(f'|{k}|{v}|')
