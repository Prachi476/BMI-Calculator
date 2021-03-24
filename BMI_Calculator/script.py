import json
import numpy as np

with open("C:/Users/prachi.k/BMI_Calculator/data.json", "r") as rf:
    output_data = json.load(rf)


BMI_list=[]

for data in output_data:
    BMI=data["WeightKg"]/(data["HeightCm"]/100)
    BMI = float("{0:.1f}". format(BMI))
    data["BMI"]=BMI
    BMI_list.append(BMI)



category=["Malnutrition risk","Low risk","Enhanced risk","Medium risk ","High risk","Very high risk"]
health_risk=["Underweight","Normal weight","Overweight", "Moderately obese","Severely obese","Very severely obese"]

for data in output_data:
    if(data["BMI"]<18.4):
        data["Category"]=category[0]
        data["Health risk"]=health_risk[0]

    elif(data["BMI"]>18.5 and data["BMI"]<24.9):
        data["Category"]=category[1]
        data["Health risk"]=health_risk[1]

    elif(data["BMI"]>25 and data["BMI"]<29.9):
        data["Category"]=category[2]
        data["Health risk"]=health_risk[2]

    elif(data["BMI"]>30 and data["BMI"]<34.9):
        data["Category"]=category[3]
        data["Health risk"]=health_risk[3]
        # print("Medium risk ")
    elif(data["BMI"]>35 and data["BMI"]<39.9):
        data["Category"]=category[4]
        data["Health risk"]=health_risk[4]

    elif(data["BMI"]>40):
        data["Category"]=category[5]
        data["Health risk"]=health_risk[5]
    else:
        pass


for data in output_data:
    print("data",data)

