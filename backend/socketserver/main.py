
HOST, PORT = "0.0.0.0", 514

REST_API_HOST_POST = '127.0.0.1:8000'

import socketserver
import requests


def makeRequest(device,content):

	url = f'{REST_API_HOST_POST}/api/log/'
	requests.post(
		url,
			data={
				"device":device,
				"content":content
			}
		)

class SyslogUDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		data = bytes.decode(self.request[0].strip(), encoding="utf-8")
		# socket = self.request[1]
		makeRequest(
			device=self.client_address[0],
			content=str(data)
		)


if __name__ == "__main__":
	try:
		server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
		server.serve_forever(poll_interval=0.5)
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")