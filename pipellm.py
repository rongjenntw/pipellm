import requests, json, sys, os

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
    
    if(config.get('pipes').get(sys.argv[1])):
        prompt = config.get('pipes').get(sys.argv[1]).get('prompt')
    else:
        prompt = sys.argv[1]

    print(generate(prompt, context))

if __name__ == "__main__":
    main()