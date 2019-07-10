import time
def event_manager(main):
    
    logo = open("media/Logo.txt", "r")
    for line in logo:
            main._wlog(line)

    main._wlog("\n" + "Welcome to uqlxViz v1.0")
    
    #while True:

