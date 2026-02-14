
def setting(
    DRIVE_CACHE_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/ccache_openvino_TF_Front.tar.gz",
    DRIVE_BIN_ARCHIVE: str = "/content/drive/MyDrive/Build_Cache/ccache_openvino_TF_Front_bin.tar.gz",
    LOCAL_CACHE_DIR: str = "/content/ccache_local",
    LOCAL_BIN_DIR: str = "content/openvino/bin"
    ):
    SETTING = {}
    SETTING["DRIVE_CACHE_ARCHIVE"] = DRIVE_CACHE_ARCHIVE
    SETTING["DRIVE_BIN_ARCHIVE"] = DRIVE_BIN_ARCHIVE
    SETTING["LOCAL_CACHE_DIR"] = LOCAL_CACHE_DIR
    SETTING["LOCAL_BIN_DIR"] = LOCAL_BIN_DIR

    return SETTING
