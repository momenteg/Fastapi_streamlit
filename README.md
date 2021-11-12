# Front end served but Fast Api on iris classification: 

## Build: 
- `docker-compose build`
- `docker-compose up -d`
- check `docker-compose ps` and `docker-compose logs` to make sure that the services started correctly

## Access: 
- connect to `http://localhost:8501/` and have fun :)
- explore the api structure at: `http://localhost:8080/docs`

## What I learned/useful things:
- how to build an api with [fastapi](https://fastapi.tiangolo.com/)
- how to build a simple frontend using streamlit
- refreshed [docker compose networking](https://docs.docker.com/compose/networking/) knowledge  

## What I would do differently: 
The frontend is really barebone, I would extend it. 

## How to create the serving model: 
How to create the ML model that is served by the webapp: 

```
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import yaml
from pathlib import Path


## GETTING AND PARSING THE DATA
data = load_iris()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(data.data, data.target, test_size=0.3, random_state=4)

## TRAINING A MODEL
logreg = LogisticRegression(solver="liblinear", multi_class="ovr")


clf = logreg.fit(Xtrain, Ytrain)
# See if the model is reasonable.
print("Score: ", clf.score(Xtest, Ytest))
# Pickle to save the model for use in our API.
joblib.dump(clf, "log_reg.pkl")
```