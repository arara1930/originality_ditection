from originality_ditection import detector

question = "インターンシップの志望動機"
answer = "インターンシップの志望動機は、自分のスキルを活かして、会社の発展に貢献したいからです。"
detector = detector("model/model.pkl")
parse_text = detector.detect(question, answer)
print(parse_text)
