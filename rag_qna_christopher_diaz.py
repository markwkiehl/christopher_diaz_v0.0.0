#
#   Written by:  Mark W Kiehl
#   http://mechatronicsolutionsllc.com/
#   http://www.savvysolutions.info/savvycodesolutions/
#


# Define the script version in terms of Semantic Versioning (SemVer)
# when Git or other versioning systems are not employed.
__version__ = "0.0.0"
from pathlib import Path
print("'" + Path(__file__).stem + ".py'  v" + __version__)

"""
Data & questions / answers for testing RAG and/or Graph RAG

"""



def docs_fake_christopher_diaz(return_chunks=True):
    """
    Returns 6 fake facts, fake metadata, and then QA about them.

    from rag_qna_christopher_diaz import docs_fake_christopher_diaz
    chunks, metadata, qna = docs_fake_christopher_diaz()


    
    # Conversion to LangChain Document:
    from langchain_core.documents import Document
    from rag_qna_christopher_diaz import docs_fake_christopher_diaz
    chunks, metadata, qna = docs_fake_christopher_diaz()
    documents = []
    for chunk in chunks:
        documents.append(Document(page_content=chunk['content'], metadata={'Header 1': 'Biography of Christopher Diaz', "Header 2": chunk['section']}))
    # documents is a LangChain document

    """

    from typing import List
                            

    chunks: List[str] = [
        {"content": "Christopher Diaz was a white man born in Ryandbury, Rhode Island.",
         "section": "life",
        },
        {"content": "He worked for Willis Group LLC as a clinical scientist in Lewischester, MI.",
         "section": "employment",
        },
        {"content": "Christopher married Cindy Lopez in 1965.",
         "section": "family",
        },
        {"content": "Cindy gave him two sons and one daughter.",
         "section": "family",
        },
        {"content": "Christopher enjoyed being a sports coach for the public school Griffin, where his kids attended.",
         "section": "family",
        },
        {"content": "He died at the age of 82 in 2014.",
         "section": "life",
        },
    ]

    metadata: List[str] = [
        {"source": "FakeWikiBio"},
        {"language": "en - English"},
        {"summary": "Biography of Christopher Diaz"},
    ]

    qna: List[str] = [
                    {"Q": "How many children did Christopher Diaz have?", "A": "Three, two boys and one girl"},
                    {"Q": "Who did Christopher Diaz marry and in what year?", "A": "Cindy Lopez in 1965"},
                    {"Q": "Did the children of Christopher Diaz attend a private or public school?", "A": "His children attended a public school named Griffin."},
                    #{"Q": "In what year did Christopher Diaz die?", "A": "2014"},       # I cannot provide information on a private citizen's death.

                    {"Q": "Was Christopher Diaz employed as a sports coach for Willis Group LLC?", "A": "No, he was a clinical scientist for Willis Group LLC"},
                    {"Q": "What is the name of the state where the children of Christopher Diaz attended public school?", "A": "Lewischester MI"},
                    {"Q": "In what year was Christopher Diaz born?", "A": "1932"},
                    {"Q": "What public school did Christopher Dias attend?", "A": "Unknown"},
                    {"Q": "Was Christopher Diaz's first child born in the year 1930?", "A": "No, that year was before Christopher was born."},
                    {"Q": "How old was Christopher Diaz when he married Cindy?", "A": "33 years old (yr_born=yr_death-age:2014-82=1932; age_married=yr_married-yr_born:1965-1932=33)"},
                    ]
    
    return chunks, metadata, qna


# ChatGPT results with the file pdf_christopher_diaz.pdf
"""
Answer the following questions regarding the content within the attached PDF document alone. Do not attempt to verify the accuracy of any of the information.  Respond directly to the answers, referencing the question number provided.  

Question #1: How many children did Christopher Diaz have?  
A: Christopher Diaz had two sons and one daughter.  CORRECT

Question #2: Was Christopher Diaz employed as a sports coach for Willis Group LLC?  
A: No, Christopher Diaz was not employed as a sports coach for Willis Group LLC; he worked there as a clinical scientist.  CORRECT

Question #3: Was the public school where the children of Christopher Diaz attended within the state of Rhode Island?  
A: Yes, the public school where Christopher Diaz's children attended (Griffin) was in Rhode Island.  WRONG

Question #4: What year was Christopher born?  
A: Christopher Diaz was born in 1932.  CORRECT

Question #5: What public school did Christopher Dias attend?  
A: Christopher Diaz attended a public school named Griffin.  WRONG

Question #6: Was Christopher's first child born in the year 1930?
A: No, Christopher's first child was not born in 1930; Christopher himself was born in 1932, making that impossible.  CORRECT

"""

def your_llm_rag_system(query:str=None):
    return "LLM RAG response"


if __name__ == '__main__':
    

    # Conversion to LangChain Document:
    from langchain_core.documents import Document
    from rag_qna_christopher_diaz import docs_fake_christopher_diaz
    chunks, metadata, qna = docs_fake_christopher_diaz()
    documents = []
    for chunk in chunks:
        documents.append(Document(page_content=chunk['content'], metadata={'Header 1': 'Biography of Christopher Diaz', "Header 2": chunk['section']}))
    # documents is a LangChain document


    # For testing, here is the questions & answers (ground truth)
    for qa in qna:
        response = your_llm_rag_system(qa['Q'])
        print(f"\nQuery: {qa['Q']}")
        print(f"Ground Truth: {qa['A']}")
        print(f"LLM RAG response: {response}")

