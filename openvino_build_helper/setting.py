
def setting(
    DRIVE_CACHE_ARCHIVE: str,
    DRIVE_BIN_ARCHIVE: str,
    LOCAL_CACHE_DIR: str = "/content/ccache_local",
    LOCAL_BIN_DIR: str = "content/openvino/bin"
    ):
    BASE_PATH = "/content/drive/MyDrive/Build_Cache/"
    # ==========================================
    # 1. 경로 설정 (CCACHE + BIN)
    # ==========================================
    # ccache 경로
    DRIVE_CACHE_ARCHIVE = BASE_PATH + "ccache_openvino_build_TF_Front.tar.gz"
    DRIVE_BIN_ARCHIVE = BASE_PATH + "ccache_openvino_build_TF_Front_bin.tar.gz"
    LOCAL_CACHE_DIR = LOCAL_CACHE_DIR
    LOCAL_BIN_DIR = LOCAL_BIN_DIR

    SETTING = {}
    SETTING["DRIVE_CACHE_ARCHIVE"] = DRIVE_CACHE_ARCHIVE
    SETTING["DRIVE_BIN_ARCHIVE"] = DRIVE_BIN_ARCHIVE
    SETTING["LOCAL_CACHE_DIR"] = LOCAL_CACHE_DIR
    SETTING["LOCAL_BIN_DIR"] = LOCAL_BIN_DIR

    return SETTING
