from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

## CNN ##

# Refsum
@app.route('/cnn/')
def cnn():
    return render_template('cnn/ent/refsum/cnn.html')

@app.route('/cnn_coverage_pers/')
def cnn_pers():
    return render_template('cnn/ent/refsum/cnn_pers.html')

@app.route('/cnn_coverage_loc/')
def cnn_loc():
    return render_template('cnn/ent/refsum/cnn_loc.html')

@app.route('/cnn_coverage_org/')
def cnn_org():
    return render_template('cnn/ent/refsum/cnn_org.html')

# BART
@app.route('/cnn_bart/')
def cnn_bart():
    return render_template('cnn/ent/bart/cnn_bart.html')

@app.route('/cnn_coverage_bart_pers/')
def cnn_bart_pers():
    return render_template('cnn/ent/bart/cnn_bart_pers.html')

@app.route('/cnn_coverage_bart_loc/')
def cnn_bart_loc():
    return render_template('cnn/ent/bart/cnn_bart_loc.html')

@app.route('/cnn_coverage_bart_org/')
def cnn_bart_org():
    return render_template('cnn/ent/bart/cnn_bart_org.html')

# Pegasus
@app.route('/cnn_pegasus/')
def cnn_pegasus():
    return render_template('cnn/ent/pegasus/cnn_pegasus.html')

@app.route('/cnn_coverage_pegasus_pers/')
def cnn_pegasus_pers():
    return render_template('cnn/ent/pegasus/cnn_pegasus_pers.html')

@app.route('/cnn_coverage_pegasus_loc/')
def cnn_pegasus_loc():
    return render_template('cnn/ent/pegasus/cnn_pegasus_loc.html')

@app.route('/cnn_coverage_pegasus_org/')
def cnn_pegasus_org():
    return render_template('cnn/ent/pegasus/cnn_pegasus_org.html')

# T5
@app.route('/cnn_t5/')
def cnn_t5():
    return render_template('cnn/ent/t5/cnn_t5.html')

@app.route('/cnn_coverage_t5_pers/')
def cnn_t5_pers():
    return render_template('cnn/ent/t5/cnn_t5_pers.html')

@app.route('/cnn_coverage_t5_loc/')
def cnn_t5_loc():
    return render_template('cnn/ent/t5/cnn_t5_loc.html')

@app.route('/cnn_coverage_t5_org/')
def cnn_t5_org():
    return render_template('cnn/ent/t5/cnn_t5_org.html')


# Fluent text
@app.route('/cnn_article_text/')
def cnn_art_text():
    filename_cnn = os.path.join(app.static_folder, 'dailymail_article_genre_fluent.json')
    with open(filename_cnn) as f_cnn:
        data_cnn = json.loads(f_cnn.read())
        f_cnn.close()
    text_cnn = []
    for element in data_cnn:
        for x, y in element.items():
            t = (x,y)
            text_cnn.append(t)
    return render_template('cnn/text/cnn_art_text.html', data_cnn=text_cnn)


@app.route('/cnn_summary_text/')
def cnn_sum_text():
    filename_cnn_sum = os.path.join(app.static_folder, 'cnn_all_sum_genre_fluent.json')
    with open(filename_cnn_sum) as f_cnn_sum:
        data_cnn_sum = json.loads(f_cnn_sum.read())
        return render_template('cnn/text/cnn_sum_text.html', data_cnn_sum=data_cnn_sum)


## Dailymail ##

# Fluent Text
@app.route('/dailymail_article_text/')
def dailymail_art_text():
    filename_dailymail = os.path.join(app.static_folder, 'dailymail_article_genre_fluent.json')
    with open(filename_dailymail) as f_dailymail:
        data_dailymail = json.loads(f_dailymail.read())
        f_dailymail.close()
    text_dailymail = []
    for element in data_dailymail:
        for x, y in element.items():
            t = (x,y)
            text_dailymail.append(t)
    return render_template('dailymail/text/dailymail_art_text.html', data_dailymail=text_dailymail)

@app.route('/dailymail_summary_text/')
def dailymail_sum_text():
    filename_dailymail_sum = os.path.join(app.static_folder, 'dailymail_all_sum_genre_fluent.json')
    with open(filename_dailymail_sum) as f_dailymail_sum:
        data_dailymail_sum = json.loads(f_dailymail_sum.read())
        return render_template('dailymail/text/dailymail_sum_text.html', data_dailymail_sum=data_dailymail_sum)


# Ref Sum
@app.route('/dailymail/')
def dailymail():
    return render_template('dailymail/ent/refsum/dailymail.html')

@app.route('/dailymail_coverage_pers/')
def dailymail_pers():
    return render_template('dailymail/ent/refsum/dailymail_pers.html')

@app.route('/dailymail_coverage_loc/')
def dailymail_loc():
    return render_template('dailymail/ent/refsum/dailymail_loc.html')

@app.route('/dailymail_coverage_org/')
def dailymail_org():
    return render_template('dailymail/ent/refsum/dailymail_org.html')

# BART
@app.route('/dailymail_bart/')
def dailymail_bart():
    return render_template('dailymail/ent/bart/dailymail_bart.html')

@app.route('/dailymail_coverage_pers_bart/')
def dailymail_bart_pers():
    return render_template('dailymail/ent/bart/dailymail_bart_pers.html')

@app.route('/dailymail_coverage_loc_bart/')
def dailymail_bart_loc():
    return render_template('dailymail/ent/bart/dailymail_bart_loc.html')

@app.route('/dailymail_coverage_org_bart/')
def dailymail_bart_org():
    return render_template('/dailymail/ent/bart/dailymail_bart_org.html')

# Pegasus
@app.route('/dailymail_pegasus/')
def dailymail_pegasus():
    return render_template('dailymail/ent/pegasus/dailymail_pegasus.html')

@app.route('/dailymail_coverage_pers_pegasus/')
def dailymail_pegasus_pers():
    return render_template('dailymail/ent/pegasus/dailymail_pegasus_pers.html')

@app.route('/dailymail_coverage_loc_pegasus/')
def dailymail_pegasus_loc():
    return render_template('dailymail/ent/pegasus/dailymail_pegasus_loc.html')

@app.route('/dailymail_coverage_org_pegasus/')
def dailymail_pegasus_org():
    return render_template('dailymail/ent/pegasus/dailymail_t5_org.html')

# T5
@app.route('/dailymail_t5/')
def dailymail_t5():
    return render_template('dailymail/ent/t5/dailymail_t5.html')

@app.route('/dailymail_coverage_pers_t5/')
def dailymail_t5_pers():
    return render_template('dailymail/ent/t5/dailymail_t5_pers.html')

@app.route('/dailymail_coverage_loc_t5/')
def dailymail_t5_loc():
    return render_template('dailymail/ent/t5/dailymail_t5_loc.html')

@app.route('/dailymail_coverage_org_t5/')
def dailymail_t5_org():
    return render_template('dailymail/ent/t5/dailymail_t5_org.html')

## BBC ##

# Fluent Text
@app.route('/bbc_article_text/')
def bbc_art_text():
    filename = os.path.join(app.static_folder, 'bbc_article_genre_fluent.json')
    with open(filename) as f:
        data = json.loads(f.read())
        f.close()
    text = []
    for element in data:
        for x, y in element.items():
            t = (x,y)
            text.append(t)
    return render_template('bbc/text/bbc_art_text.html', data=text)

@app.route('/bbc_summary_text/')
def bbc_sum_text():
    filename_sum = os.path.join(app.static_folder, 'bbc_all_sum_genre_fluent.json')
    with open(filename_sum) as f_sum:
        data1 = json.loads(f_sum.read())
        return render_template('bbc/text/bbc_sum_text.html', data_sum=data1)

# All entities
@app.route('/bbc/')
def bbc():
    return render_template('/bbc/ent/refsum/bbc.html')

@app.route('/bbc_all_bart/')
def bbc_bart():
    return render_template('bbc/ent/bart/bbc_bart.html')

@app.route('/bbc_all_pegasus/')
def bbc_pegasus():
    return render_template('bbc/ent/pegasus/bbc_pegasus.html')

@app.route('/bbc_all_t5/')
def bbc_t5():
    return render_template('bbc/ent/t5/bbc_t5.html')

# Ref Sum
@app.route('/bbc_coverage_pers/')
def bbc_pers():
    return render_template('/bbc/ent/refsum/bbc_pers.html')

@app.route('/bbc_coverage_loc/')
def bbc_loc():
    return render_template('/bbc/ent/refsum/bbc_loc.html')

@app.route('/bbc_coverage_org/')
def bbc_org():
    return render_template('/bbc/ent/refsum/bbc_org.html')

# BART
@app.route('/bbc_coverage_pers_bart/')
def bbc_bart_pers():
    return render_template('/bbc/ent/bart/bbc_bart_pers.html')

@app.route('/bbc_coverage_loc_bart/')
def bbc_bart_loc():
    return render_template('/bbc/ent/bart/bbc_bart_loc.html')

@app.route('/bbc_coverage_org_bart/')
def bbc_bart_org():
    return render_template('/bbc/ent/bart/bbc_bart_org.html')

# Pegasus
@app.route('/bbc_coverage_pers_pegasus/')
def bbc_pegasus_pers():
    return render_template('/bbc/ent/pegasus/bbc_pegasus_pers.html')

@app.route('/bbc_coverage_loc_pegasus/')
def bbc_pegasus_loc():
    return render_template('/bbc/ent/pegasus/bbc_pegasus_loc.html')

@app.route('/bbc_coverage_org_pegasus/')
def bbc_pegasus_org():
    return render_template('/bbc/ent/pegasus/bbc_pegasus_org.html')

# T5
@app.route('/bbc_coverage_pers_t5/')
def bbc_t5_pers():
    return render_template('/bbc/ent/t5/bbc_t5_pers.html')

@app.route('/bbc_coverage_loc_bart/')
def bbc_t5_loc():
    return render_template('/bbc/ent/t5/bbc_t5_loc.html')

@app.route('/bbc_coverage_org_t5/')
def bbc_t5_org():
    return render_template('/bbc/ent/t5/bbc_t5_org.html')


if __name__ == '__main__':
    app.run(debug=True)