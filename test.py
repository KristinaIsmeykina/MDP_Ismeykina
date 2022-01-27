import win32com.client 
import pandas as pd
import numpy as np
import sys 

rastr = win32com.client.Dispatch("Astra.Rastr")
rastr.Load(1, 'regime.rg2', 'C:/Users/Кристина/Documents/RastrWin3/SHABLON/режим.rg2')    
rastr.Save('траектория утяжеления.ut2', 'C:/Users/Кристина/Documents/RastrWin3/SHABLON/траектория утяжеления.ut2')
rastr.Load(1, 'траектория утяжеления.ut2', 'C:/Users/Кристина/Documents/RastrWin3/SHABLON/траектория утяжеления.ut2')
rastr.Save('сечения.sch', 'C:/Users/Кристина/Documents/RastrWin3/SHABLON/сечения.sch')
rastr.Load(1, 'сечения.sch', 'C:/Users/Кристина/Documents/RastrWin3/SHABLON/сечения.sch')
result = rastr.rgm('p')
#загрузка данных в датафрейм
faults = pd.read_json('faults.json')
sechenie = pd.read_json('flowgate.json')
tra_ut = pd.read_csv('vector.csv')


print(faults)
print(sechenie)
print(tra_ut)