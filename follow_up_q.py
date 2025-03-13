from openai import OpenAI
from examples import knowledge_update, temporal_reasoning, multi_session_reasoning, information_extraction
import json
import numpy as np
import numpy.random as random
import re



# Model configuration
#model = 'meta-llama/Meta-Llama-3.1-8B-Instruct'                 #8B on port 8005
model = 'meta-llama/Llama-3.3-70B-Instruct'               #70B on port 8001
client = OpenAI(api_key='EMPTY', base_url='http://0.0.0.0:8001/v1/')

class QueryAssistant:
    def __init__(self, examples=None, max_questions=5):
        self.examples = examples or []  # In-context examples
        self.max_questions = max_questions
        self.model = model
        self.client = client

    def ask_llm(self, prompt):
        """
        Queries the LLM and returns the model's response.
        """
        messages = [
            {"role": "system", "content": "You are an AI assistant designed to generate clarifying questions based on in-context examples."},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            n=1,
            temperature=0,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()

    def run(self, question_id, query):
        """
        Generates follow-up questions based on the provided examples.
        """
        example_text = "\n".join(
            f"Example {i+1}: {example['question']}\nFollow-up Questions:\n" + "\n".join(f"  - {q}" for q in example["follow_up"])
            for i, example in enumerate(self.examples)
        )
        
        initial_prompt = (
            f"Here is a query: '{query}'. Based on the examples below, generate a list of specific clarifying questions for the provided query. Only return a list of the 3 most relevant follow up questions. \n"
            f"Here are some examples:\n{example_text}\n\n"
        )
        
        response = self.ask_llm(initial_prompt)
        # Extracting the follow-up questions

        # Use regex to find questions in the response
        follow_up_questions = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|\n$)', response.strip())

        # Concatenating the questions into one string
        questions_concatenated = " ".join(follow_up_questions)

        self.dump_to_json(question_id, query, questions_concatenated)
        #print("\nGenerated Queries:")
        #print(response)
    
    def all_longmem_questions(n, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        indexes = range(len(data))
        questions = {}
        for index in indexes:
            questions[data[index]['question_id']] = append(data[index]['question'])

        return questions
    
    def sample_longmem_questions(n, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        indexes = np.random.randint(0,len(data), size=n)
        questions = []
        for index in indexes:
            questions.append(data[index]['question'])

        return questions
    
    def dump_to_json(self, question_id, question, response):
        structured_response = {'question_id': question_id, 'question': question, 'follow_up': response}

        with open("generated_follow_ups.jsonl", 'a') as f:
            json.dump(structured_response, f)
            f.write("\n")
            #print("Dumped to generated_follow_ups.jsonl")

def testing_assistant():
    my_test_queries = [
        "When was the last time I ordered Pizza from Dominos?", 
        "How long will it take me to drive to San Francisco if I leave at 3PM?", 
        "What did I ask you to do the last time we talked about my project?",
        "What was the conclusion from our previous discussion about my research goals?", 
        "Can you list the decisions made in the last two planning sessions for my research project?", 
        "Has there been any updates for the weather forecast tomorrow?",
        "What is the most recent development in my project involving LLM research?", 
        "Can you update me on the current traffic conditions for my commute?", 
        "What was my NLP research meeting about earlier today?", 
        "Could you list all the important deadlines I have coming up this week?"
    ]

    n = 3
    sample = np.random.choice(np.arange(0, len(test_queries)), size=n, replace=False)
    for index in sample:
        user_query = index['question']
        id = index['question_id']
        assistant.run(id, user_query)
        


if __name__ == "__main__":

    #make this faster by just adding the lists
    all_examples = information_extraction + multi_session_reasoning + temporal_reasoning + knowledge_update
    #user_query = input("Enter your query: ")
    file_path = "data/longmemeval_m.json"
    

    # ========== MULTI QUERY TEST =============
    
    # Pulling test queries 
    #test_queries = sample_longmem_questions(3, file_path)
    #print(test_queries)
    assistant = QueryAssistant(examples=all_examples)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

        i = 1
        n = len(data)
        for item in data:
            user_query = item['question']
            id = item['question_id']
            assistant.run(id, user_query)
            print(f"{i} of {n} complete")
            i+=1
    print("All follow up questions generated and dumped to generated_follow_ups.jsonl")
    #====== SINGLE QUERY TEST ========

    #user_query = "What classes am I taking right now?"         
    #print(user_query)
    #assistant = QueryAssistant(examples=all_examples)
    #assistant.run(user_query)