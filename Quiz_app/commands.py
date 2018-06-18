from django.contrib.auth.models import User
from models import qusetion,sets
event='Mains'
def create():
    #names=['Suyash','Aman','Ankita','Apurva','Ashish','Roshan','Gaurav','Inderjeet','Tamo','Smriti','Hari','Prince','Pramod','Anil1','Sourav','Nivesh','Chandan','Kumod','Thomas','Tadh','Kardikay','Ashutosh','Ravi','Abhishek','Shubham','Ravi1','Tenzing','Jaidev','Shivaji','Santosh','Sandeep','Anand','Praveen','Tsang','Devendro','Anonya','Shubham1','Tarun','Ravindra','Hari1','Saiteja','Meher','Kaushik']
    #rolls=['BT/14/06','ECE/16/07','ECE/15/02','ECE/15/27','ECE/15/26','ECE/15/18','ECE/15/28','CSE/15/04','BT/15/07','BT/15/12','EE/14/13','EE/15/35','EE/14/17','EE/16/17','ECE/16/40','ECE/15/15','EE/15/07','CSE/15/16','ECE/15/07','ECE/15/11','EE/16/10','CHE/16/10','CHE/16/13','ECE/16/04','ME/16/10','ME/16/12','EE/15/01','EE/15/15','ECE/15/20','ECE/15/23','CSE/15/23','EE/15/08','ECE/13/05','ECE/15/19','CE/16/051','CE/16/03','CE/16/06','ECE/16/05','ECE/16/18','ECE/16/03','EE/15/09','ECE/15/10','ES/16/02']
    names=['Gresshma','Priya','Mainak','Vidya','Bero','Shivam','Anurag','AmitKumar','Sonu','Monish','Shivaji','Sandeep']
    rolls=['ECE/15/21','CSE/15/23','ECE/15/12','CSE/15/18','ECE/15/04','CSE/15/01','CSE/15/19','ME/15/22','ME/15/26','ME/15/25','ECE/15/20','CSE/15/23']
    c=0
    for i in names:
        try:
            u=User.objects.create(username=i)
            u.first_name=rolls[c]
            c+=1
            u.save()
        except:
            pass
def setpass():
    allu=User.objects.all()
    for i in allu:
        u=User.objects.get(username=i)
        if u.is_superuser is False:
            u.set_password('electronika')
            u.save()
def create_sets():
    from random import shuffle
    #q=qusetion.objects.filter(event=event)
    total=40
    print total
    val=range(1,total+1)
    val2=range(1,total+1)
    shuffle(val)
    shuffle(val2)
    for i in range(0,total):
        try:
            s=sets.objects.create(no=(i+1))
        except:
            s=sets.objects.get(no=(i+1))
        s.set2_val=val[i]
        s.set3_val=val2[i]
        s.save()
def sendmail():
    from django.core.mail import EmailMessage
    email = EmailMessage('Test', 'Test', to=['biplobnath33@gmail.com'])
    email.send()