from originality_ditection import model


class detector:
    def __init__(
        self, model_path: str, ai_degree: float = 0.1, human_degree: float = 0.9
    ) -> None:
        self.model_path = model_path
        self.ai_degree = ai_degree
        self.human_degree = human_degree

    def detect(
        self,
        question: str,
        answer: str,
    ) -> str:
        detect_model = model.Model(self.model_path)
        prob_human = detect_model.predict(question, answer)
        print(f"Probability of human answers: {prob_human}")
        if prob_human > self.human_degree:
            return "it considered to be a human answer"
        elif prob_human < 0.1:
            return "it considered to be an AI answer"
        else:
            return "can't determine if it's a human or an AI answer"
