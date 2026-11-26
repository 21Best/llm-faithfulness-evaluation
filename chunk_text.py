import pymupdf
import json

pages = []
full_text = " "
sections = []


with pymupdf.open("attention-is-all-you-need.pdf") as pdf:
    
    needed_page = pdf.pages(0,6)
    for index, page in enumerate(needed_page, start = 1):
        text = page.get_text()
        page_data = {
            "page":index,
             "content":text
             }
        
        pages.append(page_data)

    for item in pages:
        full_text = full_text + item["content"]
    
    headings = [
        "1\nIntroduction",
        "2\nBackground",
        "3\nModel Architecture",
        "3.1\nEncoder and Decoder Stacks",
        "3.2\nAttention",
        "3.2.1\nScaled Dot-Product Attention",
        "3.2.2\nMulti-Head Attention",
        "3.2.3\nApplications of Attention in our Model",
        "3.3\nPosition-wise Feed-Forward Networks",
        "3.4\nEmbeddings and Softmax",
        "3.5\nPositional Encoding"
        ]


    for index, heading in enumerate(headings[:-1]):
        start = full_text.find(headings[index])
        end = full_text.find(headings[index + 1])
        section_text = full_text [start : end]

        section = {
            "Heading: " : heading,
            "Content: " : section_text
        }

        sections.append(section)
        


    with open ("chunks.json", "w", encoding="utf-8") as file:
        json.dump(sections,file, indent=4)
    


    

    
