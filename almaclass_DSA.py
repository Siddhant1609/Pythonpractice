import numpy
import pandas as pd
import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr)
# df = pd.DataFrame({"Name":['Alice','john','Charlie'],'Age':[25,30,35]})#
# print(df)

# arr = np.random.randint(0,100,size=10)
# arr_sorted = np.sort(arr)
# arr_sum = np.sum(arr)
# arr_mean = np.mean(arr)
# arr_sq = arr_sorted**2
# print(arr)
# print(arr_sorted)
# print(arr_sum)
# print(arr_mean)
# print(arr_sq)

# arr = np.array([1,2,3,4,5,7,8,])
# arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# print(arr_2d)

# my_mean = np.mean(arr)
# my_median = np.median(arr)
# my_std = np.std(arr)
#
# print(my_mean)
# print(my_median)
# print(my_std)

# arr0 = np.arange(10)
# arr2 = np.arange(4,10,2)
# arr1 = np.linspace(0,1,5)
# arr_2d = arr0.reshape(2,5)  # 2 rows and 5 columns
# print(arr0)
# print(arr2)
# print(arr1)
# print(arr_2d)
# array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr_transpose = np.transpose(array_2d)
# print(arr_transpose)
# arr_1d = arr_2d.flatten()
# print("Original 2d array:\n" , array_2d)
# print("Flattend 1d array:\n" , arr_1d)

#Let's get started with the exciting part!! Let's create our first Pandas DataFrame!!🐼
# some_2d_array= np.random.randint(3,6,(3,4))
# first_data_frame = pd.DataFrame(some_2d_array, columns=['Akash','Vandana','Viddhi','Vishwas'])
# print(first_data_frame)


# Another_data_frame = pd.DataFrame(some_2d_array, columns=['A1','V1','V2','V3'])
# print(Another_data_frame)

#Using a conventional list of lists
# list_of_lists = [['Amar',10],['Akbar',20],['Arun',30]]## Initialize list of lists
# df = pd.DataFrame(list_of_lists, columns=['NAMES','AGE'])#Create the pandas DataFrame
#print(df) # print the df

# employee_dict = {'Employee Name': ['RAJEEV','SUMIT','SUMAN',],'INCOME':[200000,140000,90000]}
# employee_df = pd.DataFrame(employee_dict)
# print(employee_df)

# series_dict = {'First_series':([10,12,13,15,16]),'Second_series': ([34,23,65,76,54,])}
# df = pd.DataFrame(series_dict)
# print(df)

# list_of_list =({'Akashat':14,'Madhoradhipate':23,'Shree krishna':34},{'Akashat':45,'Madhoradhipate':23,'Shree krishna':67})
# df= pd.DataFrame(list_of_list)
# print(df)


# actor_names = ['HANUMAN', 'SHREE RAM', 'BHOLE BABA', 'KRISHNA']
# actors_ages = [23,45,26,np.nan]
# list_of_tuple = list(zip(actor_names,actors_ages))
# actor_df = pd.DataFrame(list_of_tuple, columns=['NAME','AGES'])
# print(actor_df)


# imdb_df = pd.read_csv('https://drive.google.com/file/d/1AIOBniLPRbQbjlE1swaTAmWHv(W_wFWQm/view')
# print(imdb_df)

