# main.py  
import sys  
from aetherion import AetherionAgent  

if __name__ == "__main__":  
    agent = AetherionAgent()  
    agent.activate_modules()  # Initialize all modules for the agent  
    print("Aetherion Agent Initialized. Ready to process your instructions.")  

    while True:  
        user_input = input("\nEnter your instruction (or 'exit' to quit): ")  
        if user_input.lower() == "exit":  
            break  
        response = agent.process_instruction(user_input)  
        print(f"\nAetherion Agent Response: {response}")
