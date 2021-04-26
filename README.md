# REST-API-NBA-Players
 
This project concerns the deployment of a REST API in the form of a unit request making it possible to automatically predict whether an NBA drafted player will have a career greater than or less than 5 years.

In the AnalysisJupyterNotebook folder, we have a Jupyter Notebook performing the analysis of the considered dataset and training the model.

In the second folder, we have the Django project corresponding to the API. It was executed under the Python virtual environment, built under Pycharm. It is functional and has been tested several times under Postman.

Instructions : 
 * install requirements : pip install -r requirements.txt
 * virtual environment : venv\Scripts\activate
 * run server : python manage.py runserver
 * Postman

For any future use of this API, the variables to enter in Postman are as follows:
 * name (player name)
 * gp (number of games played)
 * min (total number of minutes played)
 * pts (points scored per game)
 * fgm (shots scored excluding free throws)
 * ftm (marked free throws)
 * fta (attempted free throws)
 * oreb (offensive rebounds)
 * dreb (defensive rebounds)
 * reb (rebounds)
 * ast (assists)
 * stl (steals)
 * blk (blocks)
 * tov (turnovers)

All of these values are floats.
