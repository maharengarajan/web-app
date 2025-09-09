# EKS Cluster Setup Script
Write-Host "Setting up EKS Cluster..." -ForegroundColor Green

# check AWS CLI is configured
Write-Host "Checking AWS CLI configuration..." -ForegroundColor Yellow
aws sts get-caller-identity

if ($LASTEXITCODE -ne 0) {
    Write-Host "AWS CLI is not configured properly. Please configure it and try again." -ForegroundColor Red
    exit 1
}
else {
    Write-Host "AWS CLI is configured properly." -ForegroundColor Green
}

# Create EKS Cluster
Write-Host "Creating EKS Cluster (this may take 10-15 minutes)..." -ForegroundColor Yellow
eksctl create cluster -f eks-cluster.yml

# Update kubeconfig
Write-Host "Updating kubeconfig..." -ForegroundColor Yellow
aws eks update-kubeconfig --name web-app-cluster --region us-east-1

# Verify cluster
Write-Host "Verifying EKS Cluster..." -ForegroundColor Yellow
kubectl get nodes

Write-Host "EKS Cluster setup complete!" -ForegroundColor Green