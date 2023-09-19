from originality_ditection import model


class parser:
    def __init__(self, model_path: str):
        self.model_path = model_path

    def parse_text(
        self,
        question: str,
        answer: str,
    ) -> str:
        detect_model = model.Model(self.model_path)
        score = detect_model.predict(question, answer)
        # DEBUG
        # print(score)
        if score > 0.9:
            return f"<mark class=highlight>{answer}</mark>"
        elif score < 0.1:
            return f"<mark class=ai_highlight>{answer}</mark>"
        else:
            return answer
