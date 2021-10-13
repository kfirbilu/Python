

import pywhatkit
import pandas as pd

df = pd.read_excel(r'ENTER HERE ROUT TO THE EXCEL FILE WITH THE NUMBERS')
numbers = list(df['numbers'])
print(numbers)

for num in numbers:
    newNum = '+972' + str(num)
    print(newNum)
    pywhatkit.sendwhatmsg_instantly(newNum, 'ENTER YOUR MESSAGE HERE!!',4, True, 4)






