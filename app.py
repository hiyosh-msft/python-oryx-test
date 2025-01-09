from flask import Flask, render_template_string
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    # Load the CSV data using pandas
    df = pd.read_csv('data.csv')
    
    # Use numpy to calculate the average age
    average_age = np.mean(df['age'])
    
    # Append a new row with the average age (for demonstration)
    df.loc[len(df.index)] = ['Average', average_age, '']
    
    # Convert the dataframe to an HTML table
    table_html = df.to_html(index=False)
    
    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pandas and Numpy</title>
    </head>
    <body>
        <h1>Pandas and Numpy Example</h1>
        <p><strong>Average Age:</strong> {{ average_age }}</p>
        {{ table | safe }}
    </body>
    </html>
    """
    
    return render_template_string(html_template, table=table_html, average_age=average_age)

if __name__ == '__main__':
    app.run()
