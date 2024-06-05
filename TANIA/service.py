import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat data service
service_data = {
    'service_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'service_type': ['Ganti Oli', 'Servis Rutin', 'Ganti Ban', 'Ganti Oli', 'Servis Rutin', 'Ganti Oli', 'Servis Rutin', 'Ganti Ban', 'Ganti Oli', 'Servis Rutin', 'Ganti Ban', 'Ganti Oli'],
    'service_date': ['2024-01-15', '2024-01-16', '2024-02-10', '2024-02-12', '2024-03-05', '2024-03-20', '2024-04-11', '2024-04-13', '2024-05-15', '2024-05-17', '2024-06-20', '2024-06-21'],
    'cost': [300, 150, 500, 120, 350, 320, 160, 520, 130, 370, 510, 140],
    'service_duration': [1.5, 1.0, 2.0, 0.5, 2.5, 1.5, 1.0, 2.0, 0.5, 2.5, 2.0, 0.5],
    'customer_id': [101, 102, 103, 104, 101, 105, 106, 107, 108, 109, 110, 111]
}

# Membuat data vehicle
vehicle_data = {
    'service_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'vehicle_type': ['Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Mobil', 'Motor']
}

# Membuat data customer
customer_data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
    'customer_name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Lee', 'Carol White', 'Dave Black', 'Eve Green', 'Frank Brown', 'Grace Kim', 'Henry Adams', 'Ivy Young']
}

# Konversi menjadi DataFrame
service_df = pd.DataFrame(service_data)
vehicle_df = pd.DataFrame(vehicle_data)
customer_df = pd.DataFrame(customer_data)

# Gabungkan data service dan vehicle
data = pd.merge(service_df, vehicle_df, on='service_id')
# Gabungkan data hasil dengan customer
data = pd.merge(data, customer_df, on='customer_id')

# Konversi kolom service_date menjadi datetime
data['service_date'] = pd.to_datetime(data['service_date'])

# 2. Tampilkan statistik deskriptif untuk kolom `cost` dan `service_duration`
print("Statistik deskriptif untuk biaya layanan:")
print(data['cost'].describe())

print("\nStatistik deskriptif untuk durasi layanan:")
print(data['service_duration'].describe())

# 3. Tampilkan jumlah layanan yang dilakukan setiap bulan
data['month'] = data['service_date'].dt.to_period('M')
monthly_services = data['month'].value_counts().sort_index()
print("\nJumlah layanan setiap bulan:")
print(monthly_services)

# 4. Tampilkan rata-rata biaya per jenis layanan
average_cost_per_service = data.groupby('service_type')['cost'].mean()
print("\nRata-rata biaya per jenis layanan:")
print(average_cost_per_service)

# 5. Buat visualisasi
plt.figure(figsize=(14, 10))

# Histogram distribusi biaya layanan
plt.subplot(2, 2, 1)
plt.hist(data['cost'], bins=20, edgecolor='k')
plt.title('Distribusi Biaya Layanan')
plt.xlabel('Biaya')
plt.ylabel('Jumlah Layanan')
plt.grid(True)

# Boxplot biaya layanan berdasarkan jenis layanan
plt.subplot(2, 2, 2)
sns.boxplot(x='service_type', y='cost', data=data)
plt.title('Biaya Layanan Berdasarkan Jenis Layanan')
plt.xlabel('Jenis Layanan')
plt.ylabel('Biaya')

# Garis waktu jumlah layanan setiap bulan
plt.subplot(2, 2, 3)
monthly_services.plot(kind='line', marker='o')
plt.title('Jumlah Layanan Setiap Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Layanan')
plt.grid(True)

# Bar chart jumlah layanan berdasarkan jenis kendaraan
plt.subplot(2, 2, 4)
vehicle_counts = data['vehicle_type'].value_counts()
vehicle_counts.plot(kind='bar', color='skyblue')
plt.title('Jumlah Layanan Berdasarkan Jenis Kendaraan')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Jumlah Layanan')

plt.tight_layout()
plt.show()

# 6. Tampilkan jenis kendaraan yang paling sering dilayani
most_common_vehicle = data['vehicle_type'].value_counts().idxmax()
print("\nJenis kendaraan yang paling sering dilayani:")
print(most_common_vehicle)

# 7. Tampilkan 5 pelanggan dengan total biaya layanan tertinggi
top_customers = data.groupby('customer_id')['cost'].sum().nlargest(5)
print("\n5 pelanggan dengan total biaya layanan tertinggi:")
print(top_customers)
