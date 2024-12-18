import pandas as pd
import json

def parse_conversations(row):
    """
    Parse a JSON-formatted message to extract message type and content.

    Args:
        row (str): A JSON-formatted string containing the message.

    Returns:
        tuple: A tuple with:
            - str: The message type ('ai' or 'human').
            - str: The message content.

    Raises:
        ValueError: If the JSON structure is invalid.
    """
    try:
        message_data = json.loads(row)
        return message_data['type'], message_data['data']['content']
    except Exception as e:
        print(f"Error parsing message{e}")
        return None, None


def get_grouped_conversations(file_path):
    """
    Process a CSV file to group conversations by session ID.

    Args:
        file_path (str): Path to the CSV file containing conversation data.

    Returns:
        pandas.core.groupby.generic.DataFrameGroupBy: 
            Grouped conversations by session ID.

    """
    # Load and read the CSV file
    df = pd.read_csv(file_path)
    
    # Check that we have a 'message' column
    if 'message' not in df.columns:
        raise ValueError("The provided CSV file does not contain a 'message' column.")
    
    # Parse existing messages
    df[['message_type', 'message_content']] = df['message'].apply(parse_conversations).apply(pd.Series)
    
    # Filter for relevant types of messages - in this example we have hardcoded "ai" and "human" to identify AI agents and human users
    df = df[df['message_type'].isin(['ai', 'human'])]
    
    # Convert the 'created_at' to datetime format and sort the list of conversation
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df = df.sort_values(by=['session_id', 'created_at'])

    # Group the conversations by their conversation IDs
    conversations = df.groupby('session_id')
    
    return conversations
