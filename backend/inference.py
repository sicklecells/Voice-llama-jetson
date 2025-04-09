import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Generator
import logging

# Initialize model and tokenizer (load only once)
model = None
tokenizer = None

def load_model():
    """Load 4-bit quantized Llama 2 for Jetson Orin Nano"""
    global model, tokenizer
    
    model_id = "TheBloke/Llama-2-7B-Chat-GPTQ"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.float16,
            revision="gptq-4bit-32g-actorder_True"
        )
        logging.info("Model loaded successfully")
    except Exception as e:
        logging.error(f"Model loading failed: {e}")
        raise

def generate_stream(text: str, max_tokens: int = 100) -> Generator[str, None, None]:
    """Yield Llama 2 responses token-by-token to minimize memory usage"""
    if not model:
        load_model()
    
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    
    with torch.inference_mode():
        for _ in range(max_tokens):
            outputs = model.generate(
                **inputs,
                max_new_tokens=1,
                pad_token_id=tokenizer.eos_token_id
            )
            yield tokenizer.decode(outputs[0][-1], skip_special_tokens=True)
            
            # Early exit if EOS token generated
            if outputs[0][-1] == tokenizer.eos_token_id:
                break

    # Force cleanup
    torch.cuda.empty_cache()
