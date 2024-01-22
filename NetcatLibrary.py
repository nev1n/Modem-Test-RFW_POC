# NetcatLibrary.py

import subprocess
import time


class NetcatLibrary:
    def __init__(self):
        self.modem_process = None

    def connect_to_modem(self, host, port):
        """Connect to the modem using netcat."""
        command = ["nc", host, str(port)]
        self.modem_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Allow time for netcat to start
        time.sleep(2)

    def send_command(self, command):
        """Send a command to the connected modem."""
        if self.modem_process:
            self.modem_process.stdin.write(command.encode('utf-8') + b'\n')
            self.modem_process.stdin.flush()

    def read_response(self):
        """Read and return the response from the connected modem."""
        if self.modem_process:
            return self.modem_process.stdout.readline().decode('utf-8').strip()

    def close_connection(self):
        """Close the connection to the modem."""
        if self.modem_process:
            self.modem_process.stdin.close()
            self.modem_process.terminate()
            self.modem_process.wait()
