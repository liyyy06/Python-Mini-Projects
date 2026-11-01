print("Welcome to Risk Profile Mini Quiz!")

score = 0
a = 1
b = 2
c = 3

name = input("Enter your name: ")
ready = input("Are you ready? *Please answer with yes or no^^*: ").lower().strip()

while ready != "yes" and ready != "no" :
    print("Jawaban harus berupa yes atau no")
    ready = input("Are you ready? *Please answer with yes or no^^*: ").lower().strip()

if ready == "yes":
    print(f"Hi {name}! Let's go!")
    input("Tekan enter untuk mengerjakan quiz!")
    print("Please answer the question with a, b or c")
    print("""Jika nilai investasimu turun cukup banyak dalam waktu singkat, apa yang paling mungkin kamu lakukan?
    a. Menjual semuanya agar aman
    b. Menahan dan menunggu
    c. Membeli lebih banyak
    """)
    jawaban_1 = input(">").lower().strip()
    while jawaban_1 != "a" and jawaban_1 != "b" and jawaban_1 != "c":
        print("Jawaban harus berupa a, b atau c!")
        jawaban_1 = input(">").lower().strip()
    if jawaban_1 == "a":
        score = score + a
    elif jawaban_1 == "b":
        score = score + b
    elif jawaban_1 == "c":
        score = score + c
    print(f"Skor sementara: {score}")
    input("Tekan enter untuk ke soal selanjutnya")

    print("""2. Apa tujuan utamamu dalam berinvestasi?
    a. Menjaga uang tetap aman
    b. Pertumbuhan yang stabil
    c. Keuntungan sebesar-besarnya
    """)
    jawaban_2 = input(">").lower().strip()
    while jawaban_2 != "a" and jawaban_2 != "b" and jawaban_2 != "c":
        print("Jawaban harus berupa a, b atau c!")
        jawaban_2 = input(">").lower().strip()
    if jawaban_2 == "a":
        score = score + a
    elif jawaban_2 == "b":
        score = score + b
    elif jawaban_2 == "c":
        score = score + c
    print(f"Skor sementara: {score}")
    input("Tekan enter untuk ke soal selanjutnya")

    print("""3. Jika ada peluang dengan potensi untung besar tetapi risiko rugi juga besar, apa yang kamu lakukan?
        a. Menghindarinya
        b. Mencoba sedikit
        c. Masuk dengan cukup besar
        """)
    jawaban_3 = input(">").lower().strip()
    while jawaban_3 != "a" and jawaban_3 != "b" and jawaban_3 != "c":
        print("Jawaban harus berupa a, b atau c!")
        jawaban_3 = input(">").lower().strip()
    if jawaban_3 == "a":
        score = score + a
    elif jawaban_3 == "b":
        score = score + b
    elif jawaban_3 == "c":
        score = score + c
    input("Tekan enter untuk mengetahui skor akhir dan risk profile")
    print(f"Skor akhir: {score}")

    if score in range(3,5):
        print("Category : Conservative")
    elif score in range(5,8):
        print("Category : Moderate")
    elif score in range(8,10):
        print("Category : Aggressive")
    else : 
        print("Skor tidak valid")
    print("Terima kasih, sampai jumpa!")
    
elif ready == "no":
    print("Baik, sampai jumpa!")