# **Sentiment Analysis Tool for Conversations**

This project analyzes the sentiment of messages or full chat exchanges using a pre-trained transformer model from Hugging Face. It supports dynamic label mapping for flexibility and can process single or multi-turn conversations.

---

## **Features**
- **Sentiment Analysis**: Classifies text into **Positive**, **Negative**, or **Neutral** sentiment.  
- **Dynamic Label Mapping**: Fetches human-readable labels dynamically to ensure compatibility with any model.  
- **Flexible Input**: Accepts individual messages or entire conversations for analysis.  
- **Scalable**: Easily extendable for additional tasks like emotion detection or fine-tuning.

---

## **Technologies Used**
- **Python 3.12+**  
- **Hugging Face Transformers**  
- **Cardiff NLP Model**: `cardiffnlp/twitter-roberta-base-sentiment`  

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone <your-repo-url>
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

## **File Structure**
```plaintext
.
├── label_fetcher.py       # Fetches dynamic label mappings from Cardiff NLP
├── main.py                # Main script for sentiment analysis
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

---

## **How It Works**
1. **Dynamic Label Mapping**:  
   Labels are fetched from a remote source (e.g., Cardiff NLP) to ensure compatibility with the sentiment model.  
2. **Message/Conversation Processing**:  
   Text data is passed to a Hugging Face pipeline for analysis.  
3. **Output**:  
   The tool outputs sentiment (**Positive**, **Neutral**, or **Negative**) along with the confidence score.

---

## **Example Output**
```plaintext
Sentiment Analysis Results:
Message 1: Sentiment: positive, Confidence: 0.98
Message 2: Sentiment: negative, Confidence: 0.76
Message 3: Sentiment: neutral, Confidence: 0.81
```

---

## **Future Improvements**
- Add support for analyzing individual user/agent exchanges in a conversation.
- Fine-tune the model for domain-specific datasets (e.g., customer support conversations).
- Add options to save results to a file (CSV, JSON, etc.).

---

## **Credits**
- [Hugging Face Transformers](https://huggingface.co/)
- [Cardiff NLP Models](https://huggingface.co/cardiffnlp)

---

## **License**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
