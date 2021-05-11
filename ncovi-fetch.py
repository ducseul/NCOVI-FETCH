import requests
import json

class ncovid_statitics():
    def __init__(self, infected, treated, recovered, dead, updateTime):
        self.infected = infected
        self.treated  = treated
        self.recovered = recovered
        self.dead = dead
        self.updateTime = updateTime

    def __init__(self, data):
        self.infected = data["infected"]
        self.treated = data["treated"]
        self.recovered = data["recovered"]
        self.dead = data["deceased"]
        self.updateTime = data["lastUpdatedAtSource"]


def crawlVNData():
    api = 'https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true'
    response = requests.get(api)
    resp = json.loads(response.text)
    return ncovid_statitics(resp)


def initFetch(data):
    output = """
                        .,          //,&                            VIETNAM                                       
      ,   .    .*/  .  /,*%         #,/      @%                          Infected: {}                             
         .     %,,*.    /,#       ,,,#   .  /,,(#                        Treated: {}                              
             ,* , #,*/,//,,//*,//*,,%,   (,,((   ..                      Recover: {}                              
            /,,*.  #/,,/*,,,(,,,,,,,*#/***,# .*(/                        Dead: {}                                 
               *,,(*,,,,,,,,,*,**,,,,,#,*,,&*,//%                        Updated Time: {}                         
               &*(,,**,,*,,,*,/*,(/,,,*,*,,((&          .            
              #,/,(#,,,,,,,,,,/,(*,,,,,,*,(,*,%..                    
      (,(..,//****,,,,,,,,,,(,,(,,,,,,,,*/,/,%*(%,                   
      ,@/  ,%(*#(,,,,(,*,,,,,,,,,,,,*,,,/,,**,*#/,*.,,,,*            
         .,.,******,,,**,,,,,,,,*,,(*,*,,,**,*,/                     
             (*,,,#/(,((**,,,,*,**#*,(,*,,/,,*(,                     
    .     .   **,,(/%,*,,*(,,,,,,,,/,,/(,//,,((/,*,,,*               
               %/,,,,,,,*,%,%,,,,**,,(,*,,,,@  .   ,((  .            
            (,*(,*#%/*,*,,/(/*,,,,,*,/,,#,*/#                        
         (//&      (*,*//%#*(,*,*,(,,(*#&,(/,*.                      
                  .    %(*,,*,,,,,*/*/      ,*,,,#                   
          .           #*,/          (,,%     ***/                    
                    (%,,        .   &/*(          .                  
                     /((               \))"""
    print(output.format(data.infected, data.treated, data.recovered, data.dead, data.updateTime))
                            
if __name__ == "__main__":
    data = crawlVNData()
    initFetch(data)
