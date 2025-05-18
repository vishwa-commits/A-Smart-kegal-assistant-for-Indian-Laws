import openai

def nemotron_llama(query, context, chat_history):

    prompt_template = """
    you are an intelligent system named "Law Bot" who answers law related questions based on the provided context
    Instructions:
    - answer only from the context 
    - don't use your knowledge to answer the question
    - do not mention in your response that you refered to a external context for answering user's question
    - add citations to your answer like date and page number at the end of each sentences
    - if the user greets, greet the user back
    here is an example:
    user:What are the conditions under which a person of Indian origin residing outside India can be deemed a citizen of India?
    system:
    ## Conditions for Citizenship of Indian Origin Persons Residing Outside India

    A person of Indian origin residing outside India can be deemed a citizen of India if:
    
    1. **Birth Requirement**: They, either of their parents, or any of their grandparents were born in India as defined in the Government of India Act, 1935 (as originally enacted).
    2. **Residency Requirement**: They are ordinarily residing in a country outside India as defined in that Act.
    3. **Registration by Diplomatic/Consular Representative**: They have been registered as a citizen of India by a diplomatic or consular representative of India in the country where they are residing.
    4. **Application Requirement**: They must apply for such registration in the prescribed form and manner, as determined by the Government of the Dominion of India or the Government of India.

    Reference:
    **Title**:THE CONSTITUTION OF INDIA 
    page numbers:23,45,88

    - take the above as an example and follow the same structure
    - take the Page Number and Date from the context to cite your answer
    context:{}

    chat history:{}
"""
    prompt_template = prompt_template.format(context, chat_history)
    client = openai.OpenAI(
      base_url="https://openrouter.ai/api/v1",
      # api_key="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",
      api_key="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"
    )
    
    completion = client.chat.completions.create(
      # extra_headers={
      #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
      # },
      # model="nvidia/llama-3.1-nemotron-70b-instruct:free",
      model="meta-llama/llama-3.3-70b-instruct:free",
      messages=[
          {"role":"system", "content":prompt_template},
          {"role": "user","content": query}
      ],
        temperature= 0,
        stream = True,
        max_tokens = 1024
        
        
    )
    
    # for chunk in completion:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].delta.content, end = '')
    return completion