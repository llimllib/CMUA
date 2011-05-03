rsync -avuz -e ssh --safe-links \
--exclude ".git" --exclude "local.py" --exclude "*.pyc" \
cmua/ cmua@md-ultimate.org:~/mdultimate/cmua

#and finally the static stuff
rsync -avuz -e ssh --safe-links \
--exclude ".git" \
static/ cmua@md-ultimate.org:~/mdultimate/static/static

ssh cmua@md-ultimate.org '~/mdultimate/init.sh restart'
