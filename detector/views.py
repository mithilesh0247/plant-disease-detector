import base64
import requests
from django.shortcuts import render
from .forms import LeafImageForm

API_URL = "https://crop.kindwise.com/api/v1"
API_KEY = "rbQnQtyX9Mr03iEOyRqm9jQUXXwwjaf4vYbNrrboFPAHpEEX55"

def home(request):
    diagnosis = None

    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save()

            # Convert image to base64
            with open(image_obj.image.path, "rb") as img:
                encoded_image = base64.b64encode(img.read()).decode()

            # Prepare and send API request
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "image": encoded_image  # Assuming API expects this key
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    diagnosis = response.json()
                else:
                    diagnosis = {"error": f"API error: {response.status_code}"}
            except Exception as e:
                diagnosis = {"error": str(e)}

    else:
        form = LeafImageForm()

    return render(request, 'index.html', {'form': form, 'diagnosis': diagnosis})
