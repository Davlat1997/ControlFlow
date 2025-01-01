matn = input("matn kirit: ")
result = ""

count = 1
for i in range(len(matn) - 1):
    if matn[i + 1] == matn[i]:
        count += 1
    else:
        result += f"{matn[i]}{count}"
        count = 1
else:
    result += f"{matn[len(matn) - 1]}{count}"

    print(result)        
