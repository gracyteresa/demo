from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        page_title="Gracy's Flask Page",
        sections=[
            {"title": "Section 1", "content": "This is the first section created by Gracy."},
            {"title": "Section 2", "content": "This is the second section created by Gracy."},
            {"title": "Section 3", "content": "This is the third section created by Gracy."}
        ]
    )

if __name__ == '__main__':
    app.run(debug=True)
