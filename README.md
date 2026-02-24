 ** Be sure to review this ENTIRE document!

# Final Project
********************************
This project brings together the work you've done this semester into a single project. As we've discussed many times, Python is great for reporting large datasets. We'll be using a moderately sized dataset for our project.
Using what you've learned this semester, it's time to write a complete program, that is similar to that of a program you might be asked to write in the real world. You'll be responsible for writing the User Interface (UI) which displays on the screen, as well as generating reports as text files.  Your final submission will represent an example of a basic, fully functional, program that would be great for you to keep and refer to in job interviews.

For this project you will be writing a program that compares REAL mortality data gathered from the Centers For Disease Control. The data is publically available on the CDC website and is updated weekly.  We'll be specifically using the database maintained to report COVID deaths, as compared to other tracked mortality rates.  To keep things simple, this data is provided for you here in Repl as the following files:

#### FILES PROVIDED
  * cdc.csv - This report includes mortality data from the start date (shown in the file).  This file is "live", meaning it will update automatically from time to time during your project.  The format will not change, but the data on mortality will certainly be updated and added to!
  * causes_of_death.txt - This file contains the causes of death used in the cdc.csv file.  While contents will not change format, it is possible that spelling and identification numbers (IE: L019,L018, etc.) could change. Therefore, should always pull this file each time you report.

  * hints.md - Fairly obvious, I hope? 
#### --
## About Grading

Your program will be hand graded.  I will be reviewing quality and efficiency of code and comments as well as function.  The expectation is that this program will be clean, complete and fully debugged prior to submission.  However, I will consider applying partial credit in most cases, so be sure to submit your best effort.

 ** You must follow the following expectations for all project portions:
  * Program should end or quit ONLY when the user selects menu item: Exit
  * Make sure your program FULLY TESTS ALL USER INPUT.  
  * Be sure to handle any system errors, unless specifically directed not to.  I should see no "red" errors while testing your code.
  * Remember to BLOCK comment your code.  Failure to properly comment your code will result in a 0 for the project. 
  * Look closely at report names and headers.  Yours must match!  Reports should also include the timestamp (automatically generated) for when the report is written.  Be sure to see the hints for that code!

***
## Part I


Your program MUST effectively implement all of the following functions as described:

* main() - Void function.  Accepts nothing. Calls banner(). Calls the menu() and receives menu values. Loops, exits, and calls other functions as needed for each menu item.

* banner() - Void function. Accepts no input. Displays an ASCII banner for your project.

* menu() - Accepts nothing. Returns one integer. Asks the user to make a selection.  Tests selection to make sure it's a valid value.  Loops until a valid value is selected. In Part 1, only items 1,2, and 5 need actions associated with them. This changes in Part 2.  Returns an integer.

* openCDCfile() - Accepts nothing.  Opens the cdc.csv file, removes unneeded lines of data and returns the file handler (NOT the whole file as a string).  Hint: use next(fileHandler) to remove a line.

* defaultReport() - void function. This function must create a report called "Full_Mortality_By_State_Report.txt".  The report should closely resemble the example given below. The report must include ALL data from the cdc.csv file.  Remember that this file's data is based on weekly reports from the CDC. Thus it can, and may, be updated at anytime. How this goal is achieved is left largely to the programmer. 

** Grading of this portion of the project will be based on efficiency of coding, quality of comments, and quality of report among other factors.

### UI Example
```
_____________________________________________________ 
╔═╗┬┌┐┌┌─┐┬    ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌─┐┬─┐  ╔╦╗╦╔═╗┬
╠╣ ││││├─┤│    ╠═╝├┬┘│ │ │├┤ │   │   │ │├┬┘   ║║║║╣ │
╚  ┴┘└┘┴ ┴┴─┘  ╩  ┴└─└─┘└┘└─┘└─┘ ┴   └─┘┴└─  ═╩╝╩╚═╝o 
_____________________________________________________ 
 

Mortality Rate Comparison Menu
    
1. Show This Menu Again
2. Full Mortality Report by State
3. Mortality for a Single State, by Date Range
4. Mortality Summary for all States
5. Exit

Make your selection from the menu: 
```

### Report File Example
```
National Mortality Rate by Cause Listed by State and Reporting Date Report    Sorted by State    
Report Generated: 11/08/2020     21:16:34
                              WEEK        TOTAL         NATURAL      C19 MULTIPLE    C19 UNDERLYING
STATE                         ENDING      DEATHS        CAUSES          CAUSES           CAUSE
--------------------------------------------------------------------------------------------------
Alabama                        1/5/19      1077            993              0              0
Alabama                       1/12/19      1090            994              0              0
Alabama                       1/19/19      1114           1042              0              0
Alabama                       1/26/19      1063            994              0              0
Alabama                        2/2/19      1095           1026              0              0
```

***

*** 
## Part II
All of the functionality must be maintained.  Everything in part 2 is an update and/or addition to that existing program!

#### Creating Comparison Reports

* menu() - Gets an update: Updates the UI with a new menu option for "5. Highest COVID mortality Week"
Accepts nothing. Returns one integer. Asks the user to make a selection.  Tests selection to make sure it's a valid value.  Loops until a valid value is selected.  Returns an integer.

* getUserInputDates() accepts nothing. Calls getAvailableDates and displays them for the user. Asks user for start and end dates. Gives the option of automatically setting start and end dates with the letter 'S' and 'E' (see output example). This function requires user to enter a valid start and end date (IE: dates covered in the data) in that order. Start and end date input requests must repeat individually until this is accomplished for both. Use the provided convertDate() function to temporarily convert strings to date objects for comparison. Returns a valid start and end date as strings (NOT as date objects)  

* getAvailableDates() accepts nothing. Calls openCDCFile() and determines the first date and the last date available in the document. Remember that this document is NOT in date order, so you cannot assume the first line is the first date and the last line is the last date. This file may also be updated at anytime, so be sure you're always reviewing the most up to date data.  Returns two strings: the start date, and the end date, in that order.

* reportSingleStateDataByDate() accepts nothing. This function is very similar to the default report. However, it reports for a single state and for a specific date range.  Ask the user to enter a State to review (no need for error checking). Call getUserInputDates() to get a date range for the function. Using this State and date range, generate a report file called "Mortality_For_State_By_Date_Range_Report.txt". The report should closely resemble the example given below. The report must include ALL data from the cdc.csv file for the selected State and date range.  Remember that this file's data is based on weekly reports from the CDC. Thus it can, and may, be updated at anytime. How this goal is achieved is left largely to the programmer. 

* totalMortalityByState() accepts nothing. This function generates a report of the sum total of deaths, as well as the total of those were natural causes, C19 Multiple Causes, and C19 Underlying Cause for the entire date range. This function creates a report file called report called "Mortality_Summary_For_All_States_By_Date_Range_Report.txt".  It then prints the headers, and loops through the data to generate each total.  Totals for each state are sent to printLineDetailReport() to be printed to the report.

* printLineDetailReport() receives the open file handler, the State, and four integers that represent the sum for each State: Total Deaths, Natural Causes, C19 Multiple Causes, and C19 Underlying Causes.  Converts the integers to strings, then appends the summary detail to the report "Mortality_Summary_For_All_States_By_Date_Range_Report.txt". 

* GetHighestMortality() Void function. Accepts nothing. This function must determine the highest reported week of COVID19 mortality as an underlying cause of death, what week that was, what state (or report location) it occured in, and what percentage of total deaths that week this number represents.  The function then prints out the message on screen as shown at the end of this readme file.


** Grading of this portion of the project will be based on efficiency of coding, quality of comments, and quality of report among other factors. 

### UI Example
```
_____________________________________________________ 
╔═╗┬┌┐┌┌─┐┬    ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌─┐┬─┐  ╔╦╗╦╔═╗┬
╠╣ ││││├─┤│    ╠═╝├┬┘│ │ │├┤ │   │   │ │├┬┘   ║║║║╣ │
╚  ┴┘└┘┴ ┴┴─┘  ╩  ┴└─└─┘└┘└─┘└─┘ ┴   └─┘┴└─  ═╩╝╩╚═╝o 
_____________________________________________________ 
 

Mortality Rate Comparison Menu
    
1. Show This Menu Again
2. Full Mortality Report by State
3. Mortality for a Single State, by Date Range
4. Mortality Summary for all States
5. Highest COVID mortality Week
6. Exit

Make your selection from the menu: 3
What State do you want to review? Virginia
Reporting is available from 1/5/19 to 10/24/20
Choose your starting date in (mm/dd/yy) format, or S for the first date of the data: 08/1/20
Select your ending date in (mm/dd/yy) format or E for the last date of the data: 20200
Not a valid date or format. Please try again.
Select your ending date in (mm/dd/yy) format or E for the last date of the data: e


**** REPORT PRINTED **** 
```

### Mortality for State By Date Range Report
```
Mortality for Virginia, by Date Range    For the selected date range 08/1/20 - 10/24/20

Report Generated: 11/08/2020     21:12:51

                              WEEK        TOTAL         NATURAL      C19 MULTIPLE    C19 UNDERLYING
STATE                         ENDING      DEATHS        CAUSES          CAUSES           CAUSE
--------------------------------------------------------------------------------------------------
Virginia                       8/1/20      1452           1326            102             97
Virginia                       8/8/20      1505           1367             87             83
Virginia                      8/15/20      1448           1361            101             89
Virginia                      8/22/20      1449           1357            123            113
```

### Mortality Summary for All States Report
```
Mortality Summary For All States By Date Range Report
For the selected date range 1/5/19 - 10/24/20

Report Generated: 11/08/2020     21:20:11

                              TOTAL    NATURAL       C19 MULTIPLE    C19 UNDERLYING
STATE                         DEATHS   CAUSES          CAUSES           CAUSE
--------------------------------------------------------------------------------------------------
Alabama                        101510     93994           3838           3838
Alaska                           8142      6793              0              0
Arizona                        121413    108669           5278           5278
```

### Highest Mortality Week Report

```
_____________________________________________________ 
╔═╗┬┌┐┌┌─┐┬    ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌─┐┬─┐  ╔╦╗╦╔═╗┬
╠╣ ││││├─┤│    ╠═╝├┬┘│ │ │├┤ │   │   │ │├┬┘   ║║║║╣ │
╚  ┴┘└┘┴ ┴┴─┘  ╩  ┴└─└─┘└┘└─┘└─┘ ┴   └─┘┴└─  ═╩╝╩╚═╝o 
_____________________________________________________ 
 

Mortality Rate Comparison Menu
    
1. Show This Menu Again
2. Full Mortality Report by State
3. Mortality for a Single State, by Date Range
4. Mortality Summary for all States
5. Highest COVID mortality Week
6. Exit

Make your selection from the menu: 5


The largest number of deaths directly attributible to COVID 19 in this report range was 0 in Some City during the week of 01/01/01.

This represents 3% of the total reported deaths in Some City that week.
