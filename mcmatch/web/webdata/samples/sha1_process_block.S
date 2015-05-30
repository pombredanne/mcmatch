   0x0000000000000070 <+0>:	push   r15
   0x0000000000000072 <+2>:	mov    rax,rsi
   0x0000000000000075 <+5>:	mov    rcx,rdi
   0x0000000000000078 <+8>:	and    rax,0xfffffffffffffffc
   0x000000000000007c <+12>:	push   r14
   0x000000000000007e <+14>:	add    rax,rdi
   0x0000000000000081 <+17>:	mov    rdi,rax
   0x0000000000000084 <+20>:	push   r13
   0x0000000000000086 <+22>:	push   r12
   0x0000000000000088 <+24>:	push   rbp
   0x0000000000000089 <+25>:	push   rbx
   0x000000000000008a <+26>:	mov    rbx,rdx
   0x000000000000008d <+29>:	sub    rsp,0x24
   0x0000000000000091 <+33>:	mov    QWORD PTR [rsp-0x34],rax
   0x0000000000000096 <+38>:	mov    eax,DWORD PTR [rdx]
   0x0000000000000098 <+40>:	mov    QWORD PTR [rsp-0x2c],rdx
   0x000000000000009d <+45>:	mov    DWORD PTR [rsp-0x48],eax
   0x00000000000000a1 <+49>:	mov    eax,DWORD PTR [rdx+0x4]
   0x00000000000000a4 <+52>:	mov    DWORD PTR [rsp-0x44],eax
   0x00000000000000a8 <+56>:	mov    eax,DWORD PTR [rdx+0x8]
   0x00000000000000ab <+59>:	mov    DWORD PTR [rsp-0x40],eax
   0x00000000000000af <+63>:	mov    eax,DWORD PTR [rdx+0xc]
   0x00000000000000b2 <+66>:	mov    DWORD PTR [rsp-0x3c],eax
   0x00000000000000b6 <+70>:	mov    eax,DWORD PTR [rdx+0x10]
   0x00000000000000b9 <+73>:	mov    DWORD PTR [rsp-0x38],eax
   0x00000000000000bd <+77>:	mov    eax,DWORD PTR [rdx+0x14]
   0x00000000000000c0 <+80>:	add    eax,esi
   0x00000000000000c2 <+82>:	mov    DWORD PTR [rdx+0x14],eax
   0x00000000000000c5 <+85>:	mov    rdx,rsi
   0x00000000000000c8 <+88>:	shr    rdx,0x20
   0x00000000000000cc <+92>:	add    edx,DWORD PTR [rbx+0x18]
   0x00000000000000cf <+95>:	cmp    esi,eax
   0x00000000000000d1 <+97>:	seta   al
   0x00000000000000d4 <+100>:	movzx  eax,al
   0x00000000000000d7 <+103>:	add    eax,edx
   0x00000000000000d9 <+105>:	cmp    rcx,rdi
   0x00000000000000dc <+108>:	mov    DWORD PTR [rbx+0x18],eax
   0x00000000000000df <+111>:	jae    0x13ba <sha1_process_block+4938>
   0x00000000000000e5 <+117>:	mov    rax,rcx
   0x00000000000000e8 <+120>:	nop    DWORD PTR [rax+rax*1+0x0]
   0x00000000000000f0 <+128>:	xor    edx,edx
   0x00000000000000f2 <+130>:	nop    WORD PTR [rax+rax*1+0x0]
   0x00000000000000f8 <+136>:	mov    ecx,DWORD PTR [rax+rdx*1]
   0x00000000000000fb <+139>:	bswap  ecx
   0x00000000000000fd <+141>:	mov    DWORD PTR [rsp+rdx*1-0x24],ecx
   0x0000000000000101 <+145>:	add    rdx,0x4
   0x0000000000000105 <+149>:	cmp    rdx,0x40
   0x0000000000000109 <+153>:	jne    0xf8 <sha1_process_block+136>
   0x000000000000010b <+155>:	mov    r11d,DWORD PTR [rsp-0x24]
   0x0000000000000110 <+160>:	mov    ebx,DWORD PTR [rsp-0x38]
   0x0000000000000114 <+164>:	add    rax,0x40
   0x0000000000000118 <+168>:	mov    edi,DWORD PTR [rsp-0x48]
   0x000000000000011c <+172>:	mov    r15d,DWORD PTR [rsp-0x40]
   0x0000000000000121 <+177>:	mov    r8d,DWORD PTR [rsp-0x44]
   0x0000000000000126 <+182>:	mov    r10d,DWORD PTR [rsp-0x20]
   0x000000000000012b <+187>:	lea    esi,[r11+rbx*1+0x5a827999]
   0x0000000000000133 <+195>:	mov    ebx,DWORD PTR [rsp-0x3c]
   0x0000000000000137 <+199>:	mov    ebp,DWORD PTR [rsp-0x18]
   0x000000000000013b <+203>:	mov    edx,edi
   0x000000000000013d <+205>:	mov    r12d,DWORD PTR [rsp-0x14]
   0x0000000000000142 <+210>:	mov    r14d,DWORD PTR [rsp-0x10]
   0x0000000000000147 <+215>:	ror    edx,0x1b
   0x000000000000014a <+218>:	add    esi,edx
   0x000000000000014c <+220>:	mov    edx,ebx
   0x000000000000014e <+222>:	lea    ecx,[r10+rbx*1+0x5a827999]
   0x0000000000000156 <+230>:	xor    edx,r15d
   0x0000000000000159 <+233>:	and    edx,r8d
   0x000000000000015c <+236>:	ror    r8d,0x2
   0x0000000000000160 <+240>:	xor    edx,ebx
   0x0000000000000162 <+242>:	mov    ebx,DWORD PTR [rsp-0x1c]
   0x0000000000000166 <+246>:	add    esi,edx
   0x0000000000000168 <+248>:	mov    edx,r15d
   0x000000000000016b <+251>:	xor    edx,r8d
   0x000000000000016e <+254>:	and    edx,edi
   0x0000000000000170 <+256>:	ror    edi,0x2
   0x0000000000000173 <+259>:	lea    r9d,[rbx+r15*1+0x5a827999]
   0x000000000000017b <+267>:	xor    edx,r15d
   0x000000000000017e <+270>:	add    edx,ecx
   0x0000000000000180 <+272>:	mov    ecx,esi
   0x0000000000000182 <+274>:	ror    ecx,0x1b
   0x0000000000000185 <+277>:	add    ecx,edx
   0x0000000000000187 <+279>:	mov    edx,edi
   0x0000000000000189 <+281>:	xor    edx,r8d
   0x000000000000018c <+284>:	and    edx,esi
   0x000000000000018e <+286>:	ror    esi,0x2
   0x0000000000000191 <+289>:	xor    edx,r8d
   0x0000000000000194 <+292>:	add    edx,r9d
   0x0000000000000197 <+295>:	mov    r9d,ecx
   0x000000000000019a <+298>:	ror    r9d,0x1b
   0x000000000000019e <+302>:	add    edx,r9d
   0x00000000000001a1 <+305>:	lea    r9d,[r8+rbp*1+0x5a827999]
   0x00000000000001a9 <+313>:	mov    r8d,esi
   0x00000000000001ac <+316>:	xor    r8d,edi
   0x00000000000001af <+319>:	and    r8d,ecx
   0x00000000000001b2 <+322>:	ror    ecx,0x2
   0x00000000000001b5 <+325>:	xor    r8d,edi
   0x00000000000001b8 <+328>:	mov    r15d,ecx
   0x00000000000001bb <+331>:	add    r8d,r9d
   0x00000000000001be <+334>:	mov    r9d,edx
   0x00000000000001c1 <+337>:	xor    r15d,esi
   0x00000000000001c4 <+340>:	ror    r9d,0x1b
   0x00000000000001c8 <+344>:	add    r8d,r9d
   0x00000000000001cb <+347>:	lea    r9d,[rdi+r12*1+0x5a827999]
   0x00000000000001d3 <+355>:	mov    edi,r15d
   0x00000000000001d6 <+358>:	and    edi,edx
   0x00000000000001d8 <+360>:	mov    r15d,DWORD PTR [rsp-0xc]
   0x00000000000001dd <+365>:	xor    edi,esi
   0x00000000000001df <+367>:	add    edi,r9d
   0x00000000000001e2 <+370>:	mov    r9d,r8d
   0x00000000000001e5 <+373>:	ror    r9d,0x1b
   0x00000000000001e9 <+377>:	ror    edx,0x2
   0x00000000000001ec <+380>:	add    edi,r9d
   0x00000000000001ef <+383>:	lea    r9d,[rsi+r14*1+0x5a827999]
   0x00000000000001f7 <+391>:	mov    esi,edx
   0x00000000000001f9 <+393>:	xor    esi,ecx
   0x00000000000001fb <+395>:	and    esi,r8d
   0x00000000000001fe <+398>:	ror    r8d,0x2
   0x0000000000000202 <+402>:	xor    esi,ecx
   0x0000000000000204 <+404>:	add    esi,r9d
   0x0000000000000207 <+407>:	mov    r9d,edi
   0x000000000000020a <+410>:	ror    r9d,0x1b
   0x000000000000020e <+414>:	add    esi,r9d
   0x0000000000000211 <+417>:	lea    r9d,[rcx+r15*1+0x5a827999]
   0x0000000000000219 <+425>:	mov    ecx,r8d
   0x000000000000021c <+428>:	xor    ecx,edx
   0x000000000000021e <+430>:	and    ecx,edi
   0x0000000000000220 <+432>:	ror    edi,0x2
   0x0000000000000223 <+435>:	xor    ecx,edx
   0x0000000000000225 <+437>:	add    ecx,r9d
   0x0000000000000228 <+440>:	mov    r9d,esi
   0x000000000000022b <+443>:	ror    r9d,0x1b
   0x000000000000022f <+447>:	add    ecx,r9d
   0x0000000000000232 <+450>:	mov    r9d,DWORD PTR [rsp-0x8]
   0x0000000000000237 <+455>:	lea    r9d,[rdx+r9*1+0x5a827999]
   0x000000000000023f <+463>:	mov    edx,edi
   0x0000000000000241 <+465>:	xor    edx,r8d
   0x0000000000000244 <+468>:	and    edx,esi
   0x0000000000000246 <+470>:	ror    esi,0x2
   0x0000000000000249 <+473>:	xor    edx,r8d
   0x000000000000024c <+476>:	add    edx,r9d
   0x000000000000024f <+479>:	mov    r9d,ecx
   0x0000000000000252 <+482>:	ror    r9d,0x1b
   0x0000000000000256 <+486>:	add    edx,r9d
   0x0000000000000259 <+489>:	mov    r9d,DWORD PTR [rsp-0x4]
   0x000000000000025e <+494>:	lea    r9d,[r8+r9*1+0x5a827999]
   0x0000000000000266 <+502>:	mov    r8d,esi
   0x0000000000000269 <+505>:	xor    r8d,edi
   0x000000000000026c <+508>:	and    r8d,ecx
   0x000000000000026f <+511>:	ror    ecx,0x2
   0x0000000000000272 <+514>:	xor    r8d,edi
   0x0000000000000275 <+517>:	mov    r13d,ecx
   0x0000000000000278 <+520>:	add    r8d,r9d
   0x000000000000027b <+523>:	mov    r9d,edx
   0x000000000000027e <+526>:	xor    r13d,esi
   0x0000000000000281 <+529>:	ror    r9d,0x1b
   0x0000000000000285 <+533>:	add    r8d,r9d
   0x0000000000000288 <+536>:	mov    r9d,DWORD PTR [rsp]
   0x000000000000028c <+540>:	lea    r9d,[rdi+r9*1+0x5a827999]
   0x0000000000000294 <+548>:	mov    edi,r13d
   0x0000000000000297 <+551>:	and    edi,edx
   0x0000000000000299 <+553>:	xor    edi,esi
   0x000000000000029b <+555>:	ror    edx,0x2
   0x000000000000029e <+558>:	add    edi,r9d
   0x00000000000002a1 <+561>:	mov    r9d,r8d
   0x00000000000002a4 <+564>:	ror    r9d,0x1b
   0x00000000000002a8 <+568>:	add    edi,r9d
   0x00000000000002ab <+571>:	mov    r9d,DWORD PTR [rsp+0x4]
   0x00000000000002b0 <+576>:	lea    r9d,[rsi+r9*1+0x5a827999]
   0x00000000000002b8 <+584>:	mov    esi,edx
   0x00000000000002ba <+586>:	xor    esi,ecx
   0x00000000000002bc <+588>:	and    esi,r8d
   0x00000000000002bf <+591>:	ror    r8d,0x2
   0x00000000000002c3 <+595>:	xor    esi,ecx
   0x00000000000002c5 <+597>:	add    esi,r9d
   0x00000000000002c8 <+600>:	mov    r9d,edi
   0x00000000000002cb <+603>:	ror    r9d,0x1b
   0x00000000000002cf <+607>:	add    esi,r9d
   0x00000000000002d2 <+610>:	mov    r9d,DWORD PTR [rsp+0x8]
   0x00000000000002d7 <+615>:	lea    r9d,[rcx+r9*1+0x5a827999]
   0x00000000000002df <+623>:	mov    ecx,r8d
   0x00000000000002e2 <+626>:	xor    ecx,edx
   0x00000000000002e4 <+628>:	and    ecx,edi
   0x00000000000002e6 <+630>:	ror    edi,0x2
   0x00000000000002e9 <+633>:	xor    ecx,edx
   0x00000000000002eb <+635>:	add    ecx,r9d
   0x00000000000002ee <+638>:	mov    r9d,esi
   0x00000000000002f1 <+641>:	ror    r9d,0x1b
   0x00000000000002f5 <+645>:	add    ecx,r9d
   0x00000000000002f8 <+648>:	mov    r9d,DWORD PTR [rsp+0xc]
   0x00000000000002fd <+653>:	lea    r9d,[rdx+r9*1+0x5a827999]
   0x0000000000000305 <+661>:	mov    edx,edi
   0x0000000000000307 <+663>:	xor    edx,r8d
   0x000000000000030a <+666>:	and    edx,esi
   0x000000000000030c <+668>:	ror    esi,0x2
   0x000000000000030f <+671>:	xor    edx,r8d
   0x0000000000000312 <+674>:	add    edx,r9d
   0x0000000000000315 <+677>:	mov    r9d,ecx
   0x0000000000000318 <+680>:	ror    r9d,0x1b
   0x000000000000031c <+684>:	add    edx,r9d
   0x000000000000031f <+687>:	mov    r9d,DWORD PTR [rsp+0x10]
   0x0000000000000324 <+692>:	lea    r9d,[r8+r9*1+0x5a827999]
   0x000000000000032c <+700>:	mov    r8d,esi
   0x000000000000032f <+703>:	xor    r8d,edi
   0x0000000000000332 <+706>:	and    r8d,ecx
   0x0000000000000335 <+709>:	ror    ecx,0x2
   0x0000000000000338 <+712>:	xor    r8d,edi
   0x000000000000033b <+715>:	mov    r13d,ecx
   0x000000000000033e <+718>:	add    r8d,r9d
   0x0000000000000341 <+721>:	mov    r9d,edx
   0x0000000000000344 <+724>:	ror    r9d,0x1b
   0x0000000000000348 <+728>:	add    r8d,r9d
   0x000000000000034b <+731>:	mov    r9d,DWORD PTR [rsp+0x14]
   0x0000000000000350 <+736>:	xor    r13d,esi
   0x0000000000000353 <+739>:	xor    r11d,ebx
   0x0000000000000356 <+742>:	xor    r11d,DWORD PTR [rsp-0x4]
   0x000000000000035b <+747>:	xor    r10d,ebp
   0x000000000000035e <+750>:	xor    r11d,DWORD PTR [rsp+0x10]
   0x0000000000000363 <+755>:	xor    r10d,DWORD PTR [rsp]
   0x0000000000000367 <+759>:	lea    r9d,[rdi+r9*1+0x5a827999]
   0x000000000000036f <+767>:	mov    edi,r13d
   0x0000000000000372 <+770>:	xor    r10d,DWORD PTR [rsp+0x14]
   0x0000000000000377 <+775>:	and    edi,edx
   0x0000000000000379 <+777>:	ror    edx,0x2
   0x000000000000037c <+780>:	xor    edi,esi
   0x000000000000037e <+782>:	add    edi,r9d
   0x0000000000000381 <+785>:	mov    r9d,r8d
   0x0000000000000384 <+788>:	ror    r11d,0x1f
   0x0000000000000388 <+792>:	ror    r9d,0x1b
   0x000000000000038c <+796>:	ror    r10d,0x1f
   0x0000000000000390 <+800>:	add    edi,r9d
   0x0000000000000393 <+803>:	mov    r9d,DWORD PTR [rsp+0x18]
   0x0000000000000398 <+808>:	lea    r9d,[rsi+r9*1+0x5a827999]
   0x00000000000003a0 <+816>:	mov    esi,edx
   0x00000000000003a2 <+818>:	xor    esi,ecx
   0x00000000000003a4 <+820>:	and    esi,r8d
   0x00000000000003a7 <+823>:	ror    r8d,0x2
   0x00000000000003ab <+827>:	xor    esi,ecx
   0x00000000000003ad <+829>:	add    esi,r9d
   0x00000000000003b0 <+832>:	mov    r9d,edi
   0x00000000000003b3 <+835>:	ror    r9d,0x1b
   0x00000000000003b7 <+839>:	add    esi,r9d
   0x00000000000003ba <+842>:	lea    r9d,[rcx+r11*1+0x5a827999]
   0x00000000000003c2 <+850>:	mov    ecx,r8d
   0x00000000000003c5 <+853>:	xor    ecx,edx
   0x00000000000003c7 <+855>:	and    ecx,edi
   0x00000000000003c9 <+857>:	ror    edi,0x2
   0x00000000000003cc <+860>:	xor    ecx,edx
   0x00000000000003ce <+862>:	add    ecx,r9d
   0x00000000000003d1 <+865>:	mov    r9d,esi
   0x00000000000003d4 <+868>:	ror    r9d,0x1b
   0x00000000000003d8 <+872>:	add    ecx,r9d
   0x00000000000003db <+875>:	lea    r9d,[rdx+r10*1+0x5a827999]
   0x00000000000003e3 <+883>:	mov    edx,edi
   0x00000000000003e5 <+885>:	xor    edx,r8d
   0x00000000000003e8 <+888>:	and    edx,esi
   0x00000000000003ea <+890>:	xor    edx,r8d
   0x00000000000003ed <+893>:	add    edx,r9d
   0x00000000000003f0 <+896>:	mov    r9d,ecx
   0x00000000000003f3 <+899>:	ror    r9d,0x1b
   0x00000000000003f7 <+903>:	xor    ebx,r12d
   0x00000000000003fa <+906>:	ror    esi,0x2
   0x00000000000003fd <+909>:	add    edx,r9d
   0x0000000000000400 <+912>:	mov    r9d,DWORD PTR [rsp+0x4]
   0x0000000000000405 <+917>:	xor    r12d,r15d
   0x0000000000000408 <+920>:	xor    r9d,ebx
   0x000000000000040b <+923>:	xor    r9d,DWORD PTR [rsp+0x18]
   0x0000000000000410 <+928>:	ror    r9d,0x1f
   0x0000000000000414 <+932>:	lea    ebx,[r8+r9*1+0x5a827999]
   0x000000000000041c <+940>:	mov    r8d,esi
   0x000000000000041f <+943>:	xor    r8d,edi
   0x0000000000000422 <+946>:	and    r8d,ecx
   0x0000000000000425 <+949>:	ror    ecx,0x2
   0x0000000000000428 <+952>:	xor    r8d,edi
   0x000000000000042b <+955>:	add    r8d,ebx
   0x000000000000042e <+958>:	mov    ebx,edx
   0x0000000000000430 <+960>:	ror    ebx,0x1b
   0x0000000000000433 <+963>:	add    ebx,r8d
   0x0000000000000436 <+966>:	mov    r8d,ebp
   0x0000000000000439 <+969>:	mov    ebp,ecx
   0x000000000000043b <+971>:	xor    r8d,r14d
   0x000000000000043e <+974>:	xor    r8d,DWORD PTR [rsp+0x8]
   0x0000000000000443 <+979>:	xor    ebp,esi
   0x0000000000000445 <+981>:	xor    r8d,r11d
   0x0000000000000448 <+984>:	ror    r8d,0x1f
   0x000000000000044c <+988>:	lea    r13d,[rdi+r8*1+0x5a827999]
   0x0000000000000454 <+996>:	mov    edi,ebp
   0x0000000000000456 <+998>:	mov    ebp,ebx
   0x0000000000000458 <+1000>:	and    edi,edx
   0x000000000000045a <+1002>:	ror    ebp,0x1b
   0x000000000000045d <+1005>:	ror    edx,0x2
   0x0000000000000460 <+1008>:	xor    edi,esi
   0x0000000000000462 <+1010>:	add    r13d,edi
   0x0000000000000465 <+1013>:	mov    edi,DWORD PTR [rsp+0xc]
   0x0000000000000469 <+1017>:	add    r13d,ebp
   0x000000000000046c <+1020>:	xor    edi,r12d
   0x000000000000046f <+1023>:	xor    edi,r10d
   0x0000000000000472 <+1026>:	ror    edi,0x1f
   0x0000000000000475 <+1029>:	lea    ebp,[rsi+rdi*1+0x6ed9eba1]
   0x000000000000047c <+1036>:	mov    esi,edx
   0x000000000000047e <+1038>:	xor    esi,ecx
   0x0000000000000480 <+1040>:	xor    esi,ebx
   0x0000000000000482 <+1042>:	add    esi,ebp
   0x0000000000000484 <+1044>:	mov    ebp,r13d
   0x0000000000000487 <+1047>:	ror    ebp,0x1b
   0x000000000000048a <+1050>:	add    ebp,esi
   0x000000000000048c <+1052>:	mov    esi,DWORD PTR [rsp-0x8]
   0x0000000000000490 <+1056>:	ror    ebx,0x2
   0x0000000000000493 <+1059>:	mov    r12d,ebp
   0x0000000000000496 <+1062>:	ror    r12d,0x1b
   0x000000000000049a <+1066>:	xor    esi,r14d
   0x000000000000049d <+1069>:	xor    esi,DWORD PTR [rsp+0x10]
   0x00000000000004a1 <+1073>:	xor    esi,r9d
   0x00000000000004a4 <+1076>:	ror    esi,0x1f
   0x00000000000004a7 <+1079>:	lea    r14d,[rcx+rsi*1+0x6ed9eba1]
   0x00000000000004af <+1087>:	mov    ecx,ebx
   0x00000000000004b1 <+1089>:	xor    ecx,edx
   0x00000000000004b3 <+1091>:	xor    ecx,r13d
   0x00000000000004b6 <+1094>:	ror    r13d,0x2
   0x00000000000004ba <+1098>:	add    r14d,ecx
   0x00000000000004bd <+1101>:	mov    ecx,DWORD PTR [rsp-0x4]
   0x00000000000004c1 <+1105>:	add    r14d,r12d
   0x00000000000004c4 <+1108>:	xor    ecx,r15d
   0x00000000000004c7 <+1111>:	xor    ecx,DWORD PTR [rsp+0x14]
   0x00000000000004cb <+1115>:	xor    ecx,r8d
   0x00000000000004ce <+1118>:	ror    ecx,0x1f
   0x00000000000004d1 <+1121>:	lea    r12d,[rdx+rcx*1+0x6ed9eba1]
   0x00000000000004d9 <+1129>:	mov    edx,r13d
   0x00000000000004dc <+1132>:	xor    edx,ebx
   0x00000000000004de <+1134>:	xor    edx,ebp
   0x00000000000004e0 <+1136>:	ror    ebp,0x2
   0x00000000000004e3 <+1139>:	add    edx,r12d
   0x00000000000004e6 <+1142>:	mov    r12d,r14d
   0x00000000000004e9 <+1145>:	ror    r12d,0x1b
   0x00000000000004ed <+1149>:	add    r12d,edx
   0x00000000000004f0 <+1152>:	mov    edx,DWORD PTR [rsp]
   0x00000000000004f3 <+1155>:	xor    edx,DWORD PTR [rsp-0x8]
   0x00000000000004f7 <+1159>:	xor    edx,DWORD PTR [rsp+0x18]
   0x00000000000004fb <+1163>:	xor    edx,edi
   0x00000000000004fd <+1165>:	ror    edx,0x1f
   0x0000000000000500 <+1168>:	lea    r15d,[rbx+rdx*1+0x6ed9eba1]
   0x0000000000000508 <+1176>:	mov    ebx,ebp
   0x000000000000050a <+1178>:	xor    ebx,r13d
   0x000000000000050d <+1181>:	xor    ebx,r14d
   0x0000000000000510 <+1184>:	ror    r14d,0x2
   0x0000000000000514 <+1188>:	add    ebx,r15d
   0x0000000000000517 <+1191>:	mov    r15d,r12d
   0x000000000000051a <+1194>:	ror    r15d,0x1b
   0x000000000000051e <+1198>:	add    ebx,r15d
   0x0000000000000521 <+1201>:	mov    r15d,DWORD PTR [rsp+0x4]
   0x0000000000000526 <+1206>:	xor    r15d,DWORD PTR [rsp-0x4]
   0x000000000000052b <+1211>:	mov    DWORD PTR [rsp-0x78],r15d
   0x0000000000000530 <+1216>:	xor    DWORD PTR [rsp-0x78],r11d
   0x0000000000000535 <+1221>:	xor    DWORD PTR [rsp-0x78],esi
   0x0000000000000539 <+1225>:	ror    DWORD PTR [rsp-0x78],0x1f
   0x000000000000053e <+1230>:	mov    r15d,DWORD PTR [rsp-0x78]
   0x0000000000000543 <+1235>:	lea    r15d,[r13+r15*1+0x6ed9eba1]
   0x000000000000054b <+1243>:	mov    r13d,r14d
   0x000000000000054e <+1246>:	xor    r13d,ebp
   0x0000000000000551 <+1249>:	xor    r13d,r12d
   0x0000000000000554 <+1252>:	ror    r12d,0x2
   0x0000000000000558 <+1256>:	add    r13d,r15d
   0x000000000000055b <+1259>:	mov    r15d,ebx
   0x000000000000055e <+1262>:	ror    r15d,0x1b
   0x0000000000000562 <+1266>:	add    r13d,r15d
   0x0000000000000565 <+1269>:	mov    r15d,DWORD PTR [rsp+0x8]
   0x000000000000056a <+1274>:	xor    r15d,DWORD PTR [rsp]
   0x000000000000056e <+1278>:	mov    DWORD PTR [rsp-0x74],r15d
   0x0000000000000573 <+1283>:	xor    DWORD PTR [rsp-0x74],r10d
   0x0000000000000578 <+1288>:	xor    DWORD PTR [rsp-0x74],ecx
   0x000000000000057c <+1292>:	ror    DWORD PTR [rsp-0x74],0x1f
   0x0000000000000581 <+1297>:	mov    r15d,DWORD PTR [rsp-0x74]
   0x0000000000000586 <+1302>:	lea    r15d,[rbp+r15*1+0x6ed9eba1]
   0x000000000000058e <+1310>:	mov    ebp,r12d
   0x0000000000000591 <+1313>:	xor    ebp,r14d
   0x0000000000000594 <+1316>:	xor    ebp,ebx
   0x0000000000000596 <+1318>:	ror    ebx,0x2
   0x0000000000000599 <+1321>:	add    ebp,r15d
   0x000000000000059c <+1324>:	mov    r15d,r13d
   0x000000000000059f <+1327>:	ror    r15d,0x1b
   0x00000000000005a3 <+1331>:	add    ebp,r15d
   0x00000000000005a6 <+1334>:	mov    r15d,DWORD PTR [rsp+0xc]
   0x00000000000005ab <+1339>:	xor    r15d,DWORD PTR [rsp+0x4]
   0x00000000000005b0 <+1344>:	mov    DWORD PTR [rsp-0x70],r15d
   0x00000000000005b5 <+1349>:	xor    DWORD PTR [rsp-0x70],r9d
   0x00000000000005ba <+1354>:	xor    DWORD PTR [rsp-0x70],edx
   0x00000000000005be <+1358>:	ror    DWORD PTR [rsp-0x70],0x1f
   0x00000000000005c3 <+1363>:	mov    r15d,DWORD PTR [rsp-0x70]
   0x00000000000005c8 <+1368>:	lea    r15d,[r14+r15*1+0x6ed9eba1]
   0x00000000000005d0 <+1376>:	mov    r14d,ebx
   0x00000000000005d3 <+1379>:	xor    r14d,r12d
   0x00000000000005d6 <+1382>:	xor    r14d,r13d
   0x00000000000005d9 <+1385>:	ror    r13d,0x2
   0x00000000000005dd <+1389>:	add    r14d,r15d
   0x00000000000005e0 <+1392>:	mov    r15d,ebp
   0x00000000000005e3 <+1395>:	ror    r15d,0x1b
   0x00000000000005e7 <+1399>:	add    r14d,r15d
   0x00000000000005ea <+1402>:	mov    r15d,DWORD PTR [rsp+0x10]
   0x00000000000005ef <+1407>:	xor    r15d,DWORD PTR [rsp+0x8]
   0x00000000000005f4 <+1412>:	mov    DWORD PTR [rsp-0x6c],r15d
   0x00000000000005f9 <+1417>:	mov    r15d,DWORD PTR [rsp-0x78]
   0x00000000000005fe <+1422>:	xor    DWORD PTR [rsp-0x6c],r8d
   0x0000000000000603 <+1427>:	xor    DWORD PTR [rsp-0x6c],r15d
   0x0000000000000608 <+1432>:	ror    DWORD PTR [rsp-0x6c],0x1f
   0x000000000000060d <+1437>:	mov    r15d,DWORD PTR [rsp-0x6c]
   0x0000000000000612 <+1442>:	lea    r15d,[r12+r15*1+0x6ed9eba1]
   0x000000000000061a <+1450>:	mov    r12d,r13d
   0x000000000000061d <+1453>:	xor    r12d,ebx
   0x0000000000000620 <+1456>:	xor    r12d,ebp
   0x0000000000000623 <+1459>:	ror    ebp,0x2
   0x0000000000000626 <+1462>:	add    r12d,r15d
   0x0000000000000629 <+1465>:	mov    r15d,r14d
   0x000000000000062c <+1468>:	ror    r15d,0x1b
   0x0000000000000630 <+1472>:	add    r12d,r15d
   0x0000000000000633 <+1475>:	mov    r15d,DWORD PTR [rsp+0x14]
   0x0000000000000638 <+1480>:	xor    r15d,DWORD PTR [rsp+0xc]
   0x000000000000063d <+1485>:	mov    DWORD PTR [rsp-0x68],r15d
   0x0000000000000642 <+1490>:	xor    DWORD PTR [rsp-0x68],edi
   0x0000000000000646 <+1494>:	mov    r15d,DWORD PTR [rsp-0x74]
   0x000000000000064b <+1499>:	xor    DWORD PTR [rsp-0x68],r15d
   0x0000000000000650 <+1504>:	ror    DWORD PTR [rsp-0x68],0x1f
   0x0000000000000655 <+1509>:	mov    r15d,DWORD PTR [rsp-0x68]
   0x000000000000065a <+1514>:	lea    r15d,[rbx+r15*1+0x6ed9eba1]
   0x0000000000000662 <+1522>:	mov    ebx,ebp
   0x0000000000000664 <+1524>:	xor    ebx,r13d
   0x0000000000000667 <+1527>:	xor    ebx,r14d
   0x000000000000066a <+1530>:	ror    r14d,0x2
   0x000000000000066e <+1534>:	add    ebx,r15d
   0x0000000000000671 <+1537>:	mov    r15d,r12d
   0x0000000000000674 <+1540>:	ror    r15d,0x1b
   0x0000000000000678 <+1544>:	add    ebx,r15d
   0x000000000000067b <+1547>:	mov    r15d,DWORD PTR [rsp+0x18]
   0x0000000000000680 <+1552>:	xor    r15d,DWORD PTR [rsp+0x10]
   0x0000000000000685 <+1557>:	mov    DWORD PTR [rsp-0x64],r15d
   0x000000000000068a <+1562>:	xor    DWORD PTR [rsp-0x64],esi
   0x000000000000068e <+1566>:	mov    r15d,DWORD PTR [rsp-0x70]
   0x0000000000000693 <+1571>:	xor    DWORD PTR [rsp-0x64],r15d
   0x0000000000000698 <+1576>:	ror    DWORD PTR [rsp-0x64],0x1f
   0x000000000000069d <+1581>:	mov    r15d,DWORD PTR [rsp-0x64]
   0x00000000000006a2 <+1586>:	lea    r15d,[r13+r15*1+0x6ed9eba1]
   0x00000000000006aa <+1594>:	mov    r13d,r14d
   0x00000000000006ad <+1597>:	xor    r13d,ebp
   0x00000000000006b0 <+1600>:	xor    r13d,r12d
   0x00000000000006b3 <+1603>:	ror    r12d,0x2
   0x00000000000006b7 <+1607>:	add    r13d,r15d
   0x00000000000006ba <+1610>:	mov    r15d,ebx
   0x00000000000006bd <+1613>:	ror    r15d,0x1b
   0x00000000000006c1 <+1617>:	add    r13d,r15d
   0x00000000000006c4 <+1620>:	mov    r15d,DWORD PTR [rsp+0x14]
   0x00000000000006c9 <+1625>:	xor    r15d,r11d
   0x00000000000006cc <+1628>:	mov    DWORD PTR [rsp-0x60],r15d
   0x00000000000006d1 <+1633>:	xor    DWORD PTR [rsp-0x60],ecx
   0x00000000000006d5 <+1637>:	mov    r15d,DWORD PTR [rsp-0x6c]
   0x00000000000006da <+1642>:	xor    DWORD PTR [rsp-0x60],r15d
   0x00000000000006df <+1647>:	ror    DWORD PTR [rsp-0x60],0x1f
   0x00000000000006e4 <+1652>:	mov    r15d,DWORD PTR [rsp-0x60]
   0x00000000000006e9 <+1657>:	lea    r15d,[rbp+r15*1+0x6ed9eba1]
   0x00000000000006f1 <+1665>:	mov    ebp,r12d
   0x00000000000006f4 <+1668>:	xor    ebp,r14d
   0x00000000000006f7 <+1671>:	xor    ebp,ebx
   0x00000000000006f9 <+1673>:	add    ebp,r15d
   0x00000000000006fc <+1676>:	mov    r15d,r13d
   0x00000000000006ff <+1679>:	ror    r15d,0x1b
   0x0000000000000703 <+1683>:	ror    ebx,0x2
   0x0000000000000706 <+1686>:	xor    r11d,r9d
   0x0000000000000709 <+1689>:	add    ebp,r15d
   0x000000000000070c <+1692>:	mov    r15d,DWORD PTR [rsp+0x18]
   0x0000000000000711 <+1697>:	xor    r15d,r10d
   0x0000000000000714 <+1700>:	mov    DWORD PTR [rsp-0x5c],r15d
   0x0000000000000719 <+1705>:	xor    DWORD PTR [rsp-0x5c],edx
   0x000000000000071d <+1709>:	mov    r15d,DWORD PTR [rsp-0x68]
   0x0000000000000722 <+1714>:	xor    DWORD PTR [rsp-0x5c],r15d
   0x0000000000000727 <+1719>:	ror    DWORD PTR [rsp-0x5c],0x1f
   0x000000000000072c <+1724>:	mov    r15d,DWORD PTR [rsp-0x5c]
   0x0000000000000731 <+1729>:	lea    r15d,[r14+r15*1+0x6ed9eba1]
   0x0000000000000739 <+1737>:	mov    r14d,ebx
   0x000000000000073c <+1740>:	xor    r14d,r12d
   0x000000000000073f <+1743>:	xor    r14d,r13d
   0x0000000000000742 <+1746>:	ror    r13d,0x2
   0x0000000000000746 <+1750>:	add    r14d,r15d
   0x0000000000000749 <+1753>:	mov    r15d,ebp
   0x000000000000074c <+1756>:	ror    r15d,0x1b
   0x0000000000000750 <+1760>:	add    r14d,r15d
   0x0000000000000753 <+1763>:	mov    r15d,DWORD PTR [rsp-0x78]
   0x0000000000000758 <+1768>:	xor    r15d,r11d
   0x000000000000075b <+1771>:	xor    r15d,DWORD PTR [rsp-0x64]
   0x0000000000000760 <+1776>:	mov    r11d,r13d
   0x0000000000000763 <+1779>:	xor    r11d,ebx
   0x0000000000000766 <+1782>:	xor    r11d,ebp
   0x0000000000000769 <+1785>:	ror    ebp,0x2
   0x000000000000076c <+1788>:	ror    r15d,0x1f
   0x0000000000000770 <+1792>:	lea    r12d,[r12+r15*1+0x6ed9eba1]
   0x0000000000000778 <+1800>:	add    r11d,r12d
   0x000000000000077b <+1803>:	mov    r12d,r14d
   0x000000000000077e <+1806>:	ror    r12d,0x1b
   0x0000000000000782 <+1810>:	add    r11d,r12d
   0x0000000000000785 <+1813>:	mov    r12d,r10d
   0x0000000000000788 <+1816>:	mov    r10d,ebp
   0x000000000000078b <+1819>:	xor    r12d,r8d
   0x000000000000078e <+1822>:	xor    r12d,DWORD PTR [rsp-0x74]
   0x0000000000000793 <+1827>:	xor    r10d,r13d
   0x0000000000000796 <+1830>:	xor    r12d,DWORD PTR [rsp-0x60]
   0x000000000000079b <+1835>:	xor    r10d,r14d
   0x000000000000079e <+1838>:	ror    r14d,0x2
   0x00000000000007a2 <+1842>:	ror    r12d,0x1f
   0x00000000000007a6 <+1846>:	lea    ebx,[rbx+r12*1+0x6ed9eba1]
   0x00000000000007ae <+1854>:	add    r10d,ebx
   0x00000000000007b1 <+1857>:	mov    ebx,r11d
   0x00000000000007b4 <+1860>:	ror    ebx,0x1b
   0x00000000000007b7 <+1863>:	add    r10d,ebx
   0x00000000000007ba <+1866>:	xor    r9d,edi
   0x00000000000007bd <+1869>:	mov    ebx,DWORD PTR [rsp-0x70]
   0x00000000000007c1 <+1873>:	mov    DWORD PTR [rsp-0x58],r9d
   0x00000000000007c6 <+1878>:	xor    DWORD PTR [rsp-0x58],ebx
   0x00000000000007ca <+1882>:	mov    r9d,DWORD PTR [rsp-0x5c]
   0x00000000000007cf <+1887>:	xor    DWORD PTR [rsp-0x58],r9d
   0x00000000000007d4 <+1892>:	mov    r9d,r14d
   0x00000000000007d7 <+1895>:	ror    DWORD PTR [rsp-0x58],0x1f
   0x00000000000007dc <+1900>:	xor    r9d,ebp
   0x00000000000007df <+1903>:	mov    ebx,DWORD PTR [rsp-0x58]
   0x00000000000007e3 <+1907>:	xor    r9d,r11d
   0x00000000000007e6 <+1910>:	ror    r11d,0x2
   0x00000000000007ea <+1914>:	lea    ebx,[r13+rbx*1+0x6ed9eba1]
   0x00000000000007f2 <+1922>:	mov    r13d,r10d
   0x00000000000007f5 <+1925>:	ror    r13d,0x1b
   0x00000000000007f9 <+1929>:	add    r9d,ebx
   0x00000000000007fc <+1932>:	add    r9d,r13d
   0x00000000000007ff <+1935>:	mov    r13d,r8d
   0x0000000000000802 <+1938>:	mov    r8d,r11d
   0x0000000000000805 <+1941>:	xor    r13d,esi
   0x0000000000000808 <+1944>:	xor    r13d,DWORD PTR [rsp-0x6c]
   0x000000000000080d <+1949>:	xor    r8d,r14d
   0x0000000000000810 <+1952>:	xor    r8d,r10d
   0x0000000000000813 <+1955>:	ror    r10d,0x2
   0x0000000000000817 <+1959>:	xor    esi,edx
   0x0000000000000819 <+1961>:	xor    r13d,r15d
   0x000000000000081c <+1964>:	ror    r13d,0x1f
   0x0000000000000820 <+1968>:	lea    ebx,[rbp+r13*1+0x6ed9eba1]
   0x0000000000000828 <+1976>:	mov    ebp,r9d
   0x000000000000082b <+1979>:	ror    ebp,0x1b
   0x000000000000082e <+1982>:	add    r8d,ebx
   0x0000000000000831 <+1985>:	add    r8d,ebp
   0x0000000000000834 <+1988>:	mov    ebp,edi
   0x0000000000000836 <+1990>:	mov    edi,r10d
   0x0000000000000839 <+1993>:	xor    ebp,ecx
   0x000000000000083b <+1995>:	xor    ebp,DWORD PTR [rsp-0x68]
   0x000000000000083f <+1999>:	xor    edi,r11d
   0x0000000000000842 <+2002>:	xor    edi,r9d
   0x0000000000000845 <+2005>:	ror    r9d,0x2
   0x0000000000000849 <+2009>:	xor    ebp,r12d
   0x000000000000084c <+2012>:	ror    ebp,0x1f
   0x000000000000084f <+2015>:	lea    ebx,[r14+rbp*1+0x6ed9eba1]
   0x0000000000000857 <+2023>:	add    edi,ebx
   0x0000000000000859 <+2025>:	mov    ebx,r8d
   0x000000000000085c <+2028>:	ror    ebx,0x1b
   0x000000000000085f <+2031>:	add    edi,ebx
   0x0000000000000861 <+2033>:	mov    ebx,DWORD PTR [rsp-0x64]
   0x0000000000000865 <+2037>:	xor    ebx,esi
   0x0000000000000867 <+2039>:	xor    ebx,DWORD PTR [rsp-0x58]
   0x000000000000086b <+2043>:	mov    esi,r9d
   0x000000000000086e <+2046>:	ror    ebx,0x1f
   0x0000000000000871 <+2049>:	xor    esi,r10d
   0x0000000000000874 <+2052>:	xor    ecx,DWORD PTR [rsp-0x78]
   0x0000000000000878 <+2056>:	lea    r11d,[r11+rbx*1+0x6ed9eba1]
   0x0000000000000880 <+2064>:	xor    esi,r8d
   0x0000000000000883 <+2067>:	ror    r8d,0x2
   0x0000000000000887 <+2071>:	xor    edx,DWORD PTR [rsp-0x74]
   0x000000000000088b <+2075>:	add    esi,r11d
   0x000000000000088e <+2078>:	mov    r11d,edi
   0x0000000000000891 <+2081>:	ror    r11d,0x1b
   0x0000000000000895 <+2085>:	add    esi,r11d
   0x0000000000000898 <+2088>:	mov    r11d,DWORD PTR [rsp-0x60]
   0x000000000000089d <+2093>:	mov    r14d,esi
   0x00000000000008a0 <+2096>:	ror    r14d,0x1b
   0x00000000000008a4 <+2100>:	xor    r11d,ecx
   0x00000000000008a7 <+2103>:	mov    ecx,r8d
   0x00000000000008aa <+2106>:	xor    r11d,r13d
   0x00000000000008ad <+2109>:	xor    ecx,r9d
   0x00000000000008b0 <+2112>:	ror    r11d,0x1f
   0x00000000000008b4 <+2116>:	xor    ecx,edi
   0x00000000000008b6 <+2118>:	ror    edi,0x2
   0x00000000000008b9 <+2121>:	lea    r10d,[r10+r11*1+0x6ed9eba1]
   0x00000000000008c1 <+2129>:	add    ecx,r10d
   0x00000000000008c4 <+2132>:	add    ecx,r14d
   0x00000000000008c7 <+2135>:	mov    r14d,DWORD PTR [rsp-0x5c]
   0x00000000000008cc <+2140>:	mov    r10d,ecx
   0x00000000000008cf <+2143>:	xor    r14d,edx
   0x00000000000008d2 <+2146>:	mov    edx,edi
   0x00000000000008d4 <+2148>:	xor    r14d,ebp
   0x00000000000008d7 <+2151>:	xor    edx,r8d
   0x00000000000008da <+2154>:	ror    r14d,0x1f
   0x00000000000008de <+2158>:	xor    edx,esi
   0x00000000000008e0 <+2160>:	ror    esi,0x2
   0x00000000000008e3 <+2163>:	lea    r9d,[r9+r14*1+0x6ed9eba1]
   0x00000000000008eb <+2171>:	add    edx,r9d
   0x00000000000008ee <+2174>:	mov    r9d,ecx
   0x00000000000008f1 <+2177>:	ror    r9d,0x1b
   0x00000000000008f5 <+2181>:	add    r9d,edx
   0x00000000000008f8 <+2184>:	mov    edx,DWORD PTR [rsp-0x78]
   0x00000000000008fc <+2188>:	xor    edx,DWORD PTR [rsp-0x70]
   0x0000000000000900 <+2192>:	mov    DWORD PTR [rsp-0x54],edx
   0x0000000000000904 <+2196>:	xor    DWORD PTR [rsp-0x54],r15d
   0x0000000000000909 <+2201>:	xor    DWORD PTR [rsp-0x54],ebx
   0x000000000000090d <+2205>:	ror    DWORD PTR [rsp-0x54],0x1f
   0x0000000000000912 <+2210>:	mov    edx,DWORD PTR [rsp-0x54]
   0x0000000000000916 <+2214>:	lea    r8d,[r8+rdx*1-0x70e44324]
   0x000000000000091e <+2222>:	mov    edx,r9d
   0x0000000000000921 <+2225>:	ror    edx,0x1b
   0x0000000000000924 <+2228>:	add    r8d,edx
   0x0000000000000927 <+2231>:	mov    edx,ecx
   0x0000000000000929 <+2233>:	or     edx,esi
   0x000000000000092b <+2235>:	and    r10d,esi
   0x000000000000092e <+2238>:	ror    ecx,0x2
   0x0000000000000931 <+2241>:	and    edx,edi
   0x0000000000000933 <+2243>:	or     edx,r10d
   0x0000000000000936 <+2246>:	mov    r10d,DWORD PTR [rsp-0x74]
   0x000000000000093b <+2251>:	xor    r10d,DWORD PTR [rsp-0x6c]
   0x0000000000000940 <+2256>:	add    edx,r8d
   0x0000000000000943 <+2259>:	mov    DWORD PTR [rsp-0x74],r10d
   0x0000000000000948 <+2264>:	xor    DWORD PTR [rsp-0x74],r12d
   0x000000000000094d <+2269>:	mov    r10d,r9d
   0x0000000000000950 <+2272>:	xor    DWORD PTR [rsp-0x74],r11d
   0x0000000000000955 <+2277>:	and    r10d,ecx
   0x0000000000000958 <+2280>:	ror    DWORD PTR [rsp-0x74],0x1f
   0x000000000000095d <+2285>:	mov    r8d,DWORD PTR [rsp-0x74]
   0x0000000000000962 <+2290>:	lea    r8d,[rdi+r8*1-0x70e44324]
   0x000000000000096a <+2298>:	mov    edi,r9d
   0x000000000000096d <+2301>:	ror    r9d,0x2
   0x0000000000000971 <+2305>:	or     edi,ecx
   0x0000000000000973 <+2307>:	and    edi,esi
   0x0000000000000975 <+2309>:	or     edi,r10d
   0x0000000000000978 <+2312>:	mov    r10d,DWORD PTR [rsp-0x70]
   0x000000000000097d <+2317>:	xor    r10d,DWORD PTR [rsp-0x68]
   0x0000000000000982 <+2322>:	add    edi,r8d
   0x0000000000000985 <+2325>:	mov    r8d,edx
   0x0000000000000988 <+2328>:	ror    r8d,0x1b
   0x000000000000098c <+2332>:	add    edi,r8d
   0x000000000000098f <+2335>:	mov    r8d,DWORD PTR [rsp-0x58]
   0x0000000000000994 <+2340>:	mov    DWORD PTR [rsp-0x70],r10d
   0x0000000000000999 <+2345>:	xor    DWORD PTR [rsp-0x70],r8d
   0x000000000000099e <+2350>:	mov    r10d,edx
   0x00000000000009a1 <+2353>:	xor    DWORD PTR [rsp-0x70],r14d
   0x00000000000009a6 <+2358>:	and    r10d,r9d
   0x00000000000009a9 <+2361>:	ror    DWORD PTR [rsp-0x70],0x1f
   0x00000000000009ae <+2366>:	mov    r8d,DWORD PTR [rsp-0x70]
   0x00000000000009b3 <+2371>:	lea    r8d,[rsi+r8*1-0x70e44324]
   0x00000000000009bb <+2379>:	mov    esi,edi
   0x00000000000009bd <+2381>:	ror    esi,0x1b
   0x00000000000009c0 <+2384>:	add    r8d,esi
   0x00000000000009c3 <+2387>:	mov    esi,edx
   0x00000000000009c5 <+2389>:	ror    edx,0x2
   0x00000000000009c8 <+2392>:	or     esi,r9d
   0x00000000000009cb <+2395>:	and    esi,ecx
   0x00000000000009cd <+2397>:	or     esi,r10d
   0x00000000000009d0 <+2400>:	mov    r10d,DWORD PTR [rsp-0x6c]
   0x00000000000009d5 <+2405>:	xor    r10d,DWORD PTR [rsp-0x64]
   0x00000000000009da <+2410>:	add    esi,r8d
   0x00000000000009dd <+2413>:	mov    r8d,DWORD PTR [rsp-0x54]
   0x00000000000009e2 <+2418>:	mov    DWORD PTR [rsp-0x6c],r10d
   0x00000000000009e7 <+2423>:	xor    DWORD PTR [rsp-0x6c],r13d
   0x00000000000009ec <+2428>:	xor    DWORD PTR [rsp-0x6c],r8d
   0x00000000000009f1 <+2433>:	ror    DWORD PTR [rsp-0x6c],0x1f
   0x00000000000009f6 <+2438>:	mov    r10d,DWORD PTR [rsp-0x6c]
   0x00000000000009fb <+2443>:	lea    r8d,[rcx+r10*1-0x70e44324]
   0x0000000000000a03 <+2451>:	mov    ecx,edi
   0x0000000000000a05 <+2453>:	mov    r10d,edi
   0x0000000000000a08 <+2456>:	or     ecx,edx
   0x0000000000000a0a <+2458>:	and    r10d,edx
   0x0000000000000a0d <+2461>:	ror    edi,0x2
   0x0000000000000a10 <+2464>:	and    ecx,r9d
   0x0000000000000a13 <+2467>:	or     ecx,r10d
   0x0000000000000a16 <+2470>:	mov    r10d,esi
   0x0000000000000a19 <+2473>:	add    ecx,r8d
   0x0000000000000a1c <+2476>:	ror    r10d,0x1b
   0x0000000000000a20 <+2480>:	add    ecx,r10d
   0x0000000000000a23 <+2483>:	mov    r10d,DWORD PTR [rsp-0x68]
   0x0000000000000a28 <+2488>:	xor    r10d,DWORD PTR [rsp-0x60]
   0x0000000000000a2d <+2493>:	mov    DWORD PTR [rsp-0x68],r10d
   0x0000000000000a32 <+2498>:	xor    DWORD PTR [rsp-0x68],ebp
   0x0000000000000a36 <+2502>:	mov    r10d,DWORD PTR [rsp-0x74]
   0x0000000000000a3b <+2507>:	xor    DWORD PTR [rsp-0x68],r10d
   0x0000000000000a40 <+2512>:	mov    r10d,esi
   0x0000000000000a43 <+2515>:	ror    DWORD PTR [rsp-0x68],0x1f
   0x0000000000000a48 <+2520>:	and    r10d,edi
   0x0000000000000a4b <+2523>:	mov    r8d,DWORD PTR [rsp-0x68]
   0x0000000000000a50 <+2528>:	lea    r9d,[r9+r8*1-0x70e44324]
   0x0000000000000a58 <+2536>:	mov    r8d,ecx
   0x0000000000000a5b <+2539>:	ror    r8d,0x1b
   0x0000000000000a5f <+2543>:	add    r8d,r9d
   0x0000000000000a62 <+2546>:	mov    r9d,esi
   0x0000000000000a65 <+2549>:	ror    esi,0x2
   0x0000000000000a68 <+2552>:	or     r9d,edi
   0x0000000000000a6b <+2555>:	and    r9d,edx
   0x0000000000000a6e <+2558>:	or     r9d,r10d
   0x0000000000000a71 <+2561>:	mov    r10d,DWORD PTR [rsp-0x64]
   0x0000000000000a76 <+2566>:	xor    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000a7b <+2571>:	add    r9d,r8d
   0x0000000000000a7e <+2574>:	mov    r8d,DWORD PTR [rsp-0x70]
   0x0000000000000a83 <+2579>:	mov    DWORD PTR [rsp-0x64],r10d
   0x0000000000000a88 <+2584>:	xor    DWORD PTR [rsp-0x64],ebx
   0x0000000000000a8c <+2588>:	xor    DWORD PTR [rsp-0x64],r8d
   0x0000000000000a91 <+2593>:	ror    DWORD PTR [rsp-0x64],0x1f
   0x0000000000000a96 <+2598>:	mov    r10d,DWORD PTR [rsp-0x64]
   0x0000000000000a9b <+2603>:	lea    r8d,[rdx+r10*1-0x70e44324]
   0x0000000000000aa3 <+2611>:	mov    edx,ecx
   0x0000000000000aa5 <+2613>:	mov    r10d,ecx
   0x0000000000000aa8 <+2616>:	or     edx,esi
   0x0000000000000aaa <+2618>:	and    r10d,esi
   0x0000000000000aad <+2621>:	ror    ecx,0x2
   0x0000000000000ab0 <+2624>:	and    edx,edi
   0x0000000000000ab2 <+2626>:	or     edx,r10d
   0x0000000000000ab5 <+2629>:	mov    r10d,r9d
   0x0000000000000ab8 <+2632>:	add    edx,r8d
   0x0000000000000abb <+2635>:	ror    r10d,0x1b
   0x0000000000000abf <+2639>:	add    edx,r10d
   0x0000000000000ac2 <+2642>:	mov    r10d,DWORD PTR [rsp-0x60]
   0x0000000000000ac7 <+2647>:	xor    r10d,r15d
   0x0000000000000aca <+2650>:	mov    DWORD PTR [rsp-0x78],r10d
   0x0000000000000acf <+2655>:	xor    DWORD PTR [rsp-0x78],r11d
   0x0000000000000ad4 <+2660>:	mov    r10d,DWORD PTR [rsp-0x6c]
   0x0000000000000ad9 <+2665>:	xor    DWORD PTR [rsp-0x78],r10d
   0x0000000000000ade <+2670>:	ror    DWORD PTR [rsp-0x78],0x1f
   0x0000000000000ae3 <+2675>:	mov    r10d,DWORD PTR [rsp-0x78]
   0x0000000000000ae8 <+2680>:	xor    r15d,DWORD PTR [rsp-0x58]
   0x0000000000000aed <+2685>:	lea    r8d,[rdi+r10*1-0x70e44324]
   0x0000000000000af5 <+2693>:	mov    edi,edx
   0x0000000000000af7 <+2695>:	mov    r10d,r9d
   0x0000000000000afa <+2698>:	ror    edi,0x1b
   0x0000000000000afd <+2701>:	and    r10d,ecx
   0x0000000000000b00 <+2704>:	xor    r15d,DWORD PTR [rsp-0x54]
   0x0000000000000b05 <+2709>:	add    r8d,edi
   0x0000000000000b08 <+2712>:	mov    edi,r9d
   0x0000000000000b0b <+2715>:	ror    r9d,0x2
   0x0000000000000b0f <+2719>:	or     edi,ecx
   0x0000000000000b11 <+2721>:	xor    r15d,DWORD PTR [rsp-0x64]
   0x0000000000000b16 <+2726>:	and    edi,esi
   0x0000000000000b18 <+2728>:	or     edi,r10d
   0x0000000000000b1b <+2731>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000b20 <+2736>:	add    edi,r8d
   0x0000000000000b23 <+2739>:	ror    r15d,0x1f
   0x0000000000000b27 <+2743>:	xor    r10d,r12d
   0x0000000000000b2a <+2746>:	mov    DWORD PTR [rsp-0x60],r10d
   0x0000000000000b2f <+2751>:	xor    DWORD PTR [rsp-0x60],r14d
   0x0000000000000b34 <+2756>:	mov    r10d,DWORD PTR [rsp-0x68]
   0x0000000000000b39 <+2761>:	xor    DWORD PTR [rsp-0x60],r10d
   0x0000000000000b3e <+2766>:	mov    r10d,edx
   0x0000000000000b41 <+2769>:	ror    DWORD PTR [rsp-0x60],0x1f
   0x0000000000000b46 <+2774>:	and    r10d,r9d
   0x0000000000000b49 <+2777>:	mov    r8d,DWORD PTR [rsp-0x60]
   0x0000000000000b4e <+2782>:	lea    r8d,[rsi+r8*1-0x70e44324]
   0x0000000000000b56 <+2790>:	mov    esi,edx
   0x0000000000000b58 <+2792>:	ror    edx,0x2
   0x0000000000000b5b <+2795>:	or     esi,r9d
   0x0000000000000b5e <+2798>:	and    esi,ecx
   0x0000000000000b60 <+2800>:	or     esi,r10d
   0x0000000000000b63 <+2803>:	mov    r10d,edi
   0x0000000000000b66 <+2806>:	add    esi,r8d
   0x0000000000000b69 <+2809>:	ror    r10d,0x1b
   0x0000000000000b6d <+2813>:	lea    r8d,[rcx+r15*1-0x70e44324]
   0x0000000000000b75 <+2821>:	add    esi,r10d
   0x0000000000000b78 <+2824>:	mov    r10d,edi
   0x0000000000000b7b <+2827>:	mov    ecx,esi
   0x0000000000000b7d <+2829>:	and    r10d,edx
   0x0000000000000b80 <+2832>:	ror    ecx,0x1b
   0x0000000000000b83 <+2835>:	add    r8d,ecx
   0x0000000000000b86 <+2838>:	mov    ecx,edi
   0x0000000000000b88 <+2840>:	or     ecx,edx
   0x0000000000000b8a <+2842>:	and    ecx,r9d
   0x0000000000000b8d <+2845>:	or     ecx,r10d
   0x0000000000000b90 <+2848>:	xor    r12d,r13d
   0x0000000000000b93 <+2851>:	xor    r12d,DWORD PTR [rsp-0x74]
   0x0000000000000b98 <+2856>:	xor    r12d,DWORD PTR [rsp-0x78]
   0x0000000000000b9d <+2861>:	add    ecx,r8d
   0x0000000000000ba0 <+2864>:	ror    edi,0x2
   0x0000000000000ba3 <+2867>:	mov    r10d,esi
   0x0000000000000ba6 <+2870>:	xor    r13d,ebx
   0x0000000000000ba9 <+2873>:	xor    r13d,DWORD PTR [rsp-0x6c]
   0x0000000000000bae <+2878>:	and    r10d,edi
   0x0000000000000bb1 <+2881>:	ror    r12d,0x1f
   0x0000000000000bb5 <+2885>:	lea    r8d,[r9+r12*1-0x70e44324]
   0x0000000000000bbd <+2893>:	mov    r9d,esi
   0x0000000000000bc0 <+2896>:	ror    esi,0x2
   0x0000000000000bc3 <+2899>:	or     r9d,edi
   0x0000000000000bc6 <+2902>:	xor    r13d,r15d
   0x0000000000000bc9 <+2905>:	and    r9d,edx
   0x0000000000000bcc <+2908>:	ror    r13d,0x1f
   0x0000000000000bd0 <+2912>:	or     r9d,r10d
   0x0000000000000bd3 <+2915>:	mov    r10d,ecx
   0x0000000000000bd6 <+2918>:	add    r9d,r8d
   0x0000000000000bd9 <+2921>:	mov    r8d,DWORD PTR [rsp-0x58]
   0x0000000000000bde <+2926>:	ror    r10d,0x1b
   0x0000000000000be2 <+2930>:	add    r9d,r10d
   0x0000000000000be5 <+2933>:	xor    r8d,ebp
   0x0000000000000be8 <+2936>:	mov    DWORD PTR [rsp-0x5c],r8d
   0x0000000000000bed <+2941>:	mov    r8d,DWORD PTR [rsp-0x70]
   0x0000000000000bf2 <+2946>:	xor    DWORD PTR [rsp-0x5c],r8d
   0x0000000000000bf7 <+2951>:	mov    r8d,DWORD PTR [rsp-0x60]
   0x0000000000000bfc <+2956>:	xor    DWORD PTR [rsp-0x5c],r8d
   0x0000000000000c01 <+2961>:	ror    DWORD PTR [rsp-0x5c],0x1f
   0x0000000000000c06 <+2966>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000c0b <+2971>:	lea    r8d,[rdx+r10*1-0x70e44324]
   0x0000000000000c13 <+2979>:	mov    edx,r9d
   0x0000000000000c16 <+2982>:	mov    r10d,ecx
   0x0000000000000c19 <+2985>:	ror    edx,0x1b
   0x0000000000000c1c <+2988>:	and    r10d,esi
   0x0000000000000c1f <+2991>:	add    r8d,edx
   0x0000000000000c22 <+2994>:	mov    edx,ecx
   0x0000000000000c24 <+2996>:	ror    ecx,0x2
   0x0000000000000c27 <+2999>:	or     edx,esi
   0x0000000000000c29 <+3001>:	and    edx,edi
   0x0000000000000c2b <+3003>:	or     edx,r10d
   0x0000000000000c2e <+3006>:	mov    r10d,r9d
   0x0000000000000c31 <+3009>:	add    edx,r8d
   0x0000000000000c34 <+3012>:	lea    r8d,[rdi+r13*1-0x70e44324]
   0x0000000000000c3c <+3020>:	mov    edi,r9d
   0x0000000000000c3f <+3023>:	or     edi,ecx
   0x0000000000000c41 <+3025>:	and    edi,esi
   0x0000000000000c43 <+3027>:	and    r10d,ecx
   0x0000000000000c46 <+3030>:	xor    ebp,r11d
   0x0000000000000c49 <+3033>:	xor    ebp,DWORD PTR [rsp-0x68]
   0x0000000000000c4d <+3037>:	or     edi,r10d
   0x0000000000000c50 <+3040>:	mov    r10d,edx
   0x0000000000000c53 <+3043>:	add    edi,r8d
   0x0000000000000c56 <+3046>:	ror    r10d,0x1b
   0x0000000000000c5a <+3050>:	ror    r9d,0x2
   0x0000000000000c5e <+3054>:	add    edi,r10d
   0x0000000000000c61 <+3057>:	mov    r10d,edx
   0x0000000000000c64 <+3060>:	xor    ebx,r14d
   0x0000000000000c67 <+3063>:	and    r10d,r9d
   0x0000000000000c6a <+3066>:	mov    DWORD PTR [rsp-0x50],ebx
   0x0000000000000c6e <+3070>:	mov    ebx,DWORD PTR [rsp-0x64]
   0x0000000000000c72 <+3074>:	xor    ebp,r12d
   0x0000000000000c75 <+3077>:	xor    DWORD PTR [rsp-0x50],ebx
   0x0000000000000c79 <+3081>:	ror    ebp,0x1f
   0x0000000000000c7c <+3084>:	lea    r8d,[rsi+rbp*1-0x70e44324]
   0x0000000000000c84 <+3092>:	mov    esi,edi
   0x0000000000000c86 <+3094>:	ror    esi,0x1b
   0x0000000000000c89 <+3097>:	add    r8d,esi
   0x0000000000000c8c <+3100>:	mov    esi,edx
   0x0000000000000c8e <+3102>:	ror    edx,0x2
   0x0000000000000c91 <+3105>:	or     esi,r9d
   0x0000000000000c94 <+3108>:	and    esi,ecx
   0x0000000000000c96 <+3110>:	or     esi,r10d
   0x0000000000000c99 <+3113>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000c9e <+3118>:	xor    DWORD PTR [rsp-0x50],r10d
   0x0000000000000ca3 <+3123>:	ror    DWORD PTR [rsp-0x50],0x1f
   0x0000000000000ca8 <+3128>:	add    esi,r8d
   0x0000000000000cab <+3131>:	mov    r10d,edi
   0x0000000000000cae <+3134>:	mov    ebx,DWORD PTR [rsp-0x50]
   0x0000000000000cb2 <+3138>:	and    r10d,edx
   0x0000000000000cb5 <+3141>:	lea    r8d,[rcx+rbx*1-0x70e44324]
   0x0000000000000cbd <+3149>:	mov    ecx,edi
   0x0000000000000cbf <+3151>:	mov    ebx,DWORD PTR [rsp-0x54]
   0x0000000000000cc3 <+3155>:	or     ecx,edx
   0x0000000000000cc5 <+3157>:	ror    edi,0x2
   0x0000000000000cc8 <+3160>:	and    ecx,r9d
   0x0000000000000ccb <+3163>:	or     ecx,r10d
   0x0000000000000cce <+3166>:	xor    r11d,ebx
   0x0000000000000cd1 <+3169>:	add    ecx,r8d
   0x0000000000000cd4 <+3172>:	mov    r8d,esi
   0x0000000000000cd7 <+3175>:	mov    DWORD PTR [rsp-0x54],r11d
   0x0000000000000cdc <+3180>:	ror    r8d,0x1b
   0x0000000000000ce0 <+3184>:	add    ecx,r8d
   0x0000000000000ce3 <+3187>:	mov    r8d,DWORD PTR [rsp-0x78]
   0x0000000000000ce8 <+3192>:	xor    DWORD PTR [rsp-0x54],r8d
   0x0000000000000ced <+3197>:	xor    DWORD PTR [rsp-0x54],r13d
   0x0000000000000cf2 <+3202>:	ror    DWORD PTR [rsp-0x54],0x1f
   0x0000000000000cf7 <+3207>:	mov    r11d,DWORD PTR [rsp-0x54]
   0x0000000000000cfc <+3212>:	lea    r9d,[r9+r11*1-0x70e44324]
   0x0000000000000d04 <+3220>:	mov    r11d,ecx
   0x0000000000000d07 <+3223>:	ror    r11d,0x1b
   0x0000000000000d0b <+3227>:	mov    r8d,r11d
   0x0000000000000d0e <+3230>:	mov    r11d,esi
   0x0000000000000d11 <+3233>:	add    r8d,r9d
   0x0000000000000d14 <+3236>:	mov    r9d,esi
   0x0000000000000d17 <+3239>:	and    r11d,edi
   0x0000000000000d1a <+3242>:	or     r9d,edi
   0x0000000000000d1d <+3245>:	ror    esi,0x2
   0x0000000000000d20 <+3248>:	and    r9d,edx
   0x0000000000000d23 <+3251>:	or     r9d,r11d
   0x0000000000000d26 <+3254>:	mov    r11d,DWORD PTR [rsp-0x74]
   0x0000000000000d2b <+3259>:	add    r9d,r8d
   0x0000000000000d2e <+3262>:	mov    r10d,r9d
   0x0000000000000d31 <+3265>:	xor    r14d,r11d
   0x0000000000000d34 <+3268>:	mov    DWORD PTR [rsp-0x74],r14d
   0x0000000000000d39 <+3273>:	mov    r14d,DWORD PTR [rsp-0x60]
   0x0000000000000d3e <+3278>:	xor    DWORD PTR [rsp-0x74],r14d
   0x0000000000000d43 <+3283>:	xor    DWORD PTR [rsp-0x74],ebp
   0x0000000000000d47 <+3287>:	ror    DWORD PTR [rsp-0x74],0x1f
   0x0000000000000d4c <+3292>:	mov    r14d,DWORD PTR [rsp-0x74]
   0x0000000000000d51 <+3297>:	lea    r8d,[rdx+r14*1-0x70e44324]
   0x0000000000000d59 <+3305>:	mov    edx,ecx
   0x0000000000000d5b <+3307>:	mov    r14d,ecx
   0x0000000000000d5e <+3310>:	or     edx,esi
   0x0000000000000d60 <+3312>:	and    r14d,esi
   0x0000000000000d63 <+3315>:	ror    ecx,0x2
   0x0000000000000d66 <+3318>:	and    edx,edi
   0x0000000000000d68 <+3320>:	and    r10d,ecx
   0x0000000000000d6b <+3323>:	or     edx,r14d
   0x0000000000000d6e <+3326>:	mov    r14d,r9d
   0x0000000000000d71 <+3329>:	add    edx,r8d
   0x0000000000000d74 <+3332>:	mov    r8d,ebx
   0x0000000000000d77 <+3335>:	mov    ebx,DWORD PTR [rsp-0x70]
   0x0000000000000d7b <+3339>:	ror    r14d,0x1b
   0x0000000000000d7f <+3343>:	add    edx,r14d
   0x0000000000000d82 <+3346>:	xor    r8d,ebx
   0x0000000000000d85 <+3349>:	mov    r14d,r8d
   0x0000000000000d88 <+3352>:	xor    r14d,r15d
   0x0000000000000d8b <+3355>:	xor    r14d,DWORD PTR [rsp-0x50]
   0x0000000000000d90 <+3360>:	ror    r14d,0x1f
   0x0000000000000d94 <+3364>:	lea    r8d,[rdi+r14*1-0x70e44324]
   0x0000000000000d9c <+3372>:	mov    edi,edx
   0x0000000000000d9e <+3374>:	ror    edi,0x1b
   0x0000000000000da1 <+3377>:	add    r8d,edi
   0x0000000000000da4 <+3380>:	mov    edi,r9d
   0x0000000000000da7 <+3383>:	ror    r9d,0x2
   0x0000000000000dab <+3387>:	or     edi,ecx
   0x0000000000000dad <+3389>:	and    edi,esi
   0x0000000000000daf <+3391>:	or     edi,r10d
   0x0000000000000db2 <+3394>:	mov    r10d,r11d
   0x0000000000000db5 <+3397>:	mov    r11d,DWORD PTR [rsp-0x6c]
   0x0000000000000dba <+3402>:	add    edi,r8d
   0x0000000000000dbd <+3405>:	mov    r8d,DWORD PTR [rsp-0x54]
   0x0000000000000dc2 <+3410>:	xor    r10d,r11d
   0x0000000000000dc5 <+3413>:	mov    DWORD PTR [rsp-0x70],r10d
   0x0000000000000dca <+3418>:	xor    DWORD PTR [rsp-0x70],r12d
   0x0000000000000dcf <+3423>:	mov    r10d,edx
   0x0000000000000dd2 <+3426>:	xor    DWORD PTR [rsp-0x70],r8d
   0x0000000000000dd7 <+3431>:	and    r10d,r9d
   0x0000000000000dda <+3434>:	ror    DWORD PTR [rsp-0x70],0x1f
   0x0000000000000ddf <+3439>:	mov    r8d,DWORD PTR [rsp-0x70]
   0x0000000000000de4 <+3444>:	lea    r8d,[rsi+r8*1-0x70e44324]
   0x0000000000000dec <+3452>:	mov    esi,edx
   0x0000000000000dee <+3454>:	ror    edx,0x2
   0x0000000000000df1 <+3457>:	or     esi,r9d
   0x0000000000000df4 <+3460>:	and    esi,ecx
   0x0000000000000df6 <+3462>:	or     esi,r10d
   0x0000000000000df9 <+3465>:	mov    r10d,edi
   0x0000000000000dfc <+3468>:	add    esi,r8d
   0x0000000000000dff <+3471>:	mov    r8d,ebx
   0x0000000000000e02 <+3474>:	mov    ebx,DWORD PTR [rsp-0x68]
   0x0000000000000e06 <+3478>:	ror    r10d,0x1b
   0x0000000000000e0a <+3482>:	add    esi,r10d
   0x0000000000000e0d <+3485>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000e12 <+3490>:	xor    r8d,ebx
   0x0000000000000e15 <+3493>:	mov    DWORD PTR [rsp-0x6c],r8d
   0x0000000000000e1a <+3498>:	xor    DWORD PTR [rsp-0x6c],r10d
   0x0000000000000e1f <+3503>:	mov    r8d,DWORD PTR [rsp-0x74]
   0x0000000000000e24 <+3508>:	xor    DWORD PTR [rsp-0x6c],r8d
   0x0000000000000e29 <+3513>:	ror    DWORD PTR [rsp-0x6c],0x1f
   0x0000000000000e2e <+3518>:	mov    r10d,DWORD PTR [rsp-0x6c]
   0x0000000000000e33 <+3523>:	lea    r8d,[rcx+r10*1-0x70e44324]
   0x0000000000000e3b <+3531>:	mov    ecx,esi
   0x0000000000000e3d <+3533>:	mov    r10d,edi
   0x0000000000000e40 <+3536>:	ror    ecx,0x1b
   0x0000000000000e43 <+3539>:	and    r10d,edx
   0x0000000000000e46 <+3542>:	add    r8d,ecx
   0x0000000000000e49 <+3545>:	mov    ecx,edi
   0x0000000000000e4b <+3547>:	ror    edi,0x2
   0x0000000000000e4e <+3550>:	or     ecx,edx
   0x0000000000000e50 <+3552>:	and    ecx,r9d
   0x0000000000000e53 <+3555>:	or     ecx,r10d
   0x0000000000000e56 <+3558>:	mov    r10d,r11d
   0x0000000000000e59 <+3561>:	mov    r11d,DWORD PTR [rsp-0x64]
   0x0000000000000e5e <+3566>:	add    ecx,r8d
   0x0000000000000e61 <+3569>:	xor    r10d,r11d
   0x0000000000000e64 <+3572>:	mov    DWORD PTR [rsp-0x68],r10d
   0x0000000000000e69 <+3577>:	xor    DWORD PTR [rsp-0x68],r13d
   0x0000000000000e6e <+3582>:	mov    r10d,esi
   0x0000000000000e71 <+3585>:	xor    DWORD PTR [rsp-0x68],r14d
   0x0000000000000e76 <+3590>:	and    r10d,edi
   0x0000000000000e79 <+3593>:	ror    DWORD PTR [rsp-0x68],0x1f
   0x0000000000000e7e <+3598>:	mov    r8d,DWORD PTR [rsp-0x68]
   0x0000000000000e83 <+3603>:	lea    r8d,[r9+r8*1-0x70e44324]
   0x0000000000000e8b <+3611>:	mov    r9d,esi
   0x0000000000000e8e <+3614>:	or     r9d,edi
   0x0000000000000e91 <+3617>:	and    r9d,edx
   0x0000000000000e94 <+3620>:	or     r9d,r10d
   0x0000000000000e97 <+3623>:	mov    r10d,ecx
   0x0000000000000e9a <+3626>:	add    r9d,r8d
   0x0000000000000e9d <+3629>:	ror    r10d,0x1b
   0x0000000000000ea1 <+3633>:	ror    esi,0x2
   0x0000000000000ea4 <+3636>:	add    r9d,r10d
   0x0000000000000ea7 <+3639>:	mov    r10d,DWORD PTR [rsp-0x78]
   0x0000000000000eac <+3644>:	xor    r10d,ebx
   0x0000000000000eaf <+3647>:	mov    ebx,DWORD PTR [rsp-0x70]
   0x0000000000000eb3 <+3651>:	mov    DWORD PTR [rsp-0x64],r10d
   0x0000000000000eb8 <+3656>:	xor    DWORD PTR [rsp-0x64],ebp
   0x0000000000000ebc <+3660>:	xor    DWORD PTR [rsp-0x64],ebx
   0x0000000000000ec0 <+3664>:	ror    DWORD PTR [rsp-0x64],0x1f
   0x0000000000000ec5 <+3669>:	mov    ebx,DWORD PTR [rsp-0x64]
   0x0000000000000ec9 <+3673>:	lea    r8d,[rdx+rbx*1-0x359d3e2a]
   0x0000000000000ed1 <+3681>:	mov    ebx,r11d
   0x0000000000000ed4 <+3684>:	mov    r11d,DWORD PTR [rsp-0x60]
   0x0000000000000ed9 <+3689>:	mov    edx,esi
   0x0000000000000edb <+3691>:	xor    edx,edi
   0x0000000000000edd <+3693>:	xor    ebx,r11d
   0x0000000000000ee0 <+3696>:	xor    edx,ecx
   0x0000000000000ee2 <+3698>:	ror    ecx,0x2
   0x0000000000000ee5 <+3701>:	mov    DWORD PTR [rsp-0x60],ebx
   0x0000000000000ee9 <+3705>:	mov    ebx,DWORD PTR [rsp-0x50]
   0x0000000000000eed <+3709>:	add    edx,r8d
   0x0000000000000ef0 <+3712>:	xor    DWORD PTR [rsp-0x60],ebx
   0x0000000000000ef4 <+3716>:	mov    r8d,r9d
   0x0000000000000ef7 <+3719>:	mov    ebx,DWORD PTR [rsp-0x6c]
   0x0000000000000efb <+3723>:	xor    DWORD PTR [rsp-0x60],ebx
   0x0000000000000eff <+3727>:	ror    r8d,0x1b
   0x0000000000000f03 <+3731>:	mov    r10d,DWORD PTR [rsp-0x78]
   0x0000000000000f08 <+3736>:	ror    DWORD PTR [rsp-0x60],0x1f
   0x0000000000000f0d <+3741>:	add    edx,r8d
   0x0000000000000f10 <+3744>:	mov    ebx,DWORD PTR [rsp-0x54]
   0x0000000000000f14 <+3748>:	mov    r8d,DWORD PTR [rsp-0x60]
   0x0000000000000f19 <+3753>:	xor    r10d,r15d
   0x0000000000000f1c <+3756>:	lea    r8d,[rdi+r8*1-0x359d3e2a]
   0x0000000000000f24 <+3764>:	mov    edi,ecx
   0x0000000000000f26 <+3766>:	mov    DWORD PTR [rsp-0x4c],r10d
   0x0000000000000f2b <+3771>:	xor    edi,esi
   0x0000000000000f2d <+3773>:	xor    DWORD PTR [rsp-0x4c],ebx
   0x0000000000000f31 <+3777>:	mov    ebx,r11d
   0x0000000000000f34 <+3780>:	xor    edi,r9d
   0x0000000000000f37 <+3783>:	ror    r9d,0x2
   0x0000000000000f3b <+3787>:	mov    r11d,DWORD PTR [rsp-0x64]
   0x0000000000000f40 <+3792>:	add    edi,r8d
   0x0000000000000f43 <+3795>:	mov    r8d,edx
   0x0000000000000f46 <+3798>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000000f4b <+3803>:	ror    r8d,0x1b
   0x0000000000000f4f <+3807>:	add    r8d,edi
   0x0000000000000f52 <+3810>:	mov    edi,DWORD PTR [rsp-0x68]
   0x0000000000000f56 <+3814>:	xor    DWORD PTR [rsp-0x4c],edi
   0x0000000000000f5a <+3818>:	ror    DWORD PTR [rsp-0x4c],0x1f
   0x0000000000000f5f <+3823>:	mov    edi,DWORD PTR [rsp-0x4c]
   0x0000000000000f63 <+3827>:	lea    edi,[rsi+rdi*1-0x359d3e2a]
   0x0000000000000f6a <+3834>:	mov    esi,r9d
   0x0000000000000f6d <+3837>:	xor    esi,ecx
   0x0000000000000f6f <+3839>:	xor    esi,edx
   0x0000000000000f71 <+3841>:	ror    edx,0x2
   0x0000000000000f74 <+3844>:	add    esi,edi
   0x0000000000000f76 <+3846>:	mov    edi,r8d
   0x0000000000000f79 <+3849>:	ror    edi,0x1b
   0x0000000000000f7c <+3852>:	add    edi,esi
   0x0000000000000f7e <+3854>:	xor    ebx,r12d
   0x0000000000000f81 <+3857>:	mov    esi,DWORD PTR [rsp-0x74]
   0x0000000000000f85 <+3861>:	mov    DWORD PTR [rsp-0x78],ebx
   0x0000000000000f89 <+3865>:	xor    DWORD PTR [rsp-0x78],esi
   0x0000000000000f8d <+3869>:	xor    r15d,r10d
   0x0000000000000f90 <+3872>:	xor    DWORD PTR [rsp-0x78],r11d
   0x0000000000000f95 <+3877>:	mov    DWORD PTR [rsp-0x5c],r15d
   0x0000000000000f9a <+3882>:	xor    r12d,r13d
   0x0000000000000f9d <+3885>:	ror    DWORD PTR [rsp-0x78],0x1f
   0x0000000000000fa2 <+3890>:	mov    ebx,DWORD PTR [rsp-0x78]
   0x0000000000000fa6 <+3894>:	lea    esi,[rcx+rbx*1-0x359d3e2a]
   0x0000000000000fad <+3901>:	mov    ecx,edx
   0x0000000000000faf <+3903>:	xor    DWORD PTR [rsp-0x5c],r14d
   0x0000000000000fb4 <+3908>:	xor    ecx,r9d
   0x0000000000000fb7 <+3911>:	xor    ecx,r8d
   0x0000000000000fba <+3914>:	ror    r8d,0x2
   0x0000000000000fbe <+3918>:	add    ecx,esi
   0x0000000000000fc0 <+3920>:	mov    esi,edi
   0x0000000000000fc2 <+3922>:	mov    r11d,r8d
   0x0000000000000fc5 <+3925>:	ror    esi,0x1b
   0x0000000000000fc8 <+3928>:	xor    r11d,edx
   0x0000000000000fcb <+3931>:	add    esi,ecx
   0x0000000000000fcd <+3933>:	mov    ecx,DWORD PTR [rsp-0x60]
   0x0000000000000fd1 <+3937>:	xor    DWORD PTR [rsp-0x5c],ecx
   0x0000000000000fd5 <+3941>:	ror    DWORD PTR [rsp-0x5c],0x1f
   0x0000000000000fda <+3946>:	mov    DWORD PTR [rsp-0x58],r12d
   0x0000000000000fdf <+3951>:	mov    ecx,DWORD PTR [rsp-0x5c]
   0x0000000000000fe3 <+3955>:	mov    r12d,DWORD PTR [rsp-0x54]
   0x0000000000000fe8 <+3960>:	lea    r9d,[r9+rcx*1-0x359d3e2a]
   0x0000000000000ff0 <+3968>:	mov    DWORD PTR [rsp-0x24],ecx
   0x0000000000000ff4 <+3972>:	mov    ecx,r11d
   0x0000000000000ff7 <+3975>:	xor    ecx,edi
   0x0000000000000ff9 <+3977>:	mov    r11d,DWORD PTR [rsp-0x70]
   0x0000000000000ffe <+3982>:	xor    DWORD PTR [rsp-0x58],r11d
   0x0000000000001003 <+3987>:	add    ecx,r9d
   0x0000000000001006 <+3990>:	mov    r9d,esi
   0x0000000000001009 <+3993>:	ror    edi,0x2
   0x000000000000100c <+3996>:	ror    r9d,0x1b
   0x0000000000001010 <+4000>:	add    ecx,r9d
   0x0000000000001013 <+4003>:	mov    r9d,DWORD PTR [rsp-0x4c]
   0x0000000000001018 <+4008>:	xor    DWORD PTR [rsp-0x58],r9d
   0x000000000000101d <+4013>:	mov    r15d,ecx
   0x0000000000001020 <+4016>:	ror    DWORD PTR [rsp-0x58],0x1f
   0x0000000000001025 <+4021>:	ror    r15d,0x1b
   0x0000000000001029 <+4025>:	mov    r9d,DWORD PTR [rsp-0x58]
   0x000000000000102e <+4030>:	mov    DWORD PTR [rsp-0x20],r9d
   0x0000000000001033 <+4035>:	lea    r9d,[rdx+r9*1-0x359d3e2a]
   0x000000000000103b <+4043>:	mov    edx,edi
   0x000000000000103d <+4045>:	xor    edx,r8d
   0x0000000000001040 <+4048>:	xor    edx,esi
   0x0000000000001042 <+4050>:	ror    esi,0x2
   0x0000000000001045 <+4053>:	add    edx,r9d
   0x0000000000001048 <+4056>:	mov    r9d,r10d
   0x000000000000104b <+4059>:	xor    r9d,ebp
   0x000000000000104e <+4062>:	xor    r9d,DWORD PTR [rsp-0x6c]
   0x0000000000001053 <+4067>:	add    edx,r15d
   0x0000000000001056 <+4070>:	mov    r15d,DWORD PTR [rsp-0x50]
   0x000000000000105b <+4075>:	mov    r10d,edx
   0x000000000000105e <+4078>:	xor    r9d,ebx
   0x0000000000001061 <+4081>:	ror    r9d,0x1f
   0x0000000000001065 <+4085>:	xor    r13d,r15d
   0x0000000000001068 <+4088>:	xor    ebp,r12d
   0x000000000000106b <+4091>:	lea    ebx,[r8+r9*1-0x359d3e2a]
   0x0000000000001073 <+4099>:	mov    r8d,esi
   0x0000000000001076 <+4102>:	ror    r10d,0x1b
   0x000000000000107a <+4106>:	xor    r8d,edi
   0x000000000000107d <+4109>:	mov    DWORD PTR [rsp-0x1c],r9d
   0x0000000000001082 <+4114>:	xor    r8d,ecx
   0x0000000000001085 <+4117>:	ror    ecx,0x2
   0x0000000000001088 <+4120>:	add    ebx,r8d
   0x000000000000108b <+4123>:	mov    r8d,DWORD PTR [rsp-0x68]
   0x0000000000001090 <+4128>:	add    ebx,r10d
   0x0000000000001093 <+4131>:	xor    r8d,r13d
   0x0000000000001096 <+4134>:	xor    r8d,DWORD PTR [rsp-0x5c]
   0x000000000000109b <+4139>:	mov    r13d,ecx
   0x000000000000109e <+4142>:	xor    r13d,esi
   0x00000000000010a1 <+4145>:	ror    r8d,0x1f
   0x00000000000010a5 <+4149>:	lea    r11d,[rdi+r8*1-0x359d3e2a]
   0x00000000000010ad <+4157>:	mov    edi,r13d
   0x00000000000010b0 <+4160>:	mov    r13d,ebx
   0x00000000000010b3 <+4163>:	xor    edi,edx
   0x00000000000010b5 <+4165>:	ror    edx,0x2
   0x00000000000010b8 <+4168>:	ror    r13d,0x1b
   0x00000000000010bc <+4172>:	add    r11d,edi
   0x00000000000010bf <+4175>:	mov    edi,DWORD PTR [rsp-0x64]
   0x00000000000010c3 <+4179>:	mov    DWORD PTR [rsp-0x18],r8d
   0x00000000000010c8 <+4184>:	add    r11d,r13d
   0x00000000000010cb <+4187>:	xor    edi,ebp
   0x00000000000010cd <+4189>:	xor    edi,DWORD PTR [rsp-0x58]
   0x00000000000010d1 <+4193>:	mov    ebp,edx
   0x00000000000010d3 <+4195>:	xor    ebp,ecx
   0x00000000000010d5 <+4197>:	ror    edi,0x1f
   0x00000000000010d8 <+4200>:	lea    r10d,[rsi+rdi*1-0x359d3e2a]
   0x00000000000010e0 <+4208>:	mov    esi,ebp
   0x00000000000010e2 <+4210>:	mov    ebp,r11d
   0x00000000000010e5 <+4213>:	xor    esi,ebx
   0x00000000000010e7 <+4215>:	ror    ebp,0x1b
   0x00000000000010ea <+4218>:	ror    ebx,0x2
   0x00000000000010ed <+4221>:	add    esi,r10d
   0x00000000000010f0 <+4224>:	mov    r10d,ebp
   0x00000000000010f3 <+4227>:	mov    ebp,ebx
   0x00000000000010f5 <+4229>:	add    r10d,esi
   0x00000000000010f8 <+4232>:	mov    esi,DWORD PTR [rsp-0x74]
   0x00000000000010fc <+4236>:	xor    ebp,edx
   0x00000000000010fe <+4238>:	mov    DWORD PTR [rsp-0x14],edi
   0x0000000000001102 <+4242>:	xor    esi,r15d
   0x0000000000001105 <+4245>:	xor    esi,DWORD PTR [rsp-0x60]
   0x0000000000001109 <+4249>:	xor    esi,r9d
   0x000000000000110c <+4252>:	ror    esi,0x1f
   0x000000000000110f <+4255>:	lea    r15d,[rcx+rsi*1-0x359d3e2a]
   0x0000000000001117 <+4263>:	mov    ecx,ebp
   0x0000000000001119 <+4265>:	mov    ebp,r10d
   0x000000000000111c <+4268>:	xor    ecx,r11d
   0x000000000000111f <+4271>:	mov    DWORD PTR [rsp-0x10],esi
   0x0000000000001123 <+4275>:	add    r15d,ecx
   0x0000000000001126 <+4278>:	mov    ecx,r12d
   0x0000000000001129 <+4281>:	ror    r11d,0x2
   0x000000000000112d <+4285>:	xor    ecx,r14d
   0x0000000000001130 <+4288>:	xor    ecx,DWORD PTR [rsp-0x4c]
   0x0000000000001134 <+4292>:	ror    ebp,0x1b
   0x0000000000001137 <+4295>:	add    r15d,ebp
   0x000000000000113a <+4298>:	xor    ecx,r8d
   0x000000000000113d <+4301>:	ror    ecx,0x1f
   0x0000000000001140 <+4304>:	lea    ebp,[rdx+rcx*1-0x359d3e2a]
   0x0000000000001147 <+4311>:	mov    edx,r11d
   0x000000000000114a <+4314>:	mov    DWORD PTR [rsp-0xc],ecx
   0x000000000000114e <+4318>:	xor    edx,ebx
   0x0000000000001150 <+4320>:	xor    edx,r10d
   0x0000000000001153 <+4323>:	ror    r10d,0x2
   0x0000000000001157 <+4327>:	add    edx,ebp
   0x0000000000001159 <+4329>:	mov    ebp,r15d
   0x000000000000115c <+4332>:	ror    ebp,0x1b
   0x000000000000115f <+4335>:	lea    r13d,[rdx+rbp*1]
   0x0000000000001163 <+4339>:	mov    edx,DWORD PTR [rsp-0x74]
   0x0000000000001167 <+4343>:	xor    edx,DWORD PTR [rsp-0x70]
   0x000000000000116b <+4347>:	xor    edx,DWORD PTR [rsp-0x78]
   0x000000000000116f <+4351>:	mov    ebp,r10d
   0x0000000000001172 <+4354>:	xor    ebp,r11d
   0x0000000000001175 <+4357>:	xor    edx,edi
   0x0000000000001177 <+4359>:	ror    edx,0x1f
   0x000000000000117a <+4362>:	lea    r12d,[rbx+rdx*1-0x359d3e2a]
   0x0000000000001182 <+4370>:	mov    ebx,ebp
   0x0000000000001184 <+4372>:	mov    ebp,r13d
   0x0000000000001187 <+4375>:	xor    ebx,r15d
   0x000000000000118a <+4378>:	ror    ebp,0x1b
   0x000000000000118d <+4381>:	mov    DWORD PTR [rsp-0x8],edx
   0x0000000000001191 <+4385>:	add    r12d,ebx
   0x0000000000001194 <+4388>:	mov    ebx,DWORD PTR [rsp-0x5c]
   0x0000000000001198 <+4392>:	ror    r15d,0x2
   0x000000000000119c <+4396>:	add    r12d,ebp
   0x000000000000119f <+4399>:	mov    ebp,DWORD PTR [rsp-0x6c]
   0x00000000000011a3 <+4403>:	xor    ebp,r14d
   0x00000000000011a6 <+4406>:	xor    ebx,ebp
   0x00000000000011a8 <+4408>:	xor    ebx,esi
   0x00000000000011aa <+4410>:	ror    ebx,0x1f
   0x00000000000011ad <+4413>:	lea    ebp,[r11+rbx*1-0x359d3e2a]
   0x00000000000011b5 <+4421>:	mov    r11d,r15d
   0x00000000000011b8 <+4424>:	mov    DWORD PTR [rsp-0x4],ebx
   0x00000000000011bc <+4428>:	xor    r11d,r10d
   0x00000000000011bf <+4431>:	xor    r11d,r13d
   0x00000000000011c2 <+4434>:	ror    r13d,0x2
   0x00000000000011c6 <+4438>:	add    r11d,ebp
   0x00000000000011c9 <+4441>:	mov    ebp,r12d
   0x00000000000011cc <+4444>:	mov    r14d,r13d
   0x00000000000011cf <+4447>:	ror    ebp,0x1b
   0x00000000000011d2 <+4450>:	add    ebp,r11d
   0x00000000000011d5 <+4453>:	mov    r11d,DWORD PTR [rsp-0x70]
   0x00000000000011da <+4458>:	xor    r11d,DWORD PTR [rsp-0x68]
   0x00000000000011df <+4463>:	xor    r11d,DWORD PTR [rsp-0x58]
   0x00000000000011e4 <+4468>:	xor    r11d,ecx
   0x00000000000011e7 <+4471>:	ror    r11d,0x1f
   0x00000000000011eb <+4475>:	lea    r13d,[r10+r11*1-0x359d3e2a]
   0x00000000000011f3 <+4483>:	mov    r10d,r14d
   0x00000000000011f6 <+4486>:	mov    DWORD PTR [rsp],r11d
   0x00000000000011fa <+4490>:	xor    r10d,r15d
   0x00000000000011fd <+4493>:	xor    r10d,r12d
   0x0000000000001200 <+4496>:	ror    r12d,0x2
   0x0000000000001204 <+4500>:	add    r10d,r13d
   0x0000000000001207 <+4503>:	mov    r13d,ebp
   0x000000000000120a <+4506>:	ror    r13d,0x1b
   0x000000000000120e <+4510>:	add    r13d,r10d
   0x0000000000001211 <+4513>:	mov    r10d,DWORD PTR [rsp-0x6c]
   0x0000000000001216 <+4518>:	xor    r10d,DWORD PTR [rsp-0x64]
   0x000000000000121b <+4523>:	xor    r10d,r9d
   0x000000000000121e <+4526>:	mov    r9d,r12d
   0x0000000000001221 <+4529>:	xor    r10d,edx
   0x0000000000001224 <+4532>:	xor    r9d,r14d
   0x0000000000001227 <+4535>:	ror    r10d,0x1f
   0x000000000000122b <+4539>:	xor    r9d,ebp
   0x000000000000122e <+4542>:	ror    ebp,0x2
   0x0000000000001231 <+4545>:	lea    r15d,[r15+r10*1-0x359d3e2a]
   0x0000000000001239 <+4553>:	mov    DWORD PTR [rsp+0x4],r10d
   0x000000000000123e <+4558>:	add    r9d,r15d
   0x0000000000001241 <+4561>:	mov    r15d,r13d
   0x0000000000001244 <+4564>:	ror    r15d,0x1b
   0x0000000000001248 <+4568>:	add    r15d,r9d
   0x000000000000124b <+4571>:	mov    r9d,DWORD PTR [rsp-0x68]
   0x0000000000001250 <+4576>:	xor    r9d,DWORD PTR [rsp-0x60]
   0x0000000000001255 <+4581>:	xor    r9d,r8d
   0x0000000000001258 <+4584>:	mov    r8d,ebp
   0x000000000000125b <+4587>:	xor    r9d,ebx
   0x000000000000125e <+4590>:	xor    r8d,r12d
   0x0000000000001261 <+4593>:	ror    r9d,0x1f
   0x0000000000001265 <+4597>:	xor    r8d,r13d
   0x0000000000001268 <+4600>:	ror    r13d,0x2
   0x000000000000126c <+4604>:	lea    ebx,[r14+r9*1-0x359d3e2a]
   0x0000000000001274 <+4612>:	mov    r14d,DWORD PTR [rsp-0x4c]
   0x0000000000001279 <+4617>:	mov    DWORD PTR [rsp+0x8],r9d
   0x000000000000127e <+4622>:	add    r8d,ebx
   0x0000000000001281 <+4625>:	mov    ebx,r15d
   0x0000000000001284 <+4628>:	ror    ebx,0x1b
   0x0000000000001287 <+4631>:	add    ebx,r8d
   0x000000000000128a <+4634>:	mov    r8d,DWORD PTR [rsp-0x64]
   0x000000000000128f <+4639>:	xor    r8d,r14d
   0x0000000000001292 <+4642>:	xor    r8d,edi
   0x0000000000001295 <+4645>:	mov    edi,r13d
   0x0000000000001298 <+4648>:	xor    r8d,r11d
   0x000000000000129b <+4651>:	ror    r8d,0x1f
   0x000000000000129f <+4655>:	xor    edi,ebp
   0x00000000000012a1 <+4657>:	lea    r11d,[r12+r8*1-0x359d3e2a]
   0x00000000000012a9 <+4665>:	xor    edi,r15d
   0x00000000000012ac <+4668>:	mov    r12d,DWORD PTR [rsp-0x78]
   0x00000000000012b1 <+4673>:	ror    r15d,0x2
   0x00000000000012b5 <+4677>:	mov    DWORD PTR [rsp+0xc],r8d
   0x00000000000012ba <+4682>:	add    edi,r11d
   0x00000000000012bd <+4685>:	mov    r11d,ebx
   0x00000000000012c0 <+4688>:	ror    r11d,0x1b
   0x00000000000012c4 <+4692>:	add    edi,r11d
   0x00000000000012c7 <+4695>:	mov    r11d,DWORD PTR [rsp-0x60]
   0x00000000000012cc <+4700>:	xor    r11d,r12d
   0x00000000000012cf <+4703>:	xor    r11d,esi
   0x00000000000012d2 <+4706>:	mov    esi,r15d
   0x00000000000012d5 <+4709>:	xor    r11d,r10d
   0x00000000000012d8 <+4712>:	xor    esi,r13d
   0x00000000000012db <+4715>:	ror    r11d,0x1f
   0x00000000000012df <+4719>:	xor    esi,ebx
   0x00000000000012e1 <+4721>:	ror    ebx,0x2
   0x00000000000012e4 <+4724>:	lea    r10d,[rbp+r11*1-0x359d3e2a]
   0x00000000000012ec <+4732>:	mov    DWORD PTR [rsp+0x10],r11d
   0x00000000000012f1 <+4737>:	mov    r11d,edi
   0x00000000000012f4 <+4740>:	ror    r11d,0x1b
   0x00000000000012f8 <+4744>:	add    esi,r10d
   0x00000000000012fb <+4747>:	mov    r10d,DWORD PTR [rsp-0x5c]
   0x0000000000001300 <+4752>:	add    esi,r11d
   0x0000000000001303 <+4755>:	mov    r11d,esi
   0x0000000000001306 <+4758>:	xor    r10d,r14d
   0x0000000000001309 <+4761>:	mov    r14d,DWORD PTR [rsp-0x48]
   0x000000000000130e <+4766>:	ror    r11d,0x1b
   0x0000000000001312 <+4770>:	xor    r10d,ecx
   0x0000000000001315 <+4773>:	mov    ecx,ebx
   0x0000000000001317 <+4775>:	xor    r10d,r9d
   0x000000000000131a <+4778>:	xor    ecx,r15d
   0x000000000000131d <+4781>:	ror    r10d,0x1f
   0x0000000000001321 <+4785>:	xor    ecx,edi
   0x0000000000001323 <+4787>:	ror    edi,0x2
   0x0000000000001326 <+4790>:	lea    r9d,[r13+r10*1-0x359d3e2a]
   0x000000000000132e <+4798>:	mov    DWORD PTR [rsp+0x14],r10d
   0x0000000000001333 <+4803>:	add    ecx,r9d
   0x0000000000001336 <+4806>:	mov    r9d,DWORD PTR [rsp-0x58]
   0x000000000000133b <+4811>:	add    ecx,r11d
   0x000000000000133e <+4814>:	xor    r9d,r12d
   0x0000000000001341 <+4817>:	xor    r9d,edx
   0x0000000000001344 <+4820>:	mov    edx,esi
   0x0000000000001346 <+4822>:	xor    r9d,r8d
   0x0000000000001349 <+4825>:	ror    edx,0x2
   0x000000000000134c <+4828>:	ror    r9d,0x1f
   0x0000000000001350 <+4832>:	lea    r8d,[r14+r9*1-0x359d3e2a]
   0x0000000000001358 <+4840>:	mov    DWORD PTR [rsp+0x18],r9d
   0x000000000000135d <+4845>:	add    r15d,r8d
   0x0000000000001360 <+4848>:	mov    r8d,edi
   0x0000000000001363 <+4851>:	xor    r8d,ebx
   0x0000000000001366 <+4854>:	add    DWORD PTR [rsp-0x44],ecx
   0x000000000000136a <+4858>:	add    DWORD PTR [rsp-0x40],edx
   0x000000000000136e <+4862>:	xor    r8d,esi
   0x0000000000001371 <+4865>:	mov    esi,ecx
   0x0000000000001373 <+4867>:	mov    ecx,DWORD PTR [rsp-0x44]
   0x0000000000001377 <+4871>:	add    r8d,r15d
   0x000000000000137a <+4874>:	ror    esi,0x1b
   0x000000000000137d <+4877>:	add    esi,r8d
   0x0000000000001380 <+4880>:	mov    r14d,esi
   0x0000000000001383 <+4883>:	mov    DWORD PTR [rsp-0x48],esi
   0x0000000000001387 <+4887>:	mov    rsi,QWORD PTR [rsp-0x2c]
   0x000000000000138c <+4892>:	mov    DWORD PTR [rsi+0x4],ecx
   0x000000000000138f <+4895>:	mov    ecx,DWORD PTR [rsp-0x40]
   0x0000000000001393 <+4899>:	mov    DWORD PTR [rsi],r14d
   0x0000000000001396 <+4902>:	mov    DWORD PTR [rsi+0x8],ecx
   0x0000000000001399 <+4905>:	add    DWORD PTR [rsp-0x3c],edi
   0x000000000000139d <+4909>:	add    DWORD PTR [rsp-0x38],ebx
   0x00000000000013a1 <+4913>:	cmp    QWORD PTR [rsp-0x34],rax
   0x00000000000013a6 <+4918>:	mov    edi,DWORD PTR [rsp-0x3c]
   0x00000000000013aa <+4922>:	mov    ebx,DWORD PTR [rsp-0x38]
   0x00000000000013ae <+4926>:	mov    DWORD PTR [rsi+0xc],edi
   0x00000000000013b1 <+4929>:	mov    DWORD PTR [rsi+0x10],ebx
   0x00000000000013b4 <+4932>:	ja     0xf0 <sha1_process_block+128>
   0x00000000000013ba <+4938>:	add    rsp,0x24
   0x00000000000013be <+4942>:	pop    rbx
   0x00000000000013bf <+4943>:	pop    rbp
   0x00000000000013c0 <+4944>:	pop    r12
   0x00000000000013c2 <+4946>:	pop    r13
   0x00000000000013c4 <+4948>:	pop    r14
   0x00000000000013c6 <+4950>:	pop    r15
   0x00000000000013c8 <+4952>:	ret    
