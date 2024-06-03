# Job Search using AI 

Objective
Develop an AI-powered tool to identify ideal investment firms for job applications using a comprehensive dataset and LLM capabilities. The project aims to:

Identify investment firms that match your ideal job criteria.
Showcase your ability to leverage AI and Python in practical applications.
Core Components
Data Acquisition and Preprocessing

Source: ESMA's register of management companies, investment firms, and related entities.
Format: CSV containing 19,000 records with columns such as entity name, member state, competent authority, type of entity, etc.
Web Scraping and Information Retrieval

Task: Extract detailed information about each firm from the internet.
Technologies:
LLM APIs (e.g., OpenAI GPT-4) for web browsing and data extraction.
Python libraries for web scraping (e.g., BeautifulSoup, Scrapy).
Criteria Matching

Task: Compare extracted firm characteristics to your ideal job criteria.
Technologies:
Natural Language Processing (NLP) for text analysis and comparison.
Python libraries for data manipulation (e.g., Pandas).
Results Compilation

Task: Generate a list of firms that match your criteria.
Technologies:
Python for data aggregation and result formatting.
Jupyter notebooks for interactive data analysis and visualization.
Project Documentation and Showcase

Task: Document the project process and results.
Technologies:
GitHub for version control and project showcase.
Markdown for documentation.
Detailed Steps
1. Data Acquisition and Preprocessing
Download the ESMA register CSV file.
Load the CSV file into a Pandas DataFrame.
Clean the data: Handle missing values, standardize text, and filter relevant columns.
2. Web Scraping and Information Retrieval
Set up LLM API: Use OpenAI's GPT-4 for web browsing capabilities.
Create web scraping functions:
Input: Firm name and website (if available).
Process: Use LLM to search the internet for relevant information.
Output: Extracted data points such as AUM, investment products, location, and quant solutions.
Store the extracted data in a structured format (e.g., another DataFrame or database).
3. Criteria Matching
Define your ideal company criteria in a document (e.g., preferred AUM range, types of investment products, location preferences, etc.).
Develop a matching algorithm:
Input: Extracted data and ideal criteria.
Process: Compare firm characteristics to the criteria using NLP techniques.
Output: A list of firms ranked by how well they match your criteria.
4. Results Compilation
Aggregate matching results: Create a comprehensive list of firms with relevant details.
Visualize the data: Use Jupyter notebooks to create charts and summaries of the matching firms.
5. Project Documentation and Showcase
Document each step of the project in Markdown files.
Upload the project to GitHub: Ensure all code, data, and documentation are well-organized and accessible.
Create a README file: Summarize the project’s purpose, methodology, and results.
Additional Elements and Technologies
Data Acquisition and Preprocessing

Technologies: Use SQL databases for efficient data handling if the dataset grows.
Additional Elements: Implement data validation checks to ensure data integrity.
Web Scraping and Information Retrieval

Technologies: Selenium for more complex web interactions if needed.
Additional Elements: Implement rate limiting and error handling to manage API usage and prevent IP bans.
Criteria Matching

Technologies: Scikit-learn for advanced data analysis and matching algorithms.
Additional Elements: Use machine learning to refine the matching criteria based on initial results.
Results Compilation

Technologies: Plotly or Matplotlib for advanced visualizations.
Additional Elements: Create an interactive dashboard (e.g., using Dash) to explore matching firms dynamically.
Project Documentation and Showcase

Technologies: GitHub Pages to create a project website for better presentation.
Additional Elements: Include a detailed project timeline and future work section to highlight ongoing improvements and iterations.
Implementation Strategy
Phase 1: Initial Setup and Data Preparation
Load and preprocess the ESMA register CSV file.
Define your ideal company criteria.
Phase 2: Web Scraping Development
Set up LLM API for web browsing.
Develop and test web scraping functions.
Phase 3: Criteria Matching Algorithm
Create a document outlining your ideal company criteria.
Develop and test the matching algorithm.
Phase 4: Results Compilation and Visualization
Aggregate and visualize the matching results.
Create interactive data analysis tools.
Phase 5: Documentation and Project Showcase
Document the entire project process.
Upload the project to GitHub and create a comprehensive README file.