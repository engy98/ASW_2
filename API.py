from flask import Flask,jsonify, request
app = Flask(__name__)


from main import Main

from config import likeDB
main = Main()



main.notfiySign.templates= likeDB.loadObject("notifySign");
main.notfiyBooking.templates= likeDB.loadObject("notfiyBooking");


import sys

from flask import Flask,session,jsonify, request,render_template,redirect,url_for



app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'



@app.route('/', methods=['GET'])
def loginGet():
    
    print("login render  ", file=sys.stderr)
    return render_template("logins_signup.html")

@app.route('/login', methods=['POST'])
def loginPost():
 
    requestD = request.get_json()
    email = requestD['recieverMail'] ;
    userName = requestD['userName']
    phone = requestD['recieverMobile'] ;
    password = requestD['password']  
    
    session['email'] =  email
    session['userName'] = userName
    session['phone'] = phone
    session['password'] = password
    NotifyUser(requestD['T_Notfication'],requestD['tID'],email,
               phone,requestD['Parameter'])
    
    response = jsonify(200)
    response.status_code = 200
    return response

@app.route('/book', methods=['GET'])
def bookGet():
    return render_template("rooms.html")

@app.route('/book', methods=['POST'])
def bookPost():
    print("booking post  ", file=sys.stderr)
    requestD = request.get_json()
    productName = requestD['productName']
    print(productName, file=sys.stderr)
    productID = requestD['productID'] ;
    T_Notfication = requestD['T_Notfication']
    tID = requestD['tID']
    
    email = session['email'] ;
    print(email, file=sys.stderr)
    userName= session['userName'] 
    phone= session['phone'] 

    
    NotifyUser(T_Notfication,tID,email,phone,
               [userName,productName,productID,phone,email])
    
    
    print("-----------------------------------", file=sys.stderr)
    response = jsonify(200)
    response.status_code = 200
    return response


@app.route('/notification/add', methods=['POST'])
def add_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        #requestD['template'] 
        template= main.makeTemplate(requestD['tID'],
                                    requestD['subject'], 
                                    requestD['content'], 
                                    requestD['languageNum'])
        if Notification_Type == 1:
            main.notfiySign.addTemplate(template)
        elif Notification_Type == 2 :
            main.notfiyBooking.addTemplate(template)
            
        response = jsonify(200)
        response.status_code = 200
        likeDB.saveObject("notifySign", main.notfiySign.templates);
        likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/notification/delete', methods=['POST'])
def delete_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        tID= requestD['tID']
        if Notification_Type == 1:
            main.notfiySign.deleteTemplate(tID)
        elif Notification_Type == 2 :
            main.notfiyBooking.deleteTemplate(tID)
        response = jsonify(200)
        response.status_code = 200
        likeDB.saveObject("notifySign", main.notfiySign.templates);
        likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/notification/update', methods=['POST'])
def update_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        tID= requestD['tID'] 
        template= main.makeTemplate(tID,
                            requestD['subject'], 
                            requestD['content'], 
                            requestD['languageNum'])
        if Notification_Type == 1:
            main.notfiySign.updateTemplate(tID,template)
        elif Notification_Type == 2 :
            main.notfiyBooking.updateTemplate(tID,template)
        response = jsonify(200)
        response.status_code = 200
        likeDB.saveObject("notifySign", main.notfiySign.templates);
        likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/notification/get', methods=['POST'])
def get_template():
    try:
        requestD = request.get_json()
        tID= requestD['tID']
        Notification_Type= requestD['T_Notfication']
        if Notification_Type == 1:
            Template = main.notfiySign.getTemplate(tID)
        elif Notification_Type == 2 :
            Template = main.notfiyBooking.getTemplate(tID)
        response = jsonify({'subject':Template.subject,
                            'content':Template.content,
                            'id':Template.id
                            
                            
                            })
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response




def NotifyUser(Notification_Type,tID,recieverMail,recieverMobile,Parameter):
    if Notification_Type == 1:
            resultTemp = main.notfiySign.getTemplate(tID)
    elif Notification_Type == 2 :
            resultTemp = main.notfiyBooking.getTemplate(tID)

    main.intilaizeMessage(resultTemp,Parameter,recieverMail,recieverMobile)
    
    
    
    #likeDB.saveObject("main", main);
@app.route('/notification/Notfiy', methods=['POST'])
def Notify():
    try:
        requestD = request.get_json()
        tID= requestD['tID']
        Notification_Type= requestD['T_Notfication']
        NotifyUser(Notification_Type, tID, requestD['recieverMail'], 
                   requestD['recieverMobile'], requestD['Parameter'])
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response


@app.route('/sendActualMessage', methods=['GET'])
def AM():
    try:
        main.sendMessage('email@gmail.com', 'password')
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/sucuessFail', methods=['GET'])
def SF():
    try:
        e = 'befor this step you shoud send actual message'
        e+= '      number of sucuess message : '+str(main.sucuessMessage)
        e+= '      number of faild message : '+str(main.faildMessage)
        response = jsonify(e)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/readyMessage', methods=['GET'])
def readyMessage():
    try:
        messageReady = []
        for i in main.Messages:
            Template = {'content':i['temp'].content,
                        'subject':i['temp'].subject,
                        'id':i['temp'].id}
            messageReady.append({'temp':Template,'mail':i['mail'],'mobile':i['mobile']})
        response = jsonify(messageReady)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response




from console import consoleProject 


if __name__ == '__main__':
     app.run(host="localhost", port=8001, debug = True)
     
     
    
     
     
     #consoleRun = consoleProject()
     #main = consoleRun.consoleRun(main)
     

   