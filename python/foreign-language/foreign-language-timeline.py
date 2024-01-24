from flask import Flask, request, render_template
app = Flask(__name__)

Category_I_Languages = [
    {'id': '1', 'name': 'Danish', 'timeline': '24 weeks'},
    {'id': '2', 'name': 'Italian'},
    {'id': '3', 'name': 'Dutch'},
    {'id': '4', 'name': 'Norwegian'},
    {'id': '5', 'name': 'Spanish'},
    {'id': '6', 'name': 'French'},
    {'id': '7', 'name': 'Portuguese'},
    {'id': '8', 'name': 'Swedish'},
]
Category_II_Languages = [
    {'id': '1', 'name': 'German'},
    {'id': '2', 'name': 'Malay'},
    {'id': '3', 'name': 'Swahili'},
    {'id': '4', 'name': 'Indonesian'}
]
Category_III_Languages = [
    {'id': '1', 'name': 'Albanian'},
    {'id': '2', 'name': 'Azerbaijani'},
    {'id': '3', 'name': 'Amharic'},
    {'id': '4', 'name': 'Armenian'},
    {'id': '5', 'name': 'Bengali'},
    {'id': '6', 'name': 'Bulgarian'},
    {'id': '7', 'name': 'Burmese'},
    {'id': '8', 'name': 'Czech'},
    {'id': '9', 'name': 'Dari'},
    {'id': '10', 'name': 'Estonian'},
    {'id': '11', 'name': 'Farsi'},
    {'id': '12', 'name': 'Georgian'},
    {'id': '13', 'name': 'Greek'},
    {'id': '14', 'name': 'Hebrew'},
    {'id': '15', 'name': 'Hindi'},
    {'id': '16', 'name': 'Hungarian'},
    {'id': '17', 'name': 'Icelandic'},
    {'id': '18', 'name': 'Kazakh'},
    {'id': '19', 'name': 'Khmer'},
    {'id': '20', 'name': 'Kyrgyz'},
    {'id': '21', 'name': 'Lao'},
    {'id': '22', 'name': 'Lithuanian'},
    {'id': '23', 'name': 'Macedonian'},
    {'id': '24', 'name': 'Mongolian'},
    {'id': '25', 'name': 'Nepali'},
    {'id': '26', 'name': 'Polish'},
    {'id': '27', 'name': 'Russian'},
    {'id': '28', 'name': 'Serbo-Croatian'},
    {'id': '29', 'name': 'Sinhala'},
    {'id': '30', 'name': 'Slovak'},
    {'id': '31', 'name': 'Somali'},
    {'id': '32', 'name': 'Tagalog'},
    {'id': '33', 'name': 'Tajiki'},
    {'id': '34', 'name': 'Tamil'},
    {'id': '35', 'name': 'Telugu'},
    {'id': '36', 'name': 'Thai'},
    {'id': '37', 'name': 'Tibetan'},
    {'id': '38', 'name': 'Turkish'},
    {'id': '39', 'name': 'Turkmen'},
    {'id': '40', 'name': 'Ukrainian'},
    {'id': '41', 'name': 'Urdu'},
    {'id': '42', 'name': 'Uzbek'},
    {'id': '43', 'name': 'Vietnamese'},
]
Category_IV_Languages = [
    {'id': '1', 'name': 'Arabic'},
    {'id': '2', 'name': 'Japanese'},
    {'id': '3', 'name': 'Korean'},
    {'id': '4', 'name': 'Chinese-Cantonese'},
    {'id': '5', 'name': 'Chinese-Mandarin'},
    {'id': '6', 'name': 'Japanese'},
]
# Root dir
@app.route('/')
def root():
    return render_template('index.html',
                           cat_I=Category_I_Languages,
                           cat_II=Category_II_Languages,
                           cat_III=Category_III_Languages,
                           cat_IV=Category_IV_Languages,
                           )
if __name__ == '__main__':
    app.run(debug=True)