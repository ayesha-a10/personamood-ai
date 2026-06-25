import os
import joblib


class PersonalityClassifier:
    """
    Big Five Personality Predictor

    Traits:
    O = Openness
    C = Conscientiousness
    E = Extraversion
    A = Agreeableness
    N = Neuroticism
    """

    def __init__(self, model_dir=None):

        if model_dir is None:
            project_root = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            model_dir = os.path.join(
                project_root,
                "models",
                "personality_model"
            )

        self.model_dir = model_dir

        self.traits = ["O", "C", "E", "A", "N"]

        # Load TF-IDF vectorizer
        self.vectorizer = joblib.load(
            os.path.join(
                self.model_dir,
                "tfidf.pkl"
            )
        )

        # Load trait models
        self.models = {}

        for trait in self.traits:

            self.models[trait] = joblib.load(
                os.path.join(
                    self.model_dir,
                    f"{trait}.pkl"
                )
            )

    def predict(self, text):
        """
        Binary predictions (0/1)
        """

        X = self.vectorizer.transform([text])

        predictions = {}

        for trait in self.traits:

            pred = self.models[trait].predict(X)[0]

            predictions[trait] = int(pred)

        return predictions

    def predict_scores(self, text):
        """
        Probability scores
        """

        X = self.vectorizer.transform([text])

        scores = {}

        for trait in self.traits:

            prob = self.models[trait].predict_proba(X)[0][1]

            scores[trait] = round(
                float(prob),
                3
            )

        return scores

    def explain(self, scores):
        """
        Convert scores into readable personality levels
        """

        explanation = {}

        trait_names = {
            "O": "Openness",
            "C": "Conscientiousness",
            "E": "Extraversion",
            "A": "Agreeableness",
            "N": "Neuroticism"
        }

        for trait, score in scores.items():

            if score >= 0.70:
                level = "Very High"

            elif score >= 0.55:
                level = "High"

            elif score >= 0.45:
                level = "Moderate"

            elif score >= 0.30:
                level = "Low"

            else:
                level = "Very Low"

            explanation[
                trait_names[trait]
            ] = {
                "score": score,
                "level": level
            }

        return explanation

    def full_prediction(self, text):
        """
        Complete personality analysis
        """

        scores = self.predict_scores(text)

        explanation = self.explain(scores)

        return {
            "scores": scores,
            "analysis": explanation
        }