def feet_meter(feet):
    meter = feet * 0.305
    return meter


def meter_feet(meter):
    feet = meter * 3.279
    return feet


print("Feet \t Meter \t\t Meter \t Feet")
for i in range(1, 21):
    print(i, "\t\t", feet_meter(i), "\t\t", i, "\t\t", meter_feet(i), sep='')
