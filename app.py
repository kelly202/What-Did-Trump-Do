# main Flask app file

from flask import Flask, request, jsonify # import Flask which is the web framework
from dotenv import load_dotenv # import load_dotenv to load environment variables
import os # import os to access environment variables
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY")) # what this does it set the API key for gemini so that we can make requests to the API
model = genai.GenerativeModel('gemini-1.5-pro') # specify the model version to use
load_dotenv() # why load api key from .env file


def gemini_analysis(news_articles, sector): # takes in news articles and sector as input, might change to take only 1 article later
    prompt = f"""
        Analyze the following news articles about Donal Trump's recent actions and their impact on the
        {sector} sector: Based on this, provide:

        1. Investor Sentiment (Bullish, Bearish, or Neutral) and explain why
        2. Short-Term Market Outlook (Up, Down, Consolidate) and explain why
        3. Long-Term Market Outlook (Up, Down, Consolidate) and explain why
        4. 4 popular example stocks in this sector that are most likely to be affected, along with their predicted short-term movement (e.g., AAPL: Up, GOOG: Consolidate).
        5. A concise, paragraph-long summary suitable for a financial news report and retail investor.

    Format your response strictly as JSON:
    {{
      "sentiment": "...",
      "whySentiment": "...",
      "shortTermOutlook": "...",
      "whyShortTermOutlook": "...",
      "longTermOutlook": "...",
      "whyLongTermOutlook": "...",
      "stocksAffected": [
        {{"ticker": "...", "movement": "..."}},
        {{"ticker": "...", "movement": "..."}},
        {{"ticker": "...", "movement": "..."}},
        {{"ticker": "...", "movement": "..."}}
      ],
      "newsSummary": "..."
    }}

     ---
    News Articles:
    {news_articles}
    """

    try:
        response = model.generate_content(prompt)
        return response.text # returns the generated text from the gemeni model after passing the prompt
    except Exception as e:
        print(f"Error generating text: {e}")
        return None



app = Flask(__name__) # create a Flask app instance, where to look for templates and static files

@app.route('/') # when someone visits homepage do the below function
def home():
    #return render_template('index.html') # render the index.html template 
    return "Hello, World!"  # temporary response for testing 

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode for development