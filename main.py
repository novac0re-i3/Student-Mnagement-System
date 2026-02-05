#Rupnagar committee Family management system
class families:
    def __init__(self,family_name,members):
        self.family_name =family_name
        self.members=members
        
    def show_info(self):
        print(f"Family Name:{self.family_name} , Number of Members: {self.members}")
        
class parents(families):
    def __init__(self,family_name,members, dad_name, mom_name, total_income=0):
        super().__init__(family_name,members)
        self.dad_name=dad_name
        self.mom_name=mom_name
        self.__total_income=total_income  #Private
        
    def set_total_income(self,total_income):
        self.__total_income=total_income

    def get_total_income(self):
        return self.__total_income
    
    def show_info(self):
        super().show_info()
        print(f"Father's name: {self.dad_name} , Mother's name: {self.mom_name} , Total Income : {self.__total_income} ")
        
    def __del__(self):
        print(f"The {self.family_name} family has been removed from the system")
        
class person(families):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_info(self):
        super().show_info()
        print(f"Admin info--- name:{self.name} , age: {self.age}")
        
class admin(person):
    def add_family(self,family_list,family): 
        family_list.append(family) 
        print(f"{family.family_name} family is added successfully")  

    def remove_family(self,family_list,family_name):
        for s in family_list:
            if s.family_name==family_name:
                family_list.remove(s)
                
                del s
                print("Family removed")
                break   

    def update_income(self,family_list,family_name,new_income):
        for s in family_list:
            if s.family_name==family_name:
                s.set_total_income(new_income)
                print("Income updated")
                break
            