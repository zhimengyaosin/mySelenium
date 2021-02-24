import subprocess

f = subprocess.Popen("mitmweb -s mitmproxy_script.py", shell=True)
f.wait()