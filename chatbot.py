# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "help" in user_input:
        return "Sure! I can help you. You can upload your text or PDF, choose a voice style, and generate your audiobook."

    elif "upload" in user_input:
        return "To upload your file, scroll up and use the 'Upload Text or PDF' section."

    elif "voice" in user_input:
        return "You can choose from various voices like male, female, or custom AI voices. Select from the dropdown list."

    elif "generate" in user_input:
        return "Once your text is ready and voice is selected, click on 'Generate Audiobook' to start the process."

    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Let me know if you need anything else."

    else:
        return "I'm not sure how to respond to that. Try asking about uploading, voices, or generating the audiobook."
