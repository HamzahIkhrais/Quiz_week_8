import matplotlib.pyplot as plt
import pandas as pd
import csv

def load_data_from_csv(filename):
  years = []
  co2 = []
  temp = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            years.append(float(row[0]))
            co2.append(float(row[1]))
            temp.append(float(row[2]))

    return years, co2, temp

def plot_data(years, co2, temp):
    plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 


if __name__ == "__main__":
   years, co2, temp = load_data_from_csv('data.csv')
    plot_data(years, co2, temp)
