from typing import Pattern
import requests
import json
import argparse
from Entity import *
        
def getVietNam():
    api = 'https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true'
    response = requests.get(api)
    resp = json.loads(response.text)
    return ncovid_statitics(resp)


def crawlWorldWide():
    url = 'https://corona-api.kompa.ai/graphql'
    query = {'query' : '{globalCasesActive {     currentlyInfectedPatients     inMildCondition     inMildConditionPercent     seriousOrCritical     seriousOrCriticalPercent     __typename   }   globalCasesClosed {     casesWhichHadAnOutcome     recovered     recoveredPercent     deaths     deathPercent     __typename   }   globalCasesSummary {     confirmed     deaths     recovered     __typename   }   globalCasesToday {     country     totalCase     newCases     totalDeaths     newDeaths     totalRecovered     activeCases     seriousCritical     totCases     __typename   }   globalCasesYesterday {     country     totalCase     newCases     totalDeaths     newDeaths     totalRecovered     activeCases     seriousCritical     totCases     __typename   }   globalCasesAge {     age     deathConfirmedPercent     deathAllPercent     __typename   }   globalCasesGender {     gender     deathConfirmedPercent     deathAllPercent     __typename   }   trendlineGlobalCases {     date     confirmed     recovered     death     __typename   } } '}
    headers = {'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Origin':'https://corona.kompa.ai',
                'Referer':'https://corona.kompa.ai'}

    r = requests.post(url=url, json=query, headers=headers)
    resp = json.loads(r.text)
    return resp["data"]
    

def renderFetch(data, pattern_id, other_country_data, global_data):
    output = []

    output.append("""
                        .,          //,&                  ` VIETNAM                 
      ,   .    .*/  .  /,*%         #,/      @%                 Infected : {}       
         .  %  %,,*.    /,#       ,,,#   .  /,,(#               Recover : {}         
             ,* , #,*/,//,,//*,//*,,%,   (,,((   ..             Dead : {}           
            /,,*.  #/,,/*,,,(,,,,,,,*#/***,# .*(/               Updated Time : {}
               *,,(*,,,,,,,,,*,**,,,,,#,*,,&*,//%               
               &*(,,**,,*,,,*,/*,(/,,,,*,*,,((&          .   
              #,/,(#,,,,,,,,,,/,(*,,,,,,,*,(,*,%..                    
      (,(..,//****,,,,,,,,,,(,,(,,,,,,,,,,,*/,/,%*(%,       WORLDWIDE            
      ,@/  ,%(*#(,,,,(,*,,,,,,,,,,,,*,,,/,,**,*#/,*.,,,,*       Infected : {}     
         .,.,******,,,**,,,,,,,,*,,(*,*,,,**,*,/                Recover : {}       
             (*,,,#/(,((**,,,,*,**#*,(,*,,/,,*(,                Dead : {}     
    .     .   **,,(/%,*,,*(,,,,,,,,/,,/(,//,,((/,*,,,*          Updated : {}     
               %/,,,,,,,*,%,%,,,,**,,(,*,,,,@  .   ,((  .       
            (,*(,*#%/*,*,,/(/*,,,,,*,/,,#,*/#                        
         (//&      (*,*//%#*(,*,*,(,,(*#&,(/,*.                      
                  .    %(*,,*,,,,,*/*/      ,*,,,#                   
          .           #*,/          (,,%     ***/                    
                    (%,,        .   &/*(          .                  
                     /((               \)""")

    output.append("""
                        .,          //,&                  ` VIETNAM               
      ,   .    .*/  .  /,*%         #,/      @%                 Infected : {}  
         .  %  %,,*.    /,#       ,,,#   .  /,,(#               Recover : {}   
             ,* , #,*/,//,,//*,//*,,%,   (,,((   ..             Dead : {}         
            /,,*.  #/,,/*,,,(,,,,,,,*#/***,# .*(/               Updated Time : {}
               *,,(*,,,,,,,,,*,**,,,,,#,*,,&*,//%               
               &*(,,**,,*,,,*,/*,(/,,,,*,*,,((&          .   
              #,/,(#,,,,,,,,,,/,(*,,,,,,,*,(,*,%..          WORLDWIDE       
      (,(..,//****,,,,,,,,,,(,,(,,,,,,,,,,,*/,/,%*(%,           Infected : {}     
      ,@/  ,%(*#(,,,,(,*,,,,,,,,,,,,*,,,/,,**,*#/,*.,,,,*       Recover : {}         
         .,.,******,,,**,,,,,,,,*,,(*,*,,,**,*,/                Dead : {}     
             (*,,,#/(,((**,,,,*,**#*,(,*,,/,,*(,                Updated : {}     
    .     .   **,,(/%,*,,*(,,,,,,,,/,,/(,//,,((/,*,,,*          
               %/,,,,,,,*,%,%,,,,**,,(,*,,,,@  .   ,((  .   
            (,*(,*#%/*,*,,/(/*,,,,,*,/,,#,*/#               {}                  
         (//&      (*,*//%#*(,*,*,(,,(*#&,(/,*.                 Infected : {}       
                  .    %(*,,*,,,,,*/*/      ,*,,,#              Recover : {}         
          .           #*,/          (,,%     ***/               Dead : {}       
                    (%,,        .   &/*(          .             Updated : {}      
                     /((               \)                                          
                                                                New Case : {} 
                                                                New Deaths: {}  
                                                            
                     """)

    output.append('List of country')

    if(pattern_id == 0):
        global_data = GlobalCasesSummary(global_data)
        other_country_data = CountryStatitics(other_country_data)
        print(output[pattern_id].format(data.infected, data.recovered, data.dead, data.updateTime,
        global_data.confirmed, global_data.recoverd, global_data.deaths, "null"))

    elif (pattern_id == 1):
        global_data = GlobalCasesSummary(global_data)
        other_country_data = CountryStatitics(other_country_data)
        print(output[pattern_id].format(data.infected, data.recovered, data.dead, data.updateTime,
        global_data.confirmed, global_data.recoverd, global_data.deaths, "null",
        other_country_data.country.upper(), other_country_data.totalCase, other_country_data.newCases, 
        other_country_data.totalRecovered,  "null", other_country_data.totalDeaths, other_country_data.newDeaths))
        pass

    elif (pattern_id == 2):
        print(output[pattern_id], other_country_data)
    


class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "Description for my NCOVI-FETCH")
        parser.add_argument("-c", "--country", help = "Other country statitics. Example: --c 'Papua New Guinea'", required = False, default = "")
        parser.add_argument("-s", "--search", help = "Search country name. Example: -s 'unite'", required = False, default = "")
    
        argument = parser.parse_args()
        
        ww_data = crawlWorldWide()

        render_pattern = 0
        other_country_data = []
        global_data = []

        if argument.search:
            render_pattern = 2
            tmp = ww_data["globalCasesToday"]
            for index in range((len(tmp)) - 1):
                if argument.search.lower() in tmp[index]["country"].lower():
                    other_country_data.append(tmp[index]["country"])
            renderFetch("", render_pattern, other_country_data, "")
            return


        if argument.country:
            render_pattern = 1
            tmp = ww_data["globalCasesToday"]
            for index in range(len(tmp)):
                if tmp[index]["country"].lower() == argument.country.lower():
                    other_country_data = tmp[index]
                    break
            
        global_data = ww_data["globalCasesSummary"]
        vn_data = getVietNam()
        renderFetch(vn_data, render_pattern, other_country_data, global_data)


if __name__ == "__main__":
    app = CommandLine()
