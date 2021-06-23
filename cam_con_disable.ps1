Start-Process powershell -Verb runas{
    Disable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *cam* -Class Camera -Status OK).InstanceId
}