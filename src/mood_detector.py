import os
import joblib


class MoodDetector:

    def __init__(self):

        project_root = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        model_path = os.path.join(
            project_root,
            "models",
            "emotion_model"
        )

        self.vectorizer = joblib.load(
            os.path.join(
                model_path,
                "tfidf.pkl"
            )
        )

        self.model = joblib.load(
            os.path.join(
                model_path,
                "emotion_model.pkl"
            )
        )

    def predict(self, text):

        X = self.vectorizer.transform([text])

        return self.model.predict(X)[0]

    def predict_proba(self, text):

        X = self.vectorizer.transform([text])

        probs = self.model.predict_proba(X)[0]

        return {
            emotion: round(float(prob), 3)
            for emotion, prob in zip(
                self.model.classes_,
                probs
            )
        }