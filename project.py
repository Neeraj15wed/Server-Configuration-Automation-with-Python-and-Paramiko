!pip install paramiko
import paramiko

def install_apache(hostname, username, password):
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        
        # Install Apache web server
        stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get install -y apache2')
        
        # Check for installation success
        if stdout.channel.recv_exit_status() == 0:
            print("Apache installed successfully.")
        else:
            print("Error installing Apache.")
            print(stderr.read().decode())
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        ssh.close()

if __name__ == "__main__":
    # Provide SSH credentials
    hostname = input("Enter hostname or IP address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Call install_apache function
    install_apache(hostname, username, password)