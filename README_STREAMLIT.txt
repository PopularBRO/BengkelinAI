BENGKELINAI WEBSITE - STREAMLIT WRAPPER
=======================================

ISI PROJECT
- app.py                 Streamlit wrapper
- static/                Website asli (HTML, CSS, JavaScript, logo, aset)
- .streamlit/config.toml Mengaktifkan static file serving
- requirements.txt       Dependensi Python

CARA MENJALANKAN DI WINDOWS
1. Extract ZIP ini ke folder, misalnya C:\BengkelinAI_Streamlit.
2. Buka folder tersebut di VS Code.
3. Buka Terminal > New Terminal.
4. Jalankan perintah berikut satu per satu:

   py -m venv .venv
   .venv\Scripts\activate
   py -m pip install -r requirements.txt
   py -m streamlit run app.py

5. Streamlit akan menampilkan alamat lokal, biasanya:
   http://localhost:8501
6. Buka alamat tersebut di browser.

CARA MENJALANKAN DI macOS / LINUX
1. Extract ZIP dan buka terminal di folder project.
2. Jalankan:

   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   streamlit run app.py

CARA KERJA
Streamlit menampilkan index.html dari folder static di dalam iframe.
Semua halaman HTML, CSS, JavaScript, dan aset asli tetap disimpan di folder
static, sehingga tautan relatif ke halaman lain dan file pendukung tetap dapat
berfungsi selama struktur folder tidak diubah.

CATATAN
- Project ini menggunakan Streamlit sebagai wrapper untuk website HTML/CSS/JS.
- UI website tetap dibuat oleh HTML, CSS, dan JavaScript, bukan komponen native
  Streamlit.
- Fitur demo tetap demo. Diagnosis AI, analisis suara AI, database bengkel,
  dan layanan mekanik nyata memerlukan backend/API tersendiri.
- Jangan pindahkan HTML keluar dari folder static tanpa memperbarui link aset.
