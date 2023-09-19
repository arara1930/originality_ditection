import torch
from torch.nn import Softmax
from transformers import BertForSequenceClassification, BertJapaneseTokenizer


class Model:
    def __init__(self, model_path: str):
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.device = device
        # Tokenizerの準備
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(
            "sonoisa/sentence-bert-base-ja-mean-tokens-v2"
        )

        self.bert_sc = BertForSequenceClassification.from_pretrained(model_path)
        self.bert_sc.to(device)

    def predict(self, q, a):
        sf = Softmax(dim=1)
        encoding = self.tokenizer(
            q,
            a,
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )

        encoding = {k: v.to(self.device) for k, v in encoding.items()}

        with torch.no_grad():
            output = self.bert_sc.forward(**encoding)
            scores = output.logits
            # labels_predicted = scores[0].argmax(-1).cpu().numpy().tolist()

        scores = sf(scores)
        return scores[0][0].item()
