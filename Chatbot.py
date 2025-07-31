import google.generativeai as genai

API_KEY = "AIzaSyDrwWW5RU91oXTTDnf5KHBzc8sAPR2JSZE"
genai.configure(api_key=API_KEY)

gemini_model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction="You are a helpful assistant. Keep answers less than 10-15 words."
)

gemini_chat = gemini_model.start_chat(history=[])

def gimini(text_input):
    try:
        response = gemini_chat.send_message(text_input)
        response_text = response.text.strip()
        print("Gemini:", response_text)
        return response_text  # ✅ Return response to Flask
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            response_text = "Daily limit reached. Try tomorrow or upgrade plan."
        else:
            response_text = "Sorry, something went wrong with Gemini."
        
        print("Gemini Error:", error_msg)
        return response_text  # ✅ Return error message
