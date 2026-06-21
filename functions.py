from models import Student, Driver, Bus


class BusSchoolManager:

    def __init__(self):
        self.students = []
        self.drivers = []
        self.buses = []

    # STUDENTS
    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        return self.students

    def edit_student(self, student_id, **kwargs):
        for s in self.students:
            if s.id == student_id:
                for k, v in kwargs.items():
                    setattr(s, k, v)
                return True
        return False

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    # DRIVERS
    def add_driver(self, driver):
        self.drivers.append(driver)

    def view_drivers(self):
        return self.drivers

    def edit_driver(self, driver_id, **kwargs):
        for d in self.drivers:
            if d.id == driver_id:
                for k, v in kwargs.items():
                    setattr(d, k, v)
                return True
        return False

    def delete_driver(self, driver_id):
        self.drivers = [d for d in self.drivers if d.id != driver_id]

    # BUSES
    def add_bus(self, bus):
        self.buses.append(bus)

    def view_buses(self):
        return self.buses

    def delete_bus(self, bus_id):
        self.buses = [b for b in self.buses if b.id != bus_id]