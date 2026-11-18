HeartConnect (frontend demo)
1. Copy this folder to C:\xampp\htdocs\HeartConnect, start Apache, open http://localhost/HeartConnect/ and press Ctrl+F5.
2. Admin login (Admin tab): admin@heartconnect.com / admin123. Change it in Settings.
HOW PEOPLE CONNECT (no couple code)
- Register, then fill "About you" in Settings so your profile shows on the People page.
- Open People, view profiles, press Chat to talk freely with anyone.
- Inside a chat, press "Ask: be in a relationship". Both people get a Yes/No popup. If both say Yes, Games and Memories unlock for them.
- Video call button in chat: built-in call (needs camera permission, https or localhost).
Accounts and chats are stored in each browser (localStorage) until the Python + MySQL backend exists.
Different devices: run chat_server.py (pip install -r requirements.txt; python chat_server.py). Use https for phone cameras.
Stuck? Use "Reset demo data" on the login page.
