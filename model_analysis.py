import pandas as pd
import torch 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix,classification_report,precision_recall_fscore_support, accuracy_score
from transformers import BertTokenizer, BertModel
from utils import remove_emoji,tokenize,remove_punct,label_encode,label2name
from training_utils import evaluate


def LoadData(path):
    '''Method to load and preprocess the data'''
    df = pd.read_csv(path) # Load the data from the CSV file located at 'path' into a pandas DataFrame
    
    # Select specific columns from the DataFrame to be included in the 'data' DataFrame
    data = df[["address", "categories", "city", "country", "name", "province", "reviews.rating", "reviews.text"]]

    # Apply a series of text processing functions to the 'reviews' column
    # The processing steps are:
    # 1. Tokenize the review text (break it into tokens/words)
    # 2. Convert the text to lowercase
    # 3. Remove emojis from the text
    # 4. Remove punctuation from the text
    # The result is a cleaned and normalized version of the review text
    df["reviews.text"] = df["reviews.text"].apply(lambda x: remove_punct(remove_emoji(tokenize(x).lower())[0][0]))

    data.dropna(inplace=True)# Drop any rows with missing values (NaN) from the 'data' DataFrame
    
    return data

def Tokenization(df, config,tokenizer):
    """
    Function that tokenizes and encodes a dataset using a BERT tokenizer.
    
    Parameters:
    - df: A pandas DataFrame containing a column of text, e.g., 'reviews'.
    - config: A configuration object that holds parameters to customize the tokenizer behavior.
    
    Returns:
    - encoded_data: The data encoded by the BERT tokenizer in tensor form, ready to be
                    processed by a BERT model.
    """

    

    # Batch encode the data using the BERT tokenizer. Here, several important parameters for tokenization
    # and preprocessing are specified:
    encoded_data = tokenizer.batch_encode_plus(
        df["reviews.text"].values,  # The text column (e.g., 'reviews') from the DataFrame containing the text data.
        add_special_tokens=config.add_special_tokens,  # Whether to add special tokens like [CLS] and [SEP].
        return_attention_mask=config.return_attention_mask,  # Whether to return the attention mask for the model.
        pad_to_max_length=config.pad_to_max_length,  # Whether to pad the sequences to make them the same length.
        max_length=config.seq_length,  # The maximum length of the sequences after padding.
        return_tensors=config.return_tensors, # Specifies the type of tensors returned (e.g., 'pt' for PyTorch).
        truncation = True
    )

    # Return the encoded data, which is now ready to be used as input to a BERT model.
    return encoded_data
    
def ErrorAnalysis(test_df,encoded_data, config,model):

    #pred_final = []
    #print(encoded_data)
    #predictions_test,true_vals_test = Process(encoded_data, config,model)
    _,predictions_test,true_vals_test = Process(encoded_data, config,model)
    # predictions = np.concatenate(predictions_test, axis=0)
    # pred_final.append(np.argmax(predictions, axis=1).flatten()[0])
    preds_flat_test = np.argmax(predictions_test, axis=1).flatten()

    test_df["pred"] = preds_flat_test
    control = test_df["pred"].values == test_df["reviews.rating"].values
    test_df["control"] = control

    test_df = test_df[test_df.control == False]
    
    name2label = {"Negative":0,#arreglar
              "Neutral":1,
             "Positive":2
             }
    label2name = {v: k for k, v in name2label.items()}#arreglar

    val_df["pred_name"] = val_df.pred.apply(lambda x: label2name.get(x)) 
    
    confmat = confusion_matrix(val_df.label_name.values, val_df.pred_name.values, labels=list(name2label.keys()))

    # Visualize Confusion Matrices
    # fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    # sns.heatmap(conf_matrix_1, annot=True, fmt='d', cmap='Blues', ax=ax[0]).set_title('Model 1')
    # sns.heatmap(conf_matrix_2, annot=True, fmt='d', cmap='Blues', ax=ax[1]).set_title('Model 2')
    # plt.show()  
    print(confmat)

    df_confusion_val = pd.crosstab(label_values, pred_name_values)
    print(df_confusion_val)
    report = classification_report(preds_flat_test, true_vals_test)
    print(report)

    precision, recall, f1_score, _= precision_recall_fscore_support(true_vals_test_1, preds_flat_test_1, average='micro')
    print(metrics)
    accuracy = accuracy_score(true_vals_test, preds_flat_test)

    return (( precision, recall, f1_score),accuracy),confmat

def ModelComparation(arg1, arg2):
    
    # true_vals_test_1,preds_flat_test_1 = arg1
    # true_vals_test_2,preds_flat_test_2 = arg2
    # # Modelo 1
    # metrics_1 = precision_recall_fscore_support(true_vals_test_1, preds_flat_test_1, average='weighted')
    # accuracy_1 = accuracy_score(true_vals_test_1, preds_flat_test_1)

    # # Modelo 2
    # metrics_2 = precision_recall_fscore_support(true_vals_test_2, preds_flat_test_2, average='weighted')
    # accuracy_2 = accuracy_score(true_vals_test_2, preds_flat_test_2)

    # # Mostrando resultados
    # print("Model 1 - Precision: {:.4f}, Recall: {:.4f}, F1-Score: {:.4f}, Accuracy: {:.4f}".format(*metrics_1, accuracy_1))
    # print("Model 2 - Precision: {:.4f}, Recall: {:.4f}, F1-Score: {:.4f}, Accuracy: {:.4f}".format(*metrics_2, accuracy_2))


    metrics_1,accuracy_1,conf_matrix_1 = arg1
    metrics_2,accuracy_2,conf_matrix_2 = arg2
    # Nombres de las métricas
    metrics_names = ['Precision', 'Recall', 'F1-Score', 'Accuracy']

    # Métricas de los dos modelos
    metrics_model_1 = list(metrics_1) + [accuracy_1]
    metrics_model_2 = list(metrics_2) + [accuracy_2]

    # Configuración del gráfico
    x = np.arange(len(metrics_names))  # Posición de las métricas
    width = 0.35  # Ancho de las barras

    # Creación del gráfico
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, metrics_model_1, width, label='Model 1')
    rects2 = ax.bar(x + width/2, metrics_model_2, width, label='Model 2')

    # Añadir etiquetas y título
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Scores')
    ax.set_title('Metrics Comparison Between Model 1 and Model 2')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics_names)
    ax.legend()

    # Mostrar las etiquetas de las barras
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    plt.show()


    # Gráficos de las matrices de confusión
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.heatmap(conf_matrix_1, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title('Confusion Matrix - Model 1')

    sns.heatmap(conf_matrix_2, annot=True, fmt='d', cmap='Blues', ax=axes[1])
    axes[1].set_title('Confusion Matrix - Model 2')

    plt.show()



    precision_diff = metrics_1[0] - metrics_2[0]
    recall_diff = metrics_1[1] - metrics_2[1]
    f1_score_diff = metrics_1[2] - metrics_2[2]
    accuracy_diff = accuracy_1 - accuracy_2

    print("Precision Difference: {:.4f}".format(precision_diff))
    print("Recall Difference: {:.4f}".format(recall_diff))
    print("F1-Score Difference: {:.4f}".format(f1_score_diff))
    print("Accuracy Difference: {:.4f}".format(accuracy_diff))


# def Process(test_df,config,model)):
#     pred_final, true_vals = [],[]
#     for i, row in tqdm(test_df.iterrows(), total=test_df.shape[0]):
        
#         review = row["Review"]
#         encoded_data_test_single = tokenizer.batch_encode_plus(
#         [review], 
#         add_special_tokens=config.add_special_tokens, 
#         return_attention_mask=config.return_attention_mask, 
#         pad_to_max_length=config.pad_to_max_length, 
#         max_length=config.seq_length,
#         return_tensors=config.return_tensors
#         )
#         input_ids_test = encoded_data_test_single['input_ids']
#         attention_masks_test = encoded_data_test_single['attention_mask']

        
#         inputs = {'input_ids':      input_ids_test.to(device),
#                 'attention_mask':attention_masks_test.to(device),
#                 }

#         with torch.no_grad():        
#             outputs = model(**inputs)
        
#         logits = outputs[0]
#         logits = logits.detach().cpu().numpy() 
#         label_ids = inputs['labels'].cpu().numpy()
#         true_vals.append(label_ids)
#         predictions.append(logits)
            
#     predictions = np.concatenate(predictions, axis=0)
#     pred_final.append(np.argmax(predictions, axis=1).flatten()[0])
#     return pred_final,true_vals

def Process(encoded_data,config,model):
    model.eval()
   
    loss_val_total = 0
    predictions, true_vals = [], []
    
    batch = tuple(encoded_data.to(config.device) for b in encoded_data)
        
    inputs = {'input_ids':      batch[0],
                'attention_mask': batch[1],
                'labels':         batch[2],
                 }

    with torch.no_grad():        
        outputs = model(**inputs)
            
    loss = outputs[0]
    logits = outputs[1]
    loss_val_total += loss.item()

    logits = logits.detach().cpu().numpy()
    label_ids = inputs['labels'].cpu().numpy()
    predictions.append(logits)
    true_vals.append(label_ids)
        
    # calculate avareage val loss
    loss_val_avg = loss_val_total/len(encoded_data) 
    
    predictions = np.concatenate(predictions, axis=0)
    true_vals = np.concatenate(true_vals, axis=0)
            
    return loss_val_avg, predictions, true_vals