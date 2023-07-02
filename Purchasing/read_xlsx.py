import pandas as pd
from flask import Flask, render_template, send_from_directory
from werkzeug.utils import safe_join

app = Flask(__name__)

@app.route('/')
def display_data():
   
    data = pd.read_excel('SDSDATABASE.xlsx')
    records = data.to_dict(orient='records')
    for record in records:
        record['PDF_path'] = f"pdf/{record['PDF']}.pdf"
    return render_template('index.html', records=records)

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    pdf_directory = 'templates\pdf'
    return send_from_directory(pdf_directory, filename)
    
@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'css.ico')

@app.route('/image', methods=['GET'])
def serve_image():
    image_directory = '\images'
    filename = 'Corsetti.png'  # Provide the correct filename
    return send_from_directory(image_directory, filename, mimetype='image/png')

app.static_folder = 'templates'
    
if __name__ == '__main__':
    app.run(debug=True)
