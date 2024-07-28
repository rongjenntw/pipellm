import requests, json, sys, os
pipellm_installation = """
    **pipellm requirements not met:
    1. download and install Ollama in ollama.com
    2. set environment variable PIPELLM_CONFIG=[path to pipellm.config]
    3. run ollama pull llama3.1 (or [llm_model] in pipellm.config)
    **compile pipellm:
    1. install python 3
    2. in pipellm directory run pip install -r requirements.txt
    3. run pyinstaller --onefile pipellm.py
    4. executable file can be found in dist directory
"""
pipellm_instruction = """
    **Usage: 
    pipellm [PROMPT] or echo [CONTEXT] | pipellm [PROMPT | keyword in pipellm.json]
    **Examples:
    pipellm "What is pipellm?"\n
    echo "I am a 5 year old boy." | pipellm "What is universe?"\n
    cat badcode.py | pipellm reviewcode\n
    cat newsarticle.txt | pipellm 5facts\n
    cat stringtheory.txt | pipellm quiz
"""
with open(os.getenv('PIPELLM_CONFIG') or 'pipellm.json', 'r') as file:
    config = json.load(file)

def generate(prompt, context, model=config.get('llm_model')):
    url = config.get('llm_url')
    data = {"model": model, "prompt": prompt, "stream": False, "system": context}
    response = requests.post(url, json=data)
    return json.loads(response.text)['response']

def main():
    sys.stdout.reconfigure(encoding='utf-8')  # Set encoding to UTF-8
    
    pipein = ""
    if not sys.stdin.isatty():
        for line in sys.stdin:
            pipein += line.strip()
    
    if len(pipein)>0:
        context = pipein
    else:
        context = config.get('pipes').get('default').get('context')
    
    if (len(sys.argv)<2):
        context = pipellm_instruction
        prompt = "I am new to pipellm."
    else:
        if(config.get('pipes').get(sys.argv[1])):
            prompt = config.get('pipes').get(sys.argv[1]).get('prompt')
        else:
            prompt = sys.argv[1]
    try:
        print(generate(prompt, context))
    except Exception as e:
        print(pipellm_installation)

if __name__ == "__main__":
    main()