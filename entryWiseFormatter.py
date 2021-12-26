

from enum import unique


def entryWiseFormatter(rawDataList):
    finalEntryWiseList = []

    for index, element in enumerate(rawDataList):
        finalEntryWiseList.append([])
        try:

            # UNIQUE ID
            uniqueId = None
            if len(element[1]) > 0 and len(element[3]) > 0:
                if len(element[3][0].split()) > 1:
                    uniqueId = element[1][0] + element[3][0].split()[0][0:2] + \
                        element[3][0].split()[1][0:2]
                else:
                    uniqueId = element[1][0] + element[3][0].split()[0][0:2]

            if uniqueId == None:
                finalEntryWiseList[index].append('')
            else:
                finalEntryWiseList[index].append(uniqueId)

            ###################################################################
            # LEDGER NUMBER
            if len(element[1]) > 0:
                finalEntryWiseList[index].append(element[1][0])
            else:
                finalEntryWiseList[index].append('')

            ####################################################################
            # FOLIO NUMBER
            if len(element[2]) > 0:
                finalEntryWiseList[index].append(element[2][0])
            else:
                finalEntryWiseList[index].append('')
            ####################################################################
            # DATE OF CONTACT
            if len(element[0]) > 0:
                finalEntryWiseList[index].append(element[0][0])
            else:
                finalEntryWiseList[index].append('')
            #####################################################################
            # INITIAL DATE OF CONTACT
            if len(element[4]) > 0:
                finalEntryWiseList[index].append(element[4][0])
            else:
                finalEntryWiseList[index].append('')

            #####################################################################
            # OPEN CLOSED
            if len(element[5]) > 0:
                finalEntryWiseList[index].append(element[5][0])
            else:
                finalEntryWiseList[index].append('')

            #####################################################################
            # CUSTOMER FULL NAME
            if len(element[3]) > 0:
                finalEntryWiseList[index].append(element[3][0])
            else:
                finalEntryWiseList[index].append('')

            #####################################################################
            # CUSTOMER ADDRESS FIRST LINE
            if len(element[10]) > 0:
                finalEntryWiseList[index].append(element[10][0])
            else:
                finalEntryWiseList[index].append('')

            #####################################################################
            # CUSTOMER ADDRESS SECOND LINE
            if len(element[11]) > 0:
                finalEntryWiseList[index].append(element[11][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # CITY
            if len(element[12]) > 0:
                finalEntryWiseList[index].append(element[12][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # STATE
            if len(element[13]) > 0:
                finalEntryWiseList[index].append(element[13][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # PINCODE
            if len(element[14]) > 0:
                finalEntryWiseList[index].append(element[14][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # LANDMARK
            if len(element[15]) > 0:
                finalEntryWiseList[index].append(element[15][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # CUSTOMER PHONE NUMBER 1
            if len(element[7]) > 0:
                finalEntryWiseList[index].append(element[7][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # CUSTOMER PHONE NUMBER 2
            if len(element[9]) > 0:
                finalEntryWiseList[index].append(element[9][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # EMAIL ADDRESS
            if len(element[6]) > 0:
                finalEntryWiseList[index].append(element[6][0])
            else:
                finalEntryWiseList[index].append('')

            ######################################################################
            # DATE OF BIRTH
            if len(element[8]) > 0:
                finalEntryWiseList[index].append(element[8][0])
            else:
                finalEntryWiseList[index].append('')

        except:
            print('Its just an error')

    print(finalEntryWiseList)
    return finalEntryWiseList
