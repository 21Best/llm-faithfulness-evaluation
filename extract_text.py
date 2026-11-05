import pymupdf

with pymupdf.open("attention-is-all-you-need.pdf") as pdf:
    needed_pages = pdf.pages(1,6)
    for index, page in enumerate(needed_pages, start = 2):
        text = page.get_text()
        with open ("extracted_text","a", encoding="utf-8") as file:
            file.write(f"============= Pages : {index} =================== \n {text}")
