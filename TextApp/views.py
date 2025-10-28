
import random
from django.shortcuts import render
from .forms import UploadFileForm

def shuffle_word(word):
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def shuffle_text(text):
    words = text.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            text = uploaded_file.read().decode('utf-8')
            shuffled_text = shuffle_text(text)
            return render(request, 'TextApp/result.html', {'text': shuffled_text})
    else:
        form = UploadFileForm()
    return render(request, 'TextApp/upload.html', {'form': form})

