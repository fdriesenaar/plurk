#
# Qiy Passphrase - phrase-based strong password generator
#
# freek.driesenaar@qiy.nl
# 
version="0.14.1"

# Change history
# 0.14  Freek Driesenaar
#       1. Changed default password length from 8 to 15.
#       2. Introduced the option 'not_keyboard_pattern'
# 0.14.1  Freek Driesenaar
#       3. Fixed quarter bug.

from tkinter import ttk
import datetime
import hashlib
import tkinter

class passphrase_handler:
    def __init__(self
                 ,lc_setting="1"
                 ,master_passphrase=""
                 ,month=""
                 ,num_setting="1"
                 ,not_keyboard_pattern=1
                 ,password_length=15
                 ,pincode=""
                 ,quarter="default"
                 ,sc_setting="1"
                 ,sitename=""
                 ,special_chars="default"
                 ,uc_setting="1"
                 ,username=""
                 ,year="default"
                 ):
        self.init__charsets()
        self.init__uppers()
        self.init__keyboard_neighbours()
        self.lc_setting=lc_setting
        self.master_passphrase=master_passphrase
        self.month=month
        if self.month=="default":
            self.month="{0:0>2d}".format(datetime.date.today().month)
        #self.not_keyboard_pattern=not_keyboard_pattern
        if int(not_keyboard_pattern)==0:
            self.not_keyboard_pattern=False
        else:
            self.not_keyboard_pattern=True
        self.num_setting=num_setting
        self.password_length=password_length
        self.pincode=pincode
        self.quarter=quarter
        if self.quarter=="default":
            self.quarter="Q{0:d}".format(divmod(datetime.date.today().month-1,3)[0]+1)
        self.sc_setting=sc_setting
        self.sitename=sitename
        self.charsets["sc"]=special_chars
        if self.charsets["sc"]=="default":
            self.charsets["sc"]=""
            for i in self.charsets["default_special"]:
                self.charsets["sc"]=self.charsets["sc"]+i
        self.uc_setting=uc_setting
        self.username=username
        self.year=year
        if self.year=="default":
            self.year="{0:4d}".format(datetime.date.today().year)
    def init__charsets(self):
        self.charsets={}
        self.charsets["default_special"]=                   "!@#$%^&*()"
        self.charsets["default_special"]=self.charsets["default_special"]+"`~-_=+[{]}|;:',<.>/?"
        self.charsets["default_special"]=self.charsets["default_special"]+"\\"
        self.charsets["default_special"]=self.charsets["default_special"]+"\""
        self.charsets["num"]="0123456789"
        self.charsets["lc"]="abcdefghijklmnopqrstuvwxyz"
        self.charsets["uc"]=self.charsets["lc"].upper()
    def init__keyboard_neighbours(self):
        l={
            'a': 'qwsz',
            'b': 'vghn',
            'c' : 'xdfv',
            'd' : 'xserfc',
            'e' : 'sw34rfd',
            'f' : 'cdrtgv',
            'g' : 'vftyhb',
            'h' : 'bgyujn',
            'i' : 'ju89ok',
            'j' : 'nhuikm',
            'k' : 'mjiol,',
            'l' : ',kop;.',
            'm' : 'njk,',
            'n' : 'bhjm',
            'o' : 'ki90pl',
            'p' : 'lo0-[;',
            'q' : '12wa',
            'r' : 'de45tf',
            's' : 'zawedx',
            't' : 'fr56yg',
            'u' : 'hy78ij',
            'v' : 'cfgb',
            'w' : 'aq23es',
            'x' : 'zsdc',
            'y' : 'gt67uh',
            'z' : 'asx',
            '`' : '1',
            '1' : '`2q',
            '2' : 'q13w',
            '3' : 'w24e',
            '4' : 'e35r',
            '5' : 'r46t',
            '6' : 't57y',
            '7' : 'y68u',
            '8' : 'u79i',
            '9' : 'i80o',
            '0' : 'o9-p',
            '-' : 'p0=[',
            '=' : '[-]',
            '[' : ';p-=]\'',
            ']' : '\'[=\\',
            '\\' : ']',
            ';' : '.lp[\'/',
            '\'' : '/;[]',
            ',' : 'mkl.',
            '.' : ',l;/',
            '/' : '.;\'',
            }
        self.keyboard_neighbours={}
        for i in l:
            self.keyboard_neighbours[i]=l[i]
            a=self.upper(i)
            b=self.upper(l[i])
            self.keyboard_neighbours[i]=self.keyboard_neighbours[i]+b
            self.keyboard_neighbours[a]=self.keyboard_neighbours[i]
    def init__uppers(self):
        l={
            '1': '!',
            '2': '@',
            '3': '#',
            '4': '$',
            '5': '%',
            '6': '^',
            '7': '&',
            '8': '*',
            '9': '(',
            '0': ')',
            '-': '_',
            '=': '+',
            '`': '~',
            '[': '{',
            ']': '}',
            '\\': '|',
            ';': ':',
            '\'': '\"',
            ',': '<',
            '.': '>',
            '/': '?',
            }
        self.uppers=l
    def upper(self,s):
        l=""
        for i in s:
            l=l+self.upper_char(i)
        return l
    def upper_char(self,char):
        c=char.upper()
        if c==char:
            c=self.uppers[char]
        return c
    def generate_password(self):
        c=""
        password=""
        print(self.keyboard_neighbours)
        for i in self.setlist:
            table=self.charsets[i]
            print(table)
            if self.not_keyboard_pattern:
                if len(c)>0:
                    print(c)
                    for j in self.keyboard_neighbours[c]:
                        table=table.replace(j,'')
            print(table)
            c=table[self.random(len(table))]
            password=c+password
        return password
    def password(self
                 ,passphrase
                 ,lc_setting="1"
                 ,master_passphrase=""
                 ,month=""
                 ,not_keyboard_pattern=1
                 ,num_setting="1"
                 ,password_length=15
                 ,pincode=""
                 ,quarter="default"
                 ,sc_setting="1"
                 ,sitename=""
                 ,special_chars="default"
                 ,uc_setting="1"
                 ,username=""
                 ,year="default"
                 ):
        self.lc_setting=lc_setting
        self.master_passphrase=master_passphrase
        self.month=month
        if self.month=="default":
            self.month="{0:0>2d}".format(datetime.date.today().month)
        print('not_keyboard_pattern '+str(not_keyboard_pattern))
        if int(not_keyboard_pattern)==0:
            self.not_keyboard_pattern=False
        else:
            self.not_keyboard_pattern=True
        print('self.not_keyboard_pattern '+str(self.not_keyboard_pattern))
        self.num_setting=num_setting
        self.password_length=password_length
        self.pincode=pincode
        self.quarter=quarter
        if self.quarter=="default":
            self.quarter="Q{0:d}".format(divmod(datetime.date.today().month-1,3)[0]+1)
        self.sc_setting=sc_setting
        self.sitename=sitename
        self.charsets["sc"]=special_chars
        if self.charsets["sc"]=="default":
            self.charsets["sc"]=""
            for i in self.charsets["default_special"]:
                self.charsets["sc"]=self.charsets["sc"]+i
        self.uc_setting=uc_setting
        self.username=username
        self.year=year
        if self.year=="default":
            self.year="{0:4d}".format(datetime.date.today().year)

        pp=self.master_passphrase\
        +self.sitename\
        +self.username\
        +self.year\
        +self.quarter\
        +self.month\
        +self.pincode\
        +passphrase
        hd=hashlib.sha256(pp.encode('utf-8')).hexdigest()
        self.hash=int(hd,16)
        self.gamble()
        pw=self.generate_password()
        return pw
    def gamble(self):
        self.settings={}
        self.settings['lc']=int(self.lc_setting)
        self.settings['uc']=int(self.uc_setting)
        self.settings['num']=int(self.num_setting)
        self.settings['sc']=int(self.sc_setting)
        # determine nofs
        self.nofs={}
        self.nofs["lc"]=-1
        self.nofs["uc"]=-1
        self.nofs["num"]=-1
        self.nofs["sc"]=-1
        # What's the jackpot?
        self.jackpot=self.password_length
        order=[]
        order.append('lc')
        order.append('uc')
        order.append('num')
        order.append('sc')
        # Who's the winner?
        for i in order:
            if self.settings[i]>=0:
                winner=i
#        print("role the dice")
        for i in order:
            self.nofs[i]=0
            if i==winner:
                self.nofs[i]=self.jackpot
                break
            if self.settings[i]<0:
                self.nofs[i]=0
            else:
                self.nofs[i]=self.roll_dice(minimum_value=self.settings[i])
                self.jackpot=self.jackpot-self.nofs[i]
#        print("compose setlist")
        self.setlist=[]
        for i in order:
            for j in range(self.nofs[i]):
                self.setlist.append(i)
        self.setlist=self.shuffle(self.setlist)
    def random(self,max_val_plus_one):
        (d,r)=divmod(self.hash,max_val_plus_one)
        self.hash=self.hash+d
        return r
    def roll_dice(self,minimum_value=0):
        jackpot=self.jackpot
        for i in self.nofs:
            if self.nofs[i]<0:
                if self.settings[i]>=0:
                    jackpot=jackpot-1
        numbers=range(minimum_value,jackpot+1)
        return numbers[self.random(len(numbers))]
    def shuffle(self,l):
        shuffled=[]
        r=[]
        aid=[]
        for i in range(len(l)):
            r.append(i)
        for i in l:
            x=self.random(len(r))
            aid.append(r[x])
            r.remove(r[x])
        for i in aid:
            shuffled.append(l[i])
        return shuffled
    def get__lc_setting(self):
        return self.lc_setting
    def get__month(self):
        return self.month
    def get__not_keyboard_pattern(self):
        return self.not_keyboard_pattern
    def get__num_setting(self):
        return self.num_setting
    def get__password_length(self):
        return self.password_length
    def get__pincode(self):
        return self.pincode
    def get__passphrase(self):
        return self.master_passphrase
    def get__sc_setting(self):
        return self.sc_setting

    def get__special_chars(self):
        return self.charsets["sc"]
    def get__quarter(self,option=""):
        q=self.quarter
        if option=="next quarter":
            q=divmod(datetime.date.today().month-1,3)[0]+1
            q="Q"+str(divmod(q,4)[1]+1)
        return q
    def get__uc_setting(self):
        return self.uc_setting
    def get__year(self,option=""):
        y=self.year
        if option=="next quarter":
            yi=datetime.date.today().year
            nq=divmod(datetime.date.today().month-1,3)[0]+1
            y=str(yi+divmod(nq,4)[0])
        return y
    def set__master_passphrase(self,master_passphrase):
        self.master_passphrase=master_passphrase
    def set__month(self,month):
        self.month=month
    def set__not_keyboard_pattern(self,not_keyboard_pattern):
        self.not_keyboard_pattern=not_keyboard_pattern
    def set__password_length(self,password_length):
        self.password_length=int(password_length)
    def set__quarter(self,quarter):
        self.quarter=quarter
    def set__special_chars(self,special_chars):
        self.special_chars=special_chars
        if self.special_chars=="default":
            self.special_chars=self.default_special_chars
        self.table=self.default_table+self.special_chars
    def set__sitename(self,sitename):
        self.sitename=sitename
    def set__username(self,username):
        self.username=username
    def set__year(self,year):
        self.year=year

class option():
    def __init__(self,text="",style="",row=0,column=0):
        self.val=tkinter.StringVar()
        self.label=ttk.Label(text=text,style=style)
        self.none=ttk.Entry(textvariable=val,style=style)
        self.row=row
        return
    def get(self):
        return self.val.get()
    def grid(self):
        self.label.grid(row=self.row,column=0)
        self.none.grid(row=self.row,column=1)
    def set(self,val):
        self.val.set(val)
    
class label_entry():
    def __init__(self,text="",style="",row=0):
        self.label=ttk.Label(text=text,style=style)
        self.row=row
        self.sv=tkinter.StringVar()
        self.entry=ttk.Entry(textvariable=self.sv,show='*')
        self.entry.bind('<FocusIn>',self.on__focus_in)
        self.entry.bind('<FocusOut>',self.on__focus_out)
        return
    def bind(self,event,callback):
        self.entry.bind(event,callback)
    def get(self):
        return self.sv.get()
    def grid(self):
        self.label.grid(row=self.row,column=0)
        self.entry.grid(row=self.row,column=1)
    def on__focus_in(self,event):
        self.entry['show']=''
    def on__focus_out(self,event):
        self.entry['show']='*'
    def set(self,val):
        return self.sv.set(val)

    
class gui():
    def __init__(self):
        self.ph=passphrase_handler()
        self.root = tkinter.Tk()
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="white")
        self.wickets={}
        self.wickets['passphrase']=label_entry(row=0,text="Passphrase",style="BW.TLabel")
        self.wickets['pincode']=label_entry(row=1,text="Pincode",style="BW.TLabel")
        self.wickets['site_name']= label_entry(row=2,text="Site name",style="BW.TLabel")
        self.wickets['username']=  label_entry(row=3,text="Username",style="BW.TLabel")
        self.wickets['year']=      label_entry(row=4,text="Year",style="BW.TLabel")
        self.wickets['quarter']=   label_entry(row=5,text="Quarter",style="BW.TLabel")
        self.wickets['month']=   label_entry(row=6,text="Month",style="BW.TLabel")
        self.wickets['special_chars']=   label_entry(row=7,text="Special chars",style="BW.TLabel")
        self.wickets['password']=  label_entry(row=8,text="Password",style="BW.TLabel")
        self.wickets['lc_setting']= label_entry(row=9,text="Lower case setting",style="BW.TLabel")
        self.wickets['uc_setting']= label_entry(row=10,text="Upper case setting",style="BW.TLabel")
        self.wickets['num_setting']= label_entry(row=11,text="Numerical setting",style="BW.TLabel")
        self.wickets['not_keyboard_pattern']= label_entry(row=12,text="Not a keyboard pattern",style="BW.TLabel")
        self.wickets['special_setting']= label_entry(row=13,text="Special char setting",style="BW.TLabel")
        self.wickets['pw_length']= label_entry(row=14,text="Password length",style="BW.TLabel")
        self.wickets['reset']=ttk.Button(text='Reset',command=self.reset)
        self.wickets['ok']=ttk.Button(text='OK',command=self.callback)
        self.reset()
    def callback(self):
        pw=self.ph.password(""
            ,master_passphrase=self.wickets['passphrase'].get()
            ,pincode=self.wickets['pincode'].get()
            ,sitename=self.wickets['site_name'].get()
            ,username=self.wickets['username'].get()
            ,year=self.wickets['year'].get()
            ,quarter=self.wickets['quarter'].get()
            ,month=self.wickets['month'].get()
            ,not_keyboard_pattern=self.wickets['not_keyboard_pattern'].get()
            ,special_chars=self.wickets['special_chars'].get()
            ,lc_setting=self.wickets['lc_setting'].get()
            ,uc_setting=self.wickets['uc_setting'].get()
            ,num_setting=self.wickets['num_setting'].get()
            ,sc_setting=self.wickets['special_setting'].get()
            ,password_length=int(self.wickets['pw_length'].get())
            )
        self.wickets['password'].set(pw)
        self.wickets['ok'].clipboard_clear()
        self.wickets['ok'].clipboard_append(pw)
    def grid(self):
        for i in self.wickets:
            self.wickets[i].grid()
            self.wickets[i].bind('<Key-Return>',self.on_enter)
        self.wickets['reset'].grid(row=15,column=0)
        self.wickets['ok'].grid(row=15,column=1)
    def mainloop(self):
        self.root.mainloop()
    def on_enter(self,event):
        self.callback()
    def reset(self):
        self.wickets['ok'].clipboard_clear()
        self.wickets['ok'].clipboard_append("")
        self.ph=passphrase_handler()
#        self.wickets['passphrase'].set("")
#        self.wickets['site_name'].set("")
#        self.wickets['username'].set("")
        self.wickets['year'].set(self.ph.get__year())
        self.wickets['quarter'].set(self.ph.get__quarter())
        self.wickets['month'].set(self.ph.get__month())
        self.wickets['special_chars'].set(self.ph.get__special_chars())
        self.wickets['password'].set("")
        self.wickets['lc_setting'].set(self.ph.get__lc_setting())
        self.wickets['uc_setting'].set(self.ph.get__uc_setting())
        self.wickets['num_setting'].set(self.ph.get__num_setting())
        self.wickets['not_keyboard_pattern'].set(self.ph.get__not_keyboard_pattern())
        self.wickets['special_setting'].set(self.ph.get__sc_setting())
        self.wickets['pw_length'].set(str(self.ph.get__password_length()))
        

pp=gui()
pp.grid()
pp.mainloop()
