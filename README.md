# Dummy File Generator

## 📌 Overview
This Python script generates random dummy files of various formats (`txt`, `pdf`, `docx`, `xlsx`). The file sizes range between **1KB to 10KB**, containing random text. The script allows users to specify the number of files to generate.

## 🛠️ Features
- Generates **random file types**: `.txt`, `.pdf`, `.docx`, `.xlsx`
- File content is filled with **random characters**
- File size varies between **1KB and 10KB**
- **User input friendly** with **emoji-enhanced CLI**
- **Simple and lightweight**, easy to run on any machine
- Automatically creates an output folder (`dummy_files/`) if it doesn’t exist

## 📦 Dependencies
Ensure you have the required libraries installed before running the script:
```bash
pip install fpdf python-docx pandas openpyxl
```

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/elsavation/dummy-file-generator.git
   cd dummy-file-generator
   ```
2. Run the script and enter the desired number of dummy files:
   ```bash
   python generate_dummy_files.py
   ```
   You'll be prompted to enter the number of files to generate.
3. The generated files will be saved in the `dummy_files/` directory.

## 📂 Output
Each file type is created with random content:
- **TXT**: Plain text file filled with random characters
- **PDF**: A PDF document with multi-line text
- **DOCX**: A Microsoft Word document with a paragraph of text
- **XLSX**: An Excel spreadsheet with random values

## 🔍 Example Output
Example console output when running the script:
```bash
📂 Enter the number of files to generate: 5
✅ Generated: dummy_files/file_1.txt (2048 bytes)
✅ Generated: dummy_files/file_2.pdf (3072 bytes)
✅ Generated: dummy_files/file_3.docx (1024 bytes)
✅ Generated: dummy_files/file_4.xlsx (5120 bytes)
✅ Generated: dummy_files/file_5.txt (8192 bytes)
🎉 File generation completed!
```

## 📝 Customization
- Modify the file size range by changing this line in the script:
  ```python
  size = random.randint(1024, 10240)  # 1KB - 10KB
  ```
- Change the output directory by modifying:
  ```python
  os.makedirs("dummy_files", exist_ok=True)
  ```

## 🤖 Automation
To generate files automatically without user input, modify the script to accept arguments:
```bash
python generate_dummy_files.py --count 10
```
For any questions or feedback, reach out via email: **your.email@example.com**

