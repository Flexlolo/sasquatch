# causes even more errors
# do not use
with open('patch0.txt', 'rb') as f:
	with open('patch0.txt.fixed', 'wb') as f2:
		for i, line in enumerate(f.readlines()):

			if line.find(b'+++') == -1:
				line = line.replace(b'\t', b'    ')

			f2.write(line)
