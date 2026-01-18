
import csv
import random
import os

def create_housing_data():
    filename = 'Datasets/house_prices.csv'
    os.makedirs('Datasets', exist_ok=True) # Ensure folder exists
    headers = ['Area_SqFt', 'Bedrooms', 'Age_Years', 'Location_Score', 'Price_Lakhs']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(200):
            area = random.randint(500, 3500)
            bedrooms = random.randint(1, 5)
            age = random.randint(0, 20)
            loc_score = random.randint(1, 10)
            
            # Formula for price (so ML can learn it)
            # Base 20L + 5k/sqft + 5L/bedroom - 0.5L/age + 2L * loc
            price = 20 + (0.005 * area) + (5 * bedrooms) - (0.5 * age) + (2 * loc_score)
            price += random.uniform(-5, 5) # Adding Noise/Randomness
            
            writer.writerow([area, bedrooms, age, loc_score, round(price, 2)])
    print(f"Created {filename}")

def create_student_data():
    filename = 'Datasets/student_scores.csv'
    headers = ['Study_Hours', 'Sleep_Hours', 'Previous_Score', 'Final_Score']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(200):
            study = round(random.uniform(1, 10), 1)
            sleep = round(random.uniform(4, 10), 1)
            prev = random.randint(40, 95)
            
            # Formula
            score = (study * 4) + (sleep * 2) + (prev * 0.4) + random.uniform(-5, 5)
            score = min(100, max(0, score))
            
            writer.writerow([study, sleep, prev, round(score, 1)])
    print(f"Created {filename}")

def create_mobile_data():
    filename = 'Datasets/mobile_prices.csv'
    headers = ['RAM_GB', 'Storage_GB', 'Camera_MP', 'Battery_mAh', 'Brand_Rating', 'Price_INR']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(100):
            ram = random.choice([4, 6, 8, 12, 16])
            storage = random.choice([64, 128, 256, 512])
            camera = random.choice([12, 48, 64, 108])
            battery = random.choice([3000, 4000, 5000, 6000])
            brand = random.randint(1, 5)
            
            price = (ram * 1000) + (storage * 50) + (camera * 100) + (battery * 2) + (brand * 2000)
            price += random.uniform(-1000, 1000)
            
            writer.writerow([ram, storage, camera, battery, brand, int(price)])
    print(f"Created {filename}")

if __name__ == "__main__":
    create_housing_data()
    create_student_data()
    create_mobile_data()
