import segno
import random

def generate_qr_code():
    random_link = "https://example.com/" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)) # <-- _k_  ga qancha qiymat berilsa oshancha tasodifiy harf va raqamlarni hosil qiladi 

    file_names = [
        "file1", "file2", "file3", "file4", "file5",
        "file6", "file7", "file8", "file9", "file10"
    ]
    
    file_name = random.choice(file_names) + ".png"
    qr = segno.make(random_link)
    qr.save(file_name, scale=10, border=2)
    return random_link, file_name


link, file_name = generate_qr_code()
print(f"Generatsiya qilingan link: {link}")
print(f"Fayl nomi: {file_name}")