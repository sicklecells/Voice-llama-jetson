import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_quantized_model():
    # 4-bit quantized Llama 2 (using bitsandbytes)
    model = AutoModelForCausalLM.from_pretrained(
        "TheBloke/Llama-2-7B-Chat-GPTQ",
        device_map="auto",
        torch_dtype=torch.float16,
        revision="gptq-4bit-32g-actorder_True"
    )
    return model

def generate_text(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    with torch.inference_mode():
        outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
