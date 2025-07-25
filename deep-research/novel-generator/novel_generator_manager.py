from agents import Runner, trace, gen_trace_id
from user_input import get_user_inputs
import asyncio

class NovelGeneratorManager:

  async def run(self):
    """ Run the deep research process, yielding the status updates and the final novel manuscript"""
    generate_novel_trace_id = gen_trace_id()
    with trace("Generate Novel trace", trace_id=generate_novel_trace_id):
        print(f"\nView trace: https://platform.openai.com/traces/trace?trace_id={generate_novel_trace_id}\n")
        print("Starting novel generation\n")
        novel_parameters = await self.get_user_parameters()        
        print("\nAwesome, now we'll generate your novel!\n")

  async def get_user_parameters(self):
    """Prompt the user for various novel parameters"""
    print("Getting user inputs\n");
    get_user_inputs()
