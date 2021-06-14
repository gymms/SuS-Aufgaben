from math import pi
# Dies ist ein Programm zur Berechnung des Kreisumfangs und der Kreisfläche
#
radius=float(input("Geben Sie den Radius in cm ein: "))
umfang=2*radius*pi
flaeche=radius*radius*pi
print("Der Radius des Kreises beträgt {0} cm".format(radius))
print("Der Umfang des Kreises beträgt {0} cm".format(umfang))
print("Die Fläche des Kreises beträgt {0} cm2".format(flaeche))
