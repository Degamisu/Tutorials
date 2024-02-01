; assembly is one of my favorite languages.
; it is a low-level language, so you can do things that are not possible in higher level languages like C or Java.

; There are many different types of assembly. Some people write in the "assembly language" that comes with their specific processor.
; The NES uses a 6502 processor, so the assembly language for that is called "6502 Assembly".

; We will be using NASM.
; Lets begin.

* = $10                        ; Start at address $1
start:
    ldx #$ff                   ; Load X with FFh ($FF). This sets up the stack pointer to point at the top of RAM ($0100-$01FF)
    ldx #$FF                   ; Load X with FFh - this will be our loop counter.
    loop:
        dex                     ; Decrement X by one. If it reaches zero, we'll jump to done.
        bne loop                ; Branch if not equal (X != 0). Jumps back to 'loop' if X isn't zero.
                                ; So, when X == 0, execution continues from after the bracketed block below.

    .done:
        jmp start               ; Jump to 'start', effectively making an infinite loop.

    .irq:
        sei                     ; Set Interrupt Mask Flag (disable interrupts).
        php                     ; PushProcessorStatus onto the stack. This saves the current status flags.
        pha                     ; PushA onto the stack. This saves A register.
        tay                     ; Transfer Y to A.
        pla                     ; PullA from the stack and into A. 
        plp                     ; Pull Processor Status from the stack and into the status flags.
        rti                     ; Return from Interrupt. Returns control to the instruction following the last.