import gradio as gr

# Simple chatbot function
def farming_chatbot(user_input):
    responses = {
        "hello": "Hi! I am your AI Farming Assistant. Ask me about crops, weather, or farming tips!",
        "how to grow wheat": "To grow wheat, you need well-drained soil, adequate sunlight, and sow seeds in cool weather.",
        "best fertilizer": "Urea and DAP are common fertilizers, but the choice depends on soil testing."
    }
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don’t know that yet. I am still learning!")

# Gradio interface
demo = gr.Interface(fn=farming_chatbot,
                    inputs="text",
                    outputs="text",
                    title="AI Farming Chatbot",
                    description="Ask me farming questions!")

if __name__ == "__main__":
    demo.launch()
