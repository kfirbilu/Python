#!/usr/bin/python3

import pywhatkit
import pandas as pd
import argparse



def main():

    # excelPath = input("Please enter a specific path the excel file containing the numbers: ")
    #
    # df = pd.read_excel(excelPath)
    #
    # numbers = list(df['numbers'])
    #
    # areaCode = input("Please enter your local area code: ")
    #
    # message = input("Please enter your message: ")

    parser = argparse.ArgumentParser(description="Whatsapp automatic message sender")

    parser.add_argument('excelPath', type=str, help="Specific path the excel file containing the numbers")

    parser.add_argument('areaCode', type=str, help="Your local area code")

    parser.add_argument('message',type=str,help="Your message")

    args = parser.parse_args()

    df = pd.read_excel(args.excelPath)

    numbers = list(df['numbers'])

    areaCode = args.areaCode

    message = args.message

    for num in numbers:
        newNum = areaCode + str(num)
        print("sendeing message to " + newNum)
        pywhatkit.sendwhatmsg_instantly(newNum, message, 6, True, 6)

    print("DONE")

if __name__ == '__main__':
    main()