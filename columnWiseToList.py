
import re

from giveCity import giveCity
from giveState import giveState


def columnWiseToList(rawData):
    finalColumnSeperatedList = []

    # Date pattern
    pattern1 = re.compile("\d\d-\w\w\w-\d\d")  # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d")  # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d")  # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d")  # 4-mar-3
    pattern5 = re.compile("\d\w\w\w-\d")  # 6mar-3
    pattern6 = re.compile("-\w\w\w-\d")  # -Dec-06
    pattern7 = re.compile("\d\d-\w\w\w- \d\d")  # 10-May- 12
    pattern8 = re.compile("\d\d\w\w\w-\d\d")  # 24Aug-07
    pattern9 = re.compile("\d-\w\w-\d")  # 4-Ap-0?
    pattern10 = re.compile("\d\d-\w\w\w-\d")  # 13-Apr-0?
    # pattern11 = re.compile("\w\w\w-\d\d")  # May-84

    for index, element in enumerate(rawData):

        finalColumnSeperatedList.append(
            [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ])

        try:

            if len(element) < 10:
                continue

            splitted = element.split()

            # Initial date of contact

            if len(splitted[0]) < 10:

                finalColumnSeperatedList[index][0].append(splitted[0])
            elif len(splitted[0]) < 14:  # 12-Apr-114103

                finalColumnSeperatedList[index][0].append(
                    splitted[0][0:len(splitted[0]) - 4])
                finalColumnSeperatedList[index][1].append(
                    splitted[0][len(splitted[0]) - 4:])

            # Ledger number
            if len(finalColumnSeperatedList[index][1]) == 0 and len(splitted[1]) < 6:
                finalColumnSeperatedList[index][1].append(
                    splitted[1])

            # Folio Number
            if len(splitted[1]) == 6:
                finalColumnSeperatedList[index][2].append(
                    splitted[1])
            elif len(splitted[2]) == 6:
                finalColumnSeperatedList[index][2].append(
                    splitted[2])

            #################################################################
            ##########EVERYTHING IS WELL AND GOOD ABOVE######################
            #################################################################

            # This is for the name or customer name
            if len(finalColumnSeperatedList[index][2]) > 0:
                folioNumberIndex = element.index(
                    finalColumnSeperatedList[index][2][0])
            else:
                folioNumberIndex = 12
            # This is just initial data if we don't able to find it okay...)_)
            if len(finalColumnSeperatedList[index][2]) > 0:
                nameLastIndex = element.index(
                    finalColumnSeperatedList[index][2][0]) + 10
            else:
                nameLastIndex = folioNumberIndex + 18
            for yoyo in range(folioNumberIndex, folioNumberIndex + 30):
                if '-' in element[yoyo]:
                    nameLastIndex = yoyo - 2
                    break

            #print('name', str(element[folioNumberIndex + 6:nameLastIndex]).strip())
            finalColumnSeperatedList[index][3].append(
                str(element[folioNumberIndex + 6:nameLastIndex]).strip())

            ##################################################################################

            # OPen and closed
            if 'OPEN' in element:
                finalColumnSeperatedList[index][5].append("OPEN")
            elif "CLOSED" in element:
                finalColumnSeperatedList[index][5].append("CLOSED")

            # DATE OF BIRTH
            # we have namelastIndex for name tracking
            dateOfBirth = ''
            Datepattern2 = re.compile('\d-\w\w\w-\d\d')
            Datepattern1 = re.compile('\d\d-\w\w\w-\d\d')

            tempdateofBirth = ''

            for j in range(nameLastIndex, nameLastIndex + 35):
                # condition that it exist or not
                try:
                    tempdateofBirth += element[j]
                except IndexError:
                    print('sorry')

            if not Datepattern1.search(tempdateofBirth) == None:
                dateOfBirth += str(Datepattern1.search(tempdateofBirth).group()).strip()
            elif not Datepattern2.search(tempdateofBirth) == None:
                dateOfBirth += str(Datepattern2.search(tempdateofBirth).group()).strip()
            # print(dateOfBirth)
            finalColumnSeperatedList[index][4].append(
                dateOfBirth)

            ###################################################################
            ###################################################################

            # Email
            tempEmail = ''
            tempHolding = ''
            for email in splitted:
                if '@' in email:
                    tempEmail += email
                    break
            emailIndex = str(element).index(tempEmail)

            while not str(element[emailIndex]).isupper():
                tempHolding = element[emailIndex] + tempHolding
                emailIndex -= 1

            if len(str(tempHolding).strip()) < 2:
                realEmail = tempEmail
            else:
                realEmail = tempHolding.strip() + tempEmail.strip()

            # print(realEmail)
            finalColumnSeperatedList[index][6].append(
                str(realEmail).strip())

            #####################################################################
            #####################################################################

            # DATE OF RECORD
            emailIndex = element.index(str(tempEmail).strip())
            allTextAfterEmail = element[emailIndex:]
            dateOfRecord = ''

            if Datepattern1.search(allTextAfterEmail):
                dateOfRecord += str(Datepattern1.search(
                    allTextAfterEmail).group()).strip()
            elif Datepattern2.search(allTextAfterEmail):
                dateOfRecord += str(Datepattern2.search(
                    allTextAfterEmail).group()).strip()

            # print(dateOfRecord)
            finalColumnSeperatedList[index][8].append(
                str(dateOfRecord).strip())

            ##########################################################################################

            # contact 1
            dateofRecordIndex = element.index(
                finalColumnSeperatedList[index][8][0])
            tempContactOne = ''
            for c1 in range(dateofRecordIndex - 15, dateofRecordIndex):
                tempContactOne += element[c1]

            numberPattern = re.compile('[0-9]')
            temptempcontactone = ''
            for yo in tempContactOne:
                if numberPattern.match(yo) or '-' in yo:
                    temptempcontactone += yo

            if len(temptempcontactone) > 5:
                # print(temptempcontactone)
                finalColumnSeperatedList[index][7].append(
                    str(temptempcontactone).strip())

    ######################################################################################################

            # Contact 2
            dateofRecordIndex = element.index(
                finalColumnSeperatedList[index][8][0]) + len(finalColumnSeperatedList[index][8][0])

            tempContactTwo = ''
            for c2 in range(dateofRecordIndex, dateofRecordIndex + 15):
                tempContactTwo += element[c2]

            temptempcontactTwo = ''
            for yo in tempContactTwo:
                if numberPattern.match(yo) or '-' in yo:
                    temptempcontactTwo += yo

            if len(temptempcontactTwo) > 5:
                # print(temptempcontactTwo)
                finalColumnSeperatedList[index][9].append(
                    str(temptempcontactTwo).strip())

    #############################################################################################
            # ADDRESS

            # contactTwoIndex = element.index(
            #     temptempcontactTwo[0:6]) + len(temptempcontactTwo)
            print(element)
            try:
                genderIndex = element.index('ale') + 3
            except:
                continue

            addresstemp = str(element[genderIndex:]).replace('"', "")
            finalColumnSeperatedList[index][10].append(addresstemp.strip())

            #######################################################################################
            # City and state
            city = giveCity(element)
            state = giveState(city)
            finalColumnSeperatedList[index][12].append(city.strip())
            finalColumnSeperatedList[index][13].append(state.strip())
        except:
            print('a little bit error again')

    return finalColumnSeperatedList
