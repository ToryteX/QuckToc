if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ToryteX/QuckToc /QuckToc
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /QuckToc
fi
cd /QuckToc
pip3 install -U -r requirements.txt
echo "Starting Bot....💥🔥"
python3 bot.py
