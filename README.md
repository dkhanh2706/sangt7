🎓 Hệ thống hỗ trợ học tập thông minh
📌 Giới thiệu

Đây là dự án xây dựng hệ thống hỗ trợ học tập thông minh, giúp:

Gợi ý câu hỏi luyện tập phù hợp
Điều chỉnh độ khó dựa trên mức độ hiểu bài
Theo dõi thời gian học tập của người dùng

👉 Mục tiêu: Cá nhân hóa việc học, giúp người dùng học hiệu quả hơn.

🛠 Công nghệ sử dụng
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
API: Flask + Flask-CORS
📂 Cấu trúc thư mục
intelligence-system/
│
├── src/
│ ├── backend/ # Flask backend
│ │ ├── app.py
│ │ ├── routes/
│ │ ├── services/
│ │ ├── models/
│ │ └── database/
│ │ └── database.db
│ │
│ └── frontend/ # Giao diện
│ ├── admin/
│ ├── css/
│ ├── js/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── profile.html
│ ├── exercises.html
│ ├── history.html
│ ├── scores.html
│ └── subjects.html
│
├── notebooks/ # Notebook phân tích ML (nếu có)
│ └── analysis.ipynb
│
├── data/ # Dataset (nếu có)
│ └── dataset.csv
│
├── venv/ ❌ (KHÔNG PUSH)
│
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Hướng dẫn cài đặt

1. Clone project
   git clone https://github.com/dkhanh2706/sangt7.git
   cd sangt7
2. Tạo môi trường ảo
   python -m venv venv
3. Kích hoạt môi trường ảo

Windows:

venv\Scripts\activate

MacOS/Linux:

source venv/bin/activate 4. Di chuyển vào backend
cd src/backend 5. Cài đặt thư viện
pip install flask flask-cors

Hoặc nếu có requirements.txt:

pip install -r requirements.txt
▶️ Chạy dự án
🔹 Chạy Backend
python server.py

👉 Server chạy tại:

http://127.0.0.1:5000
🔹 Chạy Frontend
Mở thư mục src/frontend bằng VS Code
Click chuột phải vào index.html
Chọn "Open with Live Server"

👉 Frontend chạy tại:

http://127.0.0.1:5500
⛔ Dừng server
Ctrl + C
⚠️ Lưu ý
Không push thư mục venv/ lên GitHub
Nên thêm venv/ vào .gitignore
Chạy backend trước khi mở frontend
Nếu lỗi port → kiểm tra 5000 và 5500
