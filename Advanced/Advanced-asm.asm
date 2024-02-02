; This script will show an example of a complex assembly program!
; We will be using NASM to assemble.
; This script will compute the full fibbonachi series up to 10 terms and print each term on its own line.

;Lets Begin!

section .data                      ; Section for initializing data values
    num db 10, 0                   ; The number of Fibonacci numbers we want to calculate (10)
    f1 db 0                       ; First Fibonacci Number
    f2 db 1                       ; Second Fibonacci Number
    cnt db 0                      ; Counter for keeping track of which Fibonacci number we are on

section .bss                      ; Section for uninitialized data
    temp resb 1                   ; Temporary storage for swapping variables

section .text                     ; Section where our code is stored

global _start                     ; Linker needs this to find entry point

_start:
    mov [f1], byte 0               ; Set first Fibonacci number to zero
    mov [f2], byte 1               ; Set second Fibbinnci number to one
    mov [cnt], byte 2              ; Set counter to two since we have already printed the first two numbers

print_loop:
    push dword [cnt]              ; Push the current count onto the stack so we can use it later
    call print_dec                ; Print the current count in decimal
    add esp, 4                    ; Remove the parameter from the stack
    call printf                   ; Call the C function printf with format string \n

    mov al, '\n'                  ; Load the ASCII value of newline into AL
    call printf                   ; Call the C function printf with format string \n

    mov cl, [cnt]                 ; Move the count into CL for bitwise operations
    inc cl                        ; Increment CL by 1
    mov [temp], ch                 ; Store CH (the higher 8 bits of CL) into TEMP
    shl cl, 8                      ; Shift CL down by 8 bits
    or [f1], cl                    ; Combine CL (lower 8 bits) with F1 (higher 16 bits)
   mov [f1], cl                    ; Store the result back into F1

    pop ecx                       ; Get the count back off the stack
    cmp ecx, [num]                ; Compare ECX (current count) with NUM (total counts wanted)
    jg print_loop                 ; If ECX is greater than NUM, jump to print_loop. This continues the loop until we reach the total amount of numbers requested.

end: