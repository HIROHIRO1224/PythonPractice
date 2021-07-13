Start-Process powershell -Verb runas{
    $device_class=Get-PnpDevice -Class AudioEndpoint
    $device_class|Enable-PnpDevice -Confirm:$false 
}