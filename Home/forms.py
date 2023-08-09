# forms.py
from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class UploadForm(forms.Form):
    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
