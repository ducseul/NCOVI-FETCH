class GlobalCasesSummary:
    def __init__(self, confirmed, deaths, recoverd):
        self.confirmed = confirmed
        self.deaths = deaths
        self.recoverd = recoverd

    def __init__(self, data):
        if len(data) != 0:
            self.confirmed = data["confirmed"]
            self.deaths = data["deaths"]
            self.recoverd = data["recovered"]

    def __str__(self) -> str:
        return self.confirmed + ", " + self.deaths + ", " + self.recoverd


class CountryStatitics:
    def __init__(self, country, totalCase, newCases, totalDeaths, newDeaths, totalRecovered, activeCases, seriousCritical, totCases):
        self.country = country
        self.totalCase = totalCase
        self.newCases = newCases
        self.totalDeaths = totalDeaths
        self.newDeaths = newDeaths
        self.totalRecovered = totalRecovered
        self.activeCases = activeCases
        self.seriousCritical = seriousCritical
        self.totCases = totCases

    def __init__(self, data):
        if(len(data) != 0):
            self.country = data["country"]
            self.totalCase = data["totalCase"]
            self.newCases = data["newCases"]
            self.totalDeaths = data["totalDeaths"]
            self.newDeaths = data["newDeaths"]
            self.totalRecovered = data["totalRecovered"]
            self.activeCases = data["activeCases"]
            self.seriousCritical = data["seriousCritical"]
            self.totCases = data["totCases"]

    def __str__(self) -> str:
        return self.country + ", " + self.totalCase + ", " + self.newCases + ", " 
        + self.totalDeaths + ", " + self.newDeaths + ", " + self.totalRecovered 
        + ", " + self.activeCases + ", " + self.seriousCritical + ", " + self.totCases 

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
