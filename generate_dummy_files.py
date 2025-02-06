import os
import random
import string
from fpdf import FPDF
from docx import Document
import pandas as pd

def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=size))

def generate_txt(filename, size):
    with open(filename, "w") as f:
        f.write(generate_random_text(size))

def generate_pdf(filename, size):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    text = generate_random_text(size)
    pdf.multi_cell(190, 10, text)
    pdf.output(filename)

def generate_docx(filename, size):
    doc = Document()
    doc.add_paragraph(generate_random_text(size))
    doc.save(filename)

def generate_xlsx(filename, size):
    data = {"Column1": [generate_random_text(min(10, size)) for _ in range(min(5, size//10))]}
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def generate_files(num_files):
    os.makedirs("dummy_files", exist_ok=True)
    
    for i in range(num_files):
        size = random.randint(1024, 10240)  # 1KB - 10KB
        file_type = random.choice(["txt", "pdf", "docx", "xlsx"])
        filename = f"dummy_files/file_{i+1}.{file_type}"
        
        if file_type == "txt":
            generate_txt(filename, size)
        elif file_type == "pdf":
            generate_pdf(filename, size)
        elif file_type == "docx":
            generate_docx(filename, size)
        elif file_type == "xlsx":
            generate_xlsx(filename, size)
        
        print(f"\033[92m✅ Generated: {filename} ({size} bytes)\033[0m")

if __name__ == "__main__":
    while True:
        try:
            num_files = int(input("\033[94m📂 Enter the number of files to generate: \033[0m"))
            if num_files <= 0:
                print("\033[91m❌ Please enter a positive integer.\033[0m")
            else:
                break
        except ValueError:
            print("\033[91m⚠️ Invalid input. Please enter a valid number.\033[0m")
    
    generate_files(num_files)
    print("\033[92m🎉 File generation completed!\033[0m")
