# **Sentiment Analysis Tool for Conversations**

This project provides a robust **sentiment analysis tool** designed for processing technical support or conversational datasets. It leverages a **pre-trained transformer model** from Hugging Face to classify text into **Positive**, **Neutral**, or **Negative** sentiments.

The tool supports dynamic label mapping, enabling compatibility with various models and tasks. It is particularly useful for analyzing interactions, such as customer service chats, by segmenting messages by users (AI agents vs. Humans) and summarizing sentiment trends.

This tool was built to demonstrate and test a pipeline to monitor AI and human conversations in the context of customer service via an AI chatbot.

---

## **Features**

- **Sentiment Analysis**: 
   - Classifies messages as **Positive**, **Neutral**, or **Negative**, with associated confidence scores.
- **Session-Level Insights**: 
   - Groups conversations by session and analyzes sentiment trends for **AI** and **Human** participants.
- **Dynamic Label Mapping**: 
   - Adapts to different sentiment models through automated label fetching.
- **Batch Processing**: 
   - Processes multiple messages simultaneously for improved performance, leveraging GPU support.
- **Modular Design**: 
   - Individual scripts handle conversation parsing, sentiment analysis, and label fetching, making the tool extensible.

---

## **Technologies Used**

- **Python 3.12+**  
- **Hugging Face Transformers**  
- **Cardiff NLP Model**: `cardiffnlp/twitter-roberta-base-sentiment`  
- **Pandas**: For data manipulation.  

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/themockster/SentimentAnalysis
cd <your-repo-folder>
```

### **2. Create and Activate a Virtual Environment**
#### For Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```
#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Project**
Run the script to analyze sample messages:
```bash
python main.py
```

---

## **Workflow**

### **Input**: A CSV file with the following structure:
```csv
id,session_id,message,created_at
1,session_1,"{""type"": ""ai"", ""data"": {""content"": ""Hello! How can I assist you today?""}}",2024-12-16 18:44:21
2,session_1,"{""type"": ""human"", ""data"": {""content"": ""My laptop won't turn on. Can you help me?""}}",2024-12-16 18:45:21
```

### **Process**:
1. **Conversation Parsing**:
   - Extracts `message_type` (e.g., AI or Human) and `message_content` from the dataset.
   - Groups messages by `session_id`.

2. **Sentiment Analysis**:
   - Processes AI and Human messages separately.
   - Fetches labels dynamically from Cardiff NLP’s sentiment dataset.
   - Outputs **sentiments and confidence scores** for each message.

3. **Session-Level Summaries**:
   - Aggregates sentiment trends for AI and Human participants.
   - Displays counts and average confidence for each sentiment category.

### **Output**:
```plaintext
Session-Level Sentiment Analysis Results:

Session ID: session_1
  AI Sentiments:
    - Neutral: Count = 2, Avg Confidence = 0.80
  Human Sentiments:
    - Negative: Count = 1, Avg Confidence = 0.84

Session ID: session_2
  AI Sentiments:
    - Neutral: Count = 2, Avg Confidence = 0.84
  Human Sentiments:
    - Negative: Count = 1, Avg Confidence = 0.89
```

---

## **File Structure**

```plaintext
.
├── conversation_analyzer.py  # Sentiment analysis logic using Hugging Face
├── conversation_parser.py    # Processes and groups conversation data
├── label_fetcher.py          # Fetches dynamic sentiment labels
├── main.py                   # Main script for running the analysis
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## **How It Works**

### **Dynamic Label Mapping**
- The script fetches sentiment labels dynamically from Cardiff NLP’s GitHub repository, ensuring compatibility with the selected model.

### **Conversation Parsing**
- Parses raw JSON-formatted messages in a CSV file, extracting key details such as message type (AI or Human) and content.

### **Sentiment Analysis**
- Leverages the `cardiffnlp/twitter-roberta-base-sentiment` model to analyze messages in batches for efficiency. Supports GPU acceleration for faster processing.

### **Session Summaries**
- Provides sentiment breakdowns for each session, highlighting trends for AI agents and Human users.

---

## **Example Output**

For a sample session:
```plaintext
Session ID: session_1
  AI Sentiments:
    - Neutral: Count = 2, Avg Confidence = 0.80
  Human Sentiments:
    - Negative: Count = 1, Avg Confidence = 0.84
```

---

## **Potential Future Improvements**

- **Domain-Specific Sentiments**:
   - Add labels like "Frustrated" or "Hopeful" for technical support.
- **Sentiment Shift Analysis**:
   - Track sentiment progression within sessions (e.g., "Negative → Neutral").
- **Visualization**:
   - Generate heatmaps or graphs for sentiment trends.
- **Fine-Tuning**:
   - Train the sentiment model on technical support datasets for improved accuracy.
- **Microservice Endpoint**:
   - Provide the script as a microservice endpoint to monitor conversations and flag issues with support conversations.

---

## **Credits**

- [Hugging Face Transformers](https://huggingface.co/)
- [Cardiff NLP Models](https://huggingface.co/cardiffnlp)

---

## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
