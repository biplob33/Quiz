import os
def get_question():
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    fo=file("Qusetions.txt")
    fi=fo
    q=[]
    while(True):
        d=fi.readline()
        if d=='':
            break
        else:
            q.append(d.strip('\n'))
    question=[]
    for i in range(0,len(q),6):
        question.append(q[i:(i+6)])
    fo.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
    return question
def update_file(no,res,user):
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    try:
        fo=file(str(user)+'.txt','a+')
    except:
        fo=file(str(user)+'.txt','w')
        fo.close()
    fo=file(str(user)+'.txt','a+')
    st=str(no)+' '+str(res)+'\n'
    fo.write(st)
    fo.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
def get_option(user,no):
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    try:
        fo=file(str(user)+'.txt','r')
    except:
        fo=file(str(user)+'.txt','w')
        fo.close()
    fo=file(str(user)+'.txt','r')
    fi=fo
    out=0
    while(True):
        d=fi.readline()
        if d=='':
            break
        else:
            q_no=int(d.split(' ')[0])
            x=d.split(' ')[1]
            try:
                int(x)
                if q_no==no:
                    out=int(x)
            except:
                out=0;
    fo.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
    return out
def get_marks(user):
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    fo=file(str(user)+'.txt','r')
    f_ans=fo
    f2=file('Qusetions.txt','r')
    f_ques=f2
    dic={}
    ans={}
    while(True):
        x=f_ans.readline()
        d=x.split(' ')
        if x=='':
            break
        else:
            try:
                int(d[1])
                dic[int(d[0])]=int(d[1])
            except:
                pass
    i=1
    total=0
    while(True):
        d=f_ques.readline()
        if d=='':
            break
        else:
            if i%6==0:
                ans[i/6]=int(d[0])
        i+=1
    for i in dic.keys():
        if dic[i]==ans[i]:
            total+=4
        else:
            total-=1
    fo.close()
    f2.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
    return total
def update_time(user):
    import time
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    try:
        fo=file(str(user)+'time.txt','a+')
    except:
        fo=file(str(user)+'time.txt','w')
        fo.close()
    fo=file(str(user)+'time.txt','a+')
    min=30;
    x=int(time.time()+60*min+1)
    fo.write(str(x)+'\n')
    fo.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
def get_time(user):
    import time
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz\Files')
    try:
        fo=file(str(user)+'time.txt','a+')
    except:
        fo=file(str(user)+'time.txt','w')
        fo.close()
    fo=file(str(user)+'time.txt','r')
    end_time=float(fo.readline())
    curr=time.time()
    fo.close()
    os.chdir('C:\Users\Biplob Nath\workspace\Python\Quiz')
    return int(end_time-curr)