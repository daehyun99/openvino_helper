import os

def setting(
    DRIVE_CACHE_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/ccache_openvino_TF_Front.tar.gz",
    DRIVE_BIN_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/ccache_openvino_TF_Front_bin.tar.gz",
    DRIVE_BUILD_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/build_openvino_TF_Front.tar.gz",
    LOCAL_CACHE_DIR: str = "/content/ccache_local",
    LOCAL_BIN_DIR: str = "content/openvino/bin"
    ):
    os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)

    os.environ['CCACHE_DIR'] = LOCAL_CACHE_DIR
    os.environ['CCACHE_MAXSIZE'] = "10G"

    SETTING = {}
    SETTING["DRIVE_CACHE_ARCHIVE"] = DRIVE_CACHE_ARCHIVE
    SETTING["DRIVE_BIN_ARCHIVE"] = DRIVE_BIN_ARCHIVE
    SETTING["LOCAL_CACHE_DIR"] = LOCAL_CACHE_DIR
    SETTING["LOCAL_BIN_DIR"] = LOCAL_BIN_DIR
    SETTING["DRIVE_BUILD_ARCHIVE"] = DRIVE_BUILD_ARCHIVE

    return SETTING
