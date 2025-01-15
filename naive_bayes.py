from collections import Counter

# Dataset Toko Kelontong
nama_produk = [
    "Aqua Gelas", "Teh Gelas", "Teh Pucuk", "Larutan Cap Kaki Tiga", "Susu Frisian Flag", "Pocari Sweat", "Larutan Cap Badak", "Cleo Galon", "Aqua Galon", "Beras Koi", "Minyak Sania", "Minyak Fortune", "Minyak Kita Botol", "Telur Ayam", "Bawang Putih", "Garam", "Gula Merah", "Gula Putih", "Tepung Tapioka", "Tepung Terigu", "Beras Ketan", "Mie Sukses", "Mie Sedaap", "Mie Indomie", "Mi Kering Cap Rombong Bakso", "Bihun Jagung Padamu", "Eko mie", "Masako", "Royco", "Ladaku", "Desaku", "Sajiku", "Kobe", "Saori Saos Tiram", "Micin Sasa", "Micin Ajinomoto", "Pala Bubuk", "Kecap Bango", "Kecap Manis Extra", "Mama Suka Sop", "Antaka Jagung", "Sabun Giv", "Sabun Lux", "Sabun Harmony", "Sabun Nuvo", "Sabun Dettol", "Sabun Sehat", "Sabun Lifeboy", "Sabun Shizu'i", "Pepsodent", "Ciptadent", "Closeup", "Mama Lemon", "Sunlight", "Vanish", "Bayclin", "Super Pell", "Wipol", "Vixal", "Sunsilk", "Pantene", "Lifebuoy", "Head & Shoulders", "Zinc", "Dove", "So Klin", "Rinso", "Daia", "Gentel Gen", "Downy"
]

harga = [
    "Murah", "Murah", "Murah", "Murah", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Mahal", "Mahal", "Mahal", "Murah", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Mahal", "Murah", "Murah", "Mahal", "Murah", "Murah", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Mahal", "Mahal", "Murah", "Mahal", "Mahal", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah", "Murah"
]

berat = [
    "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Berat", "Berat", "Berat", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan", "Ringan"
]

penjualan_per_minggu = [
    "Rendah", "Tinggi", "Tinggi", "Rendah", "Rendah", "Tinggi", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Rendah", "Tinggi", "Rendah", "Rendah", "Tinggi", "Tinggi", "Rendah", "Rendah", "Rendah", "Rendah", "Tinggi", "Tinggi", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Rendah", "Tinggi", "Rendah", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Tinggi", "Rendah", "Rendah", "Tinggi", "Tinggi", "Tinggi", "Rendah"
]

kategori = [
    "Minuman", "Minuman", "Minuman", "Minuman", "Minuman", "Minuman", "Minuman", "Minuman", "Minuman", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Sembako", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Sabun Mandi", "Pasta Gigi", "Pasta Gigi", "Pasta Gigi", "Cuci Piring", "Cuci Piring", "Pemutih", "Pemutih", "Disinfektan", "Disinfektan", "Disinfektan", "Sampo", "Sampo", "Sampo", "Sampo", "Sampo", "Sampo", "Deterjen", "Deterjen", "Deterjen", "Deterjen", "Deterjen"
]

kategori_prediksi = [
    "Minuman", "Bumbu", "Bumbu", "Minuman", "Minuman", "Bumbu", "Minuman", "Minuman", "Minuman", "Sembako", "Sembako", "Sembako", "Sembako", "Bumbu", "Sembako", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Sembako", "Sembako", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Sembako", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Sabun Mandi", "Sabun Mandi", "Bumbu", "Bumbu", "Sabun Mandi", "Bumbu", "Bumbu", "Sabun Mandi", "Bumbu", "Pasta Gigi", "Pasta Gigi", "Bumbu", "Bumbu", "Pemutih", "Pemutih", "Bumbu", "Disinfektan", "Disinfektan", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Bumbu", "Sampo", "Deterjen", "Bumbu", "Bumbu", "Bumbu", "Deterjen"
]

data = [
    {"harga": h, "berat": b, "penjualan": p, "kategori": k}
    for h, b, p, k in zip(harga, berat, penjualan_per_minggu, kategori)
]

def calculate_probabilities(data, feature, value):
    filtered_data = [d for d in data if d[feature] == value]
    category_counts = Counter([d["kategori"] for d in filtered_data])
    total = sum(category_counts.values())
    return {category: count / total for category, count in category_counts.items()}

# Data Baru
data_baru = {"harga": "Murah", "berat": "Ringan", "penjualan": "Rendah"}

prob_harga = calculate_probabilities(data, "harga", data_baru["harga"])
prob_berat = calculate_probabilities(data, "berat", data_baru["berat"])
prob_penjualan = calculate_probabilities(data, "penjualan", data_baru["penjualan"])

final_probabilities = Counter()
for category in prob_harga:
    final_probabilities[category] = prob_harga.get(category, 0) * prob_berat.get(category, 0) * prob_penjualan.get(category, 0)

predicted_category = final_probabilities.most_common(1)[0][0]

print("Kategori Prediksi untuk Data Baru: ", predicted_category)

# hitung confusion matrix
TP = sum(1 for true, pred in zip(kategori, kategori_prediksi) if true == pred == predicted_category)
FP = sum(1 for true, pred in zip(kategori, kategori_prediksi) if true != predicted_category and pred == predicted_category)
FN = sum(1 for true, pred in zip(kategori, kategori_prediksi) if true == predicted_category and pred != predicted_category)
TN = sum(1 for true, pred in zip(kategori, kategori_prediksi) if true != predicted_category and pred != predicted_category)

# Confusion Matrix
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

results = {
    "True Positives (TP)": TP,
    "True Negatives (TN)": TN,
    "False Positives (FP)": FP,
    "False Negatives (FN)": FN,
    "Accuracy": accuracy,
    "Precision": precision,
    "Recall": recall,
    "F1 Score": f1_score
}

for key, value in results.items():
    print(f"{key}: {value}")
