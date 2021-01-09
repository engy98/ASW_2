from config import likeDB
#main = Main()


class consoleProject :
    def consoleRun(self,main):
        while(True):
            x = int(input('''
                      1-make a temp
                      2-build message
                      3-send actual message
                      4-sucuess message and faild message
                      5-ready Message for send
                      6-load main
                      7-save main
                      o.w close prog
                      '''))
            if(x == 1):
                y = int(input('''
                          1- for sign
                          2-for booking
                          '''))
                temID = input('ID: ')
                subject = input('subject: ')
                content = input ('content with {a} for paramter: ')
                language =int(input('language 1 for english 2 for arabic: '))       
                templateUser=main.makeTemplate(temID,subject,content,language)
                if(y==1):
                    main.notfiySign.addTemplate(templateUser)
                if(y==2):
                    main.notfiyBooking.addTemplate(templateUser)
                  
            
            elif(x==2):
                y = int(input('''
                        1- for sign
                        2-for booking
                        '''))
                tempID = input('insert ID of template: ')
                if(y==1):
                    resultTemp = main.notfiySign.getTemplate(tempID)
                if(y==2):
                    resultTemp = main.notfiyBooking.getTemplate(tempID)
                if(resultTemp==None):
                    print('cant found temp with this id')
                    break
                    
                recieverMail = input('enter reciever Mail: ')
                recieverMobile = input('enter reciever Mobile: ')
                
                numberParameter = resultTemp.content.count('{a}')
                parameter = []
                for i in range(numberParameter):
                   parameter.append(input('parameter num '+str(i+1) ))
                main.intilaizeMessage(resultTemp,parameter,recieverMail,recieverMobile)
        
            elif(x==3):
                main.sendMessage('email@gmail.com', 'password')
            elif(x==4):
                print('befor this step you shoud rum send actual message')
                print('number of sucuess message : ',main.sucuessMessage)
                print('number of faild message : ',main.faildMessage)
                
                import matplotlib.pyplot as plt
                fig = plt.figure()
                ax = fig.add_axes([0,0,1,1])
                langs = ['sucuess Message', 'faild Message']
                students = [main.sucuessMessage,main.faildMessage]
                ax.bar(langs,students)
                plt.show()

                
                #plot 
            elif(x==5):
                for i in main.Messages:
                     print(i['temp'].content , " "+ i['temp'].subject , ' ', i['temp'].id)
                     print(i['mail'] , ' ' , i['mobile'] )
            elif(x==6):
                main.notifySign.templates= likeDB.loadObject("notifySign");
                main.notfiyBooking.templates= likeDB.loadObject("notfiyBooking");
                
            elif(x==7):
                likeDB.saveObject("notifySign", main.notfiySign.templates);
                likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
            
            else:
                break ;
                return main

