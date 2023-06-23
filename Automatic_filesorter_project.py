#!/usr/bin/env python
# coding: utf-8

# # BMI CACULATOR

# In[14]:


weight = int(input("Enter your weight in pounds :"))

height = int(input("Enter your height in inches :"))

BMI = (weight *703)/(height*height)
print(BMI)


# In[4]:


BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9


# In[15]:


if BMI>0:
    if(BMI<18.5):
        print("You are under weight.")
    elif(BMI<=24.9):
        print("You are normal weight.")   
    elif(BMI<=29.9):
        print("You are over weight.")
    else:
        print("Over weight.")


# # Automatic File Sorter in File Explorer

# In[53]:


import os,shutil


# In[54]:


path = r"C:/Users/fbrev/OneDrive/Dulip-documents/images/"


# In[55]:


file_name = os.listdir(path)


# In[56]:


folder_name = ['Jpg_files', 'text_files', 'png_files']

for loop in range (0,3):
    if not os.path.exists(path +folder_name[loop]):
        print(path +folder_name[loop])
        os.makedirs(path +folder_name[loop])
    


# In[24]:





# In[57]:


for file in file_name:
  if ".jpg" in file and not os.path.exists(path + " Jpg_files/ " + file):
      shutil.move(path + file, path + "Jpg_files/" + file)
  elif ".png" in file and not os.path.exists(path + " png_files/ " + file):
      shutil.move(path + file, path + "png_files/" + file)
  elif ".txt" in file and not os.path.exists(path + " text_files/ " + file):
      shutil.move(path + file, path + "text_files/" + file)    


# In[ ]:




