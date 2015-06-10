'''
Created on Apr 1, 2015

@author: niko
'''
import unittest
from mcmatch.feature.cyclo import PseudoCyclofeatureComplexityFeature
from mcmatch.db.types import Codeblock

# exp10 of musl
musl_exp10 = '''
0x000000000002c167 <+0>:  push   rbx
0x000000000002c168 <+1>:  movapd xmm1,xmm0
0x000000000002c16c <+5>:  sub    rsp,0x20
0x000000000002c170 <+9>:  lea    rdi,[rsp+0x18]
0x000000000002c175 <+14>:  movsd  QWORD PTR [rsp+0x8],xmm1
0x000000000002c17b <+20>:  call   0x32ab1 <modf>
0x000000000002c180 <+25>:  mov    rax,QWORD PTR [rsp+0x18]
0x000000000002c185 <+30>:  movsd  xmm1,QWORD PTR [rsp+0x8]
0x000000000002c18b <+36>:  mov    rdx,rax
0x000000000002c18e <+39>:  shr    rdx,0x34
0x000000000002c192 <+43>:  and    edx,0x7ff
0x000000000002c198 <+49>:  cmp    rdx,0x402
0x000000000002c19f <+56>:  ja     0x2c1f1 <exp10+138>
0x000000000002c1a1 <+58>:  movapd xmm2,xmm0
0x000000000002c1a5 <+62>:  xorps  xmm0,xmm0
0x000000000002c1a8 <+65>:  lea    rbx,[rip+0x56f11]        # 0x830c0 <p10.2456>
0x000000000002c1af <+72>:  ucomisd xmm2,xmm0
0x000000000002c1b3 <+76>:  jp     0x2c1ce <exp10+103>
0x000000000002c1b5 <+78>:  jne    0x2c1ce <exp10+103>
0x000000000002c1b7 <+80>:  mov    QWORD PTR [rsp+0x8],rax
0x000000000002c1bc <+85>:  cvttsd2si eax,QWORD PTR [rsp+0x8]
0x000000000002c1c2 <+91>:  add    eax,0xf
0x000000000002c1c5 <+94>:  cdqe   
0x000000000002c1c7 <+96>:  movsd  xmm0,QWORD PTR [rbx+rax*8]
0x000000000002c1cc <+101>:  jmp    0x2c1fe <exp10+151>
0x000000000002c1ce <+103>:  mulsd  xmm2,QWORD PTR [rip+0x56fe2]        # 0x831b8
0x000000000002c1d6 <+111>:  movapd xmm0,xmm2
0x000000000002c1da <+115>:  call   0x2c381 <exp2>
0x000000000002c1df <+120>:  cvttsd2si eax,QWORD PTR [rsp+0x18]
0x000000000002c1e5 <+126>:  add    eax,0xf
0x000000000002c1e8 <+129>:  cdqe   
0x000000000002c1ea <+131>:  mulsd  xmm0,QWORD PTR [rbx+rax*8]
0x000000000002c1ef <+136>:  jmp    0x2c1fe <exp10+151>
0x000000000002c1f1 <+138>:  movsd  xmm0,QWORD PTR [rip+0x56fc7]        # 0x831c0
0x000000000002c1f9 <+146>:  call   0x33207 <pow>
0x000000000002c1fe <+151>:  add    rsp,0x20
0x000000000002c202 <+155>:  pop    rbx
0x000000000002c203 <+156>:  ret    
'''

class Test(unittest.TestCase):


    def setUp(self):
        self.cc = PseudoCyclofeatureComplexityFeature()
        self.cb = Codeblock()
        self.cb.disassembly_from_text(musl_exp10)

    def tearDown(self):
        pass


    def testPCycloMetric(self):
        self.cc.calculate(self.cb)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
