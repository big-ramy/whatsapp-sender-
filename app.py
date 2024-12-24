from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# إعدادات Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# تحديد ورقة Google Sheets الخاصة بالأرقام المرسلة
sheet_numbers = client.open("Sent Numbers").sheet1  # ورقة Google Sheets الخاصة بالأرقام المرسلة

@app.route('/verify-participation', methods=['POST'])
def verify_participation():
    data = request.json
    phone_numbers = data.get('phone_numbers', [])
    
    if not phone_numbers:
        return jsonify({'message': 'No phone numbers provided'}), 400

    # تحقق إذا كانت الأرقام مكررة أم لا في Google Sheets
    existing_numbers = sheet_numbers.col_values(1)  # استخراج الأرقام المخزنة من العمود الأول
    new_numbers = [num for num in phone_numbers if num not in existing_numbers]

    # إضافة الأرقام غير المكررة إلى Google Sheets
    for number in new_numbers:
        sheet_numbers.append_row([number])

    # إرسال الرد بتأكيد التحقق من الأرقام
    return jsonify({'message': 'Verification successful', 'new_numbers': new_numbers, 'total_shared': len(new_numbers)}), 200

if __name__ == '__main__':
    app.run(debug=True)
