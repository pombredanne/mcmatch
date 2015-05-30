Dump of assembler code for function printf_core:
   0x000000000004cb38 <+0>:	push   r15
   0x000000000004cb3a <+2>:	push   r14
   0x000000000004cb3c <+4>:	mov    r15,rdi
   0x000000000004cb3f <+7>:	push   r13
   0x000000000004cb41 <+9>:	push   r12
   0x000000000004cb43 <+11>:	mov    r9,rsi
   0x000000000004cb46 <+14>:	push   rbp
   0x000000000004cb47 <+15>:	push   rbx
   0x000000000004cb48 <+16>:	xor    r13d,r13d
   0x000000000004cb4b <+19>:	sub    rsp,0xc8
   0x000000000004cb52 <+26>:	lea    rax,[rsp+0x74]
   0x000000000004cb57 <+31>:	mov    QWORD PTR [rsp+0x10],rdx
   0x000000000004cb5c <+36>:	mov    QWORD PTR [rsp+0x30],rcx
   0x000000000004cb61 <+41>:	mov    QWORD PTR [rsp+0x20],r8
   0x000000000004cb66 <+46>:	mov    DWORD PTR [rsp+0xc],0x0
   0x000000000004cb6e <+54>:	mov    QWORD PTR [rsp+0x40],rax
   0x000000000004cb73 <+59>:	lea    rax,[rsp+0x78]
   0x000000000004cb78 <+64>:	mov    DWORD PTR [rsp+0x60],0x0
   0x000000000004cb80 <+72>:	mov    QWORD PTR [rsp+0x48],rax
   0x000000000004cb85 <+77>:	lea    rax,[rsp+0x95]
   0x000000000004cb8d <+85>:	mov    QWORD PTR [rsp+0x50],rax
   0x000000000004cb92 <+90>:	lea    rax,[rsp+0x80]
   0x000000000004cb9a <+98>:	mov    QWORD PTR [rsp+0x58],rax
   0x000000000004cb9f <+103>:	cmp    DWORD PTR [rsp+0xc],0x0
   0x000000000004cba4 <+108>:	js     0x4cbd6 <printf_core+158>
   0x000000000004cba6 <+110>:	mov    eax,0x7fffffff
   0x000000000004cbab <+115>:	sub    eax,DWORD PTR [rsp+0xc]
   0x000000000004cbaf <+119>:	add    DWORD PTR [rsp+0xc],r13d
   0x000000000004cbb4 <+124>:	cmp    r13d,eax
   0x000000000004cbb7 <+127>:	jle    0x4cbd6 <printf_core+158>
   0x000000000004cbb9 <+129>:	mov    QWORD PTR [rsp+0x18],r9
   0x000000000004cbbe <+134>:	call   0x1d317 <__errno_location>
   0x000000000004cbc3 <+139>:	mov    r9,QWORD PTR [rsp+0x18]
   0x000000000004cbc8 <+144>:	mov    DWORD PTR [rax],0x4b
   0x000000000004cbce <+150>:	mov    DWORD PTR [rsp+0xc],0xffffffff
   0x000000000004cbd6 <+158>:	cmp    BYTE PTR [r9],0x0
   0x000000000004cbda <+162>:	je     0x4d35e <printf_core+2086>
   0x000000000004cbe0 <+168>:	mov    rbx,r9
   0x000000000004cbe3 <+171>:	mov    al,BYTE PTR [rbx]
   0x000000000004cbe5 <+173>:	cmp    al,0x25
   0x000000000004cbe7 <+175>:	je     0x4cbf2 <printf_core+186>
   0x000000000004cbe9 <+177>:	test   al,al
   0x000000000004cbeb <+179>:	je     0x4cbf2 <printf_core+186>
   0x000000000004cbed <+181>:	inc    rbx
   0x000000000004cbf0 <+184>:	jmp    0x4cbe3 <printf_core+171>
   0x000000000004cbf2 <+186>:	mov    r14,rbx
   0x000000000004cbf5 <+189>:	cmp    BYTE PTR [r14],0x25
   0x000000000004cbf9 <+193>:	je     0x4cc25 <printf_core+237>
   0x000000000004cbfb <+195>:	sub    rbx,r9
   0x000000000004cbfe <+198>:	test   r15,r15
   0x000000000004cc01 <+201>:	mov    QWORD PTR [rsp+0x38],r14
   0x000000000004cc06 <+206>:	mov    r13d,ebx
   0x000000000004cc09 <+209>:	je     0x4cc35 <printf_core+253>
   0x000000000004cc0b <+211>:	mov    rsi,r9
   0x000000000004cc0e <+214>:	movsxd rdx,ebx
   0x000000000004cc11 <+217>:	mov    rdi,r15
   0x000000000004cc14 <+220>:	mov    QWORD PTR [rsp+0x18],r9
   0x000000000004cc19 <+225>:	call   0x4be24 <out>
   0x000000000004cc1e <+230>:	mov    r9,QWORD PTR [rsp+0x18]
   0x000000000004cc23 <+235>:	jmp    0x4cc35 <printf_core+253>
   0x000000000004cc25 <+237>:	cmp    BYTE PTR [r14+0x1],0x25
   0x000000000004cc2a <+242>:	jne    0x4cbfb <printf_core+195>
   0x000000000004cc2c <+244>:	inc    rbx
   0x000000000004cc2f <+247>:	add    r14,0x2
   0x000000000004cc33 <+251>:	jmp    0x4cbf5 <printf_core+189>
   0x000000000004cc35 <+253>:	test   ebx,ebx
   0x000000000004cc37 <+255>:	je     0x4cc43 <printf_core+267>
   0x000000000004cc39 <+257>:	mov    r9,QWORD PTR [rsp+0x38]
   0x000000000004cc3e <+262>:	jmp    0x4cb9f <printf_core+103>
   0x000000000004cc43 <+267>:	movsx  eax,BYTE PTR [r14+0x1]
   0x000000000004cc48 <+272>:	sub    eax,0x30
   0x000000000004cc4b <+275>:	cmp    eax,0x9
   0x000000000004cc4e <+278>:	ja     0x4cc65 <printf_core+301>
   0x000000000004cc50 <+280>:	cmp    BYTE PTR [r14+0x2],0x24
   0x000000000004cc55 <+285>:	jne    0x4cc65 <printf_core+301>
   0x000000000004cc57 <+287>:	add    r14,0x3
   0x000000000004cc5b <+291>:	mov    DWORD PTR [rsp+0x60],0x1
   0x000000000004cc63 <+299>:	jmp    0x4cc6b <printf_core+307>
   0x000000000004cc65 <+301>:	inc    r14
   0x000000000004cc68 <+304>:	or     eax,0xffffffff
   0x000000000004cc6b <+307>:	xor    edx,edx
   0x000000000004cc6d <+309>:	mov    esi,0x12889
   0x000000000004cc72 <+314>:	mov    edi,0x1
   0x000000000004cc77 <+319>:	movsx  ecx,BYTE PTR [r14]
   0x000000000004cc7b <+323>:	mov    r8d,ecx
   0x000000000004cc7e <+326>:	sub    ecx,0x20
   0x000000000004cc81 <+329>:	cmp    ecx,0x1f
   0x000000000004cc84 <+332>:	jbe    0x4cc95 <printf_core+349>
   0x000000000004cc86 <+334>:	cmp    r8b,0x2a
   0x000000000004cc8a <+338>:	mov    r12d,edx
   0x000000000004cc8d <+341>:	jne    0x4cd43 <printf_core+523>
   0x000000000004cc93 <+347>:	jmp    0x4cca8 <printf_core+368>
   0x000000000004cc95 <+349>:	bt     esi,ecx
   0x000000000004cc98 <+352>:	jae    0x4cc86 <printf_core+334>
   0x000000000004cc9a <+354>:	mov    r10d,edi
   0x000000000004cc9d <+357>:	inc    r14
   0x000000000004cca0 <+360>:	shl    r10d,cl
   0x000000000004cca3 <+363>:	or     edx,r10d
   0x000000000004cca6 <+366>:	jmp    0x4cc77 <printf_core+319>
   0x000000000004cca8 <+368>:	movsx  rsi,BYTE PTR [r14+0x1]
   0x000000000004ccad <+373>:	mov    rcx,rsi
   0x000000000004ccb0 <+376>:	sub    esi,0x30
   0x000000000004ccb3 <+379>:	cmp    esi,0x9
   0x000000000004ccb6 <+382>:	ja     0x4ccf2 <printf_core+442>
   0x000000000004ccb8 <+384>:	cmp    BYTE PTR [r14+0x2],0x24
   0x000000000004ccbd <+389>:	jne    0x4ccf2 <printf_core+442>
   0x000000000004ccbf <+391>:	mov    rdi,QWORD PTR [rsp+0x20]
   0x000000000004ccc4 <+396>:	add    r14,0x3
   0x000000000004ccc8 <+400>:	mov    DWORD PTR [rsp+0x60],0x1
   0x000000000004ccd0 <+408>:	mov    DWORD PTR [rdi+rcx*4-0xc0],0xa
   0x000000000004ccdb <+419>:	movsx  rcx,BYTE PTR [r14-0x2]
   0x000000000004cce0 <+424>:	mov    rdi,QWORD PTR [rsp+0x30]
   0x000000000004cce5 <+429>:	shl    rcx,0x4
   0x000000000004cce9 <+433>:	mov    ebx,DWORD PTR [rdi+rcx*1-0x300]
   0x000000000004ccf0 <+440>:	jmp    0x4cd35 <printf_core+509>
   0x000000000004ccf2 <+442>:	cmp    DWORD PTR [rsp+0x60],0x0
   0x000000000004ccf7 <+447>:	je     0x4cd01 <printf_core+457>
   0x000000000004ccf9 <+449>:	or     eax,0xffffffff
   0x000000000004ccfc <+452>:	jmp    0x4d456 <printf_core+2334>
   0x000000000004cd01 <+457>:	test   r15,r15
   0x000000000004cd04 <+460>:	je     0x4cd32 <printf_core+506>
   0x000000000004cd06 <+462>:	mov    rdi,QWORD PTR [rsp+0x10]
   0x000000000004cd0b <+467>:	mov    esi,DWORD PTR [rdi]
   0x000000000004cd0d <+469>:	cmp    esi,0x30
   0x000000000004cd10 <+472>:	jae    0x4cd1f <printf_core+487>
   0x000000000004cd12 <+474>:	mov    ecx,esi
   0x000000000004cd14 <+476>:	add    esi,0x8
   0x000000000004cd17 <+479>:	add    rcx,QWORD PTR [rdi+0x10]
   0x000000000004cd1b <+483>:	mov    DWORD PTR [rdi],esi
   0x000000000004cd1d <+485>:	jmp    0x4cd30 <printf_core+504>
   0x000000000004cd1f <+487>:	mov    rdi,QWORD PTR [rsp+0x10]
   0x000000000004cd24 <+492>:	mov    rcx,QWORD PTR [rdi+0x8]
   0x000000000004cd28 <+496>:	lea    rsi,[rcx+0x8]
   0x000000000004cd2c <+500>:	mov    QWORD PTR [rdi+0x8],rsi
   0x000000000004cd30 <+504>:	mov    ebx,DWORD PTR [rcx]
   0x000000000004cd32 <+506>:	inc    r14
   0x000000000004cd35 <+509>:	test   ebx,ebx
   0x000000000004cd37 <+511>:	jns    0x4cd5d <printf_core+549>
   0x000000000004cd39 <+513>:	or     dh,0x20
   0x000000000004cd3c <+516>:	neg    ebx
   0x000000000004cd3e <+518>:	mov    r12d,edx
   0x000000000004cd41 <+521>:	jmp    0x4cd5d <printf_core+549>
   0x000000000004cd43 <+523>:	movsx  edx,BYTE PTR [r14]
   0x000000000004cd47 <+527>:	sub    edx,0x30
   0x000000000004cd4a <+530>:	cmp    edx,0x9
   0x000000000004cd4d <+533>:	ja     0x4cd59 <printf_core+545>
   0x000000000004cd4f <+535>:	imul   ebx,ebx,0xa
   0x000000000004cd52 <+538>:	inc    r14
   0x000000000004cd55 <+541>:	add    ebx,edx
   0x000000000004cd57 <+543>:	jmp    0x4cd43 <printf_core+523>
   0x000000000004cd59 <+545>:	test   ebx,ebx
   0x000000000004cd5b <+547>:	js     0x4ccf9 <printf_core+449>
   0x000000000004cd5d <+549>:	or     ebp,0xffffffff
   0x000000000004cd60 <+552>:	cmp    BYTE PTR [r14],0x2e
   0x000000000004cd64 <+556>:	jne    0x4ce1b <printf_core+739>
   0x000000000004cd6a <+562>:	cmp    BYTE PTR [r14+0x1],0x2a
   0x000000000004cd6f <+567>:	jne    0x4ce00 <printf_core+712>
   0x000000000004cd75 <+573>:	movsx  rcx,BYTE PTR [r14+0x2]
   0x000000000004cd7a <+578>:	mov    rdx,rcx
   0x000000000004cd7d <+581>:	sub    ecx,0x30
   0x000000000004cd80 <+584>:	cmp    ecx,0x9
   0x000000000004cd83 <+587>:	ja     0x4cdb7 <printf_core+639>
   0x000000000004cd85 <+589>:	cmp    BYTE PTR [r14+0x3],0x24
   0x000000000004cd8a <+594>:	jne    0x4cdb7 <printf_core+639>
   0x000000000004cd8c <+596>:	mov    rdi,QWORD PTR [rsp+0x20]
   0x000000000004cd91 <+601>:	add    r14,0x4
   0x000000000004cd95 <+605>:	mov    DWORD PTR [rdi+rdx*4-0xc0],0xa
   0x000000000004cda0 <+616>:	movsx  rdx,BYTE PTR [r14-0x2]
   0x000000000004cda5 <+621>:	mov    rdi,QWORD PTR [rsp+0x30]
   0x000000000004cdaa <+626>:	shl    rdx,0x4
   0x000000000004cdae <+630>:	mov    ebp,DWORD PTR [rdi+rdx*1-0x300]
   0x000000000004cdb5 <+637>:	jmp    0x4ce1b <printf_core+739>
   0x000000000004cdb7 <+639>:	cmp    DWORD PTR [rsp+0x60],0x0
   0x000000000004cdbc <+644>:	jne    0x4ccf9 <printf_core+449>
   0x000000000004cdc2 <+650>:	xor    ebp,ebp
   0x000000000004cdc4 <+652>:	test   r15,r15
   0x000000000004cdc7 <+655>:	je     0x4cdfa <printf_core+706>
   0x000000000004cdc9 <+657>:	mov    rdi,QWORD PTR [rsp+0x10]
   0x000000000004cdce <+662>:	mov    ecx,DWORD PTR [rdi]
   0x000000000004cdd0 <+664>:	cmp    ecx,0x30
   0x000000000004cdd3 <+667>:	jae    0x4cde2 <printf_core+682>
   0x000000000004cdd5 <+669>:	mov    edx,ecx
   0x000000000004cdd7 <+671>:	add    ecx,0x8
   0x000000000004cdda <+674>:	add    rdx,QWORD PTR [rdi+0x10]
   0x000000000004cdde <+678>:	mov    DWORD PTR [rdi],ecx
   0x000000000004cde0 <+680>:	jmp    0x4cdf8 <printf_core+704>
   0x000000000004cde2 <+682>:	mov    rcx,QWORD PTR [rsp+0x10]
   0x000000000004cde7 <+687>:	mov    rdi,QWORD PTR [rsp+0x10]
   0x000000000004cdec <+692>:	mov    rdx,QWORD PTR [rcx+0x8]
   0x000000000004cdf0 <+696>:	lea    rcx,[rdx+0x8]
   0x000000000004cdf4 <+700>:	mov    QWORD PTR [rdi+0x8],rcx
   0x000000000004cdf8 <+704>:	mov    ebp,DWORD PTR [rdx]
   0x000000000004cdfa <+706>:	add    r14,0x2
   0x000000000004cdfe <+710>:	jmp    0x4ce1b <printf_core+739>
   0x000000000004ce00 <+712>:	inc    r14
   0x000000000004ce03 <+715>:	xor    ebp,ebp
   0x000000000004ce05 <+717>:	movsx  edx,BYTE PTR [r14]
   0x000000000004ce09 <+721>:	sub    edx,0x30
   0x000000000004ce0c <+724>:	cmp    edx,0x9
   0x000000000004ce0f <+727>:	ja     0x4ce1b <printf_core+739>
   0x000000000004ce11 <+729>:	imul   ebp,ebp,0xa
   0x000000000004ce14 <+732>:	inc    r14
   0x000000000004ce17 <+735>:	add    ebp,edx
   0x000000000004ce19 <+737>:	jmp    0x4ce05 <printf_core+717>
   0x000000000004ce1b <+739>:	lea    rcx,[rip+0x3a4de]        # 0x87300 <states>
   0x000000000004ce22 <+746>:	xor    r11d,r11d
   0x000000000004ce25 <+749>:	movsx  edx,BYTE PTR [r14]
   0x000000000004ce29 <+753>:	sub    edx,0x41
   0x000000000004ce2c <+756>:	cmp    edx,0x39
   0x000000000004ce2f <+759>:	ja     0x4ccf9 <printf_core+449>
   0x000000000004ce35 <+765>:	mov    esi,r11d
   0x000000000004ce38 <+768>:	movsxd rdx,edx
   0x000000000004ce3b <+771>:	inc    r14
   0x000000000004ce3e <+774>:	imul   rsi,rsi,0x3a
   0x000000000004ce42 <+778>:	add    rdx,rsi
   0x000000000004ce45 <+781>:	movzx  esi,BYTE PTR [rcx+rdx*1]
   0x000000000004ce49 <+785>:	lea    edx,[rsi-0x1]
   0x000000000004ce4c <+788>:	cmp    edx,0x7
   0x000000000004ce4f <+791>:	ja     0x4ce56 <printf_core+798>
   0x000000000004ce51 <+793>:	mov    r11d,esi
   0x000000000004ce54 <+796>:	jmp    0x4ce25 <printf_core+749>
   0x000000000004ce56 <+798>:	test   esi,esi
   0x000000000004ce58 <+800>:	mov    QWORD PTR [rsp+0x38],r14
   0x000000000004ce5d <+805>:	je     0x4ccf9 <printf_core+449>
   0x000000000004ce63 <+811>:	cmp    esi,0x15
   0x000000000004ce66 <+814>:	jne    0x4ce71 <printf_core+825>
   0x000000000004ce68 <+816>:	test   eax,eax
   0x000000000004ce6a <+818>:	js     0x4ced2 <printf_core+922>
   0x000000000004ce6c <+820>:	jmp    0x4ccf9 <printf_core+449>
   0x000000000004ce71 <+825>:	test   eax,eax
   0x000000000004ce73 <+827>:	js     0x4cea1 <printf_core+873>
   0x000000000004ce75 <+829>:	mov    rcx,QWORD PTR [rsp+0x20]
   0x000000000004ce7a <+834>:	cdqe   
   0x000000000004ce7c <+836>:	mov    DWORD PTR [rcx+rax*4],esi
   0x000000000004ce7f <+839>:	shl    rax,0x4
   0x000000000004ce83 <+843>:	add    rax,QWORD PTR [rsp+0x30]
   0x000000000004ce88 <+848>:	mov    rdx,QWORD PTR [rax]
   0x000000000004ce8b <+851>:	mov    rax,QWORD PTR [rax+0x8]
   0x000000000004ce8f <+855>:	mov    QWORD PTR [rsp+0x80],rdx
   0x000000000004ce97 <+863>:	mov    QWORD PTR [rsp+0x88],rax
   0x000000000004ce9f <+871>:	jmp    0x4ced2 <printf_core+922>
   0x000000000004cea1 <+873>:	test   r15,r15
   0x000000000004cea4 <+876>:	jne    0x4cead <printf_core+885>
   0x000000000004cea6 <+878>:	xor    eax,eax
   0x000000000004cea8 <+880>:	jmp    0x4d456 <printf_core+2334>
   0x000000000004cead <+885>:	mov    rdx,QWORD PTR [rsp+0x10]
   0x000000000004ceb2 <+890>:	mov    rdi,QWORD PTR [rsp+0x58]
   0x000000000004ceb7 <+895>:	mov    QWORD PTR [rsp+0x28],r9
   0x000000000004cebc <+900>:	mov    DWORD PTR [rsp+0x18],r11d
   0x000000000004cec1 <+905>:	call   0x4be3b <pop_arg>
   0x000000000004cec6 <+910>:	mov    r11d,DWORD PTR [rsp+0x18]
   0x000000000004cecb <+915>:	mov    r9,QWORD PTR [rsp+0x28]
   0x000000000004ced0 <+920>:	jmp    0x4cedb <printf_core+931>
   0x000000000004ced2 <+922>:	test   r15,r15
   0x000000000004ced5 <+925>:	je     0x4cc39 <printf_core+257>
   0x000000000004cedb <+931>:	movsx  r8d,BYTE PTR [r14-0x1]
   0x000000000004cee0 <+936>:	test   r11d,r11d
   0x000000000004cee3 <+939>:	mov    r10d,r8d
   0x000000000004cee6 <+942>:	je     0x4cefa <printf_core+962>
   0x000000000004cee8 <+944>:	mov    al,r8b
   0x000000000004ceeb <+947>:	and    eax,0xf
   0x000000000004ceee <+950>:	cmp    al,0x3
   0x000000000004cef0 <+952>:	jne    0x4cefa <printf_core+962>
   0x000000000004cef2 <+954>:	and    r10d,0xffffffdf
   0x000000000004cef6 <+958>:	movsx  r8d,r10b
   0x000000000004cefa <+962>:	mov    eax,r12d
   0x000000000004cefd <+965>:	and    eax,0xfffeffff
   0x000000000004cf02 <+970>:	test   r12d,0x2000
   0x000000000004cf09 <+977>:	cmovne r12d,eax
   0x000000000004cf0d <+981>:	lea    eax,[r8-0x41]
   0x000000000004cf11 <+985>:	cmp    eax,0x37
   0x000000000004cf14 <+988>:	ja     0x4d280 <printf_core+1864>
   0x000000000004cf1a <+994>:	mov    edx,eax
   0x000000000004cf1c <+996>:	lea    rax,[rip+0x3a2cd]        # 0x871f0
   0x000000000004cf23 <+1003>:	movsxd rdx,DWORD PTR [rax+rdx*4]
   0x000000000004cf27 <+1007>:	add    rax,rdx
   0x000000000004cf2a <+1010>:	jmp    rax
   0x000000000004cf2c <+1012>:	cmp    r11d,0x7
   0x000000000004cf30 <+1016>:	ja     0x4cc39 <printf_core+257>
   0x000000000004cf36 <+1022>:	lea    rax,[rip+0x3a393]        # 0x872d0
   0x000000000004cf3d <+1029>:	mov    edx,r11d
   0x000000000004cf40 <+1032>:	movsxd rdx,DWORD PTR [rax+rdx*4]
   0x000000000004cf44 <+1036>:	add    rax,rdx
   0x000000000004cf47 <+1039>:	jmp    rax
   0x000000000004cf49 <+1041>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004cf51 <+1049>:	mov    ebx,DWORD PTR [rsp+0xc]
   0x000000000004cf55 <+1053>:	mov    DWORD PTR [rax],ebx
   0x000000000004cf57 <+1055>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004cf5c <+1060>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004cf64 <+1068>:	mov    ebx,DWORD PTR [rsp+0xc]
   0x000000000004cf68 <+1072>:	mov    WORD PTR [rax],bx
   0x000000000004cf6b <+1075>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004cf70 <+1080>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004cf78 <+1088>:	mov    bl,BYTE PTR [rsp+0xc]
   0x000000000004cf7c <+1092>:	mov    BYTE PTR [rax],bl
   0x000000000004cf7e <+1094>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004cf83 <+1099>:	movsxd rax,DWORD PTR [rsp+0xc]
   0x000000000004cf88 <+1104>:	mov    rdx,QWORD PTR [rsp+0x80]
   0x000000000004cf90 <+1112>:	mov    QWORD PTR [rdx],rax
   0x000000000004cf93 <+1115>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004cf98 <+1120>:	cmp    ebp,0x10
   0x000000000004cf9b <+1123>:	mov    eax,0x10
   0x000000000004cfa0 <+1128>:	mov    r8d,0x78
   0x000000000004cfa6 <+1134>:	cmovb  ebp,eax
   0x000000000004cfa9 <+1137>:	or     r12d,0x8
   0x000000000004cfad <+1141>:	mov    rdx,QWORD PTR [rsp+0x80]
   0x000000000004cfb5 <+1149>:	mov    ecx,r8d
   0x000000000004cfb8 <+1152>:	lea    r9,[rsp+0xc0]
   0x000000000004cfc0 <+1160>:	and    ecx,0x20
   0x000000000004cfc3 <+1163>:	mov    rax,rdx
   0x000000000004cfc6 <+1166>:	test   rax,rax
   0x000000000004cfc9 <+1169>:	je     0x4cfeb <printf_core+1203>
   0x000000000004cfcb <+1171>:	mov    rsi,rax
   0x000000000004cfce <+1174>:	lea    rdi,[rip+0x3a31b]        # 0x872f0 <xdigits>
   0x000000000004cfd5 <+1181>:	mov    r10b,cl
   0x000000000004cfd8 <+1184>:	and    esi,0xf
   0x000000000004cfdb <+1187>:	dec    r9
   0x000000000004cfde <+1190>:	shr    rax,0x4
   0x000000000004cfe2 <+1194>:	or     r10b,BYTE PTR [rdi+rsi*1]
   0x000000000004cfe6 <+1198>:	mov    BYTE PTR [r9],r10b
   0x000000000004cfe9 <+1201>:	jmp    0x4cfc6 <printf_core+1166>
   0x000000000004cfeb <+1203>:	test   rdx,rdx
   0x000000000004cfee <+1206>:	lea    r10,[rip+0x3a4fe]        # 0x874f3
   0x000000000004cff5 <+1213>:	je     0x4d103 <printf_core+1483>
   0x000000000004cffb <+1219>:	test   r12b,0x8
   0x000000000004cfff <+1223>:	je     0x4d103 <printf_core+1483>
   0x000000000004d005 <+1229>:	sar    r8d,0x4
   0x000000000004d009 <+1233>:	mov    r11d,0x2
   0x000000000004d00f <+1239>:	movsxd r8,r8d
   0x000000000004d012 <+1242>:	lea    r14,[r10+r8*1]
   0x000000000004d016 <+1246>:	jmp    0x4d109 <printf_core+1489>
   0x000000000004d01b <+1251>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004d023 <+1259>:	lea    r9,[rsp+0xc0]
   0x000000000004d02b <+1267>:	test   rax,rax
   0x000000000004d02e <+1270>:	je     0x4d044 <printf_core+1292>
   0x000000000004d030 <+1272>:	mov    dl,al
   0x000000000004d032 <+1274>:	dec    r9
   0x000000000004d035 <+1277>:	shr    rax,0x3
   0x000000000004d039 <+1281>:	and    edx,0x7
   0x000000000004d03c <+1284>:	add    edx,0x30
   0x000000000004d03f <+1287>:	mov    BYTE PTR [r9],dl
   0x000000000004d042 <+1290>:	jmp    0x4d02b <printf_core+1267>
   0x000000000004d044 <+1292>:	xor    r11d,r11d
   0x000000000004d047 <+1295>:	test   r12b,0x8
   0x000000000004d04b <+1299>:	lea    r14,[rip+0x3a4a1]        # 0x874f3
   0x000000000004d052 <+1306>:	je     0x4d109 <printf_core+1489>
   0x000000000004d058 <+1312>:	lea    rdx,[rsp+0xc0]
   0x000000000004d060 <+1320>:	movsxd rax,ebp
   0x000000000004d063 <+1323>:	sub    rdx,r9
   0x000000000004d066 <+1326>:	cmp    rdx,rax
   0x000000000004d069 <+1329>:	jl     0x4d109 <printf_core+1489>
   0x000000000004d06f <+1335>:	lea    ebp,[rdx+0x1]
   0x000000000004d072 <+1338>:	jmp    0x4d109 <printf_core+1489>
   0x000000000004d077 <+1343>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004d07f <+1351>:	test   rax,rax
   0x000000000004d082 <+1354>:	jns    0x4d097 <printf_core+1375>
   0x000000000004d084 <+1356>:	neg    rax
   0x000000000004d087 <+1359>:	mov    r11d,0x1
   0x000000000004d08d <+1365>:	mov    QWORD PTR [rsp+0x80],rax
   0x000000000004d095 <+1373>:	jmp    0x4d0d8 <printf_core+1440>
   0x000000000004d097 <+1375>:	test   r12d,0x800
   0x000000000004d09e <+1382>:	mov    r11d,0x1
   0x000000000004d0a4 <+1388>:	lea    r14,[rip+0x3a449]        # 0x874f4
   0x000000000004d0ab <+1395>:	jne    0x4d0df <printf_core+1447>
   0x000000000004d0ad <+1397>:	mov    eax,r12d
   0x000000000004d0b0 <+1400>:	lea    r10,[rip+0x3a43e]        # 0x874f5
   0x000000000004d0b7 <+1407>:	and    eax,0x1
   0x000000000004d0ba <+1410>:	cmp    eax,0x1
   0x000000000004d0bd <+1413>:	sbb    r11d,r11d
   0x000000000004d0c0 <+1416>:	inc    r11d
   0x000000000004d0c3 <+1419>:	test   eax,eax
   0x000000000004d0c5 <+1421>:	lea    rax,[rip+0x3a427]        # 0x874f3
   0x000000000004d0cc <+1428>:	cmovne rax,r10
   0x000000000004d0d0 <+1432>:	mov    r14,rax
   0x000000000004d0d3 <+1435>:	jmp    0x4d0df <printf_core+1447>
   0x000000000004d0d5 <+1437>:	xor    r11d,r11d
   0x000000000004d0d8 <+1440>:	lea    r14,[rip+0x3a414]        # 0x874f3
   0x000000000004d0df <+1447>:	mov    rdi,QWORD PTR [rsp+0x80]
   0x000000000004d0e7 <+1455>:	lea    rsi,[rsp+0xc0]
   0x000000000004d0ef <+1463>:	mov    DWORD PTR [rsp+0x18],r11d
   0x000000000004d0f4 <+1468>:	call   0x4be01 <fmt_u>
   0x000000000004d0f9 <+1473>:	mov    r11d,DWORD PTR [rsp+0x18]
   0x000000000004d0fe <+1478>:	mov    r9,rax
   0x000000000004d101 <+1481>:	jmp    0x4d109 <printf_core+1489>
   0x000000000004d103 <+1483>:	xor    r11d,r11d
   0x000000000004d106 <+1486>:	mov    r14,r10
   0x000000000004d109 <+1489>:	mov    eax,r12d
   0x000000000004d10c <+1492>:	and    eax,0xfffeffff
   0x000000000004d111 <+1497>:	test   ebp,ebp
   0x000000000004d113 <+1499>:	cmovns r12d,eax
   0x000000000004d117 <+1503>:	cmp    QWORD PTR [rsp+0x80],0x0
   0x000000000004d120 <+1512>:	sete   dl
   0x000000000004d123 <+1515>:	test   ebp,ebp
   0x000000000004d125 <+1517>:	jne    0x4d12f <printf_core+1527>
   0x000000000004d127 <+1519>:	test   dl,dl
   0x000000000004d129 <+1521>:	jne    0x4d294 <printf_core+1884>
   0x000000000004d12f <+1527>:	lea    rax,[rsp+0xc0]
   0x000000000004d137 <+1535>:	movzx  edx,dl
   0x000000000004d13a <+1538>:	movsxd rbp,ebp
   0x000000000004d13d <+1541>:	sub    rax,r9
   0x000000000004d140 <+1544>:	add    rax,rdx
   0x000000000004d143 <+1547>:	cmp    rax,rbp
   0x000000000004d146 <+1550>:	cmovge rbp,rax
   0x000000000004d14a <+1554>:	jmp    0x4d28a <printf_core+1874>
   0x000000000004d14f <+1559>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004d157 <+1567>:	mov    rdi,QWORD PTR [rsp+0x50]
   0x000000000004d15c <+1572>:	and    r12d,0xfffeffff
   0x000000000004d163 <+1579>:	xor    r11d,r11d
   0x000000000004d166 <+1582>:	lea    r14,[rip+0x3a386]        # 0x874f3
   0x000000000004d16d <+1589>:	mov    ebp,0x1
   0x000000000004d172 <+1594>:	mov    BYTE PTR [rsp+0xbf],al
   0x000000000004d179 <+1601>:	lea    r9,[rdi+0x2a]
   0x000000000004d17d <+1605>:	lea    rax,[rsp+0xc0]
   0x000000000004d185 <+1613>:	jmp    0x4d2a1 <printf_core+1897>
   0x000000000004d18a <+1618>:	call   0x1d317 <__errno_location>
   0x000000000004d18f <+1623>:	mov    edi,DWORD PTR [rax]
   0x000000000004d191 <+1625>:	call   0x1d370 <strerror>
   0x000000000004d196 <+1630>:	mov    r9,rax
   0x000000000004d199 <+1633>:	jmp    0x4d1b1 <printf_core+1657>
   0x000000000004d19b <+1635>:	mov    r9,QWORD PTR [rsp+0x80]
   0x000000000004d1a3 <+1643>:	lea    rax,[rip+0x3a353]        # 0x874fd
   0x000000000004d1aa <+1650>:	test   r9,r9
   0x000000000004d1ad <+1653>:	cmove  r9,rax
   0x000000000004d1b1 <+1657>:	movsxd r13,ebp
   0x000000000004d1b4 <+1660>:	xor    esi,esi
   0x000000000004d1b6 <+1662>:	mov    rdi,r9
   0x000000000004d1b9 <+1665>:	mov    rdx,r13
   0x000000000004d1bc <+1668>:	mov    QWORD PTR [rsp+0x18],r9
   0x000000000004d1c1 <+1673>:	call   0x507f0 <memchr>
   0x000000000004d1c6 <+1678>:	test   rax,rax
   0x000000000004d1c9 <+1681>:	mov    r9,QWORD PTR [rsp+0x18]
   0x000000000004d1ce <+1686>:	jne    0x4d1d6 <printf_core+1694>
   0x000000000004d1d0 <+1688>:	lea    rax,[r9+r13*1]
   0x000000000004d1d4 <+1692>:	jmp    0x4d1db <printf_core+1699>
   0x000000000004d1d6 <+1694>:	mov    ebp,eax
   0x000000000004d1d8 <+1696>:	sub    ebp,r9d
   0x000000000004d1db <+1699>:	and    r12d,0xfffeffff
   0x000000000004d1e2 <+1706>:	xor    r11d,r11d
   0x000000000004d1e5 <+1709>:	lea    r14,[rip+0x3a307]        # 0x874f3
   0x000000000004d1ec <+1716>:	jmp    0x4d2a1 <printf_core+1897>
   0x000000000004d1f1 <+1721>:	mov    rax,QWORD PTR [rsp+0x80]
   0x000000000004d1f9 <+1729>:	mov    DWORD PTR [rsp+0x7c],0x0
   0x000000000004d201 <+1737>:	or     ebp,0xffffffff
   0x000000000004d204 <+1740>:	mov    DWORD PTR [rsp+0x78],eax
   0x000000000004d208 <+1744>:	mov    rax,QWORD PTR [rsp+0x48]
   0x000000000004d20d <+1749>:	mov    QWORD PTR [rsp+0x80],rax
   0x000000000004d215 <+1757>:	mov    r14,QWORD PTR [rsp+0x80]
   0x000000000004d21d <+1765>:	cmp    r13d,ebp
   0x000000000004d220 <+1768>:	jae    0x4d3dc <printf_core+2212>
   0x000000000004d226 <+1774>:	mov    esi,DWORD PTR [r14]
   0x000000000004d229 <+1777>:	test   esi,esi
   0x000000000004d22b <+1779>:	je     0x4d3dc <printf_core+2212>
   0x000000000004d231 <+1785>:	mov    rdi,QWORD PTR [rsp+0x40]
   0x000000000004d236 <+1790>:	add    r14,0x4
   0x000000000004d23a <+1794>:	call   0x3a422 <wctomb>
   0x000000000004d23f <+1799>:	test   eax,eax
   0x000000000004d241 <+1801>:	js     0x4ccf9 <printf_core+449>
   0x000000000004d247 <+1807>:	mov    edx,ebp
   0x000000000004d249 <+1809>:	sub    edx,r13d
   0x000000000004d24c <+1812>:	cmp    eax,edx
   0x000000000004d24e <+1814>:	ja     0x4d3dc <printf_core+2212>
   0x000000000004d254 <+1820>:	add    r13d,eax
   0x000000000004d257 <+1823>:	jmp    0x4d21d <printf_core+1765>
   0x000000000004d259 <+1825>:	push   QWORD PTR [rsp+0x88]
   0x000000000004d260 <+1832>:	push   QWORD PTR [rsp+0x88]
   0x000000000004d267 <+1839>:	mov    edx,ebp
   0x000000000004d269 <+1841>:	mov    ecx,r12d
   0x000000000004d26c <+1844>:	mov    esi,ebx
   0x000000000004d26e <+1846>:	mov    rdi,r15
   0x000000000004d271 <+1849>:	call   0x4c030 <fmt_fp>
   0x000000000004d276 <+1854>:	mov    r13d,eax
   0x000000000004d279 <+1857>:	pop    rax
   0x000000000004d27a <+1858>:	pop    rdx
   0x000000000004d27b <+1859>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004d280 <+1864>:	lea    r14,[rip+0x3a26c]        # 0x874f3
   0x000000000004d287 <+1871>:	xor    r11d,r11d
   0x000000000004d28a <+1874>:	lea    rax,[rsp+0xc0]
   0x000000000004d292 <+1882>:	jmp    0x4d2a1 <printf_core+1897>
   0x000000000004d294 <+1884>:	lea    rax,[rsp+0xc0]
   0x000000000004d29c <+1892>:	xor    ebp,ebp
   0x000000000004d29e <+1894>:	mov    r9,rax
   0x000000000004d2a1 <+1897>:	sub    rax,r9
   0x000000000004d2a4 <+1900>:	mov    r8d,r12d
   0x000000000004d2a7 <+1903>:	mov    rdi,r15
   0x000000000004d2aa <+1906>:	mov    QWORD PTR [rsp+0x28],rax
   0x000000000004d2af <+1911>:	movsxd rax,ebp
   0x000000000004d2b2 <+1914>:	cmp    rax,QWORD PTR [rsp+0x28]
   0x000000000004d2b7 <+1919>:	cmovl  ebp,DWORD PTR [rsp+0x28]
   0x000000000004d2bc <+1924>:	mov    esi,0x20
   0x000000000004d2c1 <+1929>:	mov    QWORD PTR [rsp+0x68],r9
   0x000000000004d2c6 <+1934>:	mov    DWORD PTR [rsp+0x64],r11d
   0x000000000004d2cb <+1939>:	lea    eax,[r11+rbp*1]
   0x000000000004d2cf <+1943>:	cmp    eax,ebx
   0x000000000004d2d1 <+1945>:	mov    ecx,eax
   0x000000000004d2d3 <+1947>:	mov    DWORD PTR [rsp+0x18],eax
   0x000000000004d2d7 <+1951>:	cmovge ebx,eax
   0x000000000004d2da <+1954>:	mov    edx,ebx
   0x000000000004d2dc <+1956>:	mov    r13d,ebx
   0x000000000004d2df <+1959>:	call   0x4bfb2 <pad>
   0x000000000004d2e4 <+1964>:	movsxd rdx,DWORD PTR [rsp+0x64]
   0x000000000004d2e9 <+1969>:	mov    rsi,r14
   0x000000000004d2ec <+1972>:	mov    rdi,r15
   0x000000000004d2ef <+1975>:	call   0x4be24 <out>
   0x000000000004d2f4 <+1980>:	mov    ecx,DWORD PTR [rsp+0x18]
   0x000000000004d2f8 <+1984>:	mov    r8d,r12d
   0x000000000004d2fb <+1987>:	mov    edx,ebx
   0x000000000004d2fd <+1989>:	xor    r8d,0x10000
   0x000000000004d304 <+1996>:	mov    rdi,r15
   0x000000000004d307 <+1999>:	mov    esi,0x30
   0x000000000004d30c <+2004>:	call   0x4bfb2 <pad>
   0x000000000004d311 <+2009>:	mov    ecx,DWORD PTR [rsp+0x28]
   0x000000000004d315 <+2013>:	xor    r8d,r8d
   0x000000000004d318 <+2016>:	mov    edx,ebp
   0x000000000004d31a <+2018>:	mov    rdi,r15
   0x000000000004d31d <+2021>:	mov    esi,0x30
   0x000000000004d322 <+2026>:	call   0x4bfb2 <pad>
   0x000000000004d327 <+2031>:	mov    r9,QWORD PTR [rsp+0x68]
   0x000000000004d32c <+2036>:	mov    rdx,QWORD PTR [rsp+0x28]
   0x000000000004d331 <+2041>:	mov    rdi,r15
   0x000000000004d334 <+2044>:	mov    rsi,r9
   0x000000000004d337 <+2047>:	call   0x4be24 <out>
   0x000000000004d33c <+2052>:	mov    ecx,DWORD PTR [rsp+0x18]
   0x000000000004d340 <+2056>:	mov    r8d,r12d
   0x000000000004d343 <+2059>:	mov    edx,ebx
   0x000000000004d345 <+2061>:	xor    r8d,0x2000
   0x000000000004d34c <+2068>:	mov    esi,0x20
   0x000000000004d351 <+2073>:	mov    rdi,r15
   0x000000000004d354 <+2076>:	call   0x4bfb2 <pad>
   0x000000000004d359 <+2081>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004d35e <+2086>:	test   r15,r15
   0x000000000004d361 <+2089>:	mov    eax,DWORD PTR [rsp+0xc]
   0x000000000004d365 <+2093>:	jne    0x4d456 <printf_core+2334>
   0x000000000004d36b <+2099>:	cmp    DWORD PTR [rsp+0x60],0x0
   0x000000000004d370 <+2104>:	je     0x4cea6 <printf_core+878>
   0x000000000004d376 <+2110>:	mov    rbp,QWORD PTR [rsp+0x30]
   0x000000000004d37b <+2115>:	xor    ebx,ebx
   0x000000000004d37d <+2117>:	add    rbp,0x10
   0x000000000004d381 <+2121>:	mov    rax,QWORD PTR [rsp+0x20]
   0x000000000004d386 <+2126>:	lea    edx,[rbx+0x1]
   0x000000000004d389 <+2129>:	mov    esi,DWORD PTR [rax+rbx*4+0x4]
   0x000000000004d38d <+2133>:	test   esi,esi
   0x000000000004d38f <+2135>:	je     0x4d3b0 <printf_core+2168>
   0x000000000004d391 <+2137>:	mov    rdx,QWORD PTR [rsp+0x10]
   0x000000000004d396 <+2142>:	mov    rdi,rbp
   0x000000000004d399 <+2145>:	inc    rbx
   0x000000000004d39c <+2148>:	add    rbp,0x10
   0x000000000004d3a0 <+2152>:	call   0x4be3b <pop_arg>
   0x000000000004d3a5 <+2157>:	cmp    rbx,0x9
   0x000000000004d3a9 <+2161>:	jne    0x4d381 <printf_core+2121>
   0x000000000004d3ab <+2163>:	mov    edx,0xa
   0x000000000004d3b0 <+2168>:	mov    rbx,QWORD PTR [rsp+0x20]
   0x000000000004d3b5 <+2173>:	movsxd rax,edx
   0x000000000004d3b8 <+2176>:	lea    rcx,[rbx+rax*4]
   0x000000000004d3bc <+2180>:	xor    eax,eax
   0x000000000004d3be <+2182>:	lea    esi,[rdx+rax*1]
   0x000000000004d3c1 <+2185>:	cmp    esi,0xa
   0x000000000004d3c4 <+2188>:	je     0x4d3d5 <printf_core+2205>
   0x000000000004d3c6 <+2190>:	inc    rax
   0x000000000004d3c9 <+2193>:	cmp    DWORD PTR [rcx+rax*4-0x4],0x0
   0x000000000004d3ce <+2198>:	je     0x4d3be <printf_core+2182>
   0x000000000004d3d0 <+2200>:	jmp    0x4ccf9 <printf_core+449>
   0x000000000004d3d5 <+2205>:	mov    eax,0x1
   0x000000000004d3da <+2210>:	jmp    0x4d456 <printf_core+2334>
   0x000000000004d3dc <+2212>:	mov    r8d,r12d
   0x000000000004d3df <+2215>:	mov    ecx,r13d
   0x000000000004d3e2 <+2218>:	mov    edx,ebx
   0x000000000004d3e4 <+2220>:	mov    esi,0x20
   0x000000000004d3e9 <+2225>:	mov    rdi,r15
   0x000000000004d3ec <+2228>:	xor    ebp,ebp
   0x000000000004d3ee <+2230>:	call   0x4bfb2 <pad>
   0x000000000004d3f3 <+2235>:	mov    r14,QWORD PTR [rsp+0x80]
   0x000000000004d3fb <+2243>:	cmp    ebp,r13d
   0x000000000004d3fe <+2246>:	jb     0x4d428 <printf_core+2288>
   0x000000000004d400 <+2248>:	mov    r8d,r12d
   0x000000000004d403 <+2251>:	mov    ecx,r13d
   0x000000000004d406 <+2254>:	mov    edx,ebx
   0x000000000004d408 <+2256>:	xor    r8d,0x2000
   0x000000000004d40f <+2263>:	mov    esi,0x20
   0x000000000004d414 <+2268>:	mov    rdi,r15
   0x000000000004d417 <+2271>:	call   0x4bfb2 <pad>
   0x000000000004d41c <+2276>:	cmp    r13d,ebx
   0x000000000004d41f <+2279>:	cmovl  r13d,ebx
   0x000000000004d423 <+2283>:	jmp    0x4cc39 <printf_core+257>
   0x000000000004d428 <+2288>:	mov    esi,DWORD PTR [r14]
   0x000000000004d42b <+2291>:	test   esi,esi
   0x000000000004d42d <+2293>:	je     0x4d400 <printf_core+2248>
   0x000000000004d42f <+2295>:	mov    rdi,QWORD PTR [rsp+0x40]
   0x000000000004d434 <+2300>:	add    r14,0x4
   0x000000000004d438 <+2304>:	call   0x3a422 <wctomb>
   0x000000000004d43d <+2309>:	add    ebp,eax
   0x000000000004d43f <+2311>:	cmp    ebp,r13d
   0x000000000004d442 <+2314>:	jg     0x4d400 <printf_core+2248>
   0x000000000004d444 <+2316>:	mov    rsi,QWORD PTR [rsp+0x40]
   0x000000000004d449 <+2321>:	movsxd rdx,eax
   0x000000000004d44c <+2324>:	mov    rdi,r15
   0x000000000004d44f <+2327>:	call   0x4be24 <out>
   0x000000000004d454 <+2332>:	jmp    0x4d3fb <printf_core+2243>
   0x000000000004d456 <+2334>:	add    rsp,0xc8
   0x000000000004d45d <+2341>:	pop    rbx
   0x000000000004d45e <+2342>:	pop    rbp
   0x000000000004d45f <+2343>:	pop    r12
   0x000000000004d461 <+2345>:	pop    r13
   0x000000000004d463 <+2347>:	pop    r14
   0x000000000004d465 <+2349>:	pop    r15
   0x000000000004d467 <+2351>:	ret    
End of assembler dump.
