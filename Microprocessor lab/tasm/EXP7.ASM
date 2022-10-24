assume cs:code,ds:code,es:extra
data segment
    blk1 db 10H,20H,30H,40H,50H
data ends

extra segment
    blk2 db 05 dup(?)
    extra ends

code segment
start:
     mov Ax,data
     mov Ds,Ax

     mov Ax,extra
     mov es,Ax

     lea si,blk1
     lea di,blk2

     mov Cx,05H
     std

back:movsb
    loop back
    mov AH,4CH
    int 21H
code ends
end start
    

