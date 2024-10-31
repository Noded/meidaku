// DOM элементы
const themeToggle = document.querySelector('.theme-toggle');
const addChatButton = document.querySelector('.add-chat-button');
const modal = document.querySelector('.modal');
const modalInput = document.querySelector('.modal-input');
const modalButtons = document.querySelectorAll('.modal-button');

// Управление темой
function initTheme() {
    const isDark = localStorage.getItem('theme') === 'dark';
    if (isDark) {
        document.body.classList.add('dark-mode');
        themeToggle.textContent = '☀️';
    }
}

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    themeToggle.textContent = isDark ? '☀️' : '🌙';
});

// Обработчики событий
addChatButton.addEventListener('click', () => {
    modal.classList.add('active');
});

// Открыть модальное окно и показать первое (создание группы) по умолчанию
function showModal() {
    const modalContainer = document.getElementById('modalContainer');
    modalContainer.classList.add('active');
    switchModal('createGroupModal');
}

// Закрыть модальное окно
function closeModal() {
    const modalContainer = document.getElementById('modalContainer');
    modalContainer.classList.remove('active');
}

// Переключить видимое модальное окно
function switchModal(modalId) {
    document.querySelectorAll('.modal-content').forEach(modal => {
        modal.style.display = 'none';
    });
    
    const modalToShow = document.getElementById(modalId);
    modalToShow.style.display = 'block';
}

// Добавляем обработчики для кнопок переключения между окнами
document.querySelectorAll('.modal-button.secondary').forEach(button => {
    button.addEventListener('click', function(event) {
        event.stopPropagation(); // Останавливаем всплытие события
        if (this.closest('#createGroupModal')) {
            switchModal('joinGroupModal');
        } else {
            switchModal('createGroupModal');
        }
    });
});

// Закрытие модального окна при клике на фон
document.getElementById('modalContainer').addEventListener('click', function(event) {
    if (event.target === this) { // Проверяем, что клик был именно по фону
        closeModal();
    }
});

// Закрытие при нажатии на крестик
document.querySelector('.close-button').addEventListener('click', closeModal);

// Копирование UUID
function copyUUID(uuid) {
    navigator.clipboard.writeText(uuid).then(() => {
        alert('UUID copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy UUID:', err);
    });
}

// Инициализация
initTheme();
