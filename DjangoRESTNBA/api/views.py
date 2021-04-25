# Import necessary libraries
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np


# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful",
    }
    return Response(return_data)


@api_view(["POST"])
def predict(request):
    try:
        name = request.data.get('name', None)
        gp = request.data.get('gp', None) # gp is not necessary in the model, but we need it here to have "_by_game" values
        min = request.data.get('min', None)
        pts = request.data.get('pts', None)
        fgm = request.data.get('fgm', None)
        ftm = request.data.get('ftm', None)
        fta = request.data.get('fta', None)
        oreb = request.data.get('oreb', None)
        dreb = request.data.get('dreb', None)
        reb = request.data.get('reb', None)
        ast = request.data.get('ast', None)
        stl = request.data.get('stl', None)
        blk = request.data.get('blk', None)
        tov = request.data.get('tov', None)
        fields = [name, gp, min, pts, fgm, ftm, fta, oreb, dreb, reb, ast, stl, blk, tov]
        if not None in fields:
            # Datapreprocessing Convert the values to float
            name = str(name)
            gp = float(gp)
            pts = float(pts)
            blk = float(blk)
            min = float(min)
            reb = float(reb)
            ast = float(ast)
            stl = float(stl)
            tov = float(tov)
            fgm = float(fgm)
            ftm = float(ftm)
            fta = float(fta)
            oreb = float(oreb)
            dreb = float(dreb)

            pts_by_game = pts / gp
            min_by_game = min / gp
            tov_by_game = tov / gp
            blk_by_game = blk / gp
            ast_by_game = ast / gp
            stl_by_game = stl / gp
            reb_by_game = reb / gp
            fgm_by_game = fgm / gp
            ftm_by_game = ftm / gp
            fta_by_game = fta / gp
            oreb_by_game = oreb / gp
            dreb_by_game = dreb / gp

            result = [pts_by_game, min_by_game, tov_by_game, blk_by_game, ast_by_game, stl_by_game, reb_by_game, fgm_by_game, ftm_by_game, fta_by_game, oreb_by_game, dreb_by_game]
            # Passing data to model & loading the model from disks
            model_path = 'model/lr.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            if prediction == 0:
                prediction = "career length < 5 years"
            else:
                prediction = "career length >= 5 years"
            conf_score = np.max(classifier.predict_proba([result])) * 100
            predictions = {
                'error': '0',
                'message': 'Successfull',
                'prediction': prediction,
                'confidence_score': conf_score
            }
        else:
            predictions = {
                'error': '1',
                'message': 'Missing Parameters',
                'contenu': fields
            }
    except Exception as e:
        predictions = {
            'error': '2',
            "message": str(e)
        }

    return Response(predictions)
