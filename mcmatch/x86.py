'''
x86-related code and constants

@author: niko
'''

# A comparison of instructions by execution time/latency can be found
# in http://www.agner.org/optimize/instruction_tables.pdf
expensive_mnemonics = [
    # x87 floating point instructions
    'fsqrt', # quite fast, but with long-ish dep chain
    'fsin', 'fcos', 'fsincos', 'fptan', 'fpatan',
    # obscure, rarely used x86 integer operations
    #'aam', 'das', 'daa',
    # less obscure ones: (note, op time depends quite a lot on operand types
    'div', 'idiv',
    # logic:
    'bsr', 'bsf',
    # other
    'sti', 'cpuid',
    # MMX instructions
    'divss', 'divps', 'sqrtss', 'sqrtps']

jump_mnemonics = ['jmp',
        'je', 'jne',
        'jz', 'jnz',
        'jg', 'jge',
        'ja', 'jae',
        'jl', 'jle',
        'jb', 'jbe',
        'jo', 'jno',
        'js', 'jns',
        'loop', 'loope', 'loopne', 'loopnz', 'loopz']

arith_mnemonics = ['add', 'sub', 'mul', 'div', 'imul', 'idiv',
                   'inc', 'dec', 'neg', 'sar', 'sal', 'addl', 'subl']

bitop_mnemonics = ['shr', 'shl', 'shld', 'shrd', 'ror', 'rol',
                   'rorl', 'roll', 'rcr', 'rcl', 'and', 'or', 'xor', 'not']

call_mnemonics = ['call', 'callq', 'callf']
