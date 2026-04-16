// SmartLearn Main JS
var API_URL = 'http://localhost:3000/api';

function checkUser() {
    const user = JSON.parse(sessionStorage.getItem('user') || '{}');
    const navUser = document.getElementById('navUser');
    const userName = document.getElementById('userName');
    const userAvatar = document.getElementById('userAvatar');
    
    if (user && user.fullname) {
        if (userName) userName.textContent = user.fullname;
        if (userAvatar) userAvatar.textContent = user.fullname.charAt(0).toUpperCase();
        
        const savedImage = localStorage.getItem('avatarImage');
        let avatarContent = '<i class="fas fa-user"></i>';
        
        if (navUser) {
            let avatarStyle = 'style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)"';
            if (savedImage) {
                avatarContent = `<img src="${savedImage}" alt="Avatar">`;
                avatarStyle = 'style="background: none;"';
            }
            
            navUser.innerHTML = `
                <div class="user-logged" onclick="logout()" title="Nhấp để đăng xuất">
                    <div class="user-avatar" ${avatarStyle}>${avatarContent}</div>
                    <span class="user-name">${user.fullname}</span>
                    <i class="fas fa-sign-out-alt logout-icon"></i>
                </div>
            `;
        }
    } else {
        if (navUser) {
            navUser.innerHTML = `
                <a href="login.html" class="login-btn">
                    <i class="fas fa-sign-in-alt"></i>
                    <span>Đăng nhập</span>
                </a>
            `;
        }
    }
}

function logout() {
    if (confirm('Bạn có muốn đăng xuất?')) {
        sessionStorage.removeItem('user');
        window.location.href = 'login.html';
    }
}

// Run on page load
document.addEventListener('DOMContentLoaded', checkUser);
if (document.readyState !== 'loading') checkUser();