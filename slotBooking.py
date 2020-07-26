import random
import MySQLdb
import datetime
from time import gmtime, strftime

DataBase = MySQLdb.connect(host="localhost",    
                     user="root",        
                     passwd="1234",
                     db="vlabs_sbhs")    

sor5=DataBase.cursor()
cu1=DataBase.cursor()
querry1='SELECT * FROM tables_booking'
cu1.execute(querry1)


nowDate=datetime.datetime.now().date()
nowTime=str(datetime.datetime.now().time())
SplittedTime=nowTime.split(":")
NowdaTe=str(nowDate)
NowdaTe=NowdaTe.strip()   


CurrentAccountIdList=[]
BookedSlotId=[]

for DateTimeInBooking in cu1:
    nn=str(DateTimeInBooking[6])
    daTe = nn[0:11]
    tiMe=nn[11:13]
    daTe=daTe.strip()

    if daTe==NowdaTe and int(SplittedTime[0])+1==int(DateTimeInBooking[3]):
        CurrentAccountIdList.append(int(DateTimeInBooking[2]))
        BookedSlotId.append(int(DateTimeInBooking[3]))
print(BookedSlotId,CurrentAccountIdList)


querry2='SELECT *FROM tables_account'
cu2=DataBase.cursor()
cu2.execute(querry2)


RequiredMidList=[]
for AccountIdFromTablesAccnt in cu2:
    var=AccountIdFromTablesAccnt[0]

    for Id in range(len(CurrentAccountIdList)):
        if long(CurrentAccountIdList[Id])==(AccountIdFromTablesAccnt[0]):
            RequiredMidList.append(int(AccountIdFromTablesAccnt[9]))

print(RequiredMidList)

SuperUserMidList=[Mid for Mid in range(1,41)]
print(SuperUserMidList)

MidsTobeBooked=[mId for mId in SuperUserMidList if mId not in RequiredMidList]
print( MidsTobeBooked)

for BookMid in range(len(MidsTobeBooked)):
    ToInsert=[int((MidsTobeBooked[BookMid]))+40,int(SplittedTime[0])+1,(datetime.datetime.now()),(datetime.datetime.now()),(nowDate)]
    cursor5.execute("INSERT INTO tables_booking(account_id,slot_id,created_at,updated_at,booking_date) VALUES(%s,%s,%s,%s,%s)",ToInsert)
    DataBase.commit() 


cu1.close() 
cu2.close()
cursor5.close()
DataBase.close()
