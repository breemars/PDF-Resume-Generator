# PDF Resume Generator

This is a Python-based PDF resume generator that converts HTML/CSS into a PDF document using Playwright and Chromium.

The resume layout, styling, colors, icons, and visual elements are created in HTML/CSS, while Python handles the PDF generation process.


## 🛠️ Technologies & Tools

* **Python** — PDF generation script
* **Playwright** — Python package used for the HTML-to-PDF generation
* **Chromium** — Renders the HTML/CSS for PDF generation
* **HTML5** — Resume structure and content
* **CSS3** — Resume layout and styling
* **Lucide** — SVG icons


## 💻 Running Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install Playwright and Chromium

```bash
pip install playwright
playwright install chromium
```

### 3. Create your index.html file

Create your own resume format using HTML and CSS and save it as index.html in the same folder as the Python script

### 4. Generate the PDF

Run the Python script:

```bash
python Generate_PDF_Resume.py
```

The script will read index.html and generate resume.pdf

## 📄 Output

The Python script generates the PDF with the following specifications:

* US Letter page size
* Zero PDF margins — Allows the HTML/CSS to control the resume's margins
* Printed backgrounds enabled — Ensures background colors and images defined in the HTML/CSS are included in the generated PDF

All other design choices will be left up to the HTML and CSS.

## 📚 Project Background

I wanted to challenge myself by creating my resume entirely with code rather than using a document editor. I was surprised by how well it turned out, and I actually found it easier to control formatting and spacing with HTML and CSS. Because of that, I plan to continue editing and generating my resume this way in the future.