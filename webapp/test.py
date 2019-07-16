'''html=<html>
<body>
<h1>Hello {{ name }}!</h1>
<p>I believe your email is {{ email }} </p>
<div>
<p>I believe your phone number is  {{ phone }} </p>
</body>
</html>
'''


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
print(checkhtml('name',variables))
