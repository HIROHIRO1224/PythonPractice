Start-Process powershell -Verb runAs{
Disable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *マイク* -Class AudioEndpoint -Status OK).InstanceId}