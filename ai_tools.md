**Which AI tools did you try?**
**GitHub Copilot and ChatGPT.**

**What worked well? What didn’t?**
| Chatbot | What Worked Well | What didn't Work Well |
| --- | -- | -- |
| GitHub Copilot | Was able to address the issue directly since it was able to understand the context by reading the rest of the code block and files. For example, a 'no such file directory' error for a linear regression Jupyter notebook was resolved easily since GitHub Copilot was able to trace back the specific directory of the file | Using the Agent mode causes longer debugging durations because the code generated was not done step-by-step by my own thought process, which makes it harder to spot coding errors |
| ChatGPT | Was able to solve low-level coding issues such as assembly coding despite the limited online resources on it | The model version downgrades from GPT 5 to 4.1 on the free version once the number of prompt limits were hit | 

**When do you think AI is most useful for coding?**
- AI is effective when I am using it for **writing pseudocode for code suggestion**, which I can test the independent code blocks before proceeding to write the rest of the code. Copying entire code blocks from AI causes longer periods of debugging. 

- AI is effective when I **understand the theoretical concepts of coding**. For example, in Object Oriented Programming, prompting AI to create a Splashkit space shooter program using specific design patterns provides feedback and code blocks relevant to the project context.

- AI is effective when including the **entire context of the functional and non-functional requirements**. For example, I prompt AI 'I would like to create an ETL pipeline of stock financial data. I would like to have the raw data scrapped from yfinance aggregated and transformed into the pipeline. Assume I only want financial data from the last 5 years.