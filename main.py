from conversation_parser import get_grouped_conversations
from conversation_analyzer import analyze_message
from label_fetcher import fetch_label_mapping

# Path to the CSV file containing the conversations
csv_file_path = "conversation_data.csv"

# Call the conversation parser to clean and group conversations
conversations = get_grouped_conversations(csv_file_path)

# Set the task to "sentiment" and fetch the sentiment labels
task = "sentiment"
labels = fetch_label_mapping(task)

# Initialize an empty list to store session-level results
session_result = []

# Analyze each session and populate session_result
for session_id, group in conversations:
    #print(f"\nAnalyzing Session ID: {session_id}")

    # Extract AI and HUMAN messages
    ai_messages = group[group['message_type'] == 'ai']['message_content'].tolist()
    human_messages = group[group['message_type'] == 'human']['message_content'].tolist()

    # Run sentiment analysis for AI and HUMAN messages
    ai_sentiments = analyze_message(ai_messages, labels)
    human_sentiments = analyze_message(human_messages, labels)

    # Store the results for this session
    session_result.append({
        "session_id": session_id,
        "ai_sentiments": ai_sentiments,
        "human_sentiments": human_sentiments
    })

# Output the session-level sentiment analysis results
print("\nSession-Level Sentiment Analysis Results:")
for result in session_result:
    session_id = result['session_id']
    ai_sentiments = result['ai_sentiments']
    human_sentiments = result['human_sentiments']
    
    # Calculate proportions of sentiments for AI messages
    ai_sentiment_counts = {}
    for sentiment, confidence in ai_sentiments:
        if sentiment in ai_sentiment_counts:
            ai_sentiment_counts[sentiment].append(confidence)
        else:
            ai_sentiment_counts[sentiment] = [confidence]
    
    # Calculate proportions of sentiments for HUMAN messages
    human_sentiment_counts = {}
    for sentiment, confidence in human_sentiments:
        if sentiment in human_sentiment_counts:
            human_sentiment_counts[sentiment].append(confidence)
        else:
            human_sentiment_counts[sentiment] = [confidence]

    # Display session-level sentiment proportions
    print(f"\nSession ID: {session_id}")
    print("  AI Sentiments:")
    for sentiment, confidences in ai_sentiment_counts.items():
        avg_confidence = sum(confidences) / len(confidences)
        print(f"    - {sentiment.capitalize()}: Count = {len(confidences)}, Avg Confidence = {avg_confidence:.2f}")

    print("  Human Sentiments:")
    for sentiment, confidences in human_sentiment_counts.items():
        avg_confidence = sum(confidences) / len(confidences)
        print(f"    - {sentiment.capitalize()}: Count = {len(confidences)}, Avg Confidence = {avg_confidence:.2f}")
