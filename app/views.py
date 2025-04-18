import base64
import json
import os
from django.shortcuts import render
from .forms import ReceiptForm
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chatgpt_parse_receipt(image_path):
    with open(image_path, "rb") as img:
        image_data = base64.b64encode(img.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract data from this receipt and return it as JSON (vendor, date, total, items, taxes)."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}},
                ],
            }
        ],
        max_tokens=1000,
    )

    return response.choices[0].message.content


def upload_receipt(request):
    json_output = None
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            upload_dir = 'media/receipts'
            os.makedirs(upload_dir, exist_ok=True)  # ✅ Ensure directory exists
            path = os.path.join(upload_dir, image.name)
            with open(path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            json_output = chatgpt_parse_receipt(path)
    else:
        form = ReceiptForm()

    return render(request, 'upload.html', {'form': form, 'json_output': json.dumps(json_output, indent=2) if json_output else None})
