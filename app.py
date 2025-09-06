import gradio as gr
from transformers import pipeline

# Load Flan-T5 model (free on CPU tier)
chat_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

def farming_chatbot(user_input):
    prompt = f"Answer this farming question clearly and simply: {user_input}"
    result = chat_pipeline(prompt, max_length=200, do_sample=True)
    return result[0]['generated_text']

# Gradio interface
demo = gr.Interface(fn=farming_chatbot,
                    inputs="text",
                    outputs="text",
                    title="AI Farming Chatbot (Flan-T5)",
                    description="Ask farming-related questions and get AI-powered answers.")

if __name__ == "__main__":
    demo.launch()
