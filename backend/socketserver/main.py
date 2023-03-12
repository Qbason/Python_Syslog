import os
import socketserver
import requests

HOST, PORT = "0.0.0.0", 514

REST_API_HOST_POST = os.environ.get('REST_API_IP')#'http://127.0.0.1:8000'



def splitContent(content:str):

	index_first_space = content.find(" ") 
	all_types = content[:index_first_space]

	info = content[index_first_space:]

	return info,all_types




def makeRequest(device,content):

	url = f'{REST_API_HOST_POST}/api/log/'
	info,all_types = splitContent(content)
	requests.post(
		url,
			data={
				"device":device,
				"content":info,
				"types":all_types
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