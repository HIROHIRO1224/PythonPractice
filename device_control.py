import os


def FLUG_CHECK(FLUG):

    if FLUG in "DISABLE":
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\con_cam_disable.ps1')
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\con_mic_disable.ps1')
    
    if FLUG in "ENABLE":
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\con_cam_enable.ps1')
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\con_mic_enable.ps1')
