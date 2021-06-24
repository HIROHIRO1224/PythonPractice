Start-Process powershell -Verb runas{
    Disable-PnpDevice -InstanceId (Get-PnpDevice -Class AudioEndpoint -Status OK).InstanceId}