# 🖥️ Host Info API - Flask

A lightweight Flask-based RESTful API that returns key information about the host system, including OS details, current time, processor info, Python version, and sample environment variables. Useful for diagnostics, DevOps tasks, monitoring, or educational purposes.

---

## Features

- ✅ Returns operating system name and version
- ✅ Includes processor and machine architecture
- ✅ Displays both UTC and local time
- ✅ Shows current Python version
- ✅ Returns a sample of environment variables
- ✅ JSON response for easy integration

---

# Requirements

- Python 3.7+
- Flask

---

# Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/CyrilBaah/hostinfo-api.git
cd  hostinfo-api
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate       
```

3. Install dependencies
```bash
pip install flash
```

4. Start application
```bash
python app.py
```

5. Test app
```bash
curl http://127.0.0.1:5000/system-info
```


