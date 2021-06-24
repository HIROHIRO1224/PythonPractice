Start-Process powershell -Verb runAs{
    Enable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *マイク* -Class AudioEndpoint -Status OK).InstanceId}