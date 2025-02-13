class Hospital:
    all_doctors ={}
    appointments={}

    def __init__(self, name, specialize):
        self.name = name
        self.specialize = specialize
        Hospital.all_doctors[self.name] = [self.specialize]
        Hospital.appointments[self.name] = []
        
    @classmethod
    def add_doctor(cls):
        name=str(input("Enter the doctor's name: "))
        specialize=str(input("Enter his specializtion: "))
        if name in cls.all_doctors:
            print("This doctor is already in the system")
        
        else:
            cls.all_doctors[name] = [specialize]
            cls.appointments[name] = []
            print("the doctor has been added succefully")
            

    @classmethod
    def get_all_doctors(cls):
        print(str(Hospital.all_doctors))
        return

    @classmethod
    def get_doctors_by_specialize(cls):
        d=[]
        specialize=str(input("Enter the specialzation: "))
        
        for doctor_name, specialization in Hospital.all_doctors.items():
            if specialization[0]== specialize:
                d.append(doctor_name)
        if d:
            print(f"the doctors who specialize at {str(specialize)} are {d}")
        else:
            print("not found")
        return

    def __str__(self):
        return f"{self.name} from {self.specialize}"

    @classmethod
    def view(cls):
        doctor_name = str(input("Enter doctor name: "))
        if doctor_name not in cls.appointments:
            print(f"the name {str(doctor_name)} is not found !")
            return
        else:
            appointments = cls.appointments[doctor_name]
            if len(appointments) == 0:
                    print(f"Dr.{str(doctor_name)} has no appointments.")
            else:
                print (f"Dr.{str(doctor_name)} has appointments are {Hospital.appointments}")
                return

    @classmethod
    def book(cls):
        print(f"{Hospital.appointments}")
        name =(input("please enter doctor name: "))
        patient = (input("enter the patient name: "))
        time = int(input("time (24 hours): "))
        print(name)
        if time > 24 or time < 0:
            print("you have entered a wrong time !")
            return
        if name not in cls.appointments:
            print("You have entered a wrong doctor name. please try again!")
        for i in cls.appointments[name]:
            if i[1] == time:
                print("Sorry!, doctor has another patient in this time.")
                return
        if len(cls.appointments[name])==0 or len(cls.appointments[name]) < 3:
            cls.appointments[name].append((patient, time))
            print(f"{patient} will have an appointment at {time} with Dr. {name}")                   
        else:
            print("the doctor time taple is full")
        


doctor1 = Hospital("ahmed", "sss")
doctor2 = Hospital('ayman', "ddd")
doctor3 = Hospital("ali", "fff")
doctor4 = Hospital("mohamed", "ddd")
doctor5 = Hospital("bakry","sss")
print("welcome in our hospital \n how can we assist you today")
print("choose a munber for what you like to do : \n 1_ add a doctor")
print("2_if you want to see all of our doctors \n3_ if you want all doctors who work in a specialization")
print("4_ if you want to book\n5_if you want to view doctors plans")
while True:
    try:
        x=input()
        if x== "stop":
            break
        x=int(x)
        if x==1:
            Hospital.add_doctor()
        elif x==2:
            Hospital.get_all_doctors()
        elif x==3:
            Hospital.get_doctors_by_specialize()
        elif x==4:
            Hospital.book()
        elif x==5:
            Hospital.view()
        elif x>5:
            print("you have chosen a wrong option,please try again")
    except ValueError:
        print("you have entered a wrong option, please try again")