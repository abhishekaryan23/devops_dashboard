from flask import Flask, render_template
from integrations.confluence import get_confluence_data
from integrations.jira import get_jira_data
from integrations.dynatrace import get_dynatrace_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    confluence_data = get_confluence_data()
    jira_data = get_jira_data()
    dynatrace_data = get_dynatrace_data()

    # Render the dashboard template with the fetched data
    return render_template('dashboard.html',
                           confluence_data=confluence_data,
                           jira_data=jira_data,
                           dynatrace_data=dynatrace_data)

if __name__ == '__main__':
    app.run(debug=True)

