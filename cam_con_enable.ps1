Start-Process powershell -Verb runas{
    Enable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *webcam* -Class Camera -Status error).InstanceId
}