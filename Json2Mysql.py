#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import  csv
import codecs



def getJsonFile(fileName):
    data=[]
    with open(fileName) as file:
        for line in file:
            #print line
            data.append(json.loads(line))
    file.close()
    return data
def getCSVFile(fileName):

    with open(fileName) as file:
        f_csv=csv.reader(file)
        headers=next(f_csv)
        for row in f_csv:
            yield row
    file.close()

if __name__=='__main__':

    fileName=raw_input('please enter file path,Usage:/home/peter/fintech/data/detail.json....\n')
    #data=getJsonFile(fileName)
    #print json.dumps(data,ensure_ascii=False)

    str='\r\n'
    count=0
    for item in  getCSVFile(fileName):

        str= str+"INSERT INTO TB_OPEN_BLACK_CASE " \
             "(Black_Case_ID,Name,IDCard_Num,Mobile,Email," \
                 "QQ,Marriage,School,Degree,Graduated_Year," \
                 "IDCard_Address,Home_Address,Home_Phone,Office_Address,Position," \
                 "Job_Entry_Date,Work_Phone,Month_Income,Card_Issue_Bank,Card_Num," \
                 "Case_ID,Contract_Num,House_Value,House_Address,Car_Value," \
                 "Car_Num,Overdue_Capital,Loan_Date,Loan_Term,Repaid_Capital," \
                 "Default_Interest,Max_Overdue_Days,Sum_Overdue_Count,Black_Reason,Case_Status," \
                 "Case_Exposed_Date,Info_Source,Info_source_URL,Info_Captured_TS)" \
             "VALUES"
        str=str+"('%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s');\r\n" \
                %(item[0],item[1],item[2],item[3],item[4],
                  item[5],item[6],item[7],item[8],item[9],
                  item[10],item[11],item[12],item[13],item[14],
                  item[15],item[16],item[17],item[18],item[19],
                  item[20],item[21],item[22],item[23],item[24],
                  item[25],item[26],item[27],item[28],item[29],
                  item[30],item[31],item[32],item[33],item[34],
                  item[35],item[36],item[37],item[38]
                  )
        count=count+1
        print count,str

    sqlFileName=raw_input('please input filename you want to save....\n')
    saveFile = codecs.open(sqlFileName,'w')
    saveFile.write(str)
    saveFile.close()
    '''

    for item in data:
        #print json.dumps(item,ensure_ascii=False)

        str= str+"INSERT INTO TB_OPEN_BLACK_CASE " \
             "(Black_Case_ID,Name,IDCard_Num,Mobile,Email," \
                 "QQ,Marriage,School,Degree,Graduated_Year," \
                 "IDCard_Address,Home_Address,Home_Phone,Office_Address,Position," \
                 "Job_Entry_Date,Work_Phone,Month_Income,Card_Issue_Bank,Card_Num," \
                 "Case_ID,Contract_Num,House_Value,House_Address,Car_Value," \
                 "Car_Num,Overdue_Capital,Loan_Date,Loan_Term,Repaid_Capital," \
                 "Default_Interest,Max_Overdue_Days,Sum_Overdue_Count,Black_Reason,Case_Status," \
                 "Case_Exposed_Date,Info_Source,Info_source_URL,Info_Captured_TS,Created_Date," \
                 "Last_updated_date)" \
             "VALUES"
        str=str+"('%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s'," \
                "'%s','%s','%s','%s','%s','%s');\r\n" \
                %(item['Black_Case_ID'],item['Name'],item['IDCard_Num'],item['Mobile'],item['Email'],
                  item['QQ'],item['Marriage'],item['School'],item['Degree'],item['Graduated_Year'],
                  )

        '''