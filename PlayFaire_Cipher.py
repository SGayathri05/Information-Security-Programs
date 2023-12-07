def letteronly(text):  
    output=''
    for char in text:
        if 64 < ord(char) < 91:
            if char=='J':
                char='I'
            output+=char
    return(output)
  
def massageKey(txt):    
    userkey=letteronly(txt)
    key=''
    for char in userkey:
        if char not in key:
            key+=char
    return(key)

def massageMessage(txt):    
    usrmsg=letteronly(txt)
    msg=''     
    First=True
    for i in range(len(usrmsg)):        
        if First:
            msg+=usrmsg[i]            
            if i + 1 == len(usrmsg):
                msg+='X'           
            else:
                if usrmsg[i] == usrmsg[i+1]:
                    msg+='X'
                else:
                    First=False
        else:            
            msg+=usrmsg[i]
            First=True
    return(msg)

def showgrid(key):    
    print('\nPlayfair Grid:')
    for j in range(5):
        for i in range(5):
            print(key[i+j*5],'',end='')
        print()
    print()
    return

def showmsg(msg):    
    space=True
    for char in msg:
        print(char,end='')
        space = not space
        if space:
            print(' ',end='')
    print()
    return

def playfair(enc,msg,key):
    
    offset=-1
    if enc:
        offset=+1
    output=''
    for i in range(0,len(msg),2):
    
        lett1=msg[i]
        lett2=msg[i+1]
        
        pos1=key.find(lett1)
        pos2=key.find(lett2)
        
        coord1=[pos1%5,pos1//5]
        coord2=[pos2%5,pos2//5]
        
        if coord1[0]==coord2[0]:
            coord1[1]=(coord1[1]+offset)%5
            coord2[1]=(coord2[1]+offset)%5
        
        elif coord1[1]==coord2[1]:
            coord1[0]=(coord1[0]+offset)%5
            coord2[0]=(coord2[0]+offset)%5
        
        else:
            tmp=coord2[0]
            coord2[0]=coord1[0]
            coord1[0]=tmp
        
        pos1=coord1[0]+5*coord1[1]
        pos2=coord2[0]+5*coord2[1]
        
        lett1=key[pos1]
        lett2=key[pos2]
        
        output+=lett1
        output+=lett2
    return output

def showres(msg1,msg2):
    linesize=50
    for i in range(0,len(msg1),linesize):
        showmsg(msg1[i:i+min(linesize,len(msg1)-i)])
        showmsg(msg2[i:i+min(linesize,len(msg2)-i)])
        print()
    return

userkey=(input('Please type a key: ')+'abcdefghijklmnopqrstuvwxyz').upper()
key=massageKey(userkey)

usermsg=(input('Please type a message: ')).upper()
msg=massageMessage(usermsg)
chosen=False

while not chosen:
    choice=input('(E)ncrypt or (D)ecrypt  E/D  ? : ').upper()
    if choice=='E':
        enc=True
        chosen=True
    elif choice=='D':
        enc=False
        chosen=True

showgrid(key)
newmsg=playfair(enc,msg,key)

print('showing digraphs')
showres(msg,newmsg)

print('In one chunk:')
print(newmsg)
