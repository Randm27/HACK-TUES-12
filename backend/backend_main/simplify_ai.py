from transformers import pipeline

simplifier = pipeline("text-generation", model="google/flan-t5-small")

def simplify_text(text):
    # Конкретен, силен prompt
    prompt = (
        f"Rewrite the following text in simple English, using short sentences and easy words:\n{text}"
    )
    result = simplifier(prompt, max_length=200, do_sample=False)
    return result[0]['generated_text']

text = ("Artificial intelligence is a branch of computer science that aims to create "
        "machines capable of performing tasks that normally require human intelligence. "
        "These tasks include learning from experience, understanding natural language, "
        "recognizing patterns, solving complex problems, and making decisions.")

simplified = simplify_text(text)
print(simplified)