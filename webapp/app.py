import datetime
import flask
import logging
import inspect
import requests
import json

from flask import Flask, jsonify, render_template , request
from flask_pyoidc.flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ProviderConfiguration, ClientMetadata
from flask_pyoidc.user_session import UserSession

app = Flask(__name__)

# See http://flask.pocoo.org/docs/0.12/config/
app.config.update({'SERVER_NAME': 'IP GOES HERE',
                   'SECRET_KEY': 'dev_key',  # make sure to change this!!
                   'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=7).total_seconds(),
                   'PREFERRED_URL_SCHEME': 'http',
                   'DEBUG': True})

ISSUER = 'ISSUER GOES HERE'
CLIENT = 'CLIENT GOES HERE'
CLIENTSECRET = 'SECRET GOES HERE'
PROVIDER_NAME = 'NAME GOES HERE'
sslSession = requests.session()
#sslSession.verify_ssl = False
sslSession.verify_ssl = True
#sslSession.path = "/etc/pki/tls/certs/ca-bundle.crt" 
sslSession.verify = "/etc/pki/tls/certs/ca-bundle.crt"
PROVIDER_CONFIG = ProviderConfiguration(issuer=ISSUER,
                                         client_metadata=ClientMetadata(CLIENT, CLIENTSECRET), requests_session = sslSession)
auth = OIDCAuthentication({PROVIDER_NAME: PROVIDER_CONFIG})

data=0
variables=['name','phone','email']
possible_variables=['name','email','phone','access_token','token_type','expires_in','refresh_token','scope']
pv=possible_variables
def rn(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
def rn2(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
def rn3(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return str([k for k, v in callers_local_vars if v is var][0])
def variable_list(data,possible_variables):
    nd=[]
    pv=possible_variables
    for i in pv:
        try:
            nd.append(data[i])
        except:
            nd.append(0)
    return nd
def checkhtml(file,variables):
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    f=open(path+'//templates//'+file+'.plan','r')
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
    f=open(path+'//templates//'+file+'.html','w')
    f.write(html)
    f.close()
    return html


@auth.error_view
def error(error=None, error_description=None):
    return jsonify({'error': error, 'message': error_description})

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

@app.route('/logout')
@auth.oidc_logout
def logout():
    return "You've been successfully logged out!"

@app.route("/forward/", methods=['POST'])

@auth.oidc_auth(PROVIDER_NAME)


def loggin():
    #authorisation stuff
    user_session = UserSession(flask.session)
    user_session.verify_ssl = True
    user_session.verify = "/etc/pki/tls/certs/ca-bundle.crt"
    data = jsonify(access_token=user_session.access_token,
                   id_token=user_session.id_token,
                   userinfo=user_session.userinfo)
    global parseddata
    parseddata= json.loads(data)
    return data
    
@app.route('/endpoint')
def end():
    name='h,agf,jgaf,asgdfemjfgrymaymaymgarh,ayhdfga,hdfg,jadsf'
    email='ak,hdf,ahdsf,ajdhfjdhsvjfrshfja,rh,fasbhhfb,jr,srjabh'
    phone=',asrh,bsbhf,ashrbf,sjrhbfj,srbhfg,rsjhbfharbsbjfs,jfb'
    access_token='as.,hrkbahfb,arjhgrhgfrhrhfbbbbfhrhrhbhrbfarfsaf'
    token_type=',ashr,ahsbagfr,jabf,hraeghtjrea,jhgjarhg,ragaer,j'
    expires_in=',ahr,ahefrjebfjher,fbrejhfbrhefbrhjefbjfrehbfjerhfje'
    refresh_token='a,hrbf,eahb,jtrgtrht,jargh,jea,jeafbr,jhebea,jrb'
    scope='a.rhe,,,,,,,,,,,,,,,frgjeh,ag,jghea,jfrgheaf,jhrg,rhghragj'
    global pv
    trial={"access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
      "token_type":"bearer",
      "expires_in":3600,
      "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
      "scope":"create",
      'name':'anyone',
      'email':'me@gmail.co.uk',
      'phone':'007'
      }
    global parseddata
    try:
        data=parseddata
    except:
        data=trial
    cv=[]
    nd=variable_list(data,possible_variables)
    for i in range(0,len(nd)):
        if nd[i]!=0:
            cv.append(pv[i])
    checker=nd[pv.index(rn(name)[0])] 
    checkhtml('name',cv)
    return render_template('name.html',name=checker,email=nd[pv.index(rn(email)[0])],phone=nd[pv.index(rn(phone)[0])])
#@app.route('/hello/<name>')
#def hello(name):
    #return render_template('name.html', name=name)


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #auth.init_app(app)
    app.run(debug=True, host='0.0.0.0')
