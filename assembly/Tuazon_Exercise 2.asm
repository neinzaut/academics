.model small
.stack 100h
.data
    db 

.code
mov ax,@data
mov ds,ax


mov ah,02h  ; gotoxy
mov dl,0    ; x-axis
mov dh,3    ; y-axis
mov bh,0    ; page number
int 10h
mov ah,02h
mov dl,43   ; ASCII for 'C'
int 21h

; ----- CREATE HORIZONTAL LINE ----- 
mov ah,02h  ; gotoxy
mov dl,0    ; x-axis
mov dh,4    ; y-axis
mov bh,0    ; page number
int 10h
call line
call line
call line
call line
call line

; ----- INPUT FIRST NUMBER (TWO DECIMALS) ----- 
mov ah,02h  ; gotoxy
mov dl,2    ; x-axis
mov dh,1    ; y-axis
mov bh,0    ; page number
int 10h
mov ah,01h
int 21h
sub al,30h
mov bl,al   ; Store in bl (Tens)
mov ah,01h
int 21h
sub al,30h
mov cl,al   ; Store in cl (Ones)  



; ----- INPUT SECOND NUMBER (ONE DECIMAL) ----- 
mov ah,02h
mov dl,3    ; x-axis
mov dh,3    ; y-axis
mov bh,0    ; page number
int 10h
mov ah,01h
int 21h
sub ah,30h
mov ch,al   ; Store in ch (Ones)  


; ----- ADD THE NUMBERS ----- 
mov ax,0    
mov al,cl   ; Move Ones of first number to al
add al,ch   ; Add Ones of second number
aaa         ; Adjust ASCII for addition
mov ch,ah   ; Store Tens carry
mov cl,al   ; Store Ones result   


; ----- DISPLAY RESULT (ONES PLACE) ----- 
mov ah,02h
mov dl,3    ; x-axis
mov dh,5    ; y-axis
mov bh,0    ; page number
int 10h

mov ah,02h
add cl,30h
mov dl,cl
int 21h

; ----- ADD TENS CARRY ----- 
mov ax,0    
mov al,ch   ; Move Tens to al
add al,bl   ; Add Tens from first number
aaa        ; Adjust ASCII for addition
mov ch,ah   ; Store Tens result
mov cl,al   ; Store Ones result

; ----- DISPLAY RESULT ----- 
mov ah,02h  ; gotoxy
mov dl,1    ; x-axis
mov dh,5    ; y-axis
mov bh,0    ; page number
int 10h

mov ah,02h
add ch,30h
mov dl,ch
int 21h

add cl,30h
mov dl,cl
int 21h

mov ah,4ch
int 21h

; ----- DRAW HORIZONTAL LINE ----- 
line:
mov ah,02h
mov dl,196   
int 21h
ret
