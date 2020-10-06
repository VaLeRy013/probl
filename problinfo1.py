#De la tastatură se întroduce numărul de rînd al culorii curcubeului. De afişat
#denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.
n = int(input("Dati numarul culorii curcubeului: "))
if (n == 1):
    print("Acesta este numarul culorii rosu")
elif (n == 2):
    print("Acesta este numarul culorii oranj")
elif (n == 3):
    print("Acesta este numarul culorii galben")
elif (n == 4):
    print("Acesta este numarul culorii verde")
elif (n == 5):
    print("Acesta este numarul culorii albastru")
elif (n == 6):
    print("Acesta este numarul culorii indigo")
elif (n == 7):
    print("Acesta este numarul culorii violet")
else:
    print("Curcubeul are 7 culori")
