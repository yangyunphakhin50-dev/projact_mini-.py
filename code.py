sun = 274.0
mercury = 3.7
venus = 8.87
earth = 9.81
mars = 3.71
jupiter = 24.79
saturn = 10.44
uranus = 8.69
neptune = 11.15

mass = float(input("นํ้าหนัก: "))
name = input("ชื่อดาว: ")

if name == "sun":
    g = 274.0
elif name == "mercury":
    g = 3.7
elif name == "venus":
    g = 8.87
elif name == "earth":
    g = 9.81
elif name == "mars":
    g = 3.71
elif name == "jupiter":
    g = 24.79
elif name == "saturn":
    g = 10.44
elif name == "uranus":
    g = 8.69
elif name == "neptune":
    g = 11.15
else:
    print("error")
    g = "error"
    
if g != "error":
    w = ( mass / 9.81) * g
    w = round(w,2)
    print("นํ้าหนักของบนดาวดวงนี้คือ",w, "kg")
