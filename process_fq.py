import json
import re

# Define input and output file paths
input_file = "s_generated_follow_ups.jsonl"
output_file = "processed_s_follow_ups.jsonl"

# Process each line and write to a new JSONL file
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile):
        #if i == 4:  # Limit to processing 4 entries
        #    break
        
        data = json.loads(line.strip())  # Load each line as a JSON object
        
        if "question_id" in data and "question" in data and "follow_up" in data:
            follow_up_questions = [q.strip() for q in re.split(r"(?<=[?!.])\s+", data["follow_up"]) if q]
            
            output_data = {
                "question_id": data["question_id"],
                "question": data["question"],
                "follow_up_questions": follow_up_questions
            }
            
            outfile.write(json.dumps(output_data) + "\n")

print(f"Processed data has been saved to {output_file}")