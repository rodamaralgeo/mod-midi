cp /zynthian/mod-midi/mod-midi.service /etc/systemd/system/mod-midi.service
cp /zynthian/mod-midi/mod-midi-start.service /etc/systemd/system/mod-midi-start.service
chmod 777 /etc/systemd/system/mod-midi-start.service
chmod 777 /etc/systemd/system/mod-midi.service
chmod 777 /zynthian/mod-midi/mod-midi.py
systemctl enable mod-midi
systemctl enable mod-midi-start
systemctl daemon-reload
reboot
