# Entity Coverage for News Summarization

This repository cointains a Python Flask application for a localhost. It contains a website which visualizes the entity coverage of News articles with their summaries. 
The datasets which were used are the CNN/Dailymail and BBC (Xsum) corpora. For each newspaper, 100 articles with their reference summary were choosen and processed regarding the entities they containing. The coverage itself, which entities are appearing in the summary, which in the article, are displayed on the website.
For BBC, the entity coverage was not only processed for the reference summaries, but also for their abstractive generated summarization. The models used are BART, Pegasus and T5.

To run the website, simply download all files of this repository and open them in Python.

Make sure you have flask installed. If not just run the following command (works only if pip is installed!).

`pip install flask`

Then just open _hello.py_ and run the script.
You should get the following output:

`C:/yourdirectoy/app/hello.py
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 131-370-145
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

You can then click the URL and the Website should be displayed!

