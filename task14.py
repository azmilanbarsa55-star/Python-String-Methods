s1 = input("matn kiriting: ").strip()
s2 = input("bir xil matn kiriting: ").strip()
result = s1.lower().count(' ') == s2.lower().count(' ')
print(result)