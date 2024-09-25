import torch
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np



tokenizer = BertTokenizer.from_pretrained("src\Webapp\model_Hotel-Recommendation")


model = BertForSequenceClassification.from_pretrained(
    "src\Webapp\model_Hotel-Recommendation",
    num_labels=3,
    output_attentions=False,
    output_hidden_states=False
)
# Change fine_tuned_model to cpu
model.to("cpu")



def sentiment_analysis(comment):
    # Tokenizar el comentario
    inputs = tokenizer(comment, return_tensors='pt', padding=True, truncation=True, max_length=512)

    # Mover los tensores al dispositivo adecuado (CPU o GPU)
    device = torch.device("cpu")
    model.to(device)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    with torch.no_grad():  # Desactivar cálculo de gradientes
        outputs = model(**inputs)  # Obtener las salidas del modelo

    logits = outputs.logits  # Extraer los logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()  # Calcular probabilidades

    predicted_label = np.argmax(probabilities)  # Etiqueta predicha (índice)
    confidence_score = probabilities[0][predicted_label]  # Score de confianza

    # Mapear índice a etiqueta (ajusta según tus etiquetas)
    label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}  # Cambia esto según tus etiquetas reales
    sentiment_label = label_map[predicted_label]

    return sentiment_label, confidence_score

# Ejemplo de uso:
comment = "it is very bad."
result = sentiment_analysis(comment)
print(result)  # Debería imprimir algo como ('positive', 0.9)