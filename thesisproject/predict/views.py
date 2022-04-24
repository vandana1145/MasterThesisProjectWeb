from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        floor_num = float(request.POST.get('floor_num'))
        floor_area = float(request.POST.get('floor_area'))
        column_area = float(request.POST.get('column_area'))
        concrete_wall_areaNS = float(request.POST.get('concrete_wall_areaNS'))
        concrete_wall_areaEW = float(request.POST.get('concrete_wall_areaEW'))
        masonry_wall_areaNS = float(request.POST.get('masonry_wall_areaNS'))
        masonry_wall_areaEW = float(request.POST.get('masonry_wall_areaEW'))
        captive_column = float(request.POST.get('captive_column'))

        # Unpickle model
        model = pd.read_pickle(r".new_randomforest.pickle")
        # Make prediction
        result = model.predict([[floor_num, floor_area, column_area, concrete_wall_areaNS, 
        concrete_wall_areaEW, masonry_wall_areaNS, masonry_wall_areaEW, captive_column]])

        classification = result[0]

        PredResults.objects.create(floor_num=floor_num, floor_area=floor_area, column_area=column_area,
                                   concrete_wall_areaNS=concrete_wall_areaNS, concrete_wall_areaEW=concrete_wall_areaEW, 
                                   masonry_wall_areaNS=masonry_wall_areaNS, masonry_wall_areaEW=masonry_wall_areaEW, 
                                   captive_column=captive_column, classification=classification)

        return JsonResponse({'result': classification, 'floor_num': floor_num, 'floor_area': floor_area,
                             'column_area': column_area, 'concrete_wall_areaNS': concrete_wall_areaNS, 
                             'concrete_wall_areaEW': concrete_wall_areaEW,'masonry_wall_areaNS': masonry_wall_areaNS,
                             'masonry_wall_areaEW': masonry_wall_areaEW, 'captive_column': captive_column},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)

