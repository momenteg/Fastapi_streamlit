import joblib
from dataclasses import dataclass, field

import pathlib
import numpy as np

@dataclass
class Classifier:
    iris_type: dict = field(default_factory=lambda: {0: "setosa", 1: "versicolor", 2: "virginica"})
    clf = joblib.load(f'{pathlib.Path(__file__).parent.resolve()}/log_reg.pkl')

    def predict(self, features: dict):
        properties = [features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]
        prediction = self.clf.predict_proba([properties])

        return {'type': self.iris_type[np.argmax(prediction)], 'probability': round(max(prediction[0]), 2)}

