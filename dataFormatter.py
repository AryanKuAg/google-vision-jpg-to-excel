

import re

from giveMonthIndex import giveMonthIndex


def dataFormatter(rawDataList):
    dateMonthPattern = re.compile('[A-Z][a-z][a-z]')
    for index, element in enumerate(rawDataList):
        # INITIAL DATE OF CONTACT
        try:
            if len(element[0]) > 0:
                element[0][0] = element[0][0].replace('-', '/')

                monthMatch = dateMonthPattern.search(element[0][0]).group()

                element[0][0] = element[0][0].replace(
                    monthMatch, giveMonthIndex(monthMatch))
        except:
            print('initial date error')

        # INITIAL DATE OF RECORD
        if len(element[4]) > 0:
            try:
                element[4][0] = element[4][0].replace('-', '/')
                #########
                if not element[4][0] == '':
                    monthMatch = dateMonthPattern.search(element[4][0]).group()

                    element[4][0] = element[4][0].replace(
                        monthMatch, giveMonthIndex(monthMatch))
            except:
                pass

        # DATE OF BIRTH
        if len(element[8]) > 0:
            element[8][0] = element[8][0].replace('-', '/')
            try:
                if not element[8][0] == '':
                    monthMatch = dateMonthPattern.search(element[8][0]).group()

                    element[8][0] = element[8][0].replace(
                        monthMatch, giveMonthIndex(monthMatch))
            except:
                pass

        # PHONE NUMBER FORMATTER
        if len(element[9]) > 0:
            if len(element[9][0]) == 10:
                element[9][0] = '+91 ' + element[9][0][0:5] + \
                    " " + element[9][0][5:]
        if len(element[7]) > 0:
            if len(element[7][0]) == 10:
                element[7][0] = '+91 ' + element[7][0][0:5] + \
                    " " + element[7][0][5:]

        # EMAIL FORMATTER
        if len(element[6]) > 0:
            element[6][0] = element[6][0].replace(" ", '')

        # NAME FORMATTER
        if len(element[3]) > 0:
            element[3][0] = element[3][0].upper()

    return rawDataList
