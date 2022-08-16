# Dictionary ( Sözlük): Dictionary sınıfı eklendiği elemanları key ve value olarak kaydetmemize yarayan bir sınıfdır.
#   Değiştirilebilir.
#   Sıralıdır.
#   Kapsayıcıdır.

dictionary = {"Reg": "Regression"}
print(dictionary)
dictionary1 = {"REG": "Regression",
                "LOG": "Logistic Regression",
                "CART": "Classification and Reg"}
print(dictionary1)
print(dictionary1["REG"])
dictionary2 = {"REG": ["RMSE", 10],
               "LOG": ["MSE", 20],
               "CART": ["SSE", 30]}
print(dictionary2)
dictionary3 = {"REG": 10,
                "LOG": 20,
                "CART": 30}
print(dictionary3)
# Sözlüğün içindeki 30 değerine ulaşmak istersem;
print(dictionary2["CART"][1])
# Key Sorgulama
print("YSA" in dictionary)
print("CART" in dictionary1)
# Key'e göre Value'ya erişmek.
print(dictionary2.get("REG"))
# Value değiştirmek;
dictionary2["REG"] = ["YSA", 10]
print(dictionary2)
# Tüm Key'lere Erişmek
print(dictionary2.keys())
# Tüm Value'lara Erişmek
print(dictionary2.values())
# Tüm çiftleri TUPLE halinde listeye çevirme
print(dictionary2.items())
# Key-Value Değerini Güncellemek
dictionary2.update({"REG": 11})
print(dictionary2)
dictionary2.update({"RF": 10})
print(dictionary2)



