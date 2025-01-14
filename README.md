# Xây Dựng Chatbot AI với Flan-T5 và Python

## Các bước cài đặt và chạy

### Bước 1: Cài đặt môi trường

- Dùng python version 3.11
- Nên dùng conda, setup environment qua câu lệnh: conda create -n myenv python=3.11
- Sau đó active enviroment qua câu lệnh: conda activate myenv

### Bước 2: Cấu hình Hugging Face

1. Tạo file `.env`
2. Truy cập Hugging Face để lấy token API của bạn
Options: Login khi chạy file Chatbot.ipynb trên colab và nhập token API
### Bước 3: Chạy ứng dụng

1. Chạy file Chatbot.ipynb
Mở Terminal/Command Prompt, di chuyển vào thư mục src  `cd colab` và chạy:
```python
python Chatbot.ipynb
```
2. Download data và model từ trên colab về máy local:
3. Đưa data vào file data, và đưa lora-flan-t5-large-chat vào model
4. Run ứng dụng:
```python
python app.py
```
5. Run ứng dụng:
```python
streamlit run streamlit_app.py
```
