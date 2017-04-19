import socket 
import urlparse

def check_stream(url):
	parse = urlparse.urlparse(url)
	dest="DESCRIBE "+url+" RTSP/1.0\r\nCSeq: 2\r\nUser-Agent: python\r\nAccept: application/sdp\r\n\r\n"

	for res in socket.getaddrinfo(parse.hostname, parse.port, socket.AF_UNSPEC, socket.SOCK_STREAM):
		af, socktype, proto, canonname, sa = res

	s = socket.socket(af, socktype, proto)
	s.connect(sa)

	s.send(dest)
	recst=s.recv(32)
	print(recst)
	status = recst.split('\r\n')[0]
	if status == "RTSP/1.0 200 OK":
		return True
	else:
		return False