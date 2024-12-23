from flask import Flask, request, jsonify
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# إعدادات Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Serial Numbers").sheet1  # تحديد ورقة Google Sheets

@app.route('/verify-participation', methods=['POST'])
def verify_participation():
    data = request.json
    phone_numbers = data.get('phone_numbers', [])
    email = data.get('email', None)
    
    if not phone_numbers or not email:
        return jsonify({'message': 'No phone numbers or email provided'}), 400

    # إضافة الأرقام إلى Google Sheets
    for number in phone_numbers:
        sheet.append_row([number])

    # توليد الرقم التسلسلي
    serial_number = generate_serial_number()

    # إرسال البيانات إلى Google Sheets
    # (إذا كان البريد الإلكتروني مطلوبًا، يمكن إضافته أيضًا إلى Google Sheets)

    return jsonify({'message': 'Participation verified', 'serial_number': serial_number}), 200

def generate_serial_number():
    return 'SN' + str(random.randint(100000, 999999))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# إعدادات Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Serial Numbers").sheet1  # تحديد ورقة Google Sheets

@app.route('/verify-participation', methods=['POST'])
def verify_participation():
    data = request.json
    phone_numbers = data.get('phone_numbers', [])
    email = data.get('email', None)
    
    if not phone_numbers or not email:
        return jsonify({'message': 'No phone numbers or email provided'}), 400

    # إضافة الأرقام إلى Google Sheets
    for number in phone_numbers:
        sheet.append_row([number])

    # توليد الرقم التسلسلي
    serial_number = generate_serial_number()

    # إرسال البيانات إلى Google Sheets
    # (إذا كان البريد الإلكتروني مطلوبًا، يمكن إضافته أيضًا إلى Google Sheets)

    return jsonify({'message': 'Participation verified', 'serial_number': serial_number}), 200

def generate_serial_number():
    return 'SN' + str(random.randint(100000, 999999))

if __name__ == '__main__':
    app.run(debug=True)
