import sys
class notfication : 
    def addTemplate(self,t):
        self.templates.append(t)
        
    def deleteTemplate(self,tID):
        for i in range(len(self.templates)):
            if(int(self.templates[i].id)==int(tID)):
                self.templates.pop(i)
                return True
        return False

        
    
    def updateTemplate(self,tID,t):
        for i in range(len(self.templates)):
            if(int(self.templates[i].id)==int(tID)):
                self.templates[i]=t
                return True
        return False
    
    def getTemplate(self,tID):
        for i in self.templates:
            if(int(i.id)==int(tID)):
                return i
        return None
    
    
    