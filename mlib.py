import student
import subject
import exam


def MenuStudent():
    while True:
        print("\t\t\t Student Record Management\n")
        print("==========================================================")
        print("1. Add Student")
        print("2. Search Student Record")
        print("3. Delete Student Record")
        print("4. Update Update Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            student.InsertStudent()
        elif choice == 2:
            student.SearchStudentRec()
        elif choice == 3:
            student.DeleteStudent()
        elif choice == 4:
            student.UpdateStudent()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")


def MenuSubject():
	while True:
		print("\t\t\t Subject Record Management\n")
		print("==========================================================")
		print("1. Add Subject Record")
		print("2. Search Subject Record")
		print("3. Delete Subject Record")
		print("4. Update Subject Record")
		print("5. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter Choice between 1 to 5 ------> : "))
		if choice == 1:
			subject.InsertSubject()
		elif choice == 2:
			subject.SearchSubject()
		elif choice == 3:
			subject.DeleteSubject()
		elif choice == 4:
			subject.UpdateSubject()
		elif choice == 5:
			return
		else:
			print("Wrong Choice.....Enter Your Choice again")





def MenuExam():
	while True:
		print("\t\t\t Member Record Management\n")
		print("==========================================================")
		print("1. Add Exam")
		print("2. Delete Exam")
		print("3. View Exam")
		print("4. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter Choice between 1 to 4 ------> : "))
		if choice == 1:
			exam.AddExam()
		elif choice == 2:
			exam.DeleteExam()
		elif choice == 3:
			exam.ViewExam()
		elif choice == 4:
			return
		else:
			print("Wrong Choice.....Enter Your Choice again")