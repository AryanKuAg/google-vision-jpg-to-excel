import enum
import re


def rawToList(rawData):

    removedNewLine = rawData.replace("\n", " ")
    seperated = removedNewLine.split()
    entryInitialDateOfContact = []

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

    # loop time
    for index, element in enumerate(seperated):
        if index == len(seperated) - 5:
            break

        if (pattern1.search(element) or pattern2.search(element) or pattern3.search(element) or pattern4.search(element) or pattern5.search(element) or pattern6.search(element) or pattern7.search(element) or pattern8.search(element) or pattern9.search(element) or pattern10.search(element)) and (len(element) < 10 or element.count('-') == 2):
            # getting the exact date with element
            if 'open' in str(seperated[index + 1]).lower() or 'closed' in str(seperated[index + 1]).lower():
                # do something
                pass
            else:
                # need more accurate code for entry seperation by date
                #print('previous:', seperated[index - 1])
                # print(element)
                # print('nextelement:', seperated[index + 1])

                temptempLength = len(str(seperated[index + 1]).strip())
                if temptempLength == 4 or temptempLength == 6:

                    entryInitialDateOfContact.append(element)

    # This list contain the starting value of each entry
    # print(entryInitialDateOfContact)

    ###################################################################
    # This list contain index and date
    initialDateOfContactDictionary = []
    for element in entryInitialDateOfContact:
        gotIndex = rawData.index(element)
        initialDateOfContactDictionary.append(
            {"index": gotIndex, "date": element})

    ####################################################################

    ourFinalData = []
    for i, element in enumerate(initialDateOfContactDictionary):
        if i == 0:  # This is the first loop
            continue

        # if len(initialDateOfContactDictionary) - 1 == i:
        #     ourFinalData.append(removedNewLine[element["index"]:])
        #     break

        previousIndex = initialDateOfContactDictionary[i - 1]["index"]
        # print(removedNewLine[previousIndex:element["index"]])
        ourFinalData.append(removedNewLine[previousIndex:element["index"]])

    ourFinalData.append(removedNewLine[element["index"]:])

    puredFinalData = []

    for xyz in ourFinalData:
        if xyz.count(' ') < 10:
            continue
        puredFinalData.append(xyz)

    return puredFinalData
