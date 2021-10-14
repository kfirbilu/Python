

import pywhatkit
import pandas as pd

excelPath = input("Please enter a specific path the excel file containing the numbers: ")

df = pd.read_excel(excelPath)

numbers = list(df['numbers'])

message = input("Please enter your message: ")

for num in numbers:
    newNum = '+972' + str(num)
    print("sendeing message to " + newNum)
    pywhatkit.sendwhatmsg_instantly(newNum,message, 4, True, 4)

print("DONE")



