# DevOps Dashboard

DevOps Dashboard is a web application built with Python and Flask to monitor and manage DevOps activities. It integrates with Confluence, JIRA, and Dynatrace APIs to provide an easy-to-use interface for managing tasks, incidents, and releases.

## Getting Started

To run this project, follow the steps below:

1. Clone the repository:
```
git clone https://github.com/abhishkaryan23/devops_dashboard.git
```

2. Navigate to the project directory:
```
cd devops_dashboard
```


3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)
```

4. Install the required dependencies:
```
pip install -r requirements.txt
```

5. Set environment variables for Flask:
```
export FLASK_APP=app.py (Linux/Mac)
set FLASK_APP=app.py (Windows)
```

6. Run the Flask application:
```
flask run
```

7. Access the dashboard in your web browser at `http://127.0.0.1:5000/`.

## Project Structure
```
The project is organized as follows:

devops_dashboard/
│
├── config/
│ └── api_credentials.yml
│
├── src/
│ ├── integrations/
│ │ ├── init.py
│ │ ├── confluence.py
│ │ ├── jira.py
│ │ └── dynatrace.py
│ │
│ ├── templates/
│ │ ├── base.html
│ │ └── dashboard.html
│ │
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ └── js/
│ │ └── scripts.js
│ │
│ └── main.py
│
├── tests/
│ ├── test_confluence.py
│ ├── test_jira.py
│ └── test_dynatrace.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Contributing

We welcome contributions to the project. Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.
