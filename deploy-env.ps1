param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("dev", "qa", "prod")]
    [string]$Environment,

    [Parameter(Mandatory=$true)]
    [string]$DockerHubUsername
)

Write-Host "Deploying to $Environment environment..." -ForegroundColor Green

# Replace placeholder in deployment file
$deploymentFile = "k8s/$Environment-deployment.yaml"
(Get-Content $deploymentFile) -replace "maharengarajan", $DockerHubUsername | Set-Content $deploymentFile

# Apply deployment
kubectl apply -f $deploymentFile

# wait for rollout to complete
kubectl rollout status deployment/flask-calculator -n $Environment

# show status
kubectl get pods -n $Environment
kubectl get services -n $Environment

Write-Host "Deployment to $Environment environment complete!" -ForegroundColor Green