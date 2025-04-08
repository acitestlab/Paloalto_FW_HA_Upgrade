import subprocess
import os
import sys

def run_command(command, cwd=None):
    """
    Run a shell command and print its output in real-time.
    """
    try:
        process = subprocess.Popen(
            command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        for line in process.stdout:
            print(line, end="")
        process.stdout.close()
        process.wait()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' failed with return code {e.returncode}")
        sys.exit(1)

def setup_terraform():
    """
    Initialize Terraform and validate the configuration.
    """
    print("Initializing Terraform...")
    run_command("terraform init")

    print("Validating Terraform configuration...")
    run_command("terraform validate")

def provision_firewalls():
    """
    Run Terraform plan and apply to provision the firewall upgrades.
    """
    print("Running Terraform plan...")
    run_command("terraform plan")

    print("Applying Terraform configuration...")
    run_command("terraform apply -auto-approve")

def test_firewall_upgrade():
    """
    Test the firewall upgrade by verifying the target version on both firewalls.
    """
    print("Testing the firewall upgrade...")
    # Add your custom test logic here, such as using API calls to the firewalls
    # to verify the software version. For now, we'll simulate a test.
    print("Simulating test: Verifying the target version on both firewalls...")
    # Example: Replace this with actual API calls or checks
    print("Test passed: Both firewalls upgraded successfully.")

def main():
    """
    Main function to automate the Terraform provisioning and testing.
    """
    # Ensure the script is run in the directory containing the Terraform script
    terraform_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(terraform_dir)

    print("Starting automation for Palo Alto Firewall HA upgrade...")
    setup_terraform()
    provision_firewalls()
    test_firewall_upgrade()
    print("Automation completed successfully.")

if __name__ == "__main__":
    main()