from flask import Flask, request, jsonify
from flask_cors import CORS
from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)  # Cho phép kết nối từ frontend (Streamlit)

# Load model và tokenizer
peft_model_id = "model/lora-flan-t5-large-chat/checkpoint-3750"
config = PeftConfig.from_pretrained(peft_model_id)

model = AutoModelForSeq2SeqLM.from_pretrained(config.base_model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

model = PeftModel.from_pretrained(model, peft_model_id).to("cpu")
model.eval()

@app.route("/inference", methods=["POST"])
def inference():
    try:
        # Lấy dữ liệu từ yêu cầu
        data = request.json
        input_text = data.get("input_text", "")

        # Xử lý với mô hình
        input_ids = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=256).input_ids.to("cpu")
        outputs = model.generate(input_ids=input_ids, top_p=0.9, max_length=256)
        response = tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0]

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
