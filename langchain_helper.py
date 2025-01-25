from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_groq import ChatGroq

# Set up the Hugging Face LLM
llm = ChatGroq(
    temperature=0.7,
    groq_api_key='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',
    model_name="llama-3.3-70b-versatile",
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Generate Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Suggest Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return them as a comma-separated string."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine Chains Sequentially
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', "menu_items"]
    )

    # Execute the chain with the provided cuisine
    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    try:
        # Example usage
        result = generate_restaurant_name_and_items("Italian")
        print("Restaurant Name:", result['restaurant_name'])
        print("Menu Items:", result['menu_items'])
    except Exception as e:
        print("Error:", e)
