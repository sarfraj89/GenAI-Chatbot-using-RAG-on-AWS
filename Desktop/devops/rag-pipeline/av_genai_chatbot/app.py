
import gradio as gr
from agent import get_agent_response

def create_gradio_interface():
    with gr.Blocks(title="🤖 Chatbot with Knowledge Base") as demo:
        gr.Markdown("# 🤖 Chatbot with Knowledge Base")
        
        history = gr.Chatbot(
            elem_id="chatbot",
            label="Chat",
            show_label=False,
            height=500,
            scale=1,
            type='messages'
        )
        
        msg = gr.Textbox(
            label="Message",
            placeholder="Ask me anything...",
            show_label=False,
            container=False,
            scale=7
        )
        
        css = """
        #chatbot {
            height: 500px;
        }
        .gradio-container {
            max-width: 900px;
            margin: auto;
        }
        """
        demo.css = css
        
        with gr.Row():
            submit_btn = gr.Button("Send", variant="primary", scale=1)
            gr.ClearButton([msg, history], value="Clear Chat", scale=1)
        
        def user_submit(message, history):
            if not message:
                return "", history
            
            history = history + [{"role": "user", "content": message}]
            return "", history
        
        async def call_agent(history):
            if not history or history[-1]["role"] != "user":
                return history
            
            user_message, chat_history = history[-1]["content"], history[:-1]
            response = await get_agent_response(user_message, chat_history)
            
            history.append({"role": "assistant", "content": response})
            return history

        submit_btn.click(user_submit, [msg, history], [msg, history]).then(
            call_agent, history, history
        )
    return demo

if __name__ == "__main__":
    app = create_gradio_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=8080,
        share=False,
    )