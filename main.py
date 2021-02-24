#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Arshad Bin Azizul
#Group Name: DaBoys
#Class: <PN2004K>
#Date: 19/2/2021
#Version: <1.0>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#########################################################################
 
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
 def __init__(self):
   #load excel data (CSV format) to dataframe - 'df'
   df=pd.read_csv('MonthyVisitors.csv')
 #show specific country dataframe
   sortCountry(df)
 #displaying table from 2007-2017
 
#########################################################################
#CLASS Branch: End of Code
#########################################################################
 
#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
 
def sortCountry(df):
 
 #print number of rows in dataframe
 print("There are " + str(len(df)) + " data rows read. \n")
 
 #display dataframe (rows and columns)
 print("The following dataframe are read as follows: \n")
 print(df)
 
 #display a specific country (Australia) in column #33
 country_label = df.columns[33]
 print("\n\n" + country_label + "was selected.")
 
 #display a sorted dataframe based on selected country
 print(" The" + country_label + "was sorted in ascending order. \n")
 sorted_df =df.sort_values(country_label,ascending=[0]) 
 print("The following dataframe for SEA from 2006 to 2016 are read as follows: \n")
 
 print(df.iloc[336:468,:20].sort_index(axis=0,ascending=True))
 
 df = df.iloc[336:468,:20]
 
 visitor=[]
 visitor_Total = [] 
 country_row=[]
 Country_dict={}
 
 #find country from india to UAE (14:20)
 for country in df.columns[14:20]:
   country_row.append(country)
 for i in df[country]:
   visitor.append(i)
 for i in range(0,len(visitor)):
   visitor[i]=int(visitor[i])
 
 number_of_lines = len(visitor)
 counter = number_of_lines/len(country_row)
 
 indValue1 = 0
 indValue2 = int(counter)
 for i in range(0,len(country_row)):
   visitor_Total.append(sum(visitor[indValue1:indValue2]))
   indValue1=indValue1 + (int(counter))
   indValue2=indValue2 + (int(counter))
 
 Country_dict = { country_row[i]: visitor_Total[i] for i in range(len(country_row))}
 sort_Country_dict = sorted(Country_dict.items(), key=lambda x: x[1], reverse=True)
 df = pd.DataFrame(list(Country_dict.items()),columns = ['Country','Visitors'])
 print("The South-Asia Pacific and Middle-East visitors that travelled to Singapore from 2007-2017 are listed in descending order:","\n",df)
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################
 
#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
 
 #Project Title
 print('######################################')
 print('# Data Analysis App - PYTHON Project #')
 print('######################################')
 #perform data analysis on specific excel (CSV) file
 DataAnalysis()
#########################################################################
#Main Branch: End of Code
#########################################################################