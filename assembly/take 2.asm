.model small
.stack 100h
.data
    n1 db 'Input 1:$'  
    n2 db 10,13,'Input 2:$'
    n3 db 10,13,'Input 3:$'
    n4 db 10,13,'Input 4:$'                            

.code

mov ax,@data 
mov ds,ax

; Input 1
mov ah,09h          ;request to display a string
mov dx,offset n1    
int 21h  

mov ah,01h
int 21h
sub al,30h
mov ch,al          ; store input in ch

; Input 2
mov ah,09h          ;request to display a string
mov dx,offset n2    
int 21h  

mov ah,01h
int 21h 
sub al,30h
mov bl,al          ; store input in bl

; Input 3
mov ah,09h          ;request to display a string
mov dx,offset n3    
int 21h 

mov ah,01h
int 21h 
sub al,30h
mov cl,al          ; store input in cl

; Input 4
mov ah,09h          ;request to display a string
mov dx,offset n4    
int 21h 

mov ah,01h
int 21h 
sub al,30h          ; Convert ASCII input to integer
mov dh,al           ; store the value in dh

; Newline
mov dl,10       
mov ah,02h      ; Display newline
int 21h

; - R O W  O N E - 
; Draw lines on screen
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,5        ;y-axis
mov bh,0        ;page number 
int 10h  

call hline
call hline
call hline
call hline
call hline
call hline
call hline
call hline
call hline


; - R O W  T W O - 
; Display character from ch at a specific position
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,6        ;y-axis
mov bh,0        ;page number
int 10h

call vline 


mov ah,02h
mov dl,ch       ; Display the character stored in ch
add dl,30h      ; Convert the number in ch back to ASCII
int 21h

; Display character from bl at a specific position
mov ah,02h      ;gotoxy
mov dl,17       ;x-axis
mov dh,6        ;y-axis
mov bh,0        ;page number
int 10h

mov ah,02h
mov dl,bl       ; Display the character stored in bl
add dl,30h      ; Convert the number in bl back to ASCII
int 21h

call vline 


; - R O W  T H R E E - 
; Display character from cl at a specific position
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,7        ;y-axis
mov bh,0        ;page number
int 10h

call vline 

mov ah,02h
mov dl,cl       ; Display the character stored in cl
add dl,30h      ; Convert the number in cl back to ASCII
int 21h

; Display character from dh at a specific position
mov ah,02h      ;gotoxy
mov dl,17       ;x-axis
mov dh,7        ;y-axis
mov bh,0        ;page number
int 10h

mov ah,02h
mov dl,dh       ; Display the character stored in cd
add dl,30h      ; Convert the number in dh back to ASCII
int 21h

call vline

; - R O W  F O U R - 
; Draw lines on screen
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,8        ;y-axis
mov bh,0        ;page number 
int 10h  

call hline
call hline
call hline
call hline
call hline
call hline
call hline
call hline
call hline

; Program ends
mov ah,4ch      ;return control to OS
int 21h 

; Function to display a horizontal line
hline:
mov ah,02h
mov dl,196      ; character for horizontal line
int 21h
ret 

vline:
mov ah,02h
mov dl,179      ; character for horizontal line
int 21h
ret

end