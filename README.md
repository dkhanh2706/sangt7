🎓 Hệ thống hỗ trợ học tập thông minh
📌 Giới thiệu

Đây là dự án xây dựng hệ thống hỗ trợ học tập thông minh, giúp:

Gợi ý câu hỏi luyện tập phù hợp
Điều chỉnh độ khó dựa trên mức độ hiểu bài
Theo dõi thời gian học tập của người dùng

👉 Mục tiêu: Cá nhân hóa việc học, giúp người dùng học hiệu quả hơn.

🛠 Công nghệ sử dụng
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
API: Flask + Flask-CORS
⚙️ Hướng dẫn cài đặt và chạy project
🔹 1. Clone project
git clone https://github.com/dkhanh2706/hethongthonhminh.git
cd intelligence-system
🔹 2. Chạy Backend
➤ Di chuyển vào backend
cd src/backend
➤ Tạo môi trường ảo (venv)
python -m venv venv
➤ Kích hoạt môi trường ảo

Windows:

venv\Scripts\activate

MacOS / Linux:

source venv/bin/activate
➤ Cài đặt thư viện
pip install flask flask-cors

Hoặc nếu có requirements.txt:

pip install -r requirements.txt
➤ Chạy server
python server.py

👉 Backend sẽ chạy tại:

http://127.0.0.1:5000
🔹 3. Chạy Frontend
Mở thư mục src/frontend bằng VS Code
Click chuột phải vào file index.html
Chọn "Open with Live Server"

👉 Frontend sẽ chạy tại:

http://127.0.0.1:5500
⛔ Dừng server
Ctrl + C
⚠️ Lưu ý
Không push thư mục venv/ lên GitHub
Nên thêm venv/ vào .gitignore
Chạy backend trước khi mở frontend
Nếu lỗi → kiểm tra port 5000 hoặc 5500
📂 Cấu trúc thư mục:
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
