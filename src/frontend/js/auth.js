const API_URL = 'http://localhost:3000/api';

async function loadDatabase() {
    try {
        const response = await fetch(API_URL.replace('/api', ''));
        return await response.json();
    } catch (error) {
        console.error('Error loading database:', error);
        return { users: [], admins: [] };
    }
}

function showMessage(text, type = 'success') {
    const messageEl = document.getElementById('message');
    messageEl.textContent = text;
    messageEl.className = `message ${type} show`;
    setTimeout(() => {
        messageEl.classList.remove('show');
    }, 3000);
}

function togglePassword(button) {
    const input = button.parentElement.querySelector('input');
    const icon = button.querySelector('i');
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', () => togglePassword(button));
});

if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        
        if (!email || !password) {
            showMessage('Vui lòng nhập đầy đủ thông tin', 'error');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            const result = await response.json();

            if (result.success) {
                const userData = result.user;
                // Ensure id is properly set
                if (!userData.id) {
                    userData.id = userData[0]?.id || Date.now();
                }
                sessionStorage.setItem('user', JSON.stringify(userData));
                if (result.role === 'admin') {
                    showMessage('Đăng nhập admin thành công!', 'success');
                    setTimeout(() => window.location.href = 'admin/dashboard.html', 1000);
                } else {
                    showMessage('Đăng nhập thành công!', 'success');
                    setTimeout(() => window.location.href = 'index.html', 1000);
                }
            } else {
                showMessage(result.message, 'error');
            }
        } catch (error) {
            showMessage('Lỗi kết nối server', 'error');
        }
    });
}

if (document.getElementById('registerForm')) {
    const registerForm = document.getElementById('registerForm');
    const adminCodeGroup = document.getElementById('adminCodeGroup');
    const userBtn = document.getElementById('userBtn');
    const adminBtn = document.getElementById('adminBtn');
    
    let isAdmin = false;
    
    if (userBtn && adminBtn) {
        userBtn.addEventListener('click', () => {
            isAdmin = false;
            userBtn.classList.add('active');
            adminBtn.classList.remove('active');
            if (adminCodeGroup) adminCodeGroup.classList.remove('show');
        });

        adminBtn.addEventListener('click', () => {
            isAdmin = true;
            adminBtn.classList.add('active');
            userBtn.classList.remove('active');
            if (adminCodeGroup) adminCodeGroup.classList.add('show');
        });
    }

    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const fullname = document.getElementById('fullname').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const adminCode = document.getElementById('adminCode')?.value;

        if (!fullname || !email || !password) {
            showMessage('Vui lòng nhập đầy đủ thông tin', 'error');
            return;
        }

        if (password.length < 6) {
            showMessage('Mật khẩu phải có ít nhất 6 ký tự', 'error');
            return;
        }

        if (password !== confirmPassword) {
            showMessage('Mật khẩu xác nhận không khớp', 'error');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    fullname, 
                    email, 
                    password, 
                    isAdmin, 
                    adminCode: isAdmin ? adminCode : null 
                })
            });
            const result = await response.json();

            if (result.success) {
                showMessage(result.message, 'success');
                setTimeout(() => window.location.href = 'login.html', 1500);
            } else {
                showMessage(result.message, 'error');
            }
        } catch (error) {
            showMessage('Lỗi kết nối server', 'error');
        }
    });
}

if (document.getElementById('forgotForm')) {
    document.getElementById('forgotForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value.trim();
        
        if (!email) {
            showMessage('Vui lòng nhập email', 'error');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/forgot-password`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email })
            });
            const result = await response.json();

            if (result.success) {
                showMessage(result.message, 'success');
                setTimeout(() => window.location.href = 'login.html', 2000);
            } else {
                showMessage(result.message, 'error');
            }
        } catch (error) {
            showMessage('Lỗi kết nối server', 'error');
        }
    });
}