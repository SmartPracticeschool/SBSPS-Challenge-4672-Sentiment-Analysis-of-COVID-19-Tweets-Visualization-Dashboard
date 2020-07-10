import mysql.connector

class Data:
    def __init__(self,loc):
        self.loc = loc.lower()

        date_data_query={
            'mumbai':"""select * from mumbai_sentiment""",
            'delhi':"""select * from delhi_sentiment""",
            'banglore':"""select * from kolkata_sentiment""",
            'chennai':"""select * from chennai_sentiment""",
            'overall':"""select * from overall_sentiment"""
            }

        overall_query={
            'mumbai':"""select sum(positive),sum(negative) ,sum(neutral),sum(sad),sum(anger),sum(joy) from mumbai_sentiment""",
            'delhi':"""select sum(positive),sum(negative) ,sum(neutral),sum(sad),sum(anger),sum(joy) from delhi_sentiment""",
            'banglore':"""select sum(positive),sum(negative) ,sum(neutral),sum(sad),sum(anger),sum(joy) from kolkata_sentiment""",
            'chennai':"""select sum(positive),sum(negative) ,sum(neutral),sum(sad),sum(anger),sum(joy) from chennai_sentiment""",
            'overall':"""select sum(positive),sum(negative) ,sum(neutral),sum(sad),sum(anger),sum(joy) from overall_sentiment"""
        }

        sql1=date_data_query[self.loc]
        sql2=overall_query[self.loc]
        conn = mysql.connector.connect(
                     host="covidsentimentanalysis.mysql.pythonanywhere-services.com",
                     user="covidsentimentan",
                     password="administrator",
                     database = "covidsentimentan$tweets"
                    )
        cursor = conn.cursor()
        cursor.execute(sql1)
        self.all_data = cursor.fetchall()

        cursor2 = conn.cursor()
        cursor2.execute(sql2)
        self.temp_overall_data = cursor.fetchall()
        self.overall_data=[]
        self.overall_data.append(int(self.temp_overall_data[0][0]))
        self.overall_data.append(int(self.temp_overall_data[0][1]))
        self.overall_data.append(int(self.temp_overall_data[0][2]))
        self.overall_data.append(int(self.temp_overall_data[0][3]))
        self.overall_data.append(int(self.temp_overall_data[0][4]))
        self.overall_data.append(int(self.temp_overall_data[0][5]))
        print(self.overall_data)
        #print(sum(self.temp_overall_data))
        # j=0
        # while(j<6):
        #   sum=0
        #   i=0
        #   while(i<len(self.temp_overall_data)):
        #       sum+=self.temp_overall_data[i][j]
        #   self.overall_data.append(sum)
        conn.close
        # to convert row into convert

    def getdata(self):
        if len(self.all_data)>7:
            x=len(self.all_data)-7
            self.all_data = self.all_data[x:]
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

        # def getoverall(self):
        #     pos=0
        #     neg=0
        #     nut=0
        #     sad=0
        #     ang=0
        #     joy=0
        #     total_data=[pos,neg,nut,sad,ang,joy]
        #     for data in self.all_data:
        #         i=0
        #         while(i<7):
        #             total_data[i].append(data[i])
        #             i+=1

        #     return total_data



oc=Data('overall')
