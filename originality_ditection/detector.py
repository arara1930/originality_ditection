from transformers.utils.logging import os

from originality_ditection import model


class detector:
    def __init__(
        self, model_path: str, ai_degree: float = 0.1, human_degree: float = 0.9
    ) -> None:
        self.model_path = model_path
        self.ai_degree = ai_degree
        self.human_degree = human_degree
        self.sanity_check()
        self.detect_model = model.Model(self.model_path)

    def sanity_check(self) -> None:
        if os.path.exists(self.model_path) == False:
            raise ValueError("model_path is not found.")

        # Check ai_degree and human_degree.
        if self.ai_degree < 0.0 or self.ai_degree > 1.0:
            raise ValueError("ai_degree must be between 0.0 and 1.0.")
        if self.human_degree < 0.0 or self.human_degree > 1.0:
            raise ValueError("human_degree must be between 0.0 and 1.0.")

    def detect(
        self,
        question: str,
        answer: str,
    ) -> str:
        prob_human = self.detect_model.predict(question, answer)
        return_text = (
            f"======= \n Probability of human answers: {prob_human} \n ======= \n"
        )
        if prob_human > self.human_degree:
            return_text += "it considered to be a human answer"
        elif prob_human < self.ai_degree:
            return_text += "it considered to be an AI answer"
        else:
            return_text += "can't determine if it's a human or an AI answer"
        return return_text

    def detect_bool(
        self,
        question: str,
        answer: str,
    ) -> bool or None:
        prob_human = self.detect_model.predict(question, answer)
        if prob_human > self.human_degree:
            return True
        elif prob_human < self.ai_degree:
            return False
        else:
            return None
