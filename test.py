#!/usr/bin/env python
# coding=utf-8

import os, sys

current_path = os.getcwd()

try:
	dirname = sys.argv[1]
	pathname = current_path + '/' + dirname

except Exception as e:
	pathname = current_path

f_start = open(current_path + '/start.html')
f = open(current_path  + '/' + dirname + '/index.html', 'w')
f.write(f_start.read())
f.write('\n')
f_start.close()

files = os.listdir(pathname)
index = 1;
for file in files:
	if file != 'index.html' and file.endswith('.mp4'):
#		f.write('	<video id="my-video" class="video-js" controls preload="auto" width="640" height="264" data-setup="{}">')
#		f.write('<source src="./' + file + '">')
		f.write('<p>' + str(index) + '</p>')
		index += 1		
		v_str = '    <video src="./' + file + '"' + ' controls width="100%"></video>'
		f.write(v_str)
#		f.write('    <p class="vjs-no-js"> 1 </p>')
#		f.write('	 </video>')		
		f.write('\n')

f.write('<script src="../video.js"></script>\n')
f.write('</body>\n</html>')
f.close()


