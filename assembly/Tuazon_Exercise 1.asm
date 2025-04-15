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

; ----- REQUEST USER INPUT ----- 
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
; ----- REQUEST USER INPUT ----- 



; ----- DISPLAY -----

; - R O W  O N E - 
; Draw lines on screen
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,10        ;y-axis
mov bh,0        ;page number 
int 10h  

call uright
call hline
call hline
call hline
call hline
call hline
call hline
call hline
call uleft


; - R O W  T W O - 
; Display character from ch at a specific position
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,11        ;y-axis
mov bh,0        ;page number
int 10h

call vline 


mov ah,02h
mov dl,ch       ; Display the character stored in ch
add dl,30h      ; Convert the number in ch back to ASCII
int 21h    

; Space in between
mov ah,02h      ;gotoxy
mov dl,17       ;x-axis
mov dh,11        ;y-axis
mov bh,0        ;page number
int 10h

mov ah,02h
mov dl,bl       ; Display the character stored in bl
add dl,30h      ; Convert the number in dh back to ASCII
int 21h

call vline
; -- PAUSE DISPLAY --

  
; ----- REQUEST USER INPUT -----  
mov ah,02h      ;gotoxy
mov dl,0       ;x-axis
mov dh,1        ;y-axis
mov bh,0        ;page number 
int 10h   
  
; Input 3
mov ah,09h          ;request to display a string
mov dx,offset n3    
int 21h 

mov ah,01h
int 21h 
sub al,30h
mov ch,al          ; store input in ch

; Input 4
mov ah,09h          ;request to display a string
mov dx,offset n4    
int 21h 

mov ah,01h
int 21h 
sub al,30h          ; Convert ASCII input to integer
mov bl,al           ; store the value in bl
; ----- END REQUEST USER INPUT ----- 
 
 
 
 
 
; ----- RESUME DISPLAY -----
; - R O W  T H R E E - 
; Display character from cl at a specific position
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,12        ;y-axis
mov bh,0        ;page number
int 10h

call vline 

mov ah,02h
mov dl,ch       ; Display the character stored in ch
add dl,30h      ; Convert the number in cl back to ASCII
int 21h

; Space in between
mov ah,02h      ;gotoxy
mov dl,17       ;x-axis
mov dh,12        ;y-axis
mov bh,0        ;page number
int 10h

mov ah,02h
mov dl,bl       ; Display the character stored in bl
add dl,30h      ; Convert the number in dh back to ASCII
int 21h

call vline

; - R O W  F O U R - 
; Draw lines on screen
mov ah,02h      ;gotoxy
mov dl,10       ;x-axis
mov dh,13        ;y-axis
mov bh,0        ;page number 
int 10h  

call dright
call hline
call hline
call hline
call hline
call hline
call hline
call hline
call dleft 
; -- END DISPLAY --

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

uright:
mov ah,02h
mov dl,218      ; character for horizontal line
int 21h
ret

uleft:
mov ah,02h
mov dl,191      ; character for horizontal line
int 21h
ret

dright:
mov ah,02h
mov dl,192      ; character for horizontal line
int 21h
ret

dleft:
mov ah,02h
mov dl,217      ; character for horizontal line
int 21h
ret

end