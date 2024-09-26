sonlar = [1, 2, 3, 4, 5]
result = 0
for i in sonlar:
    result = i + result
print(result)
sonlar2 =  [5, 1, 8, 7, 2] 
sonlar2.sort()
print(sonlar2)
print(f"kichik son {sonlar2[0]} va katta son {sonlar2[-1]}")
meva = ["nok","anor","banan"]
mev1 = input("mevani nomi kirititng: ")
meva.append(mev1)
print(meva)
fruits = ["nok","anor","banan","anor"]
mevaname = input("maveni nomini kiriting:")
orin = int(input("qaysi ni orniga qoyili:"))-1
fruits.insert(orin,mevaname)
print(fruits)
nums= [2, 6, 5, 8, 3, 5, 4] 
print(len(nums))
