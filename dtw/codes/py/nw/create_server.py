import socket
import sys
import time

def test_socket_modes():
  host_name = socket.gethostname()
  ip_addr = socket.gethostbyname(host_name)
  port = 3000

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
    data = client.recv(2048)
    if data:
      print "Data: %s" %data
      client.send(data)
      print "sent %s bytes back to %s" % (data, address)
    client.close()

    # try:
    #   buf = s.recv(2048)
    # except socket.error, e:
    #   print "Error receiving data: %s" % e
    #   sys.exit(1)
    # sys.stdout.write(buf)


if __name__ == '__main__':
  test_socket_modes()