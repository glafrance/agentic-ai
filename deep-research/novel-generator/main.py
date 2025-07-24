from agents import Agent, WebSearchTool, trace, Runner, gen_trace_id, function_tool
from agents.model_settings import ModelSettings
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import asyncio
import os
from typing import Dict
from IPython.display import display, Markdown

load_dotenv(override=True)

INSTRUCTIONS = "You are a fiction author assistant. You will use user-provided parameters, \
or default parameters, to generate a creative and engaging novel. \
Do not perform web searches. Focus entirely on imaginative, coherent, and emotionally engaging content. \
Your output should read like a real novel, vivid, descriptive, and character-driven. \
After generating the novel, you will hand it off to another agent that will review the \
generated novel and offer suggestions. You can decide whether to make changes based on each \
suggestion, in producing the final output."

search_agent = Agent(
    name="Novel Generator Agent",
    instructions=INSTRUCTIONS,
    tools=[],  # No WebSearchTool
    model="gpt-4o-mini",
    model_settings=ModelSettings(),  # No tool_choice needed
)

def prompt_with_default(prompt_text, default_value=None, cast_type=str):
    user_input = input(f"{prompt_text} ")
    if user_input.strip() == "":
        return default_value
    try:
        return cast_type(user_input)
    except ValueError:
        print(f"Invalid input. Using default: {default_value}")
        return default_value

def get_user_inputs():
    # 1. Novel genre
    genre = prompt_with_default("Novel genre (press Enter for default - teen mystery):", "teen mystery")

    # 2. Title
    title = input("\nTitle (Enter for auto-generated title): ").strip()
    if not title:
        title = "Auto-Generated Title"

    # 3. Number of pages
    num_pages = prompt_with_default("\nNumber of pages in novel (Enter for default - 90 pages):", 90, int)

    # 4. Number of chapters
    num_chapters = prompt_with_default("\nNumber of chapters (Enter for default - 15):", 15, int)

    # 5. General plot
    plot = input("\nGeneral plot (Enter for auto-generated plot): ").strip()
    if not plot:
        plot = "Auto-Generated Plot"

    # 6. Max AI tokens
    while True:
        max_tokens_input = input(
            "\nMaximum AI tokens to use, after which novel \n"
            "generation will fail (about 200,000 tokens for 90): "
        ).strip()
        try:
            max_tokens = int(max_tokens_input)
            if max_tokens <= 0:
                print("Please enter a positive integer.")
                continue

            if max_tokens > 300000:
                print(f"\n⚠️  You entered {max_tokens:,} tokens, which is quite high and may be expensive.")
                confirm = input("Are you sure you want to use this value? (Yes or No): ").strip().lower()
                if confirm != "yes":
                    print("Okay, let's try again.\n")
                    continue  # Ask again

            break  # Valid and confirmed
        except ValueError:
            print("Please enter a valid integer.")

        # 7. Perform AI review
    while True:
        review_input = input("\nPerform AI review and revision? Consumes 2 - 4x tokens (Yes or No): ").strip().lower()
        if review_input in {"yes", "y"}:
            perform_review = True
            break
        elif review_input in {"no", "n"}:
            perform_review = False
            break
        else:
            print("Please enter Yes, No, Y, or N.")

    return genre, title, num_pages, num_chapters, plot, max_tokens, perform_review

if __name__ == "__main__":
    genre, title, num_pages, num_chapters, plot, max_tokens, perform_review = get_user_inputs()

    # Print collected inputs for confirmation (optional)
    print("\nCOLLECTED NOVEL CONFIGURATION:\n")
    print(f"Genre: {genre}")
    print(f"Title: {title}")
    print(f"Pages: {num_pages}")
    print(f"Chapters: {num_chapters}")
    print(f"Plot: {plot}")
    print(f"Max Tokens: {max_tokens}")
    print(f"AI Review/Revision: {'Yes' if perform_review else 'No'}")

    print("\nAwesome, now we'll generate your novel!")
