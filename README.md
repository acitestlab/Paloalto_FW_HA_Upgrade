# Paloalto_FW_HA_Upgrade
Included here is the Terraform script to upgrade a Palo Alto Firewall in a High Availability (HA) setup and a Python automation script to provision and test the upgrade.
Terraform Script for Upgrading Palo Alto Firewall HA
This script assumes you have two firewalls in an HA setup and want to upgrade both sequentially.
    main.tf
    provision_and_test_ha.py

================  =================
Steps to Use the Python Script:
1. Prerequisites:
      Ensure Python 3.x is installed on your system.
      Install Terraform and ensure it is available in your system's PATH.
      Place the Terraform script (main.tf) and the Python script (provision_and_test.py) in the same directory.
2. Define Variables:
      Create a terraform.tfvars file in the same directory with the required variables:
         firewall_hostname = "192.168.1.1"
         firewall_username = "admin"
         firewall_password = "your_password"
         target_version    = "10.2.3"
3. Run the Python Script:
      Execute the Python script to automate the process:
         python provision_and_test.py
4. What the Script Does:
      Initializes Terraform (terraform init).
      Validates the Terraform configuration (terraform validate).
      Runs terraform plan to preview the changes.
      Applies the Terraform configuration (terraform apply -auto-approve).
      Simulates a test to verify the upgrade (you can replace this with actual API calls to the firewall).
5. Custom Testing:
      Replace the test_firewall_upgrade function with actual logic to verify the upgrade, such as using the Palo Alto API to check the software version.

Notes:
   Ensure you have the necessary permissions to run Terraform and access the Palo Alto Firewall.
   Always back up your firewall configuration before running the script.
   Modify the test_firewall_upgrade function to include real validation logic based on your environment.
