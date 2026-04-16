🎓 Hệ thống hỗ trợ học tập thông minh
📌 Giới thiệu

Đây là dự án xây dựng hệ thống hỗ trợ học tập thông minh, giúp:

Gợi ý câu hỏi luyện tập phù hợp
Điều chỉnh độ khó dựa trên mức độ hiểu bài
Theo dõi thời gian học tập của người dùng

👉 Mục tiêu: cá nhân hóa việc học, giúp người dùng học hiệu quả hơn.

🛠 Công nghệ sử dụng
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
API: Flask + Flask-CORS
📂 Cấu trúc thư mục
sangt7/
│
├── src/
│ ├── backend/ # Server Flask
│ └── frontend/ # Giao diện web
│
├── README.md
└── requirements.txt (nếu có)
⚙️ Hướng dẫn cài đặt
🔹 1. Clone project
git clone https://github.com/dkhanh2706/sangt7.git
cd sangt7
🔹 2. Tạo môi trường ảo (venv)
python -m venv venv
🔹 3. Kích hoạt môi trường ảo

Windows:

venv\Scripts\activate

MacOS/Linux:

source venv/bin/activate
🔹 4. Di chuyển vào backend
cd src/backend
🔹 5. Cài đặt thư viện
pip install flask flask-cors

(hoặc nếu có file requirements.txt)

pip install -r requirements.txt
▶️ Chạy dự án
🔸 Backend
python server.py

👉 Server sẽ chạy tại:

http://127.0.0.1:5000
🔸 Frontend
Mở thư mục frontend bằng VS Code
Click chuột phải file index.html
Chọn "Open with Live Server"

👉 Frontend sẽ chạy tại:

http://127.0.0.1:5500
🔄 Cách dừng server
Ctrl + C
