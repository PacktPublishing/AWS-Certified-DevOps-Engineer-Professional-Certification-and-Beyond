#!/bin/bash
mkdir /tmp/ssm
mkdir /tmp/cw-agent
# Download and Install the SSM Agent 
cd /tmp/ssm
wget https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb
sudo dpkg -i amazon-ssm-agent.deb
sudo systemctl enable amazon-ssm-agent
# Install CollectD 
sudo apt-get update -y 
sudo apt-get install -y collectd
# Download and Install the Unified CloudWatch agent
cd /tmp/cw-agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i -E ./amazon-cloudwatch-agent.deb
sudo systemctl enable amazon-cloudwatch-agent
