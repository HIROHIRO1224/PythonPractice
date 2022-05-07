Start-Process powershell -Verb runas{
    $camera_device=Get-PnpDevice -FriendlyName *cam* -Class Camera -Status ERROR
    $camera_device|Enable-PnpDevice -Confirm:$false
}