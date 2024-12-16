from transformers import pipeline
from label_fetcher import fetch_label_mapping


sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_message(messages, label_map):
    results = []
    try:
       
       for message in messages:
        if not isinstance(message, str) or not any(c.isalpha()for c in message):
          raise ValueError("Input must be text.")
        result = sentiment_pipeline(message)
        human_label = label_map[int(result[0]['label'].split('_')[-1])]
        results.append((human_label, result[0]['score']))
       return  results
   
    except Exception as e:
        print(f"An error occured: {e}")
        return None, None
    
task = "sentiment"
labels = fetch_label_mapping(task)
        
messages = ["This is the first great message", "This is the second crappy message", "I don't really care about the third message"]
   
final_result = analyze_message(messages, labels)

print("Sentiment Analysis Results:")
for i, (sentiment, confidence) in enumerate(final_result, start=1):
    print(f"Message {i}: Sentiment: {sentiment}, Confidence: {confidence:.2f}")
    
