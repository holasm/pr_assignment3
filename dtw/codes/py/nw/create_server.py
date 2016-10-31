import socket
import sys
import time

def processBuf(buf, client):
  client.send(buf)

def test_socket_modes():
  host_name = socket.gethostname()
  ip_addr = socket.gethostbyname(host_name)
  port = 3001

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setblocking(1)
  sock.settimeout(None)
  
  sock.bind((ip_addr, port))
  socket_address = sock.getsockname()
  print "Trivial Server launched on socket: %s" %str(socket_address)
  buf = ''
  while(1):
    time.sleep(0.002)
    sock.listen(1)

    client, address = sock.accept()
    data = client.recv(2048)
    if data:
      buf += data
      processBuf(buf, client)
    client.close()


if __name__ == '__main__':
  test_socket_modes()