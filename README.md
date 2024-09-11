<h1>PDF Merger Application</h1>

  <p>This is a Python-based application that merges multiple PDF files into a single PDF using the PyMuPDF (fitz) library.</p>

  <h2>Features</h2>
  <ul>
      <li>Merges multiple PDF files into one.</li>
      <li>Outputs the merged PDF to a specified file path.</li>
      <li>Handles file existence checks and provides error messages if any input files are missing.</li>
  </ul>

  <h2>Requirements</h2>
  <p>Before running the script, make sure to install the following dependency:</p>
  <pre><code>pip install pymupdf</code></pre>

  <h2>How to Use</h2>
  <ol>
      <li>Prepare a list of PDF file paths to merge. Example paths are provided in the script.</li>
      <li>Set the output file path where you want the merged PDF to be saved.</li>
  </ol>
  <p>Example:</p>
  <pre><code>pdf_files_to_merge = [
  r'C:\Users\Mohammad\Desktop\My_Folder\pdf_one.pdf',
  r'C:\Users\Mohammad\Desktop\My_Folder\pdf_two.pdf',
  r'C:\Users\Mohammad\Desktop\My_Folder\pdf_three.pdf',
  r'C:\Users\Mohammad\Desktop\My_Folder\pdf_four.pdf'
]

output_file_path = r'C:\Users\Mohammad\Desktop\My_Folder\output.pdf'
</code></pre>

  <p>3. Run the script:</p>
  <pre><code>python merge_pdfs.py</code></pre>

  <h3>Error Handling</h3>
  <ul>
      <li>If a file doesn't exist, the application prints an error message.</li>
      <li>If no pages are found to merge, the application stops with an appropriate error message.</li>
  </ul>

  <h2>Output</h2>
  <p>The merged PDF will be saved at the location specified in the <code>output_file_path</code> variable.</p>
