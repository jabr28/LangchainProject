from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchainproject!")
    information = """
    Lionel Andrés "Leo" Messi (born 24 June 1987) is an Argentine professional footballer who plays as a forward for and captains both Major League Soccer club Inter Miami and the Argentina national team. Widely regarded as one of the greatest players in history, Messi has set numerous records for individual accolades won throughout his professional footballing career, including eight Ballon d'Ors, six European Golden Shoes, and eight times being named the world's best player by FIFA.[note 2] In 2025, he was named the All Time Men's World Best Player by the IFFHS. He is the most decorated player in the history of professional football, having won 46 team trophies.[note 3] Messi's records include most goals in a calendar year (91), most goals for a single club (672 for Barcelona), most goals in La Liga (474), most assists in international football (61), most goal contributions in the FIFA World Cup (21), and most goal contributions in the Copa América (32). A prolific goalscorer and creative playmaker, Messi has scored over 890 senior career goals and provided over 400 assists for club and country—the most of any player—resulting in over 1,300 goal contributions, the highest total in the sport's history.[25]
    Born and raised in Rosario, Messi moved to Spain at age 13 to join FC Barcelona, for whom he made his competitive debut aged 17 in October 2004. He established himself as an integral player for the club within the next three years, and in his first decade with Barcelona, he won four UEFA Champions League titles and ten La Liga titles. He also won a record six Ballon d'Or awards during his time at Barcelona. In August 2021, Messi signed for Paris Saint-Germain (PSG) after leaving Barcelona due to financial issues. He won Ligue 1 in his first season with PSG. In July 2023, he joined Inter Miami in Major League Soccer. 
"""
    summery_template = """
    given the information {information} about a person i want you to cearte:
    1. a short summery about the person in 3 sentences.
    2. a list of 5 interesting facts about the person.

"""

    summery_promot_template= PromptTemplate(
        input_variables=["information"],
        template=summery_template
    )

    llm = ChatOpenAI(model="gpt-4", temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0, base_url="http://127.0.0.1:11434")
    chain = summery_promot_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
