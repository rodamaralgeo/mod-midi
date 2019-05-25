import os
from mididings import *

config(
    backend='jack-rt',
    client_name='mod-midi-preset',
)

run([ChannelFilter(15) >> CtrlFilter(0) >> System('curl http://localhost:8888/pedalpreset/load?id=0'),
	 ChannelFilter(15) >> CtrlFilter(1) >> System('curl http://localhost:8888/pedalpreset/load?id=1'),
	 ChannelFilter(15) >> CtrlFilter(2) >> System('curl http://localhost:8888/pedalpreset/load?id=2'),
	 ChannelFilter(15) >> CtrlFilter(3) >> System('curl http://localhost:8888/pedalpreset/load?id=3'),
	 ChannelFilter(15) >> CtrlFilter(4) >> System('curl http://localhost:8888/pedalpreset/load?id=4'),
	 ChannelFilter(15) >> CtrlFilter(5) >> System('curl http://localhost:8888/pedalpreset/load?id=5'),
	 ChannelFilter(15) >> CtrlFilter(6) >> System('curl http://localhost:8888/pedalpreset/load?id=6'),
	 ChannelFilter(15) >> CtrlFilter(7) >> System('curl http://localhost:8888/pedalpreset/load?id=7'),
	 ChannelFilter(15) >> CtrlFilter(8) >> System('curl http://localhost:8888/pedalpreset/load?id=8'),
	 ChannelFilter(15) >> CtrlFilter(9) >> System('curl http://localhost:8888/pedalpreset/load?id=9'),
	 ChannelFilter(15) >> CtrlFilter(10) >> System('curl http://localhost:8888/pedalpreset/load?id=10'),
	 ChannelFilter(15) >> CtrlFilter(11) >> System('curl http://localhost:8888/pedalpreset/load?id=11'),
	 ChannelFilter(15) >> CtrlFilter(12) >> System('curl http://localhost:8888/pedalpreset/load?id=12'),
	 ChannelFilter(15) >> CtrlFilter(13) >> System('curl http://localhost:8888/pedalpreset/load?id=13'),
	 ChannelFilter(15) >> CtrlFilter(14) >> System('curl http://localhost:8888/pedalpreset/load?id=14'),
	 ChannelFilter(15) >> CtrlFilter(15) >> System('curl http://localhost:8888/pedalpreset/load?id=15'),
	 ChannelFilter(15) >> CtrlFilter(16) >> System('curl http://localhost:8888/pedalpreset/load?id=16'),
	 ChannelFilter(15) >> CtrlFilter(17) >> System('curl http://localhost:8888/pedalpreset/load?id=17'),
	 ChannelFilter(15) >> CtrlFilter(18) >> System('curl http://localhost:8888/pedalpreset/load?id=18'),
	 ChannelFilter(15) >> CtrlFilter(19) >> System('curl http://localhost:8888/pedalpreset/load?id=19'),
	 ChannelFilter(15) >> CtrlFilter(20) >> System('curl http://localhost:8888/pedalpreset/load?id=20'),     
	 ChannelFilter(13) >> CtrlFilter(7) >> System('curl -X POST http://localhost:8888/pedalpreset/save')])
