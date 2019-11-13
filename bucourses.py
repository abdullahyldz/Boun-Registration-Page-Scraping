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

input1=sys.argv[1]
input2=sys.argv[2]
starting_year,starting_term=input1.split("-")
finishing_year,finishing_term=input2.split("-")
starting_year=int(starting_year)
finishing_year=int(finishing_year)

#Manually adding all the terms
donem_list = []
donem_list.append("1998/1999-1")
donem_list.append("1998/1999-2")
donem_list.append("1998/1999-3")
donem_list.append("1999/2000-1")
donem_list.append("1999/2000-2")
donem_list.append("1999/2000-3")
donem_list.append("2000/2001-1")
donem_list.append("2000/2001-2")
donem_list.append("2000/2001-3")
donem_list.append("2001/2002-1")
donem_list.append("2001/2002-2")
donem_list.append("2001/2002-3")
donem_list.append("2002/2003-1")
donem_list.append("2002/2003-2")
donem_list.append("2002/2003-3")
donem_list.append("2003/2004-1")
donem_list.append("2003/2004-2")
donem_list.append("2003/2004-3")
donem_list.append("2004/2005-1")
donem_list.append("2004/2005-2")
donem_list.append("2004/2005-3")
donem_list.append("2005/2006-1")
donem_list.append("2005/2006-2")
donem_list.append("2005/2006-3")
donem_list.append("2006/2007-1")
donem_list.append("2006/2007-2")
donem_list.append("2006/2007-3")
donem_list.append("2007/2008-1")
donem_list.append("2007/2008-2")
donem_list.append("2007/2008-3")
donem_list.append("2008/2009-1")
donem_list.append("2008/2009-2")
donem_list.append("2008/2009-3")
donem_list.append("2009/2010-1")
donem_list.append("2009/2010-2")
donem_list.append("2009/2010-3")
donem_list.append("2010/2011-1")
donem_list.append("2010/2011-2")
donem_list.append("2010/2011-3")
donem_list.append("2011/2012-1")
donem_list.append("2011/2012-2")
donem_list.append("2011/2012-3")
donem_list.append("2012/2013-1")
donem_list.append("2012/2013-2")
donem_list.append("2012/2013-3")
donem_list.append("2013/2014-1")
donem_list.append("2013/2014-2")
donem_list.append("2013/2014-3")
donem_list.append("2014/2015-1")
donem_list.append("2014/2015-2")
donem_list.append("2014/2015-3")
donem_list.append("2015/2016-1")
donem_list.append("2015/2016-2")
donem_list.append("2015/2016-3")
donem_list.append("2016/2017-1")
donem_list.append("2016/2017-2")
donem_list.append("2016/2017-3")
donem_list.append("2017/2018-1")
donem_list.append("2017/2018-2")
donem_list.append("2017/2018-3")
donem_list.append("2018/2019-1")
donem_list.append("2018/2019-2")
donem_list.append("2018/2019-3")
#Manually adding all the departments
department_list = []
department_list.append(('ASIAN STUDIES', 'ASIA'))
department_list.append(('ASIAN STUDIES WITH THESIS', 'ASIA'))
department_list.append(("ATATURK INSTITUTE FOR MODERN TURKISH HISTORY", "ATA"))
department_list.append(("AUTOMOTIVE ENGINEERING", "AUTO"))
department_list.append(("BIOMEDICAL ENGINEERING", "BM"))
department_list.append(("BUSINESS INFORMATION SYSTEMS", "BIS"))
department_list.append(("CHEMICAL ENGINEERING", "CHEM"))
department_list.append(("CHEMISTRY", "CHEM"))
department_list.append(("CIVIL ENGINEERING", "CIV"))
department_list.append(("COGNITIVE SCIENCE", "COG"))
department_list.append(("COMPUTATIONAL SCIENCE & ENGINEERING", "CSE"))
department_list.append(("COMPUTER EDUCATION & EDUCATIONAL TECHNOLOGY", "CET"))
department_list.append(("COMPUTER ENGINEERING", "CMPE"))
department_list.append(("CONFERENCE INTERPRETING", "INT"))
department_list.append(("CONSTRUCTION ENGINEERING AND MANAGEMENT", "CEM"))
department_list.append(("CRITICAL AND CULTURAL STUDIES", "CCS"))
department_list.append(("EARTHQUAKE ENGINEERING", "EQE"))
department_list.append(("ECONOMICS", "EC"))
department_list.append(("ECONOMICS AND FINANCE", "EF"))
department_list.append(("EDUCATIONAL SCIENCES", "ED"))
department_list.append(("EDUCATIONAL TECHNOLOGY", "CET"))
department_list.append(("ELECTRICAL & ELECTRONICS ENGINEERING", "EE"))
department_list.append(("ENGINEERING AND TECHNOLOGY MANAGEMENT", "ETM"))
department_list.append(("ENVIRONMENTAL SCIENCES", "ESC"))
department_list.append(("ENVIRONMENTAL TECHNOLOGY", "ESC"))
department_list.append(("EXECUTIVE MBA", "ADEX"))
department_list.append(("FINANCIAL ENGINEERING", "FE"))
department_list.append(("FINE ARTS", "FA"))
department_list.append(("FOREIGN LANGUAGE EDUCATION", "FLED"))
department_list.append(("GEODESY", "GED"))
department_list.append(("GEOPHYSICS", "GPH"))
department_list.append(("GUIDANCE & PSYCHOLOGICAL COUNSELING", "ED"))
department_list.append(("HISTORY", "HIST"))
department_list.append(("HUMANITIES COURSES COORDINATOR", "HUM"))
department_list.append(("INDUSTRIAL ENGINEERING", "IE"))
department_list.append(("INTERNATIONAL COMPETITION AND TRADE", "INCT"))
department_list.append(("INTERNATIONAL RELATIONS:TURKEY,EUROPE AND THE MIDDLE EAST", "MIR"))
department_list.append(("INTERNATIONAL RELATIONS:TURKEY,EUROPE AND THE MIDDLE EAST WITH THESIS", "MIR"))
department_list.append(("INTERNATIONAL TRADE", "INTT"))
department_list.append(("INTERNATIONAL TRADE MANAGEMENT", "INTT"))
department_list.append(("LEARNING SCIENCES","LS"))
department_list.append(("LINGUISTICS", "LING"))
department_list.append(("MANAGEMENT", "AD"))
department_list.append(("MANAGEMENT INFORMATION SYSTEMS", "MIS"))
department_list.append(("MATHEMATICS", "MATH"))
department_list.append(("MATHEMATICS AND SCIENCE EDUCATION", "SCED"))
department_list.append(("MECHANICAL ENGINEERING", "ME"))
department_list.append(("MECHATRONICS ENGINEERING", "MECA"))
department_list.append(("MOLECULAR BIOLOGY & GENETICS", "BIO"))
department_list.append(("PHILOSOPHY", "PHIL"))
department_list.append(("PHYSICAL EDUCATION", "PE"))
department_list.append(("PHYSICS", "PHYS"))
department_list.append(("POLITICAL SCIENCE&INTERNATIONAL RELATIONS", "POLS"))
department_list.append(("PRIMARY EDUCATION", "PRED"))
department_list.append(("PSYCHOLOGY", "PSY"))
department_list.append(("SCHOOL OF FOREIGN LANGUAGES", "YADYOK"))
department_list.append(("SECONDARY SCHOOL SCIENCE AND MATHEMATICS EDUCATION", "SCED"))
department_list.append(("SOCIAL POLICY WITH THESIS", "SPL"))
department_list.append(("SOCIOLOGY", "SOC"))
department_list.append(("SOFTWARE ENGINEERING", "SWE"))
department_list.append(("SOFTWARE ENGINEERING WITH THESIS", "SWE"))
department_list.append(("SUSTAINABLE TOURISM MANAGEMENT", "TRM"))
department_list.append(("SYSTEMS & CONTROL ENGINEERING","SCO"))
department_list.append(("TOURISM ADMINISTRATION", "TRM"))
department_list.append(("TRANSLATION", "WTR"))
department_list.append(("TRANSLATION AND INTERPRETING STUDIES", "TR"))
department_list.append(("TURKISH COURSES COORDINATOR", "TK"))
department_list.append(("TURKISH LANGUAGE & LITERATURE", "TKL"))
department_list.append(("WESTERN LANGUAGES & LITERATURES", "LL"))

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
#List comprehension
[(t[1], t[0]) for t in department_list]
#Sort them at the same time
department_list, url_list = (list(t) for t in zip(*sorted(zip(department_list, url_list))))
#List comprehension
[(t[1], t[0]) for t in department_list]
#my_dict and my_dict_instr holds a set that contains all the distinct 
#courses and instructors that a department opened throughout the given input semesters
for dep in department_list:
    my_dict[dep]=set()
    my_dict_instr[dep]=set()
    

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
                
                
            
    
    
    
        