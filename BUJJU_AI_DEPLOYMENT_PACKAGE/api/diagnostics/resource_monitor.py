import shutil

def disk_usage():

    total,used,free = shutil.disk_usage("/")

    return {

        "total":total,

        "used":used,

        "free":free

    }
