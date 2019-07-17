from flask import Flask, render_template , request
import inspect
variables=['name','phone','email']
'''

'''
possible_variables=['name','email','phone','access_token','token_type','expires_in','refresh_token','scope']
pv=possible_variables
def rn(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def variable_list(data,possible_variables):
    nd=[]
    pv=possible_variables
    for i in pv:
        try:
            nd.append(data[i])
        except:
            nd.append(0)
    return nd
name=1
email=1
phone=1
access_token=1
token_type=1
expires_in=1
refresh_token=1
scope=1
data={"access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
  "token_type":"bearer",
  "expires_in":3600,
  "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
  "scope":"create",
  'name':'me',
  'email':'me@gmail.com',
  'phone':'007'}

nd=variable_list(data,possible_variables)
def checkhtml(file,variables):
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    f=open(path+'\\templates\\'+file+'.plan','r')
    html=f.read()
    f.close()
    #htmlss is html split split
    #nv is needed variables (used for each line individually)
    #htmls is html split
    #linemods is line modifications which shows which lines to remove
    split='\n'
    html_split=html.splitlines()
   # print(html_split)
    htmls=html_split
    #for i in htmls:
        #print(i)

    htmlss=list(htmls)
    for i in range(0,len(htmls)):
        htmlss[i]=htmls[i].split()
    #for i in htmlss:
        #print(i)
    nv=[]
    for i in htmlss:
        nv.append([])
    for i in range(0,len(htmlss)):
        for o in range(0,len(htmlss[i])):
            try:
                if htmlss[i][o-1].index('{{')!=-1:
                    if htmlss[i][o+1].index('}}')!=-1:
                        nv[i].append(htmlss[i][o])
            except:
                None
                        
    '''               
    for i in range(0,len(htmls)):
        works=[]
        for o in range(0,len(variables)):

        
            try:
                if htmls[i].index(variables[o])!=-1:
                    works.append(True)
            except:
                works=works

        print(works)'''
    #print(nv)
    linemods=[]
    for i in nv:
        linemods.append([])
    for line in range(0,len(nv)):
        linesuccess=True
        for variable in range(0,len(nv[line])):
            if nv[line][variable] not in variables:
                linesuccess=False
                linemods[line]=False
                              
    #print(linemods)
    for i in range(0,len(htmls)):
        if linemods[i]==False:
            htmls[i]=''
    #print(htmls)
    html=''
    for i in htmls:
        if i!='':
            html=html+'\n' + i
    
    f=open(path+'\\templates\\'+file+'.html','w')
    f.write(html)
    f.close()
    return html

app = Flask(__name__)

@app.route('/')
def about():
    checkhtml('about',[])
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #checkhtml('login',[])
    if request.method == 'POST':
        text = request.form['button']
        processed_text = text.upper()
    return render_template('login.html')
@app.route("/forward/", methods=['POST'])
def logging():
    #authorisation stuff
    print('do stuff')


@app.route('/endpoint')
def end():
    name= 'me'
    email = 'email@email'
    phone='988'
    checkhtml('name',['name','phone','email'])
    return render_template('name.html',name=nd[pv.index(rn(name)[0])],email=nd[pv.index(rn(email)[0])],phone=nd[pv.index(rn(phone)[0])])
#@app.route('/hello/<name>')
#def hello(name):
    #return render_template('name.html', name=name)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
