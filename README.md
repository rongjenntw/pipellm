# Pipe LLM
pipe the output of an LLM to another LLM as input. This is a way to chain together multiple LLMs in sequence, where each one takes as input the output from its predecessor. This can be used for complex tasks that involve several steps or stages.

# Usage
C:\\> cat example.txt | pipellm summary | pipellm 5facts

# Configure
you can add your prompts in pipellm.json
