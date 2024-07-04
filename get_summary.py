


def get_call_summary(transcription):


    import pydantic
    from langchain.llms import Ollama

    ollama = Ollama(base_url="http://localhost:11434", model="llama2")

    PROMPT = """

    ROLE: 
    You are a customer service professional. You are very competent and able to extract meaningful insights from transcripts of
    customer calls that are submitted to you

    INSTRUCTION:
    Respond to the following command:
    "Provide a short summary of the call and list any outstanding action items after the summary. Finally provide the main topic 
    and the caller's contact informattion. Do not include a preamble"

    FORMAT:
    SUMMARY: a one sentence summary
    TOPIC: main topic of the call. 1 to 3 words
    ACTION ITEMS:
    a bulleted list of sufficiently detailed action items
    CONTACT INFORMATION:
    Name: first name, last name
    Phone Number: the callers phone number

    """.strip()


    CONTEXT = transcription

    full_prompt = f"{PROMPT}\n\n{CONTEXT}"

    
    # Generate the response using the Ollama model
    response = ollama(full_prompt)

    return response





