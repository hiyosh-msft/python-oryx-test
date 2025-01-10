from flask import Flask, render_template_string
import numpy as np

app = Flask(__name__)

# Hardcoded data (list of dictionaries)
data = [
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Alice", "age": 24, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 30, "city": "San Francisco"},
    {"name": "Eve", "age": 29, "city": "Boston"},
]

@app.route('/')
def home():
    # Extract headers and rows
    headers = data[0].keys()  # Get column names from dictionary keys
    rows = [list(item.values()) for item in data]  # Convert each dictionary to a list of values
    
    # Extract ages and calculate statistics using NumPy
    ages = [item['age'] for item in data]
    average_age = np.mean(ages)
    max_age = np.max(ages)
    min_age = np.min(ages)

    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Table with NumPy</title>
        <style>
            table {
                width: 50%;
                border-collapse: collapse;
                margin: 20px auto;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            .stats {
                text-align: center;
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align:center;">Data Table with NumPy</h1>
        <div class="stats">
            <p><strong>Average Age:</strong> {{ average_age }}</p>
            <p><strong>Max Age:</strong> {{ max_age }}</p>
            <p><strong>Min Age:</strong> {{ min_age }}</p>
        </div>
        <table>
            <thead>
                <tr>
                    {% for header in headers %}
                        <th>{{ header }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in rows %}
                    <tr>
                        {% for cell in row %}
                            <td>{{ cell }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return render_template_string(
        html_template, 
        headers=headers, 
        rows=rows, 
        average_age=average_age, 
        max_age=max_age, 
        min_age=min_age
    )

if __name__ == '__main__':
    app.run(debug=True)
