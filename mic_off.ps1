Start-Process powershell -Verb runas{
    $device_class=Get-PnpDevice -Class AudioEndpoint
   $device_class| Disable-PnpDevice -Confirm:$false 
}
# if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole("Administrators")) { Start-Process powershell.exe "-File `"$PSCommandPath`"" -Verb RunAs; exit }
# $d = Get-PnpDevice| where {$_.class -like "AudioEndpoint"}
# $d |Disable-PnpDevice -Confirm:$false
