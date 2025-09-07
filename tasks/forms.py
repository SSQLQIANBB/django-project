from .models import Task
from django import forms


# 使用Form和ModelForm创建表单
class BookForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter book title', }),
        label='Book Title',
        help_text='Enter the title of the book (max 100 characters).',
        error_messages={
            'max_length': 'Book title cannot exceed 100 characters.',
            'required': 'Book title is required.',
        }
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Enter book description', 'rows': 4, }),
        label='Book Description',
        help_text='Enter a brief description of the book (optional).',
    )


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Enter task name', }),
            'status': forms.Select(attrs={ 'class': 'form-control', }),
        }

        labels = {
            'name': 'Task Name',
            'status': 'Task Status',
        }

        help_texts = {
            'name': 'Enter a unique task name (max 65 characters).',
            'status': 'Select the current status of the task.',
        }

        error_messages = {
            'name': {
                'max_length': 'Task name cannot exceed 65 characters.',
                'unique': 'A task with this name already exists.',
                'required': 'Task name is required.',
            },
            'status': {
                'required': 'Task status is required.',
                'invalid_choice': 'Select a valid status.',
            }
        }