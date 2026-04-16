import os
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user',
        createdAt TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER NOT NULL,
        subject TEXT NOT NULL,
        score INTEGER NOT NULL,
        total INTEGER NOT NULL,
        answers TEXT,
        createdAt TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        question TEXT NOT NULL,
        answers TEXT NOT NULL,
        correct INTEGER NOT NULL,
        difficulty TEXT DEFAULT 'easy',
        createdAt TEXT NOT NULL
    )''')
    
    c.execute("SELECT COUNT(*) FROM questions")
    if c.fetchone()[0] == 0:
        default_questions = [
            ('python', "Biến trong Python được khai báo bằng từ khóa nào?", '["var", "let", "Không cần khai báo", "define"]', 2),
            ('python', "Hàm print() trong Python dùng để làm gì?", '["Khai báo biến", "In ra màn hình", "Tính toán", "Tạo vòng lặp"]', 1),
            ('python', "Cách khai báo list trong Python là?", '["list = {}", "list = ()", "list = []", "list = <>"]', 2),
            ('python', "Toán tử lũy thừa trong Python là?", '["**", "^^", "^", "pow"]', 0),
            ('python', "Hàm len() trong Python dùng để?", '["Tính tổng", "Đếm phần tử", "Sắp xếp", "Tìm kiếm"]', 1),
            ('python', "Cách comment một dòng trong Python?", '["//", "/* */", "#", "<!-- -->"]', 2),
            ('python', "Kiểu dữ liệu nào là số nguyên trong Python?", '["float", "int", "str", "bool"]', 1),
            ('python', "Từ khóa để tạo hàm trong Python?", '["function", "def", "func", "create"]', 1),
            ('python', "Cách import module trong Python?", '["import module", "#include", "require", "using"]', 0),
            ('python', "Vòng lặp for trong Python có cú pháp?", '["for i in range(n)", "for (i=0; i<n; i++)", "for i in n", "loop i to n"]', 0),
            ('javascript', "Cách khai báo biến trong JavaScript ES6?", '["var", "let và const", "int", "define"]', 1),
            ('javascript', "Hàm console.log() dùng để?", '["Tạo hộp thoại", "In ra console", "Tính toán", "Khai báo hàm"]', 1),
            ('javascript', "Kiểu dữ liệu nào là số trong JS?", '["string", "number", "boolean", "array"]', 1),
            ('javascript', "Cách tạo mảng trong JavaScript?", '["arr = {}", "arr = ()", "arr = []", "arr = <>"]', 2),
            ('javascript', "Toán tử so sánh bằng trong JS?", '["=", "==", "===", "both B and C"]', 3),
            ('javascript', "Hàm setTimeout() dùng để?", '["Lặp vô hạn", "Chạy sau một thời gian", "Dừng chương trình", "Tính toán"]', 1),
            ('javascript', "Cách viết hàm arrow function?", '["function =>", "() => {}", "-> function", "arrow()"]', 1),
            ('javascript', "Event click trong JS viết là?", '["onClick", "onclick", "click", "eventClick"]', 1),
            ('javascript', "Cách thêm phần tử vào mảng?", '["push()", "add()", "append()", "insert()"]', 0),
            ('javascript', "Từ khóa khai báo hằng số?", '["var", "let", "const", "static"]', 2),
            ('math', "Đạo hàm của x² là?", '["x", "2x", "x²", "2"]', 1),
            ('math', "Tích phân của 2x là?", '["x²", "2x²", "x² + C", "2x + C"]', 2),
            ('math', "Sin(90°) bằng?", '["0", "1", "0.5", "√3"]', 1),
            ('math', "Log10(100) bằng?", '["1", "2", "10", "100"]', 1),
            ('math', "Đạo hàm của sin(x) là?", '["sin(x)", "cos(x)", "-sin(x)", "-cos(x)"]', 1),
            ('math', "Tam giác vuông có cạnh 3,4 thì cạnh huyền?", '["5", "6", "7", "8"]', 0),
            ('math', "Đạo hàm của e^x là?", '["e^x", "xe^x", "e^(x+1)", "e"]', 0),
            ('math', "Tổng các góc trong tam giác?", '["90°", "180°", "360°", "270°"]', 1),
            ('math', "Giá trị của π (pi) xấp xỉ?", '["2.14", "3.14", "4.14", "5.14"]', 1),
            ('math', "Căn bậc 2 của 144?", '["10", "11", "12", "13"]', 2),
            ('english', "She ___ a student.", '["is", "are", "be", "been"]', 0),
            ('english', "What ___ your name?", '["is", "are", "am", "be"]', 0),
            ('english', "I ___ to the gym yesterday.", '["go", "went", "going", "gone"]', 1),
            ('english', "He ___ playing football now.", '["is", "are", "am", "was"]', 0),
            ('english', "This book is ___ than that one.", '["good", "better", "best", "more good"]', 1),
            ('english', "She ___ English very well.", '["speaks", "speak", "speaking", "spoke"]', 0),
            ('english', "___ you like coffee?", '["Do", "Does", "Did", "Is"]', 0),
            ('english', "I have ___ apple.", '["a", "an", "the", "some"]', 1),
            ('english', "They ___ in Paris.", '["live", "lives", "living", "lived"]', 0),
            ('english', "She is the ___ student in class.", '["smart", "smarter", "smartest", "most smart"]', 2),
        ]
        c.executemany("INSERT INTO questions (subject, question, answers, correct, createdAt) VALUES (?, ?, ?, ?, ?)",
                     [(q[0], q[1], q[2], q[3], datetime.now().isoformat()) for q in default_questions])
    
    conn.commit()
    conn.close()

init_db()

def row_to_dict(cursor, row):
    return dict(zip([col[0] for col in cursor.description], row))

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    fullname = data.get('fullname')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('isAdmin', False)
    admin_code = data.get('adminCode')
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    if is_admin:
        if admin_code != '123':
            conn.close()
            return jsonify({"success": False, "message": "Mã admin không đúng!"}), 400
        
        c.execute("SELECT * FROM users WHERE email = ? AND role = 'admin'", (email,))
        if c.fetchone():
            conn.close()
            return jsonify({"success": False, "message": "Email admin đã tồn tại"}), 400
        
        c.execute("INSERT INTO users (fullname, email, password, role, createdAt) VALUES (?, ?, ?, 'admin', ?)",
                  (fullname, email, password, datetime.now().isoformat()))
    else:
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        if c.fetchone():
            conn.close()
            return jsonify({"success": False, "message": "Email đã được sử dụng"}), 400
        if len(password) < 6:
            conn.close()
            return jsonify({"success": False, "message": "Mật khẩu phải có ít nhất 6 ký tự"}), 400
        
        c.execute("INSERT INTO users (fullname, email, password, role, createdAt) VALUES (?, ?, ?, 'user', ?)",
                  (fullname, email, password, datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Đăng ký thành công!"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE email = ? AND password = ? AND role = 'admin'", (email, password))
    admin = c.fetchone()
    if admin:
        conn.close()
        return jsonify({"success": True, "role": "admin", "user": dict(admin)})
    
    c.execute("SELECT * FROM users WHERE email = ? AND password = ? AND role = 'user'", (email, password))
    user = c.fetchone()
    if user:
        conn.close()
        return jsonify({"success": True, "role": "user", "user": dict(user)})
    
    conn.close()
    return jsonify({"success": False, "message": "Email hoặc mật khẩu không đúng"}), 401

@app.route('/api/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    
    if user:
        return jsonify({"success": True, "message": "Liên kết khôi phục đã gửi qua email!"})
    
    return jsonify({"success": False, "message": "Email không tồn tại trong hệ thống"}), 404

@app.route('/api/save-result', methods=['POST'])
def save_result():
    data = request.json
    user_id = data.get('userId')
    subject = data.get('subject')
    score = data.get('score')
    total = data.get('total')
    answers = data.get('answers', [])
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("INSERT INTO history (userId, subject, score, total, answers, createdAt) VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, subject, score, total, str(answers), datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Lưu kết quả thành công!"})

@app.route('/api/history/<user_id>', methods=['GET'])
def get_history(user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT * FROM history WHERE userId = ? ORDER BY createdAt DESC", (user_id,))
    history = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(history)

@app.route('/api/all-users', methods=['GET'])
def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT id, fullname, email, role, createdAt FROM users")
    users = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(users)

@app.route('/api/all-history', methods=['GET'])
def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT h.*, u.fullname, u.email FROM history h LEFT JOIN users u ON h.userId = u.id ORDER BY h.createdAt DESC")
    history = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(history)

@app.route('/api/change-password', methods=['POST'])
def change_password():
    data = request.json
    user_id = data.get('userId')
    new_password = data.get('newPassword')
    admin_id = data.get('adminId')
    
    if not user_id or not new_password:
        return jsonify({"success": False, "message": "Thiếu thông tin"}), 400
    
    if len(new_password) < 6:
        return jsonify({"success": False, "message": "Mật khẩu phải có ít nhất 6 ký tự"}), 400
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if str(user_id) == str(admin_id):
        conn.close()
        return jsonify({"success": False, "message": "Không thể đổi mật khẩu của chính mình"}), 400
    
    c.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
    
    if c.rowcount == 0:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy user"}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Đổi mật khẩu thành công!"})

@app.route('/api/delete-user', methods=['POST'])
def delete_user():
    data = request.json
    user_id = data.get('userId')
    admin_id = data.get('adminId')
    
    if str(user_id) == str(admin_id):
        return jsonify({"success": False, "message": "Không thể xóa tài khoản đang đăng nhập"}), 400
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("SELECT role FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    
    if not user:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy user"}), 404
    
    if user[0] == 'admin':
        conn.close()
        return jsonify({"success": False, "message": "Không thể xóa tài khoản admin khác"}), 400
    
    c.execute("DELETE FROM history WHERE userId = ?", (user_id,))
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Xóa user thành công!"})

@app.route('/api/questions/<subject>', methods=['GET'])
def get_questions(subject):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT * FROM questions WHERE subject = ?", (subject,))
    questions = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(questions)

@app.route('/api/all-questions', methods=['GET'])
def get_all_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT * FROM questions ORDER BY subject, id")
    questions = [dict(row) for row in c.fetchall()]
    conn.close()
    
    return jsonify(questions)

@app.route('/api/questions', methods=['POST'])
def add_question():
    data = request.json
    subject = data.get('subject')
    question = data.get('question')
    answers = data.get('answers')
    correct = data.get('correct')
    difficulty = data.get('difficulty', 'easy')
    
    if not subject or not question or not answers or correct is None:
        return jsonify({"success": False, "message": "Thiếu thông tin"}), 400
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("INSERT INTO questions (subject, question, answers, correct, difficulty, createdAt) VALUES (?, ?, ?, ?, ?, ?)",
              (subject, question, answers, correct, difficulty, datetime.now().isoformat()))
    
    conn.commit()
    new_id = c.lastrowid
    conn.close()
    
    return jsonify({"success": True, "message": "Thêm câu hỏi thành công!", "id": new_id})

@app.route('/api/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.json
    subject = data.get('subject')
    question = data.get('question')
    answers = data.get('answers')
    correct = data.get('correct')
    difficulty = data.get('difficulty', 'easy')
    
    if not subject or not question or not answers or correct is None:
        return jsonify({"success": False, "message": "Thiếu thông tin"}), 400
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("UPDATE questions SET subject = ?, question = ?, answers = ?, correct = ?, difficulty = ? WHERE id = ?",
              (subject, question, answers, correct, difficulty, question_id))
    
    if c.rowcount == 0:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy câu hỏi"}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Cập nhật câu hỏi thành công!"})

@app.route('/api/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("DELETE FROM questions WHERE id = ?", (question_id,))
    
    if c.rowcount == 0:
        conn.close()
        return jsonify({"success": False, "message": "Không tìm thấy câu hỏi"}), 404
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Xóa câu hỏi thành công!"})

if __name__ == '__main__':
    print("Server running at http://localhost:3000")
    print(f"Database: {DB_PATH}")
    app.run(port=3000, debug=True)