try:
    file = open("data.txt", "r") # opening the file in read mode (use w instead of r for writing
    file.write("This is the data for the file")
    file.close()
except IOError:
    print("IO error found")
except:
    print("General error")
else:
    print("Process completed succesfully")
finally:
    print("Process finished")
