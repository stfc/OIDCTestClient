from flask import Flask, render_template , request
variables=['name','phone','email']
def checkhtml(file,variables):
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    f=open(path+'/templates/'+file+'.plan','r')
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
    
    f=open(path+'/templates/'+file+'.html','w')
    f.write(html)
    f.close()
    return html

app = Flask(__name__)

@app.route('/')
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def my_form_post():
    user = ['Username']
    
    #authenticate
    return text
@app.route('/endpoint')
def end():
    name= 'me'
    email = 'email@email'
    phone='988'
    checkhtml('name',['name','phone','email'])
    return render_template('name.html',name=name,email=email,phone=phone)
#@app.route('/hello/<name>')
#def hello(name):
    #return render_template('name.html', name=name)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
