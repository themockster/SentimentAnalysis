from transformers import pipeline
from label_fetcher import fetch_label_mapping

# Setup of the Hugging Face pipeline for sentiment-analysis, using GPU (device=0)
sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="cardiffnlp/twitter-roberta-base-sentiment", 
    device=0
)

def analyze_message(messages, label_map):
    """
    Analyze a list of messages using the sentiment pipeline.

    Args:
        messages (list): A list of text messages.
        label_map (dict): Mapping of sentiment labels to human-readable labels.

    Returns:
        list: A list of tuples with (sentiment_label, confidence_score).
    """
    results = []
    try:
        if not all(isinstance(msg, str) and any(c.isalpha() for c in msg) for msg in messages):
            raise ValueError("All inputs must be non-empty text strings.")

        # Pass the entire list of messages to the pipeline at once (batch processing)
        pipeline_results = sentiment_pipeline(messages)

        # Map the results
        for result in pipeline_results:
            human_label = label_map[int(result['label'].split('_')[-1])]
            results.append((human_label, result['score']))

        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
