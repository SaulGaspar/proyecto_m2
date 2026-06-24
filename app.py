from flask import Flask, render_template, request
import pickle
from pathlib import Path

app = Flask(__name__)

MODEL_PATH = Path(__file__).with_name('modelo_concreto.pkl')
with open(MODEL_PATH, 'rb') as f:
    artifact = pickle.load(f)

pipeline = artifact['pipeline']
FEATURES = artifact['features']
METRICS = artifact.get('metrics', {})

FIELD_LABELS = {
    'cement': 'Cemento',
    'blast_furnace_slag': 'Escoria de alto horno',
    'fly_ash': 'Ceniza volante',
    'water': 'Agua',
    'superplasticizer': 'Superplastificante',
    'coarse_aggregate': 'Agregado grueso',
    'fine_aggregate': 'Agregado fino',
    'age': 'Edad de curado'
}

FIELD_HELP = {
    'cement': 'kg/m3',
    'blast_furnace_slag': 'kg/m3',
    'fly_ash': 'kg/m3',
    'water': 'kg/m3',
    'superplasticizer': 'kg/m3',
    'coarse_aggregate': 'kg/m3',
    'fine_aggregate': 'kg/m3',
    'age': 'dias'
}

DEFAULT_VALUES = {
    'cement': 540.0,
    'blast_furnace_slag': 0.0,
    'fly_ash': 0.0,
    'water': 162.0,
    'superplasticizer': 2.5,
    'coarse_aggregate': 1040.0,
    'fine_aggregate': 676.0,
    'age': 28
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    values = DEFAULT_VALUES.copy()

    if request.method == 'POST':
        try:
            for feature in FEATURES:
                values[feature] = float(request.form.get(feature, ''))

            row = [[values[feature] for feature in FEATURES]]
            prediction = float(pipeline.predict(row)[0])

        except ValueError:
            error = 'Ingresa solo valores numericos en todos los campos.'
        except Exception as exc:
            error = f'No se pudo realizar la prediccion: {exc}'

    return render_template(
        'index.html',
        features=FEATURES,
        labels=FIELD_LABELS,
        help_text=FIELD_HELP,
        values=values,
        prediction=prediction,
        error=error,
        metrics=METRICS
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)