import sys
import socket
from header import *

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f"Serving HTTP on port {PORT} ...")


while True:
	(client_connection, client_address) = listen_socket.accept()
	try:
		while True:		
			http_request = client_connection.recv(1024)

			if not http_request:
				break

			try:
				print (http_request.decode('utf-8'))
			except UnicodeDecodeError:
				print('')
				pass

			content = "HELLO WORLD"
			http_response = (
				"HTTP/1.1 200 OK\r\n"
				f"Content-Type: {HTTP_Content_Type.TEXT_PLAIN}\r\n"
				f"Content-Length: {len(content)}\r\n"
				"\r\n"
				f"{content}"
			)
			client_connection.sendall(http_response.encode('utf-8'))
	finally:
		client_connection.close()

