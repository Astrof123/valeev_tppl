%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro


%macro print 2
    pushd
    mov rax, 1
    mov rdi, 1
    mov rsi, %1
    mov rdx, %2
    syscall
    popd
%endmacro


%macro dprint 0
   pushd
   mov rbx, 0
   mov rcx, 10
   %%divide:
       xor rdx, rdx
       div rcx

       push rdx
       inc rbx
       cmp rax, 0
       jne %%divide

   %%digit:
       pop rax
       add rax, '0'
       mov [result], rax
       print result, 1
       dec rbx
       cmp rbx, 0
       jg %%digit
   popd
%endmacro



section .text
global _start


_start:
    mov rbx, 0          ;счетчик
    mov eax, 0          ;здесь будет сумма
    mov rcx, lenx

sum_arrays:
    add eax, x[4 * rbx]
    sub eax, y[4 * rbx]

    inc rbx
    cmp rbx, rcx

    jne sum_arrays

    jmp print_sign


print_sign:
    cmp eax, 0
    jnl print_int
    print minus, 1
    
    neg eax
    jmp print_int

print_int:
    div rcx
    dprint

    cmp rdx, 0

    je end

    print dot, 1
    mov rbx, 0

    jmp print_float
    


print_float:
    inc rbx
    mov rdi, 10
    
    mov rax, rdx
    mul rdi

    div rcx
    dprint

    cmp rbx, 6
    je end
    
    cmp rdx, 0
    jne print_float
    jmp end


end:
    print newline, nlen
    print done, len
    print newline, nlen
    mov rax, 60
    xor rdi, rdi
    syscall


section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    lenx equ ($ - x) / 4
    y dd 0, 10, 1, 9, 2, 8, 5


    minus db '-'
    dot db '.'

    done db 'Done', 0xA, 0xD
    len equ $ - done
    newline db 0xA, 0xD
    nlen equ $ - newline

section .bss
    result resb 1