import sqlite3
roll_no int(input("Enter  roll no of a student"))

def viweall(roll_no):
    conn = sqlite3.connect("college.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM attedance where roll_no* ?",(roll_no,))
    global data
    data=cur.fetchall()
    
def feedfile(data):
    f=open("details_for_a_student.csv ','w")
      for row in data::
          for ele in row:
              f.write(str(ele))
              f.write(',')
            f.write('\n')      
        f.close()
view all(roll_no)
feedfile(data)
