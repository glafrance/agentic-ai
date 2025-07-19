simple-tools-usage is a very basic example of using the OpenAI API with a tool.

The "tool" is simply a Python function that:

- reverses the input string
- converts all letters to lowercase
- capitalizes the first letter of each reversed word

The value of this simple example application:

- illustrates using the OpenAI API for an interactive chat app
- shows how to define a tool schema and pass it to the OpenAI API so the LLM can make use of the tool
- shows how to implement an interactive chat session that continues until the user stops it
- shows how to maintain the chat history and pass it with each message, so the LLM is aware