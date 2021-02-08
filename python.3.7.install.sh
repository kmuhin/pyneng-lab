sudo apt-get install build-essential checkinstall python3-dev python3-setuptools
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev
sudo apt-get install libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev

wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
tar xvf Python-3.7.3.tgz
cd Python-3.7.3
./configure --enable-optimizations --enable-loadable-sqlite-extensions
sudo make altinstall

