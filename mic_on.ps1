Start-Process powershell -Verb runas{
    Enable-PnpDevice -InstanceId (Get-PnpDevice -Class AudioEndpoint -Status OK).InstanceId}