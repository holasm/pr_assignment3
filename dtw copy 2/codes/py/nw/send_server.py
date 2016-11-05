import socket
import sys
import time

def test_socket_modes():
  host_name = socket.gethostname()
  ip_addr = socket.gethostbyname(host_name)
  port = 3001

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setblocking(1)
  sock.settimeout(None)
  
  sock.connect((ip_addr, port))
  try:
    sock.sendall('This is charli calling bravo.')
    while(1):
      data = sock.recv(2048)
      if(data):
        print data
        break
  except sock.errno, e:
    print "Socket error: %s" %str(e)
  except Exception, e:
    print "Other exception: %s" %str(e)
  finally:
    sock.close()

    # try:
    #   buf = s.recv(2048)
    # except socket.error, e:
    #   print "Error receiving data: %s" % e
    #   sys.exit(1)
    # sys.stdout.write(buf)


if __name__ == '__main__':
  test_socket_modes()