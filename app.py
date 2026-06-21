from functions import BusSchoolManager
from report import generate_report

app = BusSchoolManager()

print("\n--------------------- WELCOME TO BUS SCHOOL MANAGEMENT SYSTEM ---------------------")

while True:

  print("\n1. Add Student")
  print("2. View Students")
  print("3. Edit Student")
  print("4. Delete Student")

  print("\n5. Add Driver")
  print("6. View Drivers")
  print("7. Edit Driver")
  print("8. Delete Driver")

  print("\n9. Add Bus")
  print("10. View Buses")
  print("11. Edit Bus")
  print("12. Delete Bus")

  print("\n13. Generate Report")
  print("14. Exit")

  choice = input("\nChoose an option: ")

  if choice == "1":
      print("\n--- Add Student ---")

      sid = int(input("ID: "))
      fullname = input("Full Name: ")
      gender = input("Gender: ")
      student_class = input("Class: ")
      parent_name = input("Parent Name: ")
      parent_phone = input("Parent Phone: ")
      fee = float(input("Fee: "))
      driver = input("Driver: ")

      from models import Student

      student = Student(
          sid,
          fullname,
          gender,
          student_class,
          parent_name,
          parent_phone,
          fee,
          driver
      )

      app.add_student(student)

      print("Student Added Successfully!")

  elif choice == "2":

      print("\n--- Students List ---")

      for student in app.view_students():
          print(student)

  elif choice == "3":

      sid = int(input("Student ID: "))
      new_name = input("New Full Name: ")

      app.edit_student(
          sid,
          fullname=new_name
      )

      print("Student Updated Successfully!")

  elif choice == "4":

      sid = int(input("Student ID: "))

      app.delete_student(sid)

      print("Student Deleted Successfully!")

  elif choice == "5":

      print("\n--- Add Driver ---")

      did = int(input("ID: "))
      fullname = input("Full Name: ")
      phone = input("Phone: ")
      license_number = input("License Number: ")
      salary = float(input("Salary: "))

      from models import Driver

      driver = Driver(
          did,
          fullname,
          phone,
          license_number,
          salary
      )

      app.add_driver(driver)

      print("Driver Added Successfully!")

  elif choice == "6":

      print("\n--- Drivers List ---")

      for driver in app.view_drivers():
          print(driver)

  elif choice == "7":

      did = int(input("Driver ID: "))
      new_name = input("New Full Name: ")

      app.edit_driver(
          did,
          fullname=new_name
      )

      print("Driver Updated Successfully!")

  elif choice == "8":

      did = int(input("Driver ID: "))

      app.delete_driver(did)

      print("Driver Deleted Successfully!")

  elif choice == "9":

      print("\n--- Add Bus ---")

      bid = int(input("ID: "))
      bus_number = input("Bus Number: ")
      capacity = int(input("Capacity: "))
      driver = input("Driver: ")

      from models import Bus

      bus = Bus(
          bid,
          bus_number,
          capacity,
          driver
      )

      app.add_bus(bus)

      print("Bus Added Successfully!")

  elif choice == "10":

      print("\n--- Bus List ---")

      for bus in app.view_buses():
          print(bus)

  elif choice == "11":

      bid = int(input("Bus ID: "))
      new_bus_number = input("New Bus Number: ")

      app.edit_bus(
          bid,
          bus_number=new_bus_number
      )

      print("Bus Updated Successfully!")

  elif choice == "12":

      bid = int(input("Bus ID: "))

      app.delete_bus(bid)

      print("Bus Deleted Successfully!")

  elif choice == "13":

      generate_report(app)

      print("Report Generated Successfully!")

  elif choice == "14":

      print("\nGood Bye!")
      break

  else:

      print("Invalid Choice!")

