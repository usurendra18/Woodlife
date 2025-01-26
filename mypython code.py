from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel file
DATA_PATH = "C:\Users\91964\myproject\Candiour 40.xlsx"

def load_data():
    return pd.read_excel(DATA_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    df = load_data()
    search_query = request.form.get("search", "")
    selected_flag = request.form.get("flag", "")

    # Apply filters
    if search_query:
        df = df[
            df["name"].str.contains(search_query, case=False, na=False)
            | df["mobile"].astype(str).str.contains(search_query)
        ]
    if selected_flag:
        df = df[df["flag"] == selected_flag]

    # Count rows and prepare data for display
    count = len(df)
    data = df.to_dict(orient="records")

    return render_template("index.html", data=data, count=count, search_query=search_query, selected_flag=selected_flag)

if __name__ == "__main__":
    app.run(debug=True)
