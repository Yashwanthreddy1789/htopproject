from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import getpass
import subprocess
import datetime
import pytz
def htop_view(request):
    # Replace with your real name
    full_name = "sample_name"
    
    # Get system username
    username = getpass.getuser()

    # IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist)

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error running top: {e}"

    # Build response string
    response = f"""\
Name: {full_name}
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
"""

    return HttpResponse(f"<pre>{response}</pre>", content_type="text/html")