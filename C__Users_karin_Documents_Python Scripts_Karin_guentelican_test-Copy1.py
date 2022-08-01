#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip instal pandas
#pip install json


# In[2]:


import pandas as pd
import json


# In[3]:


data = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'


# In[4]:


json_file = json.loads(data)
json_file


# In[5]:


data_table = [["Underweight","18.4 and below", "Malnutrition risk"],
              ["Normal weight","18.5 - 24.9", "Low risk"],
              ["Overweight","25 - 29.9", "Enhanced risk"],
              ["Moderately obese","30 - 34.9", "Medium risk"],
              ["Severely obese","35 - 39.9", "High risk"],
              ["Very severely obese","40 and above", "Very high risk"],
              ]

table1 = pd.DataFrame(data_table, columns=["BMI Category", "BMI Range (kg/m2)", "Health Risk"])
table1


# In[6]:


def BMI (json, column_mass, column_height):
    for element in json:
        if (len(element) == 3): 
             bmi = element[column_mass]/ (element[column_height]/100)**2   
            
        if (bmi <= 18.4):
                element["BMI Category"] = table1["BMI Category"][0]
                element["Health Risk"] = table1["Health Risk"][0]
        elif (bmi >= 18.5 and bmi <= 24.9 ):
                element["BMI Category"] = table1["BMI Category"][1]
                element["Health Risk"] = table1["Health Risk"][1]
        elif (bmi >= 25 and bmi <= 29.9 ):
                element["BMI Category"] = table1["BMI Category"][2]
                element["Health  Risk"] = table1["Health Risk"][2]
        elif (bmi >= 30 and bmi <= 34.9 ):
                element["BMI Category"] = table1["BMI Category"][4]
                element["Health Risk"] = table1["Health Risk"][4]
        elif (bmi >= 35 and bmi <= 39.9 ):
                element["BMI Category"] = table1["BMI Category"][5]
                element["Health Risk"] = table1["Health Risk"][5]
        else:
                element["BMI Category"] = table1["BMI Category"][6]
                element["Health Risk"] = table1["Health Risk"][6]
    return json 


# In[7]:


final_json = BMI (json_file,"WeightKg","HeightCm" )
final_json


# In[8]:


count_overwight = sum([1 for i in final_json if i["BMI Category"] == "Overweight"])
count_overwight


# In[9]:


data_test = '[{"Gender": "Male", "HeightCm": 152, "WeightKg": 82 },{ "Gender": "Male", "HeightCm": 120, "WeightKg": 33 }]'
json_test = json.loads(data_test)


# In[10]:


final_json_test = BMI (json_test,"WeightKg","HeightCm" )
final_json_test


# In[ ]:




