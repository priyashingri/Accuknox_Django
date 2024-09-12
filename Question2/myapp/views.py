import threading
from django.http import HttpResponse
from .models import MyModel

def test_signal_view(request):
    print(f"Main thread: {threading.current_thread().name}") 
    MyModel.objects.create(name='Test')
    return HttpResponse("Signal Test Complete")
