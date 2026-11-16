import psycopg

def getAllStudents(cursor):
    #Sends query to retrieve all student info, loads the response from the cursor object, and prints each value
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    print("\n")
    for student in students:
        print(student)


def addStudent(cursor, first_name, last_name, email, enrollment_date):
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))

def updateStudentEmail(cursor, student_id, new_email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))

def deleteStudent(cursor, student_id):
    cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))


def main():

    #Creates connection to server
    conn = psycopg.connect(
        host="localhost",
        dbname="student_db",
        user="postgres",
        password='PASSWORD',
        port=5432
    )
    cursor = conn.cursor()

    #Query loop
    while True:
        answer = input("\n\nEnter which command you'd like. Enter the number from 1-5, followed by necessary inputs in order space seperated.\n1. Get All Students\n2. Add Student (first name, last name, email, enrollment date)\n3. Update Student Email (Student ID, New Email)\n4. Delete Student (Student ID)\n5. Quit application\n:")
        answer = answer.split(" ")
        #Checks which query is requested and calls related function
        match answer[0]:
            case "1":
                getAllStudents(cursor)
            #For all modifying functions, call conn.commi to save changes to database
            case "2":
                addStudent(cursor, answer[1], answer[2], answer[3], answer[4])
                conn.commit()
            case "3":
                updateStudentEmail(cursor, int(answer[1]), answer[2])
                conn.commit()
            case "4":
                deleteStudent(cursor, int(answer[1]))
                conn.commit()
            case "5":
                break
            case "_":
                print("Invalid command")

    conn.close()

        
if __name__ == "__main__":
    main()