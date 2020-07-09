#import mysql.connector

class Data:
    def __init__(self,loc):
        self.loc = loc
        self.table_name = loc.lower() + '_sentiment'
        '''
        conn = mysql.connector.connect(user='covidsentimentanalysis', password='administrator',
                                       host='covidsentimentanalysis.mysql.pythonanywhere-services.com',
                                       database='covidsentimentanalysis$covidsentimentan')
        cursor = conn.cursor()
        sql ="""select * from %s"""
        cursor.execute(sql, self.table_name)
        self.all_data = cursor.fetchall()
        sql="""select positive,negative ,neutral,sad,anger,joy from %s"""
        cursor.execute(sql, self.table_name)
        '''
        self.all_data=[('5-7-2020',100,150, 200, 100, 30, 250), ('6-7-2020',50,100, 300, 10, 20, 100)] #sql='''select * from %s'''; conn.execute(sql,loc)
        self.overall_data=['100','150', '200', '100', '300', '250']
        #self.overall_data = cursor.fetchall()
    def getdata(self):
        if len(self.all_data)>7:
            self.all_data = self.all_data[:6]
        dates=[]
        pos=[]
        neg=[]
        nut=[]
        sad=[]
        ang=[]
        joy=[]
        total_data=[dates,pos,neg,nut,sad,ang,joy]
        for data in self.all_data:
            i=0
            while(i<7):
                total_data[i].append(data[i])
                i+=1

        return total_data

