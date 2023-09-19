from originality_ditection import detector

# Answer text should be one sentence.
question = "インターンシップの志望動機"
answer = "インターンシップの志望動機は、自分のスキルを活かして、会社の発展に貢献したいからです。"

"""
    @param model_path: Path to the model file.
    @param ai_degree: The degree of the AI answer. (0.0 ~ 1.0)
    default: 0.1
    @param human_degree: The degree of the human answer. (0.0 ~ 1.0)
    default: 0.9
"""
detector = detector.detector("YOUR MODEL PATH", ai_degree=0.1, human_degree=0.9)

# You can get the result as a string.
parse_text_result = detector.detect(question=question, answer=answer)
print(parse_text_result)

# You can get the result as a boolean True or False or None.
parse_bool_result = detector.detect_bool(question=question, answer=answer)
print(parse_bool_result)
