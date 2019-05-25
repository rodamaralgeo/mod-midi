systemctl disable mod-midi
systemctl disable mod-midi-start
systemctl daemon-reload
rm -rf /etc/systemd/system/mod-midi.service
rm -rf /etc/systemd/system/mod-midi-start.service
git pull
