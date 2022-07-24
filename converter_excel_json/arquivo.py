import pandas as pd 
def createJson(planilha):
    grid=planilha
    x=pd.read_excel(str(grid)+'.xlsx')
    c=list(x.columns)
    js="["
    for linha in range(len(x)): 
        j="{"
        for col in c: 
            valor=  str(x[col].iloc[linha]) 
            if(str(valor)=="nan" or str(valor)=="\\N"):
                valor=""
            if(j=="{"):
                j+="\"" + str(col)+"\":\"" + str(valor) + "\"" 
            else:
                j+=",\"" + str(col)+"\":\"" + str(valor) + "\"" 
        j+="}"
        if(js=="["):
            js+=j
        else:
            js+=","+j
    final=js+"]"   
    with open(str(grid)+'.json','w',encoding="utf-8") as texto:
        texto.write(final)

    
        
       
createJson("instituicao")