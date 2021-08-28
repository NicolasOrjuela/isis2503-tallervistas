from variables.models import Variable
from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(llave):
    measurement = Measurement.objects.filter(pk=llave)
    return measurement

def delete_measurement(llave):
    measurement = Measurement.objects.filter(pk=llave)
    measurement.delete()
    return measurement

def create_measurement(variable, value, unit, place):
    variable1 = Variable.objects.get(name=variable)
    measurement = Measurement(variable=variable1, value=value, unit=unit, place=place)
    measurement.save()
    measurement1 = Measurement.objects.filter(variable=variable1, value=value, unit=unit, place=place)
    return measurement1

def modify_measurement(llave, opcion, variable):
    if opcion == 1:
        Measurement.objects.filter(pk=llave).update(variable=variable)

    elif opcion == 2:
        Measurement.objects.filter(pk=llave).update(value=variable)

    elif opcion == 3:
        Measurement.objects.filter(pk=llave).update(unit=variable)

    elif opcion == 4:
        Measurement.objects.filter(pk=llave).update(place=variable)

    measurement = Measurement.objects.filter(pk=llave)
    return measurement
