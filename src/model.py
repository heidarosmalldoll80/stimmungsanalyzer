import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

# Dummy Trainingdaten und Labels
texts = ['Ich liebe das!', 'Das ist schrecklich.', 'Es ist okay.']
labels = ['positiv', 'negativ', 'neutral']

# Erstellen des Modells
model = make_pipeline(CountVectorizer(), LogisticRegression())
model.fit(texts, labels)

# Modell speichern
joblib.dump(model, 'dein_modell.pkl')
