import os
from mididings import *

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
	 ChannelFilter(15) >> CtrlFilter(11) >> System('curl http://localhost:8888/pedalpreset/load?id=11')])
