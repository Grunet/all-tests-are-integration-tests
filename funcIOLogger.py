
def logIO(func):
    def funcWithLogging(*args, **kwargs):
        
        output = func(*args, **kwargs)
        
        return output
        
    return funcWithLogging