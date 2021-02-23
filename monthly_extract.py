
roll_no int(input("Enter  roll no of a student"))
month int(input("Enter month in digits:"))
year int(input("Enter  year:"))


def viweall(roll_no,month,year):
    sdate=datetime.date(year,month,1)
    edate=datetime.date(year,month,30)
    conn = sqlite3.connect("college.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM attedance where roll_no* ? and day<=?",(roll_no,sdate,edate))
    
    global data
    data=cur.fetchall()
    
def feedfile(data):
    f=open("student_details_for_a_month.csv ','w")
      for row in data::
          for ele in row:
              f.write(str(ele))
              f.write(',')
            f.write('\n')      
        f.close()
view all(roll_no)
feedfile(data)
