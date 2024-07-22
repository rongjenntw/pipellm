# Pipe LLM
pipe the output of an LLM to another LLM as input. This is a way to chain together multiple LLMs in sequence, where each one takes as input the output from its predecessor. This can be used for complex tasks that involve several steps or stages.

# Usage
C:\\> cat example.txt | pipellm summary | pipellm 5facts

# Configure
this requires ollama installed 
modify pipellm.json
1. "llm_url": your ollama host url
2. "llm_model": your ollama model
3. you can add your prompts in pipellm.json
