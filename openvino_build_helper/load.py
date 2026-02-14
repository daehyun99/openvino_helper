import os
import shutil

def load(SETTING):
    DRIVE_CACHE_ARCHIVE = SETTING["DRIVE_CACHE_ARCHIVE"]
    DRIVE_BIN_ARCHIVE = SETTING["DRIVE_BIN_ARCHIVE"]
    LOCAL_CACHE_DIR = SETTING["LOCAL_CACHE_DIR"]
    
    if os.path.exists(DRIVE_CACHE_ARCHIVE):
        print("📥 [CCACHE] 구글 드라이브에서 캐시를 가져오는 중...")
        os.system(f"tar -xzf '{DRIVE_CACHE_ARCHIVE}' -C /")
        print("✅ [CCACHE] 복원 완료!")
    else:
        print("ℹ️ [CCACHE] 저장된 캐시가 없습니다. 새로 시작합니다.")

    os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)
    os.environ['CCACHE_DIR'] = LOCAL_CACHE_DIR
    os.environ['CCACHE_MAXSIZE'] = "100G"

    if os.path.exists(DRIVE_BIN_ARCHIVE):
        print("📥 [BIN] 구글 드라이브에서 실행 파일(bin)을 가져오는 중...")
        os.system("rm -rf /content/openvino/bin")
        os.system(f"tar -xzf '{DRIVE_BIN_ARCHIVE}' -C /")
        print("✅ [BIN] 복원 완료!")
    else:
        print("ℹ️ [BIN] 저장된 실행 파일이 없습니다. 빌드가 필요합니다.")

    # 4. 설정 확인
    print("\n📊 현재 CCACHE 상태:")
    os.system("ccache -s")
