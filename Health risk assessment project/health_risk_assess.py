class Patient:
    def __init__(self,name,age,gender,weight_kg,height_cm,lifestyle,water_intake):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight_kg=weight_kg
        self.height_cm=height_cm
        self.lifestyle=lifestyle
        self.water_intake=water_intake
    def get_profile(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Weight_kg": self.weight_kg,
            "Height_cm": self.height_cm,
            "Lifestyle(Smoker/Non-Smoker)": self.lifestyle,
            "Water Intake": self.water_intake
        }
class Calculator:
    def BMI_calc(self,Patient_obj):
        BMI = Patient_obj.weight_kg / (Patient_obj.height_cm / 100) ** 2
        return BMI
    def water_calc(self,Patient_obj):
        water_needed=Patient_obj.weight_kg*0.033
        return water_needed
class RiskScore(Calculator):
    def __init__(self):
        self.point=0
    def bmi_eval(self,BMI):
        if BMI< 18.5: 
            self.point+=1
        elif(BMI>=18.5 and BMI<24.9):
            self.point+=0
        elif(BMI>=25.0 and BMI<29.9):
            self.point+=1
        else:
            self.point+=2
    def lifestle_eval(self,lifestyle):
        if lifestyle=='Smoker':
            self.point+=1
        else:
            self.point+=0
    def water_eval(self,water_intake,water_needed):
        if water_intake<water_needed:
            self.point+=1
    def get_report(self):
        if self.point==0:
            return "Green Flag"
        elif self.point==1:
            return "Yellow Flag"
        else:
            return "Red Flag"
    
def save_report(Patient_obj,BMI,water_needed,report):
    try:
        with open("Patient_Health_assessment.txt", "a") as file:
            file.write(f"Name:{Patient_obj.name}\n")
            file.write(f"BMI:{BMI}\n")
            file.write(f"Water Needed:{water_needed}L\n")
            file.write(f"Health Status:{report}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    input_name = input("Enter Name: ")
    while True:
        #Age with error handling
        while True:
            try:
                input_age = int(input("Enter Age: "))
                if input_age >= 1 and input_age <= 99:
                    break
                else:
                    print("Age should be between 1 to 99")
            except ValueError:
                print("Age entered should be in numeric digits")
        # Gender with error handling
        while True:
            try:
                input_gender = input("Enter Gender: ")
                if input_gender=="Male" or input_gender=="Female":
                    break
                else:
                    print("Enter either Male or Female")
            except Exception as exc:
                print("An error occurred while entering gender :", exc)
        #Weight Error Handling
        while True:
            try:
                input_weight = float(input("Enter Weight in kg :"))
                if input_weight>1 and input_weight<=300:
                    break
                else:
                    print("Weight Should be less tha 300 Kgs and more than 1kgs")
            except Exception as exc:
                print("An Error occured",exc)
        #Height error handling 
        while True:
            try:
                input_height = float(input("Enter Height in cm :"))
                if input_height>=1 and input_height<=250:
                    break
                else:
                    print("Enter valid height")
            except Exception as exc:
                print("An error occured")
        #Life style Error handling
        while True:
            try:
                input_lifestyle = input("Smoker/Non-Smoker :")
                if input_lifestyle=="Smoker" or input_lifestyle=="Non-Smoker":
                    break
                else:
                    print("Either enter Smoker or Non-Smoker(Case sensitive)")
            except Exception as exc:
                print("An Error occured")
        while True:
            try:
                input_water_intake =float(input("Enter Water intake :"))
                if input_water_intake<15:
                    break
                else:
                    print("Enter Valid water intake")
            except ValueError:
                print("Water intake cannot be negative")
        p = Patient(input_name, input_age, input_gender, input_weight, input_height, input_lifestyle, input_water_intake)
        r = RiskScore()
        calculated_bmi = r.BMI_calc(p)
        r.bmi_eval(calculated_bmi)

        needed_water = r.water_calc(p)
        r.water_eval(p.water_intake, needed_water)

        r.lifestle_eval(p.lifestyle)
        print("\n---------------------- Final Report ---------------------------")
        print(r.get_report())

        save_report(p, calculated_bmi, needed_water, r.get_report())

        choice = input("\nDo you want to check for another patient? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the Health Assessment tool. Stay Healthy!")
            break

if __name__ == "__main__":
    main()