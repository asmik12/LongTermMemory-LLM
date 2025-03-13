import json
import argparse
from follow_up_q import QueryAssistant

def collect_outputs(chat_system, input_data):
    outputs = []
    
    for entry in input_data:
        question_id = entry['question_id']
        timestamped_history = entry['timestamped_history']
        
        # Simulate feeding to your chat system
        hypothesis = chat_system.get_response(timestamped_history)
        
        outputs.append({
            'question_id': question_id,
            'hypothesis': hypothesis
        })
    
    return outputs

def save_to_jsonl(outputs, output_file):
    with open(output_file, 'w') as f:
        for item in outputs:
            f.write(json.dumps(item) + '\n')

def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate LongMemEval outputs")
    parser.add_argument('--input_file', type=str, required=True, help="Input file with timestamped history")
    parser.add_argument('--output_file', type=str, required=True, help="Output file for saving results in JSONL format")
    return parser.parse_args()

def main():
    QueryAssistant()
    #args = parse_args()

    # Load input data
    input_file = 'generated_follow_ups.jsonl'
    history_file = 'data/longmemeval_oracle.json'
    i = 0

    with open(history_file, "r") as h:
        history = json.load(h)
    

    with open(input_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())  # Convert JSON string to dictionary
            #print(data["question_id"], data["question"], data["follow_up"])  # Access fields

            #answer_prompt_template taken from cot in generation.py
            #answer_prompt_template = 'I will give you several history chats between you and a user. Please answer the question based on the relevant chat history. Answer the question step by step: first extract all the relevant information, and then reason over the information to get the answer.\n\n\nHistory Chats:\n\n{}\n\nCurrent Date: {}\nQuestion: {}\nAnswer (step by step):'
             

            #Call the model and have it generate outputs based on history

        

    # Assuming you have a chat system object ready
    #chat_system = YourChatSystem()  # Replace with your actual chat system

    # Collect outputs by feeding the data to the chat system
    #outputs = collect_outputs(chat_system, input_data)
    
    # Save outputs to JSONL format
    #save_to_jsonl(outputs, args.output_file)
    
    #print(f"Results saved to {args.output_file}")

if __name__ == "__main__":
    main()