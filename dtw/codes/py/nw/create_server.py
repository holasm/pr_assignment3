import socket
import sys
import time


def processBuf(client, buf='', ):
  client.send(buf)
  buf = ''

def getClient(client, address):
  print 'New connection from ' + str(address)

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
  while(1):
    time.sleep(0.002)
    sock.listen(1)

    client, address = sock.accept()
    getClient(client, address)
    data = client.recv(2048)
    if data:
      buf += data
      processBuf(client, buf)
    client.close()


if __name__ == '__main__':
  test_socket_modes()