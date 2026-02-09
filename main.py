import os
import argparse
from dotenv import load_dotenv
from prompts import system_prompt
from google import genai
from google.genai import types
from functions.call_function import call_function, available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key missing")
client = genai.Client(api_key = api_key)
parser = argparse.ArgumentParser(description="AIAgent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
message = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0)
            )
if message.usage_metadata == None:
    raise RuntimeError("Metadata is not available")
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {message.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {message.usage_metadata.candidates_token_count}")
function_results= []
if message.function_calls != None:
    for function_call in message.function_calls:
        function_call_result = call_function(function_call)
        if len(function_call_result.parts) == 0:
            raise Exception("Function call list is empty")
        if not function_call_result.parts[0].function_response:
            raise Exception("FunctionResponse is None")
        if not function_call_result.parts[0].function_response.response:
            raise Exception("FunctionResponse.response is None")
        function_results += function_call_result.parts[0]
        print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(message.text)