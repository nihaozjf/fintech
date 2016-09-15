#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from util import initLogger
from util import initDB

logger=initLogger('log.conf','dlmLogger')

data={
    u'姓名':'Name',
    u'身份证':'IDCard_Num',
    u'身份证号':'IDCard_Num',
    u'手机号码': 'Mobile',
    u'手机号': 'Mobile',
    u'联系邮箱': 'Email',
    u'邮箱地址': 'Email',
    u'QQ': 'QQ',
    u'QQ号': 'QQ',
    u'婚姻状况': 'Marriage',
    u'学历': 'Degree',
    u'毕业学校': 'School',
    u'毕业年份': 'Graduated_Year',
    u'户口地址': 'IDCard_Address',
    u'证件地址': 'IDCard_Address',
    u'家庭住址': 'Home_Address',
    u'居住地址': 'Home_Address',
    u'家庭电话': 'Home_Phone',
    u'居住电话': 'Home_Phone',
    u'单位地址': 'Office_Address',
    u'公司地址': 'Office_Address',
    u'公司名称': 'Office_Name',
    u'具体职位': 'Position',
    u'入职时间': 'Job_Entry_Date',
    u'工作电话': 'Work_Phone',
    u'公司电话': 'Work_Phone',
    u'月收入': 'Month_Income',
    u'银行卡开户行': 'Card_Issue_Bank',
    u'信用卡发卡银行': 'CreditCard_Issue_Bank',
    u'银行卡卡号': 'Card_Num',
    u'案件编号(源)': 'Case_ID',
    u'标号/合同号': 'Contract_Num',
    u'房产市值': 'House_Value',
    u'房产地址': 'House_Address',
    u'车辆市值': 'Car_Value',
    u'车辆编号': 'Car_Num',
    u'总逾期本金': 'Overdue_Capital',
    u'本金/本息': 'Overdue_Capital',
    u'借款时间': 'Loan_Date',
    u'借款期数': 'Loan_Term',
    u'已还金额': 'Repaid_Capital',
    u'未还/罚息': 'Default_Interest',
    u'逾期最大天数': 'Max_Overdue_Days',
    u'总逾期借款笔数': 'Sum_Overdue_Count',
    u'原因描述': 'Black_Reason',
    u'状态': 'Case_Status',
    u'上传时间': 'Case_Exposed_Date',
    u'信息来源更新时间': 'Case_Exposed_Date',
    u'信息来源': 'Info_Source',
    u'信息来源URL': 'Info_source_URL',
    u'信息来源网址': 'Info_source_URL',
    u'抓取时间': 'Info_Captured_TS',
    u'创建日期': 'Created_Date',
    u'修改日期': 'Last_updated_date',


}

if __name__=='__main__':
    #print 'please enter the table you want to convert'
    tableName = raw_input('please enter the table you want to convert.....\n')

    logger.info('connect to table '+tableName)
    table = initDB('fintech', tableName)
    jsonTable=initDB('fintech',tableName+'_json')

    for t in table.find():
        jsonData={}
        for key in t.keys():
            if(key!='_id' and  key!=u'妻子电话'  and key!=u'丈夫'):
                #print data[key],t[key]

                jsonKey=data[key]
                jsonValue=t[key]
                print jsonKey,jsonValue
                jsonData[jsonKey]=jsonValue

        #print jsonData
        jsonTable.insert_one(jsonData)

        print 20*'*'



