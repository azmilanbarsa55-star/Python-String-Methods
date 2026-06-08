s1 = input("Birinchi matnni kiriting: ").strip()
s2 = input("Ikkinchi matnni kiriting: ").strip()

result = s2.lower() in s1.lower()
print(result)