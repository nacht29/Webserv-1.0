import sys
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f"Serving HTTP on port {PORT} ...")

while True:
	(client_connection, client_address) = listen_socket.accept()
	request_data = client_connection.recv(1024)
	print(request_data.decode('utf-8'))

	content = "HELLO WORLD"
	http_response = (
		"HTTP/1.1 200 OK\r\n"
		"Content-Type: text/plain\r\n"
		f"Content-Length: {len(content)}\r\n"
		"\r\n"
		f"{content}"
	)

	client_connection.sendall(http_response.encode('utf-8'))
	client_connection.close()
