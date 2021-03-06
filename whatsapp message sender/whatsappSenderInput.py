import pywhatkit
import pandas as pd


def main():
    excelPath = input("Please enter a specific path the excel file containing the numbers: ")

    df = pd.read_excel(excelPath)

    numbers = list(df['numbers'])

    areaCode = input("Please enter your local area code: ")

    message = input("Please enter your message: ")

    for num in numbers:
        newNum = areaCode + str(num)
        print("sendeing message to " + newNum)
        pywhatkit.sendwhatmsg_instantly(newNum, message, 4, True, 4)

    print("DONE")

if __name__ == '__main__':
    main()