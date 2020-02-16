#!/usr/bin/env python3
"""
Created on Mon Apr 15 22:35:39 2019

@author: Abdullah & Meltem
"""
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
url1 = "https://registration.boun.edu.tr/scripts/sch.asp?donem="
import sys


#Manually adding all the departments
department_list = open("/departments.txt")

'''
department_list_sorted=[]
for dep in department_list:
    department_list_sorted.append((dep[1],dep[0]))
'''
#Manually adding all the url extensions
url_list=[]
url_list.append("&kisaadi=ASIA&bolum=ASIAN+STUDIES")
url_list.append("&kisaadi=ASIA&bolum=ASIAN+STUDIES+WITH+THESIS")
url_list.append("&kisaadi=ATA&bolum=ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY")
url_list.append("&kisaadi=AUTO&bolum=AUTOMOTIVE+ENGINEERING")
url_list.append("&kisaadi=BM&bolum=BIOMEDICAL+ENGINEERING")
url_list.append("&kisaadi=BIS&bolum=BUSINESS+INFORMATION+SYSTEMS")
url_list.append("&kisaadi=CHE&bolum=CHEMICAL+ENGINEERING")
url_list.append("&kisaadi=CHEM&bolum=CHEMISTRY")
url_list.append("&kisaadi=CE&bolum=CIVIL+ENGINEERING")
url_list.append("&kisaadi=COGS&bolum=COGNITIVE+SCIENCE")
url_list.append("&kisaadi=CSE&bolum=COMPUTATIONAL+SCIENCE+%26+ENGINEERING")
url_list.append("&kisaadi=CET&bolum=COMPUTER+EDUCATION+%26+EDUCATIONAL+TECHNOLOGY")
url_list.append("&kisaadi=CMPE&bolum=COMPUTER+ENGINEERING")
url_list.append("&kisaadi=INT&bolum=CONFERENCE+INTERPRETING")
url_list.append("&kisaadi=CEM&bolum=CONSTRUCTION+ENGINEERING+AND+MANAGEMENT")
url_list.append("&kisaadi=CCS&bolum=CRITICAL+AND+CULTURAL+STUDIES")
url_list.append("&kisaadi=EQE&bolum=EARTHQUAKE+ENGINEERING")
url_list.append("&kisaadi=EC&bolum=ECONOMICS")
url_list.append("&kisaadi=EF&bolum=ECONOMICS+AND+FINANCE")
url_list.append("&kisaadi=ED&bolum=EDUCATIONAL+SCIENCES")
url_list.append("&kisaadi=CET&bolum=EDUCATIONAL+TECHNOLOGY")
url_list.append("&kisaadi=EE&bolum=ELECTRICAL+%26+ELECTRONICS+ENGINEERING")
url_list.append("&kisaadi=ETM&bolum=ENGINEERING+AND+TECHNOLOGY+MANAGEMENT")
url_list.append("&kisaadi=ENV&bolum=ENVIRONMENTAL+SCIENCES")
url_list.append("&kisaadi=ENVT&bolum=ENVIRONMENTAL+TECHNOLOGY")
url_list.append("&kisaadi=XMBA&bolum=EXECUTIVE+MBA")
url_list.append("&kisaadi=FE&bolum=FINANCIAL+ENGINEERING")
url_list.append("&kisaadi=PA&bolum=FINE+ARTS")
url_list.append("&kisaadi=FLED&bolum=FOREIGN+LANGUAGE+EDUCATION")
url_list.append("&kisaadi=GED&bolum=GEODESY")
url_list.append("&kisaadi=GPH&bolum=GEOPHYSICS")
url_list.append("&kisaadi=GUID&bolum=GUIDANCE+%26+PSYCHOLOGICAL+COUNSELING")
url_list.append("&kisaadi=HIST&bolum=HISTORY")
url_list.append("&kisaadi=HUM&bolum=HUMANITIES+COURSES+COORDINATOR")
url_list.append("&kisaadi=IE&bolum=INDUSTRIAL+ENGINEERING")
url_list.append("&kisaadi=INCT&bolum=INTERNATIONAL+COMPETITION+AND+TRADE")
url_list.append("&kisaadi=MIR&bolum=INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST")
url_list.append("&kisaadi=MIR&bolum=INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST+WITH+THESIS")
url_list.append("&kisaadi=INTT&bolum=INTERNATIONAL+TRADE")
url_list.append("&kisaadi=INTT&bolum=INTERNATIONAL+TRADE+MANAGEMENT")
url_list.append("&kisaadi=LS&bolum=LEARNING+SCIENCES")
url_list.append("&kisaadi=LING&bolum=LINGUISTICS")
url_list.append("&kisaadi=AD&bolum=MANAGEMENT")
url_list.append("&kisaadi=MIS&bolum=MANAGEMENT+INFORMATION+SYSTEMS")
url_list.append("&kisaadi=MATH&bolum=MATHEMATICS")
url_list.append("&kisaadi=SCED&bolum=MATHEMATICS+AND+SCIENCE+EDUCATION")
url_list.append("&kisaadi=ME&bolum=MECHANICAL+ENGINEERING")
url_list.append("&kisaadi=MECA&bolum=MECHATRONICS+ENGINEERING")
url_list.append("&kisaadi=BIO&bolum=MOLECULAR+BIOLOGY+%26+GENETICS")
url_list.append("&kisaadi=PHIL&bolum=PHILOSOPHY")
url_list.append("&kisaadi=PE&bolum=PHYSICAL+EDUCATION")
url_list.append("&kisaadi=PHYS&bolum=PHYSICS")
url_list.append("&kisaadi=POLS&bolum=POLITICAL+SCIENCE%26INTERNATIONAL+RELATIONS")
url_list.append("&kisaadi=PRED&bolum=PRIMARY+EDUCATION")
url_list.append("&kisaadi=PSY&bolum=PSYCHOLOGY")
url_list.append("&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES")
url_list.append("&kisaadi=SCED&bolum=SECONDARY+SCHOOL+SCIENCE+AND+MATHEMATICS+EDUCATION")
url_list.append("&kisaadi=SPL&bolum=SOCIAL+POLICY+WITH+THESIS")
url_list.append("&kisaadi=SOC&bolum=SOCIOLOGY")
url_list.append("&kisaadi=SWE&bolum=SOFTWARE+ENGINEERING")
url_list.append("&kisaadi=SWE&bolum=SOFTWARE+ENGINEERING+WITH+THESIS")
url_list.append("&kisaadi=TRM&bolum=SUSTAINABLE+TOURISM+MANAGEMENT")
url_list.append("&kisaadi=SCO&bolum=SYSTEMS+%26+CONTROL+ENGINEERING")
url_list.append("&kisaadi=TRM&bolum=TOURISM+ADMINISTRATION")
url_list.append("&kisaadi=WTR&bolum=TRANSLATION")
url_list.append("&kisaadi=TR&bolum=TRANSLATION+AND+INTERPRETING+STUDIES")
url_list.append("&kisaadi=TK&bolum=TURKISH+COURSES+COORDINATOR")
url_list.append("&kisaadi=TKL&bolum=TURKISH+LANGUAGE+%26+LITERATURE")
url_list.append("&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES")
my_dict = {}
my_dict_instr = {}

#my_dict and my_dict_instr holds a set that contains all the distinct 
#courses and instructors that a department opened throughout the given input semesters
for dep in department_list:
    my_dict[dep]=set()
    my_dict_instr[dep]=set()
    
starting_year = 2018
starting_term = "Spring"
finishing_year = 2018
finishing_term = "Fall"

#Starting index is calculated by simple calculations
#This index will determine the range of semester    
starting_index = (starting_year -1999)*3

if starting_term == "Spring" :
    starting_index +=1
elif starting_term == "Summer" :
    starting_index +=2
elif starting_term == "Fall" :
    starting_index +=3
    
#finishing index is calculated by simple calculations
#This index will determine the range of semester    
finishing_index = (finishing_year -1999)*3

if finishing_term == "Spring" :
    finishing_index +=1
elif finishing_term == "Summer" :
    finishing_index +=2
elif finishing_term == "Fall" :
    finishing_index +=3

#Dictionaries to make a pandas table
dict_total_offering={}
deptsList = {}

#returns the code and name of courses of given department list
def bombos(List):
    listTemp = []
    for x in List:
        listTemp.append(x[0])
    return listTemp

#for all departments we create some dictionaries
#key-values are 
#department names- semesters
#semesters-U/I/G
for ijm in range(len(url_list)):
    semesterDict = {}
    course_temp = {}
    total_course = {}
    total_course['U'] = 0
    total_course['G'] = 0
    total_course['I'] = 0
    
    #for all input semester range
    #loop iterates 
    for ijk in range(starting_index, finishing_index+1):#+1 makes sure last semester is included
        check = False
        semesterTemp = {}
        url_composed = url1+donem_list[ijk]+url_list[ijm] # url is composed by concatenation
        #print(url_composed)
#        r 
        r = requests.get(url_composed, timeout = 5)
        soup = BeautifulSoup(r.content,'html.parser')
        i=0
        indexes=[]
        #if no table is found then department doesnt open any classes
        if (soup.find('tr',{'class':'schtitle'})==None):
            U=G=I=0
            course_list = []
            check = True
        #else we read the html file by beautiful soup 4 
        else:    
            #U-I-G values are initially zero every iteration
            #They hold local undergraduate-graduate-instructor number
            #we observed sometimes instructor names are in 6th column
            #we guarantee that we will catch those
            U=G=I=0   
            for td in soup.find('tr',{'class':'schtitle'}).find_all('td'):
                if(td.text=="Code.Sec"):
                    indexes.append(i)
                elif(td.text=="Name"):
                    indexes.append(i)
                elif(td.text=="Instr."):
                    indexes.append(i)
                i+=1    
        
            course_list=[]
            #course_list has the info about a lecture
            #it is a tuple of which has the first entry code and name tuple 
            #second value is instructor name
            for tr in soup.find_all('tr',{'class':'schtd'}):
                str_=""
                str_1=""
                str_2=""
                str_1=str_1+str(tr.find_all('td')[indexes[1]].text.strip())
                #if lab or ps then pass those rows
                if(str_1=="LAB"):
                    continue
                elif(str_1=="P.S."):
                    continue
                str_=str_+str(tr.find_all('td')[indexes[0]].text.strip())
                str_=str_[:str_.index('.')]
                str_2=str_2+str(tr.find_all('td')[indexes[2]].text.strip())
                course_list.append(((str_,str_1),str_2))
            for tr in soup.find_all('tr',{'class':'schtd2'}):
                #in the html we saw that important data are between tr class schtd and tr class schtd2 
                str_=""
                str_1=""
                str_2=""
                str_1=str_1+str(tr.find_all('td')[indexes[1]].text.strip())
                if(str_1=="LAB"):
                    continue
                elif(str_1=="P.S."):
                    continue
                str_=str_+str(tr.find_all('td')[indexes[0]].text.strip())
                str_=str_[:str_.index('.')]
                str_2=str_2+str(tr.find_all('td')[indexes[2]].text.strip())
                course_list.append(((str_,str_1),str_2))
            
            course_list_set = set()
            course_list_instructors=set()
            #Distinct instructor and course names are found using set
            for x in course_list:
                if(not(x[1]=="STAFF" or  x[1]== "STAFF STAFF" or x[1]=="staff")):
                    course_list_instructors.add(x[1])
                    my_dict_instr[department_list[ijm]].add(x[1])
                    
                if x[0] not in course_temp and x[1] != 'STAFF STAFF' :
                    #increase total offering U/G by 1
                    course_temp[x[0]] = [1,1]
                elif x[0] not in course_temp and x[1] == 'STAFF STAFF':
                    course_temp[x[0]] = [1,0]
                elif x[0] in course_temp:
                    course_temp[x[0]][0] += 1
                    if x[1] not in my_dict_instr[department_list[ijm]] and x[1] != 'STAFF STAFF' :
                        course_temp[x[0]][1] += 1
                    
                course_list_set.add((x[0][0],x[0][1]))
                #my_dict holds name and code of key department
                my_dict[department_list[ijm]].add((x[0][0],x[0][1]))
                #if staff then dont contribute
                
                    
            for x in course_list_set:
                #calculation of local U and G
                if(x[0][-3]<='4'):
                    U+=1
                else:
                    G+=1
        #put them into dictionary
        semesterTemp['U'] = U
        semesterTemp['G'] = G
        if check == True :
            semesterTemp['I'] = 0
        else :
            semesterTemp['I'] = len(course_list_instructors)
        semesterDict[ijk] = [course_list, semesterTemp]
        #calculation of total offering U and G
    for course in my_dict[department_list[ijm]] :
        if(course[0][-3] <= '4') :
            total_course['U'] +=1
        else :
            total_course['G'] +=1
            
        for ijk in range(starting_index, finishing_index+1):
            listTemp = bombos(semesterDict[ijk][0])
            if course in listTemp :
                #if course is opened once then x 
                course_temp[course].append('x')
            else :
                #else empty slot
                course_temp[course].append(' ')
    #length of the set will be number of instructors of that department
    #print(my_dict_instr[department_list[ijm]])
    total_course['I'] = len(my_dict_instr[department_list[ijm]])
    deptsList[ijm] = [semesterDict, course_temp, total_course]
    #print(deptsList[ijm])
    #print('**********************************************')
    
#Creation of data frame table
#Check are used for quick determinations that a given value is included or not
def constructTable() :
    
    columns = ['Dep./Prog.(name)', 'Course Code', 'Course Name']
    check1 = False
    check2 = False
    checkAll = True
    frameDict = {'Dep./Prog.(name)' : [None],
                 'Course Code' : [None],
                 'Course Name' : [None],
                 'Total Offerings' : [None]
                 }
    year_semester = []
    for year in range(starting_year, finishing_year+1):
        for semester in ['Spring', 'Summer', 'Fall']:
            if year == starting_year and semester == starting_term:
                check1 = True
            if year == finishing_year and semester == finishing_term:
                check2 = True
            if check1 == True and checkAll == True:
                yearSemester = str(year) + '-' + str(semester)
                year_semester.append(yearSemester)
                frameDict.update({yearSemester : [None]})
                #Add semester columns to df
                columns.extend([yearSemester])
            if check2 == True:
                checkAll = False
           
    #after extending column by one per semesters
    #finally add Total Offerings column
    columns.extend(['Total Offerings'])
    return frameDict, columns, year_semester
#construct table returns 
#dataframe created by pandas
#columns of dataframe
#and information inside
frameDict,columnsTemp, year_semester = constructTable()

for index, dep in enumerate(department_list) :
    indexTemp = starting_index
    depName = str(dep[1]) + '(' + str(dep[0]) + ')'
    frameDict['Dep./Prog.(name)'].extend([depName])
    totalName = 'U' + str(deptsList[index][2]['U']) + ' G' + str(deptsList[index][2]['G'])
    frameDict['Course Code'].extend([totalName])
    frameDict['Course Name'].extend([' '])
    totalSemesterU = 0
    totalSemesterG = 0
    totalSemesterI = deptsList[index][2]['I']
    for yearSemester in year_semester:
        semesterTemp = 'U' + str(deptsList[index][0][indexTemp][1]['U']) + ' G' + str(deptsList[index][0][indexTemp][1]['G']) + ' I' + str(deptsList[index][0][indexTemp][1]['I'])
        frameDict[yearSemester].extend([semesterTemp])
        totalSemesterU += deptsList[index][0][indexTemp][1]['U']
        totalSemesterG += deptsList[index][0][indexTemp][1]['G']
        indexTemp += 1
               
    totalSemester = 'U' + str(totalSemesterU) + ' G' + str(totalSemesterG) + ' I' + str(deptsList[index][2]['I'])
    frameDict['Total Offerings'].extend([totalSemester])
    
    for xd in deptsList[index][1] :
        frameDict['Dep./Prog.(name)'].extend([' '])
        frameDict['Course Code'].extend([xd[0]])
        frameDict['Course Name'].extend([xd[1]])
        totalOfferings = str(deptsList[index][1][xd][0]) + '/' + str(deptsList[index][1][xd][1])
        frameDict['Total Offerings'].extend([totalOfferings])
        for index1, yearSemester in enumerate(year_semester) :        
            frameDict[yearSemester].extend([deptsList[index][1][xd][index1+2]])
    #print(frameDict)
    
#dataframe object is created                
df = pd.DataFrame(frameDict, columns = columnsTemp)
df = df.iloc[1:]
df.to_csv("cout.csv",encoding='utf-8',index=False)
print(df)    
                
                
            
    
    
    
        