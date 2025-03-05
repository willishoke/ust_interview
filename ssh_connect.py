import paramiko
import yaml

class SSH_Connect:
    def __init__(self, config_file="credentials.yml"):
        self.ssh_client = None
        self.session_active = False
        self.output_buffer = ""
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """Loads SSH credentials from a YAML configuration file."""
        try:
            with open(self.config_file, "r") as file:
                config = yaml.safe_load(file)
                self.hostname = config.get("hostname")
                self.username = config.get("username")
                self.password = config.get("password")
        except Exception as e:
            print(f"Error loading configuration: {e}")
            self.hostname = self.username = self.password = None

    def connect(self):
        """Establishes an SSH connection and invokes a shell."""
        if not self.hostname or not self.username or not self.password:
            print("Missing SSH credentials.")
            return
        
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            self.shell = self.ssh_client.invoke_shell()
            self.session_active = True
            print("SSH connection established.")
        except Exception as e:
            print(f"Failed to connect: {e}")
            self.session_active = False

    def send_cmd(self, command):
        """Sends a command to the remote machine."""
        if self.session_active and self.shell:
            self.shell.send(command + "\n")
        else:
            print("No active SSH session.")

    def read(self):
        """Checks if the session is active and reads output."""
        if self.session_active and self.shell:
            while self.shell.recv_ready():
                self.output_buffer += self.shell.recv(1024).decode()
            return self.output_buffer
        return "No active session or no output."

    def close(self):
        """Closes the SSH session."""
        if self.ssh_client:
            self.ssh_client.close()
            self.session_active = False
            print("SSH connection closed.")

ssh = SSH_Connect()
print(ssh.hostname, ssh.username, ssh.password)
ssh.connect()
ssh.send_cmd("ls")
print(ssh.read())
ssh.close()