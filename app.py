from flask import Flask, request, jsonify, render_template_string
from textblob import TextBlob

app = Flask(__name__)

# HTML template to serve as the front-end
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <p class="heading">Sentiment Analysis</p>
    <div class="container">
        <div class="contents">
            <p class="subheading">Steps:</p>
            <p class="text">i.&nbsp;&nbsp;&nbsp;Enter the comment you want to analyse the sentiment
                of.<br>ii.&nbsp;&nbsp;Choose a ML model from the dropdown.<br>iii.&nbsp;Click on 'Submit' to view
                result.
            </p>
            <form id="sentiment-form">
                <input type="text" name="comment" id="comment" placeholder="Enter your comment here">
                <select>
                    <option value="" disabled selected>Select model</option>
                    <option value="svm">SVM</option>
                    <option value="logistic_regression">Logistic Regression</option>
                    <option value="naive_bayes">Naive Bayes</option>
                </select>
                <button type="submit">Submit</button>
            </form>
        </div>
        <div class="results">
            <p id="result">hello</p>
        </div>
    </div>
    <footer>
        <p>Licensed under the terms of MIT License.<br>&copy; 2025 Tanishka Saxena. All Rights Reserved.</p>
    </footer>
    <style>
    *{
    margin: 0;
    padding: 0;
}
body{
    background-color: rgb(16, 16, 16);
    color:white;
}
.heading{
    margin: 20px;
    font-size: 30px;
    font-weight: 700;
    border-bottom: 1px solid white;
}
.container{
    display: flex;
    justify-content: space-around;
}
.contents{
    width: 40%;
}
.results{
    background-color: rgb(55, 55, 55);
    height: 30vh;
    width: 40%;
    padding:20px;
}
form{
    display: flex;
    flex-direction: column;
    margin-top: 50px;
}
input{
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
    color:white;
    border: none;
    background-color: rgba(124, 124, 124, 0.126);
}
select{
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
    color:white;
    border: none;
    background-color:  rgba(124, 124, 124, 0.126);
}
button{
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
    align-self: flex-end;
    width: 100px;
    border: none;
    color: white;
    cursor: pointer;
    transition-duration: 0.3s;
    background-color:  rgba(124, 124, 124, 0.126);
}
button:hover{
    background-color: rgb(226, 226, 226);
    color: black;
}
footer{
    position: fixed;
    bottom: 0;
    width:calc(100vw - 70px);
    margin-left: 30px;
    background-color: rgb(16, 16, 16);
    color: rgb(95, 95, 95);
    padding: 5px;
    padding-bottom: 10px;
    font-size: 14px;
    border-top: 1px solid rgb(103, 103, 103);
}
.subheading{
    margin: 20px;
    font-size: 20px;
    font-weight: 700;
}
.text{
    margin: 20px;
    font-size: 17px;
    line-height: 25px;
}
@media screen and (max-width: 800px){
    .container{
        flex-direction: column;
        align-items: center;
    }
    .results{
        margin-top: 20px;
        width:calc(100vw - 110px);
        margin-bottom: 100px;
    }
    .contents{
        width: 90%;
    }
}
</style>
    <script>
    document.getElementById('sentiment-form').addEventListener('submit', async function(event) {
      event.preventDefault(); // Prevent form from reloading the page

      const comment = document.getElementById('comment').value;

      // Send the comment to the server for analysis
      const response = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comment })
      });

      const result = await response.json();
      document.getElementById('result').innerText = `Sentiment: ${result.sentiment}`;
    });
  </script>
</body>

</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    comment = data['comment']

    # Perform sentiment analysis
    blob = TextBlob(comment)
    sentiment = 'Positive' if blob.sentiment.polarity > 0 else 'Negative' if blob.sentiment.polarity < 0 else 'Neutral'

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
