Start-Process powershell -Verb runas{
    $camera_device=Get-PnpDevice -FriendlyName *cam* -Class Camera -Status OK
    $camera_device|Disable-PnpDevice -Confirm:$false
}