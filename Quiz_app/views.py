#from django.template.context_processors import request
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.shortcuts import render_to_response, render
from read2 import get_question,update_file,get_option,get_marks,update_time,get_time
noq=40
def root(request):
    return render_to_response('home.html')
def login_my_user(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)
def auth_my_user(request):
    name=request.POST.get('Name')
    passw=request.POST.get('password')
    print name,passw
    user=auth.authenticate(username=name,password=passw)
    print user
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/start/')
    else:
        return HttpResponseRedirect('/invalid/')
def logout_my_user(request):
    auth.logout(request)
    return HttpResponse('logout.html')
def update(request):
    auth.logout(request)
    return render(request,'thankyou.html')
def question(request,ah):
    username=auth.get_user(request)
    if str(username) == 'AnonymousUser':
        return HttpResponseRedirect('/login/')
    else:
        no=int(ah)
        a=get_question(no,username)
        image=False
        urli=''
        q=''
        if a[0][:1]=='1':
            urli=a[0].split('0')[0][1:]
            image=True
            q=a[0].split('0')[1]
        ques=a[0]
        opt1=a[1]
        opt2=a[2]
        opt3=a[3]
        opt4=a[4]
        x=get_option(username,no)
        opt='val'+str(x)
        time=get_time(username)
        l=range(1,noq+1)
        c={}
        c.update(csrf(request))
        context={"Ques":ques,"opt1":opt1,"opt2":opt2,"opt3":opt3,"opt4":opt4,opt:'checked','image':image,'urli':urli,'q':q,'no':no,'time':time,'Prev':(no-1),'l':l,'c':c,}
        return render(request,'question.html',context)
def question_body(request):
    username=auth.get_user(request)
    if str(username) == 'AnonymousUser':
        return HttpResponseRedirect('/login/')
    else:
        time=get_time(username)
        l=range(1,noq+1)
        context={'time':time,'l':l,}
        return render(request,'question1.html',context)
def question_or(request,ah):
    username=auth.get_user(request)
    no=int(ah)
    a=get_question(no,username)
    image=False
    urli=''
    q=''
    if a[0][:1]=='1':
        urli=a[0].split('0')[0][1:]
        image=True
        q=a[0].split('0')[1]
    ques=a[0]
    opt1=a[1]
    opt2=a[2]
    opt3=a[3]
    opt4=a[4]
    x=get_option(username,no)
    opt='val'+str(x)
    c={}
    c.update(csrf(request))
    context={"Ques":ques,"opt1":opt1,"opt2":opt2,"opt3":opt3,"opt4":opt4,opt:'checked','image':image,'urli':urli,'q':q,'no':no,'Prev':(no-1),'c':c,'Next':(noq-no),}
    return render(request,'question2.html',context)
def question_eval(request):
    res=request.POST.get('ans')
    no=request.POST.get('no')
    user=auth.get_user(request)
    print 'user=',user,'no=',no,'res=',res
    if res is not None:
        update_file(no,res,user)
    if int(no)==noq:
        url='/questions/'+str(int(no))
        return HttpResponseRedirect(url)
    else:
        url='/questions/'+str(int(no)+1)
        return HttpResponseRedirect(url)
def marks_eval(request):
    user=auth.get_user(request)
    if str(user) == 'AnonymousUser':
        return HttpResponseRedirect('/login/')
    total=get_marks(user)
    print total
    user.last_name=int(total)
    if user.is_superuser is False:
        user.set_password('1234567890')
    user.save()
    return HttpResponseRedirect('/update/')
def start(request):
    user=auth.get_user(request)
    if str(user)=='AnonymousUser' :
        return HttpResponseRedirect('/login/')
    else:
        return render(request,'start.html')
def invalid(request):
    return render(request,'invalid.html')
def time(request):
    update_time(auth.get_user(request))
    return HttpResponseRedirect('/questions/')