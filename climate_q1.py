import matplotlib.pyplot as plt
import sqlite3

def fetch_data_from_db(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
        
    years = []
    co2 = []
    temp = []


    cursor.execute("SELECT years, co2, temp FROM climate_data")
    rows = cursor.fetchall()


    for row in rows:
        years_list.append(row[0])
        co2_list.append(row[1])
        temp_list.append(row[2])

    conn.close()

    return years_list, co2_list, temp_list

if __name__ == "__main__":
    db_path = "climate.db"
   years, co2, temp = fetch_data_from_db(db_path)
    print("Years Data:", years)
    print("co2 Data:", co2)
    print("temp Data:", temp)
        
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
plt.savefig("co2_temp_1.png") 
