import os


def FLUG_CHECK(FLUG):

    if FLUG in "DISABLE":
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\cam_con_disable.ps1')
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\mic_con_disable.ps1')
    
    if FLUG in "ENABLE":
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\cam_con_enable.ps1')
        os.system('powershell -Command' + ' ' +\
            'powershell -ExecutionPolicy RemoteSigned .\\mic_con_enable.ps1')
