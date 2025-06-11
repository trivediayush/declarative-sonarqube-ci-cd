ZeroTouch Environment Provisioner
=================================

**Automated infrastructure and application provisioning pipeline using Terraform, Ansible, Jenkins, and Docker.**

📌 Objective
------------

This project provisions on-demand environments for QA/UAT teams with zero manual intervention. A complete CI/CD pipeline spins up infrastructure on AWS EC2, configures Docker-based services using Ansible, and deploys a containerized Flask application with PostgreSQL.

🛠️ Tools & Technologies
------------------------

*   Terraform (AWS EC2 provisioning)
*   Ansible (environment configuration & deployment)
*   Docker & Docker Compose (app and DB services)
*   Jenkins (declarative multistage pipeline)
*   Ubuntu (base image for EC2 instance)

🚀 Features
-----------

*   Automated AWS EC2 provisioning with Terraform
*   Infrastructure-as-Code using best practices
*   Declarative Jenkins pipeline for CI/CD
*   Secure handling of secrets (AWS, DB credentials, SSH)
*   Ansible automation for installing Docker and deploying Compose services
*   Scalable, containerized backend using Flask + PostgreSQL

🔒 Secret Management
--------------------

All sensitive values (e.g., AWS keys, SSH keys, DB credentials) are managed using Jenkins Credentials and Ansible environment lookups.

📦 Deployment Steps
-------------------

1.  Configure Jenkins with Terraform, Ansible, and credentials.
2.  Push to the main branch to trigger CI/CD pipeline.
3.  Terraform provisions EC2 → Public IP is extracted.
4.  Ansible installs Docker, configures app using Docker Compose.
5.  Application and database come online and ready for QA/UAT use.

🔍 Monitoring & Validation
--------------------------

*   Post-deployment validation via HTTP status check
*   Optional: Extend with Prometheus Node Exporter

📬 Notification
---------------

A notification script (\`notify.sh\`) can send post-deployment messages to email or Slack.

📈 Diagram Reference
--------------------

See included architecture blueprint for CI/CD and provisioning flow.

📌 Author
---------

**Ayush Trivedi** 