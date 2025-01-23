
MCQ Generator from PDF using OpenAI and LangChain
This project is designed to generate multiple-choice questions (MCQs) from a provided PDF document. By leveraging OpenAI's language models in conjunction with the LangChain framework, the application processes the text content of the PDF to create relevant and contextually accurate MCQs.

Features
PDF Text Extraction: Utilizes PyMuPDF to extract text content from PDF files.
MCQ Generation: Employs OpenAI's language models to formulate multiple-choice questions based on the extracted text.
Streamlit Interface: Provides an interactive web interface using Streamlit for users to upload PDFs and receive generated MCQs.
Installation
Clone the Repository:

bash

git clone https://github.com/UniteUniverse/Project-1.git
cd Project-1
Install Dependencies:

Ensure you have Python installed. Then, install the required packages:

bash

pip install -r requirement.txt
Usage
Run the Streamlit Application:

bash

streamlit run StreamlitAPP.py
Upload PDF:

Access the local Streamlit interface (typically at http://localhost:8501).
Upload your desired PDF file through the interface.
Generate MCQs:

After uploading, the application will process the PDF and display the generated MCQs.
Project Structure
StreamlitAPP.py: Main application file containing the Streamlit interface and logic.
src/: Directory containing the core modules for PDF processing and MCQ generation.
requirement.txt: Lists all the dependencies required for the project.
setup.py: Script for packaging the project.
.gitignore: Specifies files and directories to be ignored by Git.
Dependencies
openai: Interface to OpenAI's language models.
langchain: Framework for building applications with language models.
streamlit: Library for creating interactive web applications.
PyMuPDF: Library for PDF text extraction.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Special thanks to the contributors of the open-source libraries utilized in this project.

Note: Ensure you have an active OpenAI API key and the necessary permissions to use the provided PDF content.
