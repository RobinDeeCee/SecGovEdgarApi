from .usGaap.UsGaapHandler import UsGaapHandler

class TerminationHandler():
    
    def get_usGaap(cik: str, sortingKey:str):
        usGaapWrapper = {}
        usGaapWrapper["usGaap"] = UsGaapHandler.getUsGaapFacts(UsGaapHandler(), cik=cik, sortingKey=sortingKey)

        return [usGaapWrapper]
        
        