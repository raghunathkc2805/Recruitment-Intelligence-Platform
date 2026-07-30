$ErrorActionPreference = "Stop"



Write-Host "=== Authentication Test ==="



$login = Invoke-RestMethod `

    -Method Post `

    -Uri "http://127.0.0.1:8000/auth/login" `

    -ContentType "application/json" `

    -Body '{"email":"admin@example.com","password":"Admin@123"}'



$token = $login.access_token



if (!$token) {

    throw "Authentication failed"

}



Write-Host "Authentication Passed"



Write-Host ""

Write-Host "=== Knowledge Engine Test ==="



Invoke-RestMethod `

    -Method Post `

    -Uri "http://127.0.0.1:8000/knowledge/search" `

    -Headers @{

        Authorization="Bearer $token"

    } `

    -ContentType "application/json" `

    -Body '{"domain":"Recruitment","key":"DWDM"}' | ConvertTo-Json -Depth 10



Write-Host ""

Write-Host "=== Recruiter AI Test ==="



Invoke-RestMethod `

    -Method Post `

    -Uri "http://127.0.0.1:8000/recruiter-ai/search-assistant" `

    -Headers @{

        Authorization="Bearer $token"

    } `

    -ContentType "application/json" `

    -Body '{"query":"Nokia DWDM Engineer"}' | ConvertTo-Json -Depth 10



Write-Host ""

Write-Host "API SMOKE TEST PASSED"