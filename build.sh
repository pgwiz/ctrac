pip3 install -r requirements.txt
python3.9 manage.py collectstatic
#rsync -avz --delete <local-directory>/ <user>@<vps-ip>:<remote-directory>/
#git pull origin main
