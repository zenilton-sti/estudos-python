import pandas as pd 
import json
def createJson(planilha):
    grid=planilha
    x=pd.read_excel(str(grid)+'.xlsx')
    c=list(x.columns)
    js=[]
    for linha in range(len(x)): 
        j={}
        for col in c: 
            valor=  str(x[col].iloc[linha]) 
            if(str(valor)=="nan" or str(valor)=="\\N"):
                valor=""
            j[col]=valor
        js.append(j)      
      
    with open(str(grid)+'.json','w',encoding="utf-8") as texto:
        texto.write(json.dumps(js).encode("latin1").decode("unicode_escape"))

    
        
       
createJson("instituicao")