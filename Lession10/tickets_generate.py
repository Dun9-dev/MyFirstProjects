file_name = "../other_files/generate.txt"
with open(file_name, "w") as file_object:
    for i in range(1, 100000):
        if i < 10:
            k = str(i)
            file_object.write(f"0000{k}SN\n")
            i += 1
        elif i < 100:
            k = str(i)
            file_object.write(f"000{k}SN\n")
            i += 1
        elif i < 1000:
            k = str(i)
            file_object.write(f"00{k}SN\n")
            i += 1
        elif i < 10000:
            k = str(i)
            file_object.write(f"0{k}SN\n")
            i += 1
        elif i < 100000:
            k = str(i)
            file_object.write(f"{k}SN\n")
            i += 1
