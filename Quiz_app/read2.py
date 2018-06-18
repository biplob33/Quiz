from models import qusetion,userprof,sets
from django.contrib.auth.models import User
event='Mains'
def get_question(nos,user):
    u=userprof.objects.get(username=(User.objects.get(username=user)))
    set_no=u.set
    year=u.Year
    question=[]
    s=sets.objects.get(no=nos)
    if set_no==1:
        q=qusetion.objects.get(no=nos,event=event,Year=year)
    elif set_no==2:
        q=qusetion.objects.get(no=s.set2_val ,event=event,Year=year)
    else:
        q=qusetion.objects.get(no=s.set3_val,event=event,Year=year)
    question.append(q.data)
    question.append(q.opt1)
    question.append(q.opt2)
    question.append(q.opt3)
    question.append(q.opt4)
    return question
def update_file(no,res,user):
    q=userprof.objects.get(username=(User.objects.get(username=user)))
    set_no=q.set
    s=sets.objects.get(no=no)
    if set_no==2:
        no=s.set2_val
    elif set_no==3:
        no=s.set3_val
    setattr(q,'q'+str(no),int(res))
    q.save()
def get_option(user,no):
    q=userprof.objects.get(username=(User.objects.get(username=user)))
    set_no=q.set
    s=sets.objects.get(no=no)
    if set_no==2:
        no=s.set2_val
    elif set_no==3:
        no=s.set3_val
    out=getattr(q, 'q'+str(no))
    return out
def get_marks(user):
    total=0
    noq=len(qusetion.objects.filter(event=event,Year='1'))
    u=userprof.objects.get(username=(User.objects.get(username=user)))
    year=u.Year
    for i in range(1,noq+1):
        qu=qusetion.objects.get(no=i,event=event,Year=year)
        if qu.ans==getattr(u, 'q'+str(i)):
            total+=4
        elif getattr(u, 'q'+str(i))!=0:
            total-=1
    u.Score=total
    u.save()
    return total
def update_time(user):
    import time
    mins=60;
    x=int(time.time()+60*mins+1)
    try:
        userprof.objects.create(username=(User.objects.get(username=user)))
    except:
        pass
    u=User.objects.get(username=user)
    q=userprof.objects.get(username=u)
    roll=u.first_name.split('/')
    t=['ECE','CSE','EE','EEE','BT','CHE','ME','CE']
    if roll[0] in t:
        q.Roll_No=u.first_name
        q.Year=17-int(roll[1])
        q.set=int(roll[2])%3+1
    else:
        q.Roll_No=u.first_name
        q.Year = 4
        q.set=int(roll[2])%3
    if q.given is False:
        q.time=x
        q.given=True
    q.save()
def get_time(user):
    import time
    q=userprof.objects.get(username=(User.objects.get(username=user)))
    end_time=q.time
    curr=time.time()
    return int(end_time-curr)