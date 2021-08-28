from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement
from .logic.logic_measurements import create_measurement
from .logic.logic_measurements import delete_measurement
from .logic.logic_measurements import modify_measurement
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurementDetail(request, llave):
    measurement = get_measurement(llave)
    measurement_json = serializers.serialize('json', measurement)
    return HttpResponse(measurement_json, content_type='application/json')

def delete_measurementDetail(request, llave):
    measurement = delete_measurement(llave)
    measurement_json = serializers.serialize('json', measurement)
    return HttpResponse(measurement_json, content_type='application/json')

def create_measurementDetail(request, variable, value, unit, place):
    measurement = create_measurement(variable, value, unit, place)
    measurement_json = serializers.serialize('json', measurement)
    return HttpResponse(measurement_json, content_type='application/json')

def modify_measurementDetail(request, llave, opcion, variable):
    measurement = modify_measurement(llave, opcion, variable)
    measurement_json = serializers.serialize('json', measurement)
    return HttpResponse(measurement_json, content_type='application/json')