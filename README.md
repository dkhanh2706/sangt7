# 🎓 Hệ thống hỗ trợ học tập thông minh

## 📌 Giới thiệu

Đây là dự án xây dựng hệ thống hỗ trợ học tập thông minh, giúp gợi ý câu hỏi luyện tập dựa trên mức độ hiểu bài và thời gian học của người dùng.

---

## 🛠 Công nghệ sử dụng

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **API**: Flask + Flask-CORS

---

## ⚙️ Hướng dẫn cài đặt và chạy project

### 🔹 1. Clone project

```bash
git clone https://github.com/dkhanh2706/hethongthonhminh.git
cd intelligence-system
🔹 2. Chạy Backend
bash
cd backend
➤ Tạo môi trường ảo (venv)
bash
python -m venv venv
➤ Kích hoạt môi trường ảo
bash
venv\Scripts\activate
➤ Cài đặt thư viện
bash
pip install flask flask-cors
Hoặc nếu có file requirements.txt:

bash
pip install -r requirements.txt
➤ Chạy server
bash
python app.py
👉 Server sẽ chạy tại: http://127.0.0.1:5000

⛔ Dừng server
bash
CTRL + C
🔹 3. Chạy Frontend
Mở file:

text
frontend/index.html
Dùng Live Server để chạy

⚠️ Lưu ý
❌ Không push thư mục venv/

❌ Không push file .env

🔄 Nếu lỗi thư viện:

bash
pip install --upgrade pip
📂 Cấu trúc thư mục
intelligence-system/
│
├── src/
│   ├── backend/                # Flask backend
│   │   ├── app.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── database/
│   │       └── database.db
│   │
│   └── frontend/               # Giao diện
│       ├── admin/
│       ├── css/
│       ├── js/
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       ├── exercises.html
│       ├── history.html
│       ├── scores.html
│       └── subjects.html
│
├── notebooks/                  # Notebook phân tích ML (nếu có)
│   └── analysis.ipynb
│
├── data/                       # Dataset (nếu có)
│   └── dataset.csv
│
├── venv/                       ❌ (KHÔNG PUSH)
│
├── requirements.txt
├── .gitignore
└── README.md
```
