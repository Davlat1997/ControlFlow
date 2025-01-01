matn = input("Matinni kiriting: ")

matn_array = matn.split()

max_array = matn_array[0]

for i in matn_array:
    if len(max_array) < len(i):
        max_array = i
print("result: {}".format(max_array))