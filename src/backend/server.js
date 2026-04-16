const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const DB_PATH = path.join(__dirname, '../../data/database.json');

app.use(cors());
app.use(express.json());

function readDB() {
    try {
        const data = fs.readFileSync(DB_PATH, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        return { users: [], admins: [] };
    }
}

function writeDB(data) {
    fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2));
}

app.post('/api/register', (req, res) => {
    const { fullname, email, password, isAdmin, adminCode } = req.body;
    const db = readDB();

    if (isAdmin) {
        if (adminCode !== '123') {
            return res.status(400).json({ success: false, message: 'Mã admin không đúng!' });
        }
        if (db.admins.find(a => a.email === email)) {
            return res.status(400).json({ success: false, message: 'Email admin đã tồn tại' });
        }
        db.admins.push({
            id: Date.now(),
            fullname,
            email,
            password,
            createdAt: new Date().toISOString()
        });
    } else {
        if (db.users.find(u => u.email === email)) {
            return res.status(400).json({ success: false, message: 'Email đã được sử dụng' });
        }
        if (password.length < 6) {
            return res.status(400).json({ success: false, message: 'Mật khẩu phải có ít nhất 6 ký tự' });
        }
        db.users.push({
            id: Date.now(),
            fullname,
            email,
            password,
            createdAt: new Date().toISOString()
        });
    }

    writeDB(db);
    res.json({ success: true, message: 'Đăng ký thành công!' });
});

app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    const db = readDB();

    const admin = db.admins.find(a => a.email === email && a.password === password);
    if (admin) {
        return res.json({ success: true, role: 'admin', user: { ...admin, role: 'admin' } });
    }

    const user = db.users.find(u => u.email === email && u.password === password);
    if (user) {
        return res.json({ success: true, role: 'user', user: { ...user, role: 'user' } });
    }

    res.status(401).json({ success: false, message: 'Email hoặc mật khẩu không đúng' });
});

app.post('/api/forgot-password', (req, res) => {
    const { email } = req.body;
    const db = readDB();

    const user = db.users.find(u => u.email === email);
    const admin = db.admins.find(a => a.email === email);

    if (user || admin) {
        return res.json({ success: true, message: 'Liên kết khôi phục đã gửi qua email!' });
    }

    res.status(404).json({ success: false, message: 'Email không tồn tại trong hệ thống' });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});