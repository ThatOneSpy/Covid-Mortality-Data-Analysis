
# comments start with the hash.  
# Be sure to read these!

# Don't change this line:
from datetime import datetime

# Put your name here: Jerry Huang

# Calls function banner() and menu(). Receives menu values. Loops, exits, and calls other functions as needed for each menu item
# Accepts nothing
def main():

  banner()

  while True:
    userInput = menu()
    if userInput == 1:
      pass

    elif userInput == 2: 
      cdcData=openCDCfile()
      defaultReport(cdcData)
      
    elif userInput == 3: 
      reportSingleStateDataByDate()
      
    elif userInput == 4:
      (data, state, totalDeaths, naturalCauses, c19Multiple, c19Underlying) = totalMortalityByState()
      printLineDetailReport(data, state, totalDeaths, naturalCauses, c19Multiple, c19Underlying)
      
    elif userInput == 5:
      GetHighestMortality()

    else:
      print('**** EXITING MENU ****')
      break

# Displays an ASCII banner
# Accepts nothing
def banner():
    print(
        ''' ___ __ __   __   _______ _______ _______   _______ ___ ______   _______ ______  
|   |  |  |_|  | |       |       |       | |       |   |    _ | |       |      | 
|   |__|       | |_     _|   _   |   _   | |_     _|   |   | || |    ___|  _    |
|   |  |       |   |   | |  | |  |  | |  |   |   | |   |   |_||_|   |___| | |   |
|   |  |       |   |   | |  |_|  |  |_|  |   |   | |   |    __  |    ___| |_|   |
|   |  | ||_|| |   |   | |       |       |   |   | |   |   |  | |   |___|       |
|___|  |_|   |_|   |___| |_______|_______|   |___| |___|___|  |_|_______|______| 
 _______ _______ ______     _______ __   __ ___ _______                          
|       |       |    _ |   |       |  | |  |   |       |                         
|    ___|   _   |   | ||   |_     _|  |_|  |   |  _____|                         
|   |___|  | |  |   |_||_    |   | |       |   | |_____                          
|    ___|  |_|  |    __  |   |   | |       |   |_____  |                         
|   |   |       |   |  | |   |   | |   _   |   |_____| |                         
|___|   |_______|___|  |_|   |___| |__| |__|___|_______|                         
==================================================================================\n''')

# Asks the user to make a selection. Tests selection to make sure it's a valid value. Loops until a valid value is selected.
# Accepts nothing
# Returns an integer
def menu():
  
  print('Mortality Rate Comparison Menu')
  print('')
  print('1. Show This Menu Again')
  print('2. Full Mortality Report by State')
  print('3. Mortality for a Single State, by Date Range')
  print('4. Mortality Summary for all States')
  print('5. Highest COVID mortality Week')
  print('6. Exit')
  print('')
  
  while True:
    try:
      userInput = int(input('Make your selection from the menu: '))
      print('=============================================')
   
      if userInput in (1, 2, 3, 4, 5, 6):
      
        return userInput
        break
      else:
        print('Please Select From The Menu')
    
    except:
      print('=============================================')
      print('Please Select From The Menu')

# Opens the cdc.csv file, removes unneeded lines of data
# Accepts nothing
# Returns file handler
def openCDCfile():

  with open('cdc.csv', "r") as cdcData:
    cdcData=cdcData.readlines()[7:]

  return(cdcData)

# Creates a report called "Full_Mortality_By_State_Report.txt" using a file handler formated neatly
# Writes header for report
# Writes current date and time to report
# Gets rid of any hidden characters
# Replaces any empty values with the number 0
# Adds appropriate spacing to text
# Accepts file handler
def defaultReport(data):

  report = open('Full_Mortality_By_State_Report','w')
  
  report.write('National Mortality Rate by Cause Listed by State and Reporting Date Report Sorted by State \n')

  now = datetime.now()
  dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
  report.write('\nReport Generated: '+dt_string+'\n\n')

  report.write('''       |STATE|         |WEEK|   |TOTAL DEATHS| |NATURAL DEATHS| |C-19 MULTIPLE| |C-19 UNDERLYING|
  ===============================================================================================
  \n''')
 
  for eachLine in data:
    
    eachLine=eachLine.strip()
   
    eachLine = eachLine.split(',')

    eachLine[5]=str(replaceSpaceWithZero(eachLine[5]))
    
    eachLine[17]=str(replaceSpaceWithZero(eachLine[17]))

    eachLine[18]=str(replaceSpaceWithZero(eachLine[18]))
         
    report.write(eachLine[0].center(22) + eachLine[3].ljust(15) + eachLine[4].ljust(15) + eachLine[5].ljust(15) + eachLine[17].ljust(15) + eachLine[18].ljust(15) + '\n')
  print('**** REPORT PRINTED ****')
  
  report.close()

# Calls getAvailableDates() and displays them for the user. Asks user for start and end dates. Gives the option of automatically setting start and end dates with the letter 'S' and 'E'.
# Validates dates input. Calls convertDate() function to temporarily convert strings to date objects for comparison. 
# Calls convertDate() and restructures data to be usable in function
# Orders dates in chronological order
# Accepts nothing
# Returns two variables
def getUserInputDates():
  (oldestDate, newestDate) = getAvailableDates()
  print('Reporting is available from',oldestDate,'to',newestDate+'.\n')
  
  while True:
    startDate = input('Choose your starting date in (mm/dd/yy) format\nor input S for the first date of the data: ')
    try:
      if startDate == 'S' or startDate == 's':
        startDate = oldestDate
        print('')
        break
      
      elif convertDate(oldestDate) <= convertDate(startDate) <= convertDate(newestDate):
        print('')
        break

      else:
        print('Not a valid date or format. Please try again.')
        print('=============================================')

    except:  
      print('Not a valid date or format. Please try again.')
      print('=============================================')
  
  while True:
    endDate = input('Choose your ending date in (mm/dd/yy) format\nor input E for the last date of the data: ')
    try:
      if endDate == 'E' or endDate == 'e':
        endDate = newestDate
        print('\n**** REPORT PRINTED ****')
        print('=============================================')
        break
      
      elif convertDate(oldestDate) <= convertDate(endDate) <= convertDate(newestDate):
        print('\n**** REPORT PRINTED ****')
        print('=============================================')
        break

      else:
        print('Not a valid date or format. Please try again.')
        print('=============================================')

    except:  
      print('Not a valid date or format. Please try again.')
      print('=============================================')

  if convertDate(startDate) <= convertDate(endDate):
    olderDate = startDate
    newerDate = endDate
  else:
    olderDate = endDate
    newerDate = startDate
  return olderDate, newerDate

# Calls openCDCFile() and determines the first date and the last date available in the document. 
# Calls convertDate() and restructures data to be usable in function
# Accepts nothing
# Returns two strings: the start date, and the end date, in that order.
def getAvailableDates():
  dates = []
  cdcData=openCDCfile()
  for eachLine in cdcData:
    eachLine = eachLine.strip()
    eachLine = eachLine.split(',')

    eachLine[3] = eachLine[3][:-4]
    
    str(eachLine[1])
    eachLine[1] = eachLine[1].replace('20','',1)

    fixedDates = eachLine[3] + eachLine[1]
    fixedDates = convertDate(fixedDates)
    dates.append(fixedDates)

  oldestDate = str(min(dates))
  newestDate = str(max(dates))
  
  oldestDate = oldestDate[:-9].split('-')
  newestDate = newestDate[:-9].split('-')

  oldestDate = (oldestDate[1] +'/'+ oldestDate[2] +'/'+ oldestDate[0][-2:])
  newestDate = (newestDate[1] +'/'+ newestDate[2] +'/'+ newestDate[0][-2:])

  return oldestDate, newestDate
  
# Generates a reports for a single state and for a specific date range. Asks the user to enter a State to review
# Calls getUserInputDates() to get a date range for the function. Using State and date range, generates a report file called "Mortality_For_State_By_Date_Range_Report.txt".
# Writes current date and time to report
# Gets rid of any hidden characters
# Replaces any empty values with the number 0
# Adds appropriate spacing to text
# Accepts nothing
def reportSingleStateDataByDate():
  data=openCDCfile()

  inputState = input('What State do you want to review? ')
  inputState = inputState.title()

  startDate, endDate = getUserInputDates()

  report = open('Mortality_For_State_By_Date_Range_Report','w')
  report.write('Mortality for ('+inputState+') by Date Range\n') 
  report.write('For the selected date range '+startDate+' - '+endDate+'\n')
  report.write('''\nIf your selected state isn't shown then it's either not in the database or something was input incorrectly!\n''')

  now = datetime.now()
  dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
  report.write('\nReport Generated: '+dt_string+'\n\n')

  report.write('''       |STATE|         |WEEK|   |TOTAL DEATHS| |NATURAL DEATHS| |C-19 MULTIPLE| |C-19 UNDERLYING|
  ===============================================================================================
  \n''')
  testList=[]
  for eachLine in data:
    
    eachLine=eachLine.strip()
   
    eachLine = eachLine.split(',')

    eachLine[5]=str(replaceSpaceWithZero(eachLine[5]))
    eachLine[17]=str(replaceSpaceWithZero(eachLine[17]))
    eachLine[18]=str(replaceSpaceWithZero(eachLine[18]))
    
    eachLine[1] = str(eachLine[1].replace('20','',1))

    if inputState in eachLine and convertDate(startDate) <= convertDate(eachLine[3][:-4] +eachLine[1]) <= convertDate(endDate):
      report.write(eachLine[0].center(22) + eachLine[3].ljust(15) + eachLine[4].ljust(15) + eachLine[5].ljust(15) + eachLine[17].ljust(15) + eachLine[18].ljust(15) + '\n')
      testList.append((int(eachLine[4])))
    else:
      pass
  report.close()
  
# Generates a report of the sum of total deaths, death by natural causes, COVID-19 Multiple Causes, and COVID-19 Underlying Cause for a entire date range. Function creates a report file called "Mortality_Summary_For_All_States_By_Date_Range_Report.txt". Then prints the headers, and loops through the data to generate each total. Totals for each state are sent to printLineDetailReport() to be printed to the report.
# Writes current date and time to report
# Gets rid of any hidden characters
# Replaces any empty values with the number 0
# Accepts nothing
# Returns six variables
def totalMortalityByState():
  (startDate, endDate) = getUserInputDates()
  data = openCDCfile()
  report = open('Mortality_Summary_For_All_States_By_Date_Range_Report','w')
  report.write('Mortality Summary For All States By Date Range Report \n')
  report.write('For the selected date range '+startDate+' - '+endDate+'\n')

  now = datetime.now()
  dt_string = now.strftime("%m/%d/%Y     %H:%M:%S")
  report.write('\nReport Generated: '+dt_string+'\n\n')

  report.write('''       |STATE|    |TOTAL DEATHS|  |NATURAL DEATHS| |C-19 MULTIPLE| |C-19 UNDERLYING|
  ==========================================================================================
  \n''')

  totalDeaths = 0
  naturalDeaths = 0
  c19Multiple = 0
  c19Underlying = 0
  totalDeathsList = []
  naturalDeathsList = []
  c19MultipleList = []
  c19UnderlyingList = []
  stateIndex = 0
  states = []
  singleStates = []

  for eachLine in data:
    eachLine = eachLine.strip()
    eachLine = eachLine.split(',')
    states.append(eachLine[0])

  for state in states:
    if state not in singleStates:
      singleStates.append(state)
  for eachLine in data:
    eachLine = eachLine.strip()
    eachLine = eachLine.split(',')
    str(eachLine[1])
    eachLine[1] = eachLine[1].replace('20','',1)
        
    currentState = (singleStates[stateIndex])

    if currentState == eachLine[0]:
      if convertDate(startDate) <= convertDate(eachLine[3][:-4] +eachLine[1]) <= convertDate(endDate):
        totalDeaths+=int(replaceSpaceWithZero(eachLine[4]))
        naturalDeaths+=int(replaceSpaceWithZero(eachLine[5]))
        c19Multiple+=int(replaceSpaceWithZero(eachLine[17]))
        c19Underlying+=int(replaceSpaceWithZero(eachLine[18]))
      else:
        pass
    else:
      totalDeathsList.append(totalDeaths)
      naturalDeathsList.append(naturalDeaths)
      c19MultipleList.append(c19Multiple)
      c19UnderlyingList.append(c19Underlying)
      totalDeaths = 0
      naturalDeaths = 0
      c19Multiple = 0
      c19Underlying = 0
      stateIndex+=1 
  
  totalDeathsList.append(totalDeaths)
  naturalDeathsList.append(naturalDeaths)
  c19MultipleList.append(c19Multiple)
  c19UnderlyingList.append(c19Underlying)
  
  return (data, singleStates, totalDeathsList, naturalDeathsList, c19MultipleList, c19UnderlyingList)
  report.close


# Converts the integers to strings, then appends the summary detail to the report "Mortality_Summary_For_All_States_By_Date_Range_Report.txt".
# Adds appropriate spacing to text
# Accepts six variables(open file handler, the State, and four integers that represent the sum for each State: Total Deaths, Natural Causes, C19 Multiple Causes, and C19 Underlying Causes)
def printLineDetailReport(data, states, totalDeaths, naturalCauses, c19Multiple, c19Underlying):
  
  index=0
  report = open('Mortality_Summary_For_All_States_By_Date_Range_Report','a')
  for eachline in states:
    totalDeaths[index] = str(totalDeaths[index])
    naturalCauses[index] = str(naturalCauses[index])
    c19Multiple[index] = str(c19Multiple[index])
    c19Underlying[index] = str(c19Underlying[index])
    
    report.write(states[index].center(22) +' '+ totalDeaths[index].ljust(15) +' '+ naturalCauses[index].ljust(15) +' '+ c19Multiple[index].ljust(15) +' '+ c19Underlying[index].ljust(15) + '\n')
    index+=1
  
  report.close
      
# Determines the highest reported week of COVID19 mortality as an underlying cause of death, what week that was, what state (or report location) it occured in, and what percentage of total deaths that week this number represents. The function then prints out the message on screen
# Gets rid of any hidden characters
# Replaces any empty values with the number 0
# Accepts nothing
def GetHighestMortality():
  cdcData = openCDCfile()
  deathList = []
  dates = []
  states = []
  totalDeaths = []

  for eachLine in cdcData:
    eachLine = eachLine.strip()
    eachLine = eachLine.split(',')
    
    eachLine[18]=replaceSpaceWithZero(eachLine[18])

    deathList.append(int(eachLine[18]))
    dates.append(eachLine[3])
    states.append(eachLine[0])
    totalDeaths.append(int(eachLine[4]))    

  mostCovidDeaths = max(deathList)
  mostDeathsIndex = deathList.index(mostCovidDeaths)

  mostDeathsWeek = dates[mostDeathsIndex]
  mostDeathsState = states[mostDeathsIndex]
  targetTotalDeaths = totalDeaths[mostDeathsIndex]

  percent = mostCovidDeaths / targetTotalDeaths
  percent = round(percent, 2)
    
  print('The largest number of deaths directly attributable to COVID 19 in this report range was', mostCovidDeaths,'in',mostDeathsState,'during the week of',mostDeathsWeek+'.')

  print('This represents',str(percent)+'% of the total reported deaths in',mostDeathsState,'that week.')
  print('=============================================')

# Make no changes below this line!
# --------------------------------

###  HELPER FUNCTION FOR YOU ###

# use this function when you need to compare date strings
# you can't actually compare strings that "look" like dates because they aren't
# date objects. They won't sort like you expect them to.
# This function accepts date in mm/dd/yy format as a string
# returns date in yy/mm/dd format as a date object (not a string!!!)
def convertDate(dateString):
  objDate = datetime.strptime(dateString, '%m/%d/%y')
  return objDate

# use this function to replace blank values with zero so that any math will work
def replaceSpaceWithZero(uString):
  if uString == '':
    uString = 0
  return int(uString)


# I've called main() for you.
# This line is a special way to call main
# that allows me to test your code.  Do not change it!
if __name__ == '__main__':
    main()
